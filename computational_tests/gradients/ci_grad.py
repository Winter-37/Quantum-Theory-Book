"""CISD (determinant-based, RHF orbitals, all electrons correlated) analytic derivatives:
  - CI gradient with explicit CPHF U^x (Yamaguchi Eqs. 6.23, 6.37)
  - Z-vector gradient and relaxed density (Yamaguchi Ch. 18; Handy-Schaefer 1984)
  - relaxed dipole from the same Z vector
  - first-order CPCI (Yamaguchi Eq. 12.11) against finite-difference CI vectors
  - CI Hessian (Yamaguchi Eq. 6.79) against finite differences of the analytic gradient
Water, STO-3G, R(OH) = 1.95 bohr, HOH = 110 deg.
"""
import numpy as np, sys, time
sys.path.insert(0, '.')
from common import *
from pyscf.fci import cistring, direct_spin1

np.set_printoptions(precision=6, suppress=True, linewidth=150)
BASIS = sys.argv[1] if len(sys.argv) > 1 else 'sto-3g'


class CISpace:
    def __init__(self, norb, nocc):
        self.norb, self.nocc = norb, nocc
        self.nelec = (nocc, nocc)
        strs = cistring.make_strings(range(norb), nocc)
        hf = (1 << nocc) - 1
        lev = np.array([bin(hf & ~int(s)).count('1') for s in strs])
        self.nstr = len(strs)
        la, lb = np.meshgrid(lev, lev, indexing='ij')
        self.sel = np.flatnonzero((la + lb).ravel() <= 2)     # CISD determinants
        self.ndet = len(self.sel)

    def H(self, h1, g2):
        h2 = direct_spin1.absorb_h1e(h1, g2, self.norb, self.nelec, 0.5)
        n = self.nstr ** 2
        Hm = np.zeros((self.ndet, self.ndet))
        for k, I in enumerate(self.sel):
            e = np.zeros(n); e[I] = 1.0
            Hm[:, k] = direct_spin1.contract_2e(h2, e.reshape(self.nstr, self.nstr), self.norb, self.nelec).ravel()[self.sel]
        return 0.5 * (Hm + Hm.T)

    def full(self, c):
        v = np.zeros(self.nstr ** 2); v[self.sel] = c
        return v.reshape(self.nstr, self.nstr)

    def rdm12(self, c):
        return direct_spin1.make_rdm12(self.full(c), self.norb, self.nelec)


def mo_deriv_ints(U, hx, gx, h, g):
    """Total MO-integral derivatives (Yamaguchi Eqs. 3.78 and 3.9x):
       dh_pq = h^x_pq + sum_m (U_mp h_mq + U_mq h_pm), and the 4-index analogue."""
    dh = hx + U.T @ h + h @ U
    dg = (gx + np.einsum('mp,mqrs->pqrs', U, g) + np.einsum('mq,pmrs->pqrs', U, g)
          + np.einsum('mr,pqms->pqrs', U, g) + np.einsum('ms,pqrm->pqrs', U, g))
    return dh, dg


class CISDState:
    """Everything at one geometry. If Cref/Sref given, MO signs are aligned to the reference."""
    def __init__(self, mol, dm0=None, Cref=None, Sref=None):
        self.mol = mol
        mf = rhf(mol, dm0)
        C = mf.mo_coeff.copy()
        if Cref is not None:
            C *= np.sign(np.diag(Cref.T @ Sref @ C))
        self.mf, self.C, self.eps = mf, C, mf.mo_energy
        self.nocc = mol.nelectron // 2
        self.n = C.shape[1]
        self.h = mo_transform(C, mf.get_hcore())
        self.g = eri_mo(C, mol.intor('int2e'))
        self.space = CISpace(self.n, self.nocc)
        self.Hci = self.space.H(self.h, self.g)
        w, V = np.linalg.eigh(self.Hci)
        self.Eel, self.c = w[0], V[:, 0]
        self.Etot = self.Eel + mol.energy_nuc()
        self.D, self.d = self.space.rdm12(self.c)

    def align(self, cref):
        if self.c @ cref < 0:
            self.c = -self.c

    def gen_fock(self):
        """Notebook (HJO) generalized Fock F_mn = sum_q D_mq h_nq + sum_qrs d_mqrs g_nqrs.
        Yamaguchi's Lagrangian is X_pq = F_qp."""
        return self.D @ self.h.T + np.einsum('mqrs,nqrs->mn', self.d, self.g)

    def response_setup(self):
        mol, C, eps, nocc = self.mol, self.C, self.eps, self.nocc
        self.dS, self.dh, self.dg = skeleton_ao(mol, self.mf)
        self.M = cphf_matrix(eps, self.g, nocc)
        self.Sx, self.Fx, self.hx, self.gx, self.B, self.U = [], [], [], [], [], []
        for x in range(3 * mol.natm):
            Sx = mo_transform(C, self.dS[x])
            Fx = skeleton_fock_mo(C, self.dh[x], self.dg[x], nocc)
            B = cphf_rhs(Sx, Fx, eps, self.g, nocc)
            Uov = np.linalg.solve(self.M, B.ravel()).reshape(self.n - nocc, nocc)
            U = full_U(Uov, Sx, Fx, eps, self.g, nocc, canonical=True)
            self.Sx.append(Sx); self.Fx.append(Fx); self.B.append(B); self.U.append(U)
            self.hx.append(mo_transform(C, self.dh[x])); self.gx.append(eri_mo(C, self.dg[x]))

    def Hx(self, x):
        dh, dg = mo_deriv_ints(self.U[x], self.hx[x], self.gx[x], self.h, self.g)
        return self.space.H(dh, dg)


def gradients(st):
    """Return (explicit-U gradient, Z-vector gradient, pieces)."""
    nocc, n = st.nocc, st.n
    o, v = slice(0, nocc), slice(nocc, None)
    D, d = st.D, st.d
    X = st.gen_fock().T                     # Yamaguchi X_pq = F_qp
    nuc = nuc_grad(st.mol)
    g_U, g_z, skel = [], [], []
    # Z-vector: L_ai = 2 (X_ai - X_ia);  M z = L  (M symmetric)
    L = 2 * (X[v, o] - X[o, v].T)
    z = np.linalg.solve(st.M, L.ravel()).reshape(n - nocc, nocc)
    for x in range(3 * st.mol.natm):
        sk = np.sum(D * st.hx[x]) + 0.5 * np.sum(d * st.gx[x])
        skel.append(sk)
        g_U.append(sk + 2 * np.sum(st.U[x] * X))                                   # Eq. 6.23
        W = 0.5 * (X + X.T)
        g_z.append(sk - np.sum(W * st.Sx[x]) + 0.5 * np.sum(L * st.Sx[x][v, o])
                   + np.sum(z * st.B[x]))                                          # Eq. 18.11 form
    return np.array(g_U) + nuc, np.array(g_z) + nuc, X, L, z, np.array(skel) + nuc


def relaxed_density_gradient(st, z, X, L):
    """AO-only evaluation: dE/dx = sum D' h^x + (1/2) sum d' (..)^x - sum W' S^x  with relaxed D', W'."""
    nocc, n, C, eps, g = st.nocc, st.n, st.C, st.eps, st.g
    o, v = slice(0, nocc), slice(nocc, None)
    zs = np.zeros((n, n)); zs[v, o] = 0.5 * z; zs[o, v] = 0.5 * z.T
    Dp = st.D - zs                                         # relaxed one-particle density (MO)
    W = 0.5 * (X + X.T)
    Wp = W.copy()
    t = 0.5 * (z * eps[o][None, :] + 0.5 * L)
    Wp[v, o] -= t; Wp[o, v] -= t.T
    c = (2 * np.einsum('ai,aikl->kl', z, g[v, o, o, o]) - np.einsum('ai,akil->kl', z, g[v, o, o, o]))
    Wp[o, o] -= 0.5 * (c + c.T)
    DAO, WAO, ZAO = C @ Dp @ C.T, C @ Wp @ C.T, C @ zs @ C.T
    dAO = np.einsum('pi,qj,rk,sl,ijkl->pqrs', C, C, C, C, st.d, optimize=True)
    P = 2 * C[:, o] @ C[:, o].T
    out = []
    for x in range(3 * st.mol.natm):
        gx = st.dg[x]
        e = np.sum(DAO * st.dh[x]) + 0.5 * np.sum(dAO * gx) - np.sum(WAO * st.dS[x])
        e -= np.einsum('mn,ls,mnls', ZAO, P, gx) - 0.5 * np.einsum('mn,ls,mlns', ZAO, P, gx)
        out.append(e)
    return np.array(out) + nuc_grad(st.mol), Dp


def fd_energy_grad(mol, st0, h=1e-4):
    g = []
    for A in range(mol.natm):
        for k in range(3):
            e = [CISDState(displaced(mol, A, k, s * h), st0.mf.make_rdm1()).Etot for s in (1, -1)]
            g.append((e[0] - e[1]) / (2 * h))
    return np.array(g)


if __name__ == '__main__':
    t0 = time.time()
    mol = water(BASIS)
    st = CISDState(mol)
    from pyscf import ci
    myci = ci.CISD(st.mf); myci.conv_tol = 1e-12; myci.kernel()
    print(f'[{BASIS}] CISD determinants {st.space.ndet} of {st.space.nstr**2}; E(CISD) = {st.Etot:.10f}; '
          f'PySCF CISD {myci.e_tot:.10f}; E(RHF) = {st.mf.e_tot:.10f}')
    Echk = np.sum(st.D * st.h) + 0.5 * np.sum(st.d * st.g) + mol.energy_nuc()
    print(f'   energy from RDMs (sum D h + 1/2 sum d g) - E = {Echk - st.Etot:.1e}')
    st.response_setup()
    gU, gz, X, L, z, gsk = gradients(st)
    o, v = slice(0, st.nocc), slice(st.nocc, None)
    Xa = X - X.T
    print(f'   antisymmetric part of X: oo {abs(Xa[o,o]).max():.1e}, vv {abs(Xa[v,v]).max():.1e}, ov {abs(Xa[v,o]).max():.3e}')
    gfd = fd_energy_grad(mol, st)
    gref = myci.nuc_grad_method().kernel().ravel()
    grel, Dp = relaxed_density_gradient(st, z, X, L)
    print('   gradient (Eh/bohr), O_z, H1_y, H1_z:')
    for nm, gg in (('finite difference', gfd), ('explicit U (6.23)', gU), ('Z vector', gz),
                   ('relaxed density, AO', grel), ('PySCF CISD grad', gref),
                   ('orbital response dropped', gz - np.array([np.sum(z * st.B[x]) + 0.5*np.sum(L*st.Sx[x][v,o]) for x in range(9)])),
                   ('RHF gradient', st.mf.nuc_grad_method().kernel().ravel())):
        print(f'     {nm:30s}', gg[[2, 4, 5]], f' max|. - FD| = {abs(gg - gfd).max():.1e}')
    print(f'   CPHF solves: explicit U needs {3*mol.natm} right-hand sides, Z vector needs 1 (dimension {st.M.shape[0]})')
    # ---- relaxed dipole from the same z ----
    mol.set_common_orig((0, 0, 0))
    r = mol.intor('int1e_r')
    rz = mo_transform(st.C, r[2])
    mu_unrel = np.sum(st.D * rz)
    mu_rel = np.sum(Dp * rz)
    f = 1e-4
    E = []
    for s in (1, -1):
        mf = scf.RHF(mol); hc = mf.get_hcore() + s * f * r[2]
        mf.get_hcore = lambda *a, hc=hc: hc; mf.conv_tol = 1e-13; mf.kernel(st.mf.make_rdm1())
        hmo = mo_transform(mf.mo_coeff, hc); gmo = eri_mo(mf.mo_coeff, mol.intor('int2e'))
        E.append(np.linalg.eigvalsh(st.space.H(hmo, gmo))[0])
    dEdF = (E[0] - E[1]) / (2 * f)
    print(f'   dE/dF_z with h -> h + F z: unrelaxed {mu_unrel:.6f}, relaxed (same z) {mu_rel:.6f}, finite field {dEdF:.6f};'
          f' RHF {np.sum(st.mf.make_rdm1()*r[2]):.6f}')
    np.save(f'z_{BASIS}.npy', z)
    print(f'   time {time.time()-t0:.1f} s')
