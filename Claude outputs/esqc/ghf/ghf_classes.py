"""Symmetry diagnostics for the H3/STO-3G Hartree-Fock solutions (Stuber-Paldus classes).
Sz variance of a determinant: sum_{i occ, a virt} |<a|sz|i>|^2 ; complex conjugation test: max|Im C|."""
import numpy as np, scipy.linalg as sl
from pyscf import scf
from ghf_h3 import run, spin_guess
R = 1.5
mol, rohf, uhf, g = run(R); n = mol.nao; S = mol.intor('int1e_ovlp')
def sz_var(mf):
    C = mf.mo_coeff; occ = mf.mo_occ > 0
    Sz = 0.5*sl.block_diag(S, -S); A = C.conj().T @ Sz @ C
    return np.sum(abs(A[np.ix_(~occ, occ)])**2), np.real(np.trace(A[np.ix_(occ, occ)]))
gu = scf.addons.convert_to_ghf(uhf)
for name, mf in [("UHF (as GHF)", gu), ("real GHF", g)]:
    v, m = sz_var(mf)
    print(f"{name:14s} E={mf.e_tot:.8f}  <Sz>={m:+.4f}  Var(Sz)={v:.4f}  <S2>={mf.spin_square()[0]:.4f}  max|Im C|={abs(np.imag(mf.mo_coeff)).max():.1e}")
# try to lower the real GHF solution with complex (time-reversal / K breaking) perturbations
best = None
for seed in range(6):
    rng = np.random.default_rng(seed)
    P0 = g.make_rdm1().astype(complex)
    X = rng.normal(size=(2*n, 2*n)) + 1j*rng.normal(size=(2*n, 2*n)); X = 0.05*(X + X.conj().T)
    gc = scf.GHF(mol); gc.conv_tol = 1e-12; gc.max_cycle = 500
    gc.kernel(P0 + X)
    if best is None or gc.e_tot < best.e_tot: best = gc
print(f"complex GHF from 6 complex-perturbed starts: lowest E={best.e_tot:.8f}, E - E(real GHF) = {best.e_tot-g.e_tot:.1e}")
# complex stability check of the real GHF via its Hessian (pyscf: real GHF internal only) -> report
