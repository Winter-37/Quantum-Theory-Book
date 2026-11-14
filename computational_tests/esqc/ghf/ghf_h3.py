"""GHF for equilateral H3 (doublet), STO-3G: ROHF vs UHF vs collinear/non-collinear GHF.
Checks Loos Eqs. (3.41)-(3.51): spinor Fock matrix, energy, magnetization blocks, collinearity."""
import numpy as np, scipy.linalg as sl
from pyscf import gto, scf
from pyscf.scf import stability

def h3(R, basis='sto-3g'):
    h = R*np.sqrt(3)/2
    return gto.M(atom=f"H 0 0 0; H {R} 0 0; H {R/2} {h} 0", basis=basis, spin=1, verbose=0)

def spin_guess(mol, angles):
    """one electron per H 1s, spin direction at angle theta in the xz plane (real spinors)"""
    n = mol.nao; S = mol.intor('int1e_ovlp'); C = np.zeros((2*n, 3))
    for A, th in enumerate(angles):
        C[A, A] = np.cos(th/2); C[n+A, A] = np.sin(th/2)
    S2 = sl.block_diag(S, S); C = C @ sl.fractional_matrix_power(C.T@S2@C, -0.5)
    return C @ C.T

def blocks(P, n):
    return P[:n,:n], P[:n,n:], P[n:,:n], P[n:,n:]

def magnetization(P, n):
    aa, ab, ba, bb = blocks(P, n)
    sym = lambda M: 0.5*(M+M.T)          # only the symmetric part contributes to m_k(r) for real AOs
    return [sym(np.real(0.5*(ab+ba))), sym(np.real((ba-ab)/2j)), sym(np.real(0.5*(aa-bb)))]

def gram(P, mol):
    S = mol.intor('int1e_ovlp'); M = magnetization(P, mol.nao)
    return np.array([[np.trace(a@S@b@S) for b in M] for a in M])

def atom_moments(P, mol):
    S = mol.intor('int1e_ovlp'); M = magnetization(P, mol.nao)
    return np.array([[np.trace((Mk@S)[s0:s1, s0:s1]) for Mk in M]
                     for s0, s1 in mol.aoslice_by_atom()[:, 2:]])

def run(R, verbose=False):
    mol = h3(R); n = mol.nao
    rohf = scf.ROHF(mol).run(conv_tol=1e-12)
    uhf = scf.UHF(mol); uhf.conv_tol = 1e-12; uhf.kernel()
    mo, _, st, _ = uhf.stability(return_status=True)
    while not st:
        uhf.kernel(uhf.make_rdm1(mo, uhf.mo_occ)); mo, _, st, _ = uhf.stability(return_status=True)
    g = scf.GHF(mol); g.conv_tol = 1e-12; g.max_cycle = 500
    g.kernel(spin_guess(mol, [0, 2*np.pi/3, 4*np.pi/3]))
    return mol, rohf, uhf, g

if __name__ == '__main__':
    print(" R/A     E_ROHF        E_UHF       <S2>_UHF    E_GHF       E_GHF-E_UHF(mEh)  <S2>_GHF  Gram eigs(GHF)")
    for R in [0.8, 1.0, 1.5, 2.0, 2.5, 3.0]:
        mol, rohf, uhf, g = run(R)
        w = np.linalg.eigvalsh(gram(g.make_rdm1(), mol))
        print(f"{R:4.1f} {rohf.e_tot:12.8f} {uhf.e_tot:12.8f} {uhf.spin_square()[0]:8.4f} {g.e_tot:12.8f} {1e3*(g.e_tot-uhf.e_tot):10.3f} {g.spin_square()[0]:8.4f}  {np.round(w,5)}")
    # detailed checks at R = 1.5 A
    mol, rohf, uhf, g = run(1.5); n = mol.nao
    P = g.make_rdm1(); aa, ab, ba, bb = blocks(P, n)
    H = mol.intor('int1e_kin') + mol.intor('int1e_nuc'); eri = mol.intor('int2e')
    J = lambda D: np.einsum('mnls,ls->mn', eri, D); K = lambda D: np.einsum('mlsn,ls->mn', eri, D)
    F = np.block([[H+J(aa)+J(bb)-K(aa), -K(ab)], [-K(ba), H+J(aa)+J(bb)-K(bb)]])
    print("\nR=1.5: max|F(Eq.3.49) - F_pyscf| =", abs(F-g.get_fock()).max())
    E = 0.5*np.trace((sl.block_diag(H, H)+F)@P) + mol.energy_nuc()
    print("E = 1/2 Tr[(H+F)P] + Vnn :", E, " pyscf:", g.e_tot)
    m = atom_moments(P, mol)
    print("atomic spin moments (x,y,z):\n", np.round(m, 4))
    ang = [np.degrees(np.arccos(m[i]@m[j]/np.linalg.norm(m[i])/np.linalg.norm(m[j]))) for i, j in [(0,1),(1,2),(0,2)]]
    print("angles between moments:", np.round(ang, 2), " total moment:", np.round(m.sum(0), 8))
    print("Gram eigs, UHF embedded as GHF:", np.round(np.linalg.eigvalsh(gram(scf.addons.convert_to_ghf(uhf).make_rdm1(), mol)), 6))
    e = stability.ghf_stability(scf.addons.convert_to_ghf(uhf), return_status=True)
    print("GHF stability of the UHF solution (stable?):", e[-1] if isinstance(e, tuple) else e)
    print("GHF orbital energies:", np.round(g.mo_energy, 5))
