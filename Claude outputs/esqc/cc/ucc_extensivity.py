"""Size-extensivity of exact VCCSD and UCCSD: (H2)2 at 50 A separation vs 2 x H2, STO-3G."""
import numpy as np, itertools, scipy.linalg as sl, scipy.optimize as so
from pyscf import gto
from fermi import jw_ops, basis_index, spin_orbital_integrals, hamiltonian_matrix
from ucc_vcc import Tmat, e_vcc, e_ucc
def build(atoms):
    mol = gto.M(atom=atoms, basis='sto-3g', verbose=0)
    h, g, no, enuc, mf = spin_orbital_integrals(mol)
    n = h.shape[0]; ops = jw_ops(n); ad = [o.T.tocsr() for o in ops]
    H = hamiltonian_matrix(h, g, ops).toarray(); ref = np.zeros(2**n); ref[basis_index(range(no), n)] = 1
    spin = np.array([0, 1]*(n//2)); occ, vir = range(no), range(no, n); taus = []
    for i, a in itertools.product(occ, vir):
        if spin[i] == spin[a]: taus.append((ad[a] @ ops[i]).toarray())
    for (i, j), (a, b) in itertools.product(itertools.combinations(occ, 2), itertools.combinations(vir, 2)):
        if spin[i]+spin[j] == spin[a]+spin[b]: taus.append((ad[a] @ ad[b] @ ops[j] @ ops[i]).toarray())
    Nmask = np.array([bin(k).count('1') == no for k in range(2**n)])
    Efci = np.linalg.eigvalsh(H[np.ix_(Nmask, Nmask)])[0]
    return H, ref, taus, enuc, Efci
res = {}
for name, atoms in [("H2", "H 0 0 0; H 0 0 0.74"), ("(H2)2", "H 0 0 0; H 0 0 0.74; H 50 0 0; H 50 0 0.74")]:
    H, ref, taus, enuc, Efci = build(atoms)
    t0 = np.full(len(taus), 0.01)
    Ev = so.minimize(e_vcc, t0, args=(H, ref, taus), method='BFGS', options={'gtol': 1e-10}).fun
    Eu = so.minimize(e_ucc, t0, args=(H, ref, taus), method='BFGS', options={'gtol': 1e-10}).fun
    res[name] = (Ev+enuc, Eu+enuc, Efci+enuc)
    print(name, "total: VCCSD %.10f UCCSD %.10f FCI %.10f" % res[name])
for k, lab in enumerate(["VCCSD", "UCCSD", "FCI"]):
    print(f"{lab}: E(dimer) - 2 E(monomer) = {res['(H2)2'][k]-2*res['H2'][k]:.2e}")
