import numpy as np
from pyscf import gto, scf, ao2mo

y, z = 1.95 * np.sin(np.radians(55)), 1.95 * np.cos(np.radians(55))   # R(OH) = 1.95 bohr, HOH = 110 deg
mol = gto.M(atom=f"O 0 0 0; H 0 {y} {z}; H 0 {-y} {z}",
            unit="Bohr", basis="6-31g")
mf = scf.RHF(mol).run(conv_tol=1e-12)
C, eps, nocc = mf.mo_coeff, mf.mo_energy, mol.nelectron // 2
nmo = C.shape[1]; nvir = nmo - nocc
o, v = slice(0, nocc), slice(nocc, None)
g = ao2mo.restore(1, ao2mo.full(mol, C), nmo)          # (pq|rs), MO basis

# CPHF matrix M_{ai,bj} = (e_a - e_i) d_ab d_ij + 4(ai|bj) - (ab|ij) - (aj|ib)
M = (4 * g[v, o, v, o]
     - g[v, v, o, o].transpose(0, 2, 1, 3)
     - g[v, o, o, v].transpose(0, 2, 3, 1)).reshape(nvir * nocc, -1)
M += np.diag((eps[v, None] - eps[None, o]).ravel())

# electric field: h -> h + F_k r_k, so S^F = 0 and the skeleton Fock derivative is r_k
r = mol.intor("int1e_r")                                # origin at O
rmo = [C.T @ rk @ C for rk in r]
U = [np.linalg.solve(M, -rk[v, o].ravel()) for rk in rmo]   # M U = B,  B_ai = -r_ai
alpha = np.array([[-4 * U[k] @ rmo[l][v, o].ravel() for l in range(3)] for k in range(3)])
print(np.diag(alpha))                                   # static polarizability, a.u.
