import numpy as np
from pyscf import gto, scf

y, z = 1.95 * np.sin(np.radians(55)), 1.95 * np.cos(np.radians(55))   # R(OH) = 1.95 bohr, HOH = 110 deg
mol = gto.M(atom=f"O 0 0 0; H 0 {y} {z}; H 0 {-y} {z}",
            unit="Bohr", basis="sto-3g")
mf = scf.RHF(mol).run(conv_tol=1e-12)
C, eps, nocc = mf.mo_coeff, mf.mo_energy, mol.nelectron // 2
Co = C[:, :nocc]
P = 2 * Co @ Co.T                          # density matrix
W = 2 * Co @ np.diag(eps[:nocc]) @ Co.T    # energy-weighted density matrix

ipovlp = mol.intor("int1e_ipovlp")         # <d mu/dr | nu>
ip1 = mol.intor("int2e_ip1")               # (d mu/dr nu | lam sig)
hcore_deriv = mf.nuc_grad_method().hcore_generator(mol)
grad = np.zeros((mol.natm, 3))
for A, (_, _, p0, p1) in enumerate(mol.aoslice_by_atom()):
    dh = hcore_deriv(A)                    # dh/dX_A including the operator derivative
    for k in range(3):
        dS = np.zeros_like(P); dS[p0:p1] = -ipovlp[k, p0:p1]; dS += dS.T
        dg = np.zeros((mol.nao,) * 4); dg[p0:p1] = -ip1[k, p0:p1]
        dg += dg.transpose(1, 0, 2, 3); dg += dg.transpose(2, 3, 0, 1)
        grad[A, k] = (np.sum(P * dh[k])
                      + 0.5 * np.einsum("mn,ls,mnls", P, P, dg)
                      - 0.25 * np.einsum("ml,ns,mnls", P, P, dg)
                      - np.sum(W * dS))
Z, R = mol.atom_charges(), mol.atom_coords()
for A in range(mol.natm):                  # nuclear repulsion
    for B in range(mol.natm):
        if A != B:
            d = R[A] - R[B]
            grad[A] -= Z[A] * Z[B] * d / np.linalg.norm(d) ** 3
print(grad)
print(abs(grad - mf.nuc_grad_method().kernel()).max())
