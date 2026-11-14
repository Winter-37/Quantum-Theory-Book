"""First-order CPCI (Yamaguchi Eq. 12.11) and the CISD Hessian (Eq. 6.79), water STO-3G.
CPCI:  sum_J (H_IJ - d_IJ E + 2 C_I C_J) dC_J/dx = - sum_J (dH_IJ/dx - d_IJ dE/dx) C_J
Hessian: d2E/dxdy = sum_IJ C_I C_J d2H_IJ/dxdy - 2 sum_IJ dC_I/dx (H_IJ - d_IJ E) dC_J/dy
The first Hessian term is obtained as a finite difference of C0^T (dH/dx)(R) C0 with the CI vector C0 frozen
(orbitals follow the geometry through CPHF at each R); the CPCI term is analytic.
Reference: central differences of the analytic CISD gradient.
"""
import numpy as np, sys, time
sys.path.insert(0, '.')
from common import *
from ci_grad import CISDState, gradients

np.set_printoptions(precision=6, suppress=True, linewidth=160)
t0 = time.time()
mol = water('sto-3g')
st = CISDState(mol); st.response_setup()
S0 = mol.intor('int1e_ovlp')
n3 = 3 * mol.natm
H0, E0, c0 = st.Hci, st.Eel, st.c
Kmat = H0 - E0 * np.eye(len(c0)) + 2 * np.outer(c0, c0)
gU, gz, X, L, z, _ = gradients(st)

dC, Ex = [], []
for x in range(n3):
    Hx = st.Hx(x)
    ex = c0 @ Hx @ c0                        # Eq. 6.16: dE/dx = C^T (dH/dx) C
    Ex.append(ex)
    dC.append(np.linalg.solve(Kmat, -(Hx - ex * np.eye(len(c0))) @ c0))
dC = np.array(dC)
print(f'max|C^T(dH/dx)C + V_nuc^x - gradient| = {abs(np.array(Ex) + nuc_grad(mol) - gz).max():.1e}')
print(f'max|C . dC/dx| (normalization, Eq. 12.12) = {abs(dC @ c0).max():.1e}')

h = 1e-4
states = {}
for A in range(mol.natm):
    for k in range(3):
        for s in (1, -1):
            sd = CISDState(displaced(mol, A, k, s * h), st.mf.make_rdm1(), Cref=st.C, Sref=S0)
            sd.align(c0); sd.response_setup()
            states[(3 * A + k, s)] = sd
worst = 0
for y in range(n3):
    fd = (states[(y, 1)].c - states[(y, -1)].c) / (2 * h)
    worst = max(worst, abs(fd - dC[y]).max())
print(f'CPCI dC/dx (canonical U) vs finite-difference CI vectors: max diff {worst:.1e}; max|dC/dx| {abs(dC).max():.3f}')

# Hessian
Hss = np.zeros((n3, n3)); Hfd = np.zeros((n3, n3))
for y in range(n3):
    gp = np.array([c0 @ states[(y, 1)].Hx(x) @ c0 for x in range(n3)]) + nuc_grad(states[(y, 1)].mol)
    gm = np.array([c0 @ states[(y, -1)].Hx(x) @ c0 for x in range(n3)]) + nuc_grad(states[(y, -1)].mol)
    Hss[:, y] = (gp - gm) / (2 * h)
    Hfd[:, y] = (gradients(states[(y, 1)])[1] - gradients(states[(y, -1)])[1]) / (2 * h)
Hcpci = -2 * dC @ (H0 - E0 * np.eye(len(c0))) @ dC.T
Hci = Hss + Hcpci
print(f'CISD Hessian: max|Eq.6.79 - FD of analytic gradient| = {abs(Hci - Hfd).max():.1e}; '
      f'asymmetry of Eq.6.79 {abs(Hci - Hci.T).max():.1e}; max|H| = {abs(Hfd).max():.3f}')
print(f'   size of the CPCI term: max {abs(Hcpci).max():.4f};  O_z,O_z: fixed-C part {Hss[2,2]:.5f}, CPCI part {Hcpci[2,2]:.5f}, total {Hci[2,2]:.5f}')
print(f'   CPCI term is negative semidefinite: eigenvalues {np.linalg.eigvalsh(0.5*(Hcpci+Hcpci.T))[[0,-1]]}')
# RHF Hessian vs CISD Hessian, harmonic frequencies would need mass weighting; just report O_z,O_z
print(f'time {time.time()-t0:.0f} s')

# dependence of dC/dx on the (arbitrary) oo/vv part of U
from ci_grad import mo_deriv_ints
diff = 0
for x in range(n3):
    Us = full_U(st.U[x][st.nocc:, :st.nocc], st.Sx[x], st.Fx[x], st.eps, st.g, st.nocc, canonical=False)
    dh_, dg_ = mo_deriv_ints(Us, st.hx[x], st.gx[x], st.h, st.g)
    Hxs = st.space.H(dh_, dg_)
    ex = c0 @ Hxs @ c0
    dCs = np.linalg.solve(Kmat, -(Hxs - ex * np.eye(len(c0))) @ c0)
    diff = max(diff, abs(dCs - dC[x]).max())
    assert abs(ex - Ex[x]) < 1e-12
print(f'dC/dx with symmetric (non-canonical) oo/vv U differs from canonical by up to {diff:.3f}; dE/dx unchanged')
