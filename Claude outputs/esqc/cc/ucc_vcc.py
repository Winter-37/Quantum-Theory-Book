"""Projective CCSD, variational CCSD (VCC) and unitary CCSD (UCC) with exact exponentials in Fock space,
against FCI, for linear H4/STO-3G. Also: non-termination of the UCC BCH series."""
import numpy as np, itertools, scipy.linalg as sl, scipy.optimize as so
from pyscf import gto, scf, cc, fci
from fermi import jw_ops, basis_index, spin_orbital_integrals, hamiltonian_matrix
from math import factorial

def build(R):
    mol = gto.M(atom='; '.join(f'H 0 0 {k*R}' for k in range(4)), basis='sto-3g', verbose=0)
    h, g, no, enuc, mf = spin_orbital_integrals(mol)
    n = h.shape[0]; ops = jw_ops(n); ad = [o.T.tocsr() for o in ops]
    H = hamiltonian_matrix(h, g, ops).toarray()
    ref = np.zeros(2**n); ref[basis_index(range(no), n)] = 1
    spin = np.array([0, 1]*(n//2))
    occ, vir = range(no), range(no, n)
    taus = []
    for i, a in itertools.product(occ, vir):
        if spin[i] == spin[a]: taus.append((ad[a] @ ops[i]).toarray())
    for (i, j), (a, b) in itertools.product(itertools.combinations(occ, 2), itertools.combinations(vir, 2)):
        if spin[i] + spin[j] == spin[a] + spin[b]: taus.append((ad[a] @ ad[b] @ ops[j] @ ops[i]).toarray())
    return mol, mf, H, ref, taus, enuc

def Tmat(t, taus): return sum(ti*tau for ti, tau in zip(t, taus))

def e_vcc(t, H, ref, taus):
    psi = sl.expm(Tmat(t, taus)) @ ref; return psi @ H @ psi / (psi @ psi)

def e_ucc(t, H, ref, taus):
    T = Tmat(t, taus); psi = sl.expm(T - T.T) @ ref; return psi @ H @ psi

def ccsd_proj(H, ref, taus, t0):
    def res(t):
        T = Tmat(t, taus); Hb = sl.expm(-T) @ H @ sl.expm(T) @ ref
        return np.array([ref @ tau.T @ Hb for tau in taus])
    t = so.root(res, t0, tol=1e-12).x
    T = Tmat(t, taus); return ref @ sl.expm(-T) @ H @ sl.expm(T) @ ref, t

if __name__ == "__main__":
  for R in (0.8, 1.2, 1.6, 2.0):
      mol, mf, H, ref, taus, enuc = build(R)
      Efci = np.linalg.eigvalsh(H[np.ix_(*(np.where([bin(k).count('1') == 4 for k in range(H.shape[0])])[0],)*2)])[0]
      t0 = np.zeros(len(taus))
      Ecc, tcc = ccsd_proj(H, ref, taus, t0)
      mcc = cc.GCCSD(scf.addons.convert_to_ghf(mf)); mcc.conv_tol = 1e-12; mcc.kernel()
      Ev = so.minimize(e_vcc, tcc, args=(H, ref, taus), method='BFGS', options={'gtol': 1e-9}).fun
      Eu = so.minimize(e_ucc, tcc, args=(H, ref, taus), method='BFGS', options={'gtol': 1e-9}).fun
      EHF = ref @ H @ ref
      print(f"R={R}: E_HF={EHF+enuc:.6f}  E_FCI={Efci+enuc:.8f} | CCSD {1e3*(Ecc-Efci):8.3f}  (PySCF GCCSD {1e3*(mf.e_tot+mcc.e_corr-enuc-Efci):8.3f})  VCCSD {1e3*(Ev-Efci):8.3f}  UCCSD {1e3*(Eu-Efci):8.3f}  mEh   [{len(taus)} amplitudes]")
      if R == 2.0:
          res = so.minimize(e_ucc, tcc, args=(H, ref, taus), method='BFGS', options={'gtol': 1e-9})
          T = Tmat(res.x, taus); sig = T - T.T
          term = H.copy(); Ek = 0.0
          print("  UCCSD energy from the BCH series truncated after k commutators (E_k - E_UCC, mEh):")
          for k in range(0, 9):
              Ek += ref @ term @ ref / factorial(k)
              print(f"    k={k}: {1e3*(Ek-res.fun):10.4f}")
              term = term @ sig - sig @ term
          T = Tmat(tcc, taus); term = H.copy(); Ek = 0.0; vals = []
          for k in range(0, 7):
              vals.append(np.linalg.norm((term @ ref)) / factorial(k)); term = term @ T - T @ term
          print("  traditional CC: || (1/k!) [..[H,T],..T] |HF> ||  for k=0..6:", np.round(vals, 8))
