"""Shared machinery for the analytic-derivative notes (RHF, CPHF, CI, CPCI, Z-vector).

Conventions (match the notebook):
  mu,nu,lam,sig  AO;  i,j,k,l occupied;  a,b,c,d virtual;  p,q,r,s,m general MOs
  x, y           nuclear Cartesian coordinates (Yamaguchi et al. call them a, b)
  U^x_pq         dC_{mu q}/dx = sum_p C_{mu p} U^x_pq   (column q responds, row p is the admixed MO)
  (pq|rs)        chemists' notation, real orbitals
  P = 2 C_occ C_occ^T,  W = 2 C_occ eps_occ C_occ^T  (Yamaguchi's D and W are half of these)
"""
import numpy as np
from pyscf import gto, scf

BOHR = 0.52917721092


def water(basis, R=1.95, theta=110.0, unit='Bohr'):
    t = np.deg2rad(theta / 2)
    geom = [['O', (0, 0, 0)],
            ['H', (0, R * np.sin(t), R * np.cos(t))],
            ['H', (0, -R * np.sin(t), R * np.cos(t))]]
    return gto.M(atom=geom, basis=basis, unit=unit, verbose=0)


def coords(mol):
    return mol.atom_coords().copy()  # bohr


def displaced(mol, A, k, h):
    c = coords(mol)
    c[A, k] += h
    m = mol.copy()
    m.set_geom_(c, unit='Bohr')
    m.build()
    return m


def rhf(mol, dm0=None):
    mf = scf.RHF(mol)
    mf.conv_tol = 1e-13
    mf.conv_tol_grad = 1e-10
    mf.kernel(dm0)
    assert mf.converged
    return mf


# ---------- skeleton (core) AO derivative integrals, analytic ----------
def skeleton_ao(mol, mf=None):
    """Return lists over 3N coordinates of dS, dh, deri (full 4-index) at fixed AO labels."""
    nao = mol.nao
    natm = mol.natm
    aoslices = mol.aoslice_by_atom()
    ipovlp = mol.intor('int1e_ipovlp')          # <d mu | nu>, d = d/dr (electron)
    ip1 = mol.intor('int2e_ip1')                 # (d mu nu | lam sig)
    if mf is None:
        mf = scf.RHF(mol)
    hgen = mf.nuc_grad_method().hcore_generator(mol)
    dS, dh, deri = [], [], []
    for A in range(natm):
        p0, p1 = aoslices[A, 2:]
        hA = hgen(A)
        for k in range(3):
            s = np.zeros((nao, nao))
            s[p0:p1, :] -= ipovlp[k, p0:p1, :]
            s = s + s.T
            dS.append(s)
            dh.append(hA[k])
            g = np.zeros((nao,) * 4)
            g[p0:p1] -= ip1[k, p0:p1]
            g = g + g.transpose(1, 0, 2, 3)
            g = g + g.transpose(2, 3, 0, 1)
            deri.append(g)
    return dS, dh, deri


def nuc_grad(mol):
    Z = mol.atom_charges()
    R = coords(mol)
    g = np.zeros((mol.natm, 3))
    for A in range(mol.natm):
        for B in range(mol.natm):
            if A != B:
                d = R[A] - R[B]
                g[A] -= Z[A] * Z[B] * d / np.linalg.norm(d) ** 3
    return g.ravel()


def mo_transform(C, M):
    return C.T @ M @ C


def eri_mo(C, g):
    return np.einsum('pi,qj,rk,sl,pqrs->ijkl', C, C, C, C, g, optimize=True)


def cphf_matrix(eps, eri, nocc):
    """M_{ai,bj} = (e_a-e_i) d_ab d_ij + 4(ai|bj) - (ab|ij) - (aj|ib); a,b virtual; i,j occupied."""
    o = slice(0, nocc)
    v = slice(nocc, None)
    nv = len(eps) - nocc
    M = (4 * eri[v, o, v, o]
         - eri[v, v, o, o].transpose(0, 2, 1, 3)
         - eri[v, o, o, v].transpose(0, 2, 3, 1))
    M = M.reshape(nv * nocc, nv * nocc)
    de = (eps[v][:, None] - eps[o][None, :]).ravel()
    return M + np.diag(de)


def cphf_rhs(Sx, Fx_skel, eps, eri, nocc):
    """B^x_ai = -F^x_ai + S^x_ai e_i + sum_kl S^x_kl [2(ai|kl) - (ak|il)]   (sign so that M U = B)."""
    o = slice(0, nocc)
    v = slice(nocc, None)
    B = (-Fx_skel[v, o] + Sx[v, o] * eps[o][None, :]
         + 2 * np.einsum('kl,aikl->ai', Sx[o, o], eri[v, o, o, o])
         - np.einsum('kl,akil->ai', Sx[o, o], eri[v, o, o, o]))
    return B


def skeleton_fock_mo(C, hx, gx, nocc):
    """F^x_pq = h^x_pq + sum_k [2(pq|kk)^x - (pk|qk)^x]  in MO basis, with AO-derivative integrals."""
    P = 2 * C[:, :nocc] @ C[:, :nocc].T
    J = np.einsum('mnls,ls->mn', gx, P)
    K = np.einsum('mlns,ls->mn', gx, P)
    return mo_transform(C, hx + J - 0.5 * K)


def full_U(Uov, Sx, Fx_skel, eps, eri, nocc, canonical=True):
    """Assemble the full U^x matrix.
    ov block from CPHF; U_ia = -U_ai - S^x_ai (orthonormality, Yamaguchi Eq. 3.46).
    oo and vv blocks: canonical choice (Yamaguchi Eq. 10.26, keeps F diagonal) or the
    symmetric choice U = -S^x/2 (allowed when the energy is invariant to those rotations)."""
    o = slice(0, nocc)
    v = slice(nocc, None)
    U = -0.5 * Sx.copy()
    U[v, o] = Uov
    U[o, v] = -Uov.T - Sx[o, v]
    if canonical:
        # A-contraction is independent of the antisymmetric oo part, so use U as is
        AU = Acontract(U, eri, nocc)
        n = len(eps)
        for blk in (o, v):
            idx = np.arange(n)[blk]
            for p in idx:
                for q in idx:
                    if p != q:
                        U[p, q] = (Fx_skel[p, q] - Sx[p, q] * eps[q] + AU[p, q]) / (eps[q] - eps[p])
    return U


def Acontract(U, eri, nocc):
    """sum_{k all, l occ} U_kl A_pq,kl,  A_pq,kl = 4(pq|kl) - (pk|ql) - (pl|qk)."""
    o = slice(0, nocc)
    Ukl = U[:, o]
    return (4 * np.einsum('kl,pqkl->pq', Ukl, eri[:, :, :, o])
            - np.einsum('kl,pkql->pq', Ukl, eri[:, :, :, o])
            - np.einsum('kl,plqk->pq', Ukl, eri[:, o, :, :]))


def fock_derivative_mo(U, Fx_skel, eps, eri, nocc):
    """Total dF_pq/dx (Yamaguchi Eq. 10.6): F^x_pq + sum_k (U_kp F_kq + U_kq F_pk) + sum_{k, l occ} U_kl A_pq,kl."""
    F = np.diag(eps)
    return Fx_skel + U.T @ F + F @ U + Acontract(U, eri, nocc)
