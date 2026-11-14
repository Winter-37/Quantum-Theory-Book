"""RHF gradient (Yamaguchi Eq. 4.21/4.25), first-order CPHF (Eq. 10.22) and RHF Hessian (Eq. 4.54),
checked against PySCF and finite differences. Water, R(OH)=1.95 bohr, HOH=110 deg."""
import numpy as np, sys
sys.path.insert(0, '.')
from common import *
np.set_printoptions(precision=6, suppress=True, linewidth=150)

def analysis(basis):
    mol = water(basis)
    mf = rhf(mol)
    C, eps = mf.mo_coeff, mf.mo_energy
    nocc = mol.nelectron // 2
    n = C.shape[1]
    o, v = slice(0, nocc), slice(nocc, None)
    eri = eri_mo(C, mol.intor('int2e'))
    dS, dh, dg = skeleton_ao(mol, mf)
    P = 2 * C[:, o] @ C[:, o].T
    W = 2 * C[:, o] @ np.diag(eps[o]) @ C[:, o].T
    ncoord = 3 * mol.natm
    # ---- gradient, AO form (Eq. 4.25 rewritten with P, W) ----
    g_ao = np.array([np.sum(P * dh[x]) + 0.5 * np.einsum('mn,ls,mnls', P, P, dg[x])
                     - 0.25 * np.einsum('ml,ns,mnls', P, P, dg[x]) - np.sum(W * dS[x])
                     for x in range(ncoord)]) + nuc_grad(mol)
    # ---- gradient, MO form (Eq. 4.21) ----
    g_mo = []
    for x in range(ncoord):
        hx = mo_transform(C, dh[x]); Sx = mo_transform(C, dS[x])
        gx = eri_mo(C[:, :], dg[x]) if n < 15 else None
        e = 2 * np.trace(hx[o, o]) + 2 * np.einsum('iijj', gx[o, o, o, o]) - np.einsum('ijij', gx[o, o, o, o]) \
            - 2 * np.sum(np.diag(Sx)[o] * eps[o])
        g_mo.append(e)
    g_mo = np.array(g_mo) + nuc_grad(mol)
    g_ref = mf.nuc_grad_method().kernel().ravel()
    print(f'[{basis}] |g| = {np.linalg.norm(g_ref):.5f}; max|AO form - PySCF| = {abs(g_ao-g_ref).max():.1e};'
          f' max|MO form - PySCF| = {abs(g_mo-g_ref).max():.1e}')
    # ---- CPHF ----
    M = cphf_matrix(eps, eri, nocc)
    Us, Fsk, Sxs = [], [], []
    for x in range(ncoord):
        Sx = mo_transform(C, dS[x])
        Fx = skeleton_fock_mo(C, dh[x], dg[x], nocc)
        B = cphf_rhs(Sx, Fx, eps, eri, nocc)
        Uov = np.linalg.solve(M, B.ravel()).reshape(n - nocc, nocc)
        U = full_U(Uov, Sx, Fx, eps, eri, nocc, canonical=True)
        Us.append(U); Fsk.append(Fx); Sxs.append(Sx)
        dF = fock_derivative_mo(U, Fx, eps, eri, nocc)
        off = dF - np.diag(np.diag(dF))
        if x == 0:
            print(f'   CPHF dim {M.shape[0]}; coordinate O_x: max|dF_offdiag| with canonical U = {abs(off).max():.1e}')
    return mol, mf, C, eps, nocc, eri, dS, dh, dg, Us, Fsk, Sxs, M

def U_vs_fd(mol, mf, C, Us, h=1e-4):
    S0 = mol.intor('int1e_ovlp'); worst = 0
    for A in range(mol.natm):
        for k in range(3):
            Cs = []
            for s in (+1, -1):
                m = displaced(mol, A, k, s * h)
                mm = rhf(m, mf.make_rdm1())
                Cd = mm.mo_coeff
                sgn = np.sign(np.diag(C.T @ S0 @ Cd)); Cs.append(Cd * sgn)
            dC = (Cs[0] - Cs[1]) / (2 * h)
            U_fd = C.T @ S0 @ dC     # since C^T S0 C = 1 -> U = C^T S0 dC/dx
            worst = max(worst, abs(U_fd - Us[3 * A + k]).max())
    return worst

for basis in ('sto-3g', '6-31g'):
    out = analysis(basis)
    mol, mf, C, eps, nocc, eri, dS, dh, dg, Us, Fsk, Sxs, M = out
    print('   max |U(CPHF, canonical) - U(finite difference of canonical MOs)| =', f'{U_vs_fd(mol, mf, C, Us):.1e}')
    if basis == 'sto-3g':
        np.save('h2o_sto3g_U.npy', np.array(Us))

# ---------------- RHF Hessian, Yamaguchi Eq. (4.54) ----------------
def skeleton_first(mol, P, W):
    dS, dh, dg = skeleton_ao(mol)
    return np.array([np.sum(P * dh[x]) + 0.5 * np.einsum('mn,ls,mnls', P, P, dg[x])
                     - 0.25 * np.einsum('ml,ns,mnls', P, P, dg[x]) - np.sum(W * dS[x])
                     for x in range(3 * mol.natm)]) + nuc_grad(mol)

def hessian(basis, canonical=True, h=1e-4):
    mol, mf, C, eps, nocc, eri, dS, dh, dg, Us, Fsk, Sxs, M = analysis(basis)
    o = slice(0, nocc)
    if not canonical:
        Us = [full_U(U[nocc:, :nocc], Sxs[x], Fsk[x], eps, eri, nocc, canonical=False) for x, U in enumerate(Us)]
    P = 2 * C[:, o] @ C[:, o].T
    W = 2 * C[:, o] @ np.diag(eps[o]) @ C[:, o].T
    n3 = 3 * mol.natm
    # skeleton second-derivative part (+ nuclear): d/dy of the skeleton gradient at FIXED P, W
    Hsk = np.zeros((n3, n3))
    for A in range(mol.natm):
        for k in range(3):
            y = 3 * A + k
            Hsk[:, y] = (skeleton_first(displaced(mol, A, k, h), P, W)
                         - skeleton_first(displaced(mol, A, k, -h), P, W)) / (2 * h)
    Hsk = 0.5 * (Hsk + Hsk.T)
    # response part
    Ar = 4 * eri - eri.transpose(0, 2, 1, 3) - eri.transpose(0, 3, 2, 1)   # A_pq,rs = 4(pq|rs)-(pr|qs)-(ps|qr)
    Ar = Ar[:, o, :, o]                                                    # A_pj,ql, j,l occupied
    Hr = np.zeros((n3, n3))
    for x in range(n3):
        for y in range(n3):
            Ux, Uy, Sx, Sy = Us[x], Us[y], Sxs[x], Sxs[y]
            eta_ii = 2 * (np.einsum('im,im->i', Ux[o], Uy[o]) - np.einsum('im,im->i', Sx[o], Sy[o]))
            t = -2 * np.sum(eta_ii * eps[o])
            t += 4 * (np.sum(Uy[:, o] * Fsk[x][:, o]) + np.sum(Ux[:, o] * Fsk[y][:, o]))
            t += 4 * np.sum(Ux[:, o] * Uy[:, o] * eps[:, None])
            t += 4 * np.einsum('pj,ql,pjql', Ux[:, o], Uy[:, o], Ar)
            Hr[x, y] = t
    Htot = Hsk + Hr
    Href = mf.Hessian().kernel().transpose(0, 2, 1, 3).reshape(n3, n3)
    print(f'[{basis}] Hessian ({"canonical" if canonical else "symmetric oo/vv"} U): max|Eq.4.54 - PySCF| = '
          f'{abs(Htot - Href).max():.1e}; asymmetry {abs(Htot - Htot.T).max():.1e}; max|H| = {abs(Href).max():.3f}')
    return Htot, Href, Hsk, Hr

for b in ('sto-3g', '6-31g'):
    H, Hr_, Hsk, Hr = hessian(b)
    if b == '6-31g':
        hessian(b, canonical=False)
        w = np.linalg.eigvalsh(H)
        print('   skeleton-only max|H| vs response max|H|:', f'{abs(Hsk).max():.3f}', f'{abs(Hr).max():.3f}')
        print('   O z,z element: skeleton', f'{Hsk[2,2]:.5f}', 'response', f'{Hr[2,2]:.5f}', 'total', f'{H[2,2]:.5f}')
