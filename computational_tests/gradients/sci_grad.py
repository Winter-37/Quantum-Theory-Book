"""Selected-CI analytic gradient on canonical RHF orbitals (Coe, JCTC 19, 874 (2023)), verified.
Water, STO-3G, R(OH) = 1.95 bohr, HOH = 110 deg (same geometry as ci_grad.py).
The determinant list is chosen once, at the reference geometry, as all FCI determinants with |c| > tau,
and is then held fixed (by orbital index) at displaced geometries.
Gradients compared:
  FD        central finite differences of the fixed-list CI energy (step 1e-4 bohr)
  full      Coe Eq. 7: skeleton + 2 sum_pq U^x_pq X_pq, U^x canonical for all pairs (9 CPHF solves)
  zvec      Coe Eqs. 15-16: one CPHF-sized solve with the modified Lagrangian dF'
  vo-only   oo and vv response dropped (U_oo, U_vv = -S/2), i.e. treating the list as if invariant
  noCPHF    Coe's 'analytic without CPHF': 2 sum dF U dropped, -sum F~ S kept
  seminum   Coe Eq. 5: RDMs fixed, MO-integral derivatives by central differences
  HF force  <Psi|dH/dX|Psi>, operator derivative only (Hellmann-Feynman)
"""
import numpy as np, sys, time
sys.path.insert(0, '.')
from common import *
from ci_grad import mo_deriv_ints
from pyscf import fci, symm, gto
from pyscf.fci import cistring, direct_spin1
np.set_printoptions(precision=6, suppress=True, linewidth=160)


class ListSpace:
    """CI in an arbitrary fixed list of determinants (flat indices into the alpha x beta string grid)."""
    def __init__(self, norb, nocc, sel):
        self.norb, self.nocc, self.nelec = norb, nocc, (nocc, nocc)
        self.nstr = cistring.num_strings(norb, nocc)
        self.sel = np.array(sorted(sel)); self.ndet = len(self.sel)

    def H(self, h1, g2):
        h2 = direct_spin1.absorb_h1e(h1, g2, self.norb, self.nelec, 0.5)
        Hm = np.zeros((self.ndet, self.ndet)); n = self.nstr ** 2
        for k, I in enumerate(self.sel):
            e = np.zeros(n); e[I] = 1.0
            Hm[:, k] = direct_spin1.contract_2e(h2, e.reshape(self.nstr, self.nstr),
                                                self.norb, self.nelec).ravel()[self.sel]
        return 0.5 * (Hm + Hm.T)

    def full(self, c):
        v = np.zeros(self.nstr ** 2); v[self.sel] = c
        return v.reshape(self.nstr, self.nstr)

    def rdm12(self, c):
        return direct_spin1.make_rdm12(self.full(c), self.norb, self.nelec)


class State:
    def __init__(self, mol, sel, dm0=None, Cref=None, Sref=None):
        self.mol = mol
        mf = rhf(mol, dm0); C = mf.mo_coeff.copy()
        if Cref is not None:
            C *= np.sign(np.diag(Cref.T @ Sref @ C))
        self.mf, self.C, self.eps = mf, C, mf.mo_energy
        self.nocc = mol.nelectron // 2; self.n = C.shape[1]
        self.h = mo_transform(C, mf.get_hcore()); self.g = eri_mo(C, mol.intor('int2e'))
        self.space = ListSpace(self.n, self.nocc, sel)
        w, V = np.linalg.eigh(self.space.H(self.h, self.g))
        self.Eel, self.c = w[0], V[:, 0]
        self.Etot = self.Eel + mol.energy_nuc()
        self.D, self.d = self.space.rdm12(self.c)
        self.X = (self.D @ self.h.T + np.einsum('mqrs,nqrs->mn', self.d, self.g)).T   # X_pq = F_qp

    def setup(self):
        mol, C, eps, nocc = self.mol, self.C, self.eps, self.nocc
        self.dS, self.dh, self.dg = skeleton_ao(mol, self.mf)
        self.M = cphf_matrix(eps, self.g, nocc)
        self.Sx, self.Fx, self.hx, self.gx, self.B, self.Uc, self.Unc = [], [], [], [], [], [], []
        for x in range(3 * mol.natm):
            Sx = mo_transform(C, self.dS[x]); Fx = skeleton_fock_mo(C, self.dh[x], self.dg[x], nocc)
            B = cphf_rhs(Sx, Fx, eps, self.g, nocc)
            Uov = np.linalg.solve(self.M, B.ravel()).reshape(self.n - nocc, nocc)
            self.Uc.append(full_U(Uov, Sx, Fx, eps, self.g, nocc, canonical=True))
            self.Unc.append(full_U(Uov, Sx, Fx, eps, self.g, nocc, canonical=False))
            self.Sx.append(Sx); self.Fx.append(Fx); self.B.append(B)
            self.hx.append(mo_transform(C, self.dh[x])); self.gx.append(eri_mo(C, self.dg[x]))


def gradients(st):
    n, nocc, X, eps, g = st.n, st.nocc, st.X, st.eps, st.g
    o, v = slice(0, nocc), slice(nocc, None)
    nuc = nuc_grad(st.mol)
    sk = np.array([np.sum(st.D * st.hx[x]) + 0.5 * np.sum(st.d * st.gx[x]) for x in range(len(st.Sx))])
    full = sk + np.array([2 * np.sum(U * X) for U in st.Uc]) + nuc
    vo_only = sk + np.array([2 * np.sum(U * X) for U in st.Unc]) + nuc
    W = 0.5 * (X + X.T)
    # Coe 'without CPHF': drop 2 sum_{t>p} dF U, keep -sum F~ S  (F~ = symmetrized here; equal value)
    nocphf = sk - np.array([np.sum(W * S) for S in st.Sx]) + nuc
    # ---- Z vector with the modified Lagrangian (Coe Eq. 16), derived as T^x = T0^x + l . U^x_vo
    # l_ai = 2(X_ai - X_ia) + sum_{p != q, same block} 2 X_pq A_pq,ai / (e_q - e_p)
    l = 2 * (X[v, o] - X[o, v].T)
    A = (4 * g[:, :, v, o] - np.einsum('paqi->pqai', g[:, v, :, o]) - np.einsum('piqa->pqai', g[:, o, :, v]))
    gap = eps[None, :] - eps[:, None]                     # e_q - e_p
    mask = np.zeros((n, n), bool); mask[o, o] = True; mask[v, v] = True; np.fill_diagonal(mask, False)
    fac = np.where(mask, 2 * X / np.where(mask, gap, 1.0), 0.0)
    l_mod = l + np.einsum('pq,pqai->ai', fac, A)
    zp = np.linalg.solve(st.M, l_mod.ravel()).reshape(n - nocc, nocc)
    zvec = []
    for x in range(len(st.Sx)):
        U0 = full_U(np.zeros((n - nocc, nocc)), st.Sx[x], st.Fx[x], eps, g, nocc, canonical=True)
        zvec.append(sk[x] + 2 * np.sum(U0 * X) + np.sum(zp * st.B[x]))
    return dict(full=full, zvec=np.array(zvec) + nuc, vo_only=vo_only, noCPHF=nocphf, skel=sk + nuc), zp, l, l_mod


def hf_force(st):
    """<Psi| dV_ne/dR_A |Psi> + dV_nn/dR_A, AOs held fixed (operator derivative only).
    d/dR_A <mu|-Z_A/|r-R_A||nu> = -Z_A (<d mu|1/r_A|nu> + <mu|1/r_A|d nu>)  (integration by parts)."""
    mol = st.mol; P = st.C @ st.D @ st.C.T; out = []
    for A in range(mol.natm):
        with mol.with_rinv_at_nucleus(A):
            ip = mol.intor('int1e_iprinv', comp=3)
        for k in range(3):
            out.append(-mol.atom_charge(A) * np.sum(P * (ip[k] + ip[k].T)))
    return np.array(out) + nuc_grad(mol)


def hf_force_fd(st, h=1e-5):
    """Same quantity by finite differences of the nuclear-attraction integral, AOs fixed."""
    mol = st.mol; P = st.C @ st.D @ st.C.T; R = coords(mol); out = []
    for A in range(mol.natm):
        for k in range(3):
            e = []
            for s in (1, -1):
                r = R[A].copy(); r[k] += s * h
                with mol.with_rinv_origin(r):
                    e.append(-mol.atom_charge(A) * np.sum(P * mol.intor('int1e_rinv')))
            out.append((e[0] - e[1]) / (2 * h))
    return np.array(out) + nuc_grad(mol)


def fd(mol, st0, sel, h=1e-4):
    out = []
    for A in range(mol.natm):
        for k in range(3):
            e = [State(displaced(mol, A, k, s * h), sel, st0.mf.make_rdm1(), st0.C, st0.mf.get_ovlp()).Etot
                 for s in (1, -1)]
            out.append((e[0] - e[1]) / (2 * h))
    return np.array(out)


def seminumerical(mol, st0, sel, h=1e-4):
    """Coe Eq. 5: sum D dh/dx + 1/2 sum d d(pq|rs)/dx with D, d fixed and MO integrals differenced."""
    out = []
    for A in range(mol.natm):
        for k in range(3):
            e = []
            for s in (1, -1):
                m = displaced(mol, A, k, s * h)
                mf = rhf(m, st0.mf.make_rdm1()); C = mf.mo_coeff.copy()
                C *= np.sign(np.diag(st0.C.T @ st0.mf.get_ovlp() @ C))
                hm = mo_transform(C, mf.get_hcore()); gm = eri_mo(C, m.intor('int2e'))
                e.append(np.sum(st0.D * hm) + 0.5 * np.sum(st0.d * gm) + m.energy_nuc())
            out.append((e[0] - e[1]) / (2 * h))
    return np.array(out)


def torque(mol, gg):
    return abs(np.cross(coords(mol), gg.reshape(-1, 3)).sum(0)).max()


def orb_irreps(mol, C):
    ms = mol.copy(); ms.symmetry = True; ms.build()
    assert np.allclose(ms.atom_coords(), mol.atom_coords()), 'symmetry build reoriented the molecule'
    return symm.label_orb_symm(ms, ms.irrep_name, ms.symm_orb, C)


if __name__ == '__main__':
    t0 = time.time()
    mol = water('sto-3g')
    mf = rhf(mol); nocc = mol.nelectron // 2; n = mf.mo_coeff.shape[1]
    h = mo_transform(mf.mo_coeff, mf.get_hcore()); g = eri_mo(mf.mo_coeff, mol.intor('int2e'))
    efci, cfci = fci.direct_spin1.kernel(h, g, n, (nocc, nocc), tol=1e-13)
    print(f'E(RHF) {mf.e_tot:.10f}   E(FCI) {efci + mol.energy_nuc():.10f}   FCI determinants {cfci.size}')
    irr = orb_irreps(mol, mf.mo_coeff)
    print('MO irreps:', list(irr), ' eps:', np.round(mf.mo_energy, 4))
    for tau in [float(t) for t in (sys.argv[1:] or ['0.05', '0.02', '0.0'])]:
        sel = np.flatnonzero(np.abs(cfci.ravel()) > tau) if tau > 0 else np.arange(cfci.size)
        st = State(mol, sel); st.setup()
        o, v = slice(0, nocc), slice(nocc, None)
        dF = st.X - st.X.T
        offirr = max(abs(dF[p, q]) for p in range(n) for q in range(n) if irr[p] != irr[q])
        offd = lambda b: abs(dF[b, b] - np.diag(np.diag(dF[b, b]))).max()
        G, zp, l, lmod = gradients(st)
        gfd = fd(mol, st, sel)
        gsn = seminumerical(mol, st, sel)
        ghf, ghf_fd = hf_force(st), hf_force_fd(st)
        print(f'\n=== tau = {tau}: {st.space.ndet} of {cfci.size} determinants; E = {st.Etot:.10f} '
              f'(E - E_FCI = {st.Etot - efci - mol.energy_nuc():.2e})')
        print(f'   |dF| = |X - X^T| max: oo {offd(o):.2e}  vv {offd(v):.2e}  vo {abs(dF[v,o]).max():.2e};'
              f'  pairs in different irreps {offirr:.1e}')
        mg = min(abs(st.eps[p]-st.eps[q]) for p in range(n) for q in range(p) if ((p<nocc)==(q<nocc)) and abs(dF[p,q])>1e-10) if offd(o)+offd(v)>1e-10 else float('nan')
        print(f'   smallest same-block gap with dF != 0: {mg:.4f} Eh;  |l_mod - l| max = {abs(lmod-l).max():.2e}')
        print('   gradient (Eh/bohr)          O_z        H1_y       H1_z    max|.-FD|  net force  net torque')
        rows = [('finite difference', gfd), ('full U, all pairs (Eq. 7)', G['full']), ('Z vector, Eq. 16', G['zvec']),
                ('seminumerical (Eq. 5)', gsn), ('vo response only', G['vo_only']), ('without CPHF', G['noCPHF']),
                ('Hellmann-Feynman force', ghf)]
        for nm, gg in rows:
            net = abs(gg.reshape(-1, 3).sum(0)).max()
            print(f'   {nm:27s}', gg[[2, 4, 5]], f' {abs(gg - gfd).max():.1e}   {net:.1e}   {torque(mol, gg):.1e}')
        print(f'   HF force analytic vs FD of V_ne: {abs(ghf - ghf_fd).max():.1e}')
    print(f'time {time.time() - t0:.1f} s')
