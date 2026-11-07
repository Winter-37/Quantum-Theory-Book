---
id: rhf-analytic-gradient
title: The closed-shell RHF analytic gradient - why no CPHF is needed and where the energy-weighted density comes from
summary: Differentiating the RHF energy gives skeleton derivative integrals plus a term 4 Σ U^x_pi F_pi. The Brillouin condition F_ai = 0 removes the occupied-virtual response, and orthonormality turns what is left into −2 Σ_ij S^x_ij F_ij. Result, in AO form: dE/dx = Σ P h^x + ½ Σ (P P − ½ P P)(μν|λσ)^x − Σ W S^x + V_nn^x, with W the energy-weighted density. Checked against PySCF to 10⁻¹⁴ for water; the large one- and two-electron terms cancel to a gradient two orders of magnitude smaller.
status: in-progress
kind: derivation
level: advanced
tags: [analytic-gradients, rhf, energy-weighted-density, pulay-forces, skeleton-integrals, nuclear-gradient]
prerequisites: [derivative-integrals-and-u-matrices, rhf, brillouin-theorem]
related: [analytic-gradients-and-force-constants, cphf-closed-shell, rhf-analytic-hessian, ci-analytic-gradient, geometry-optimization, hellmann-feynman-and-virial-theorems]
order: 40
date: 2026-11-07
---

Notation: [[derivative-integrals-and-u-matrices]]. Here $x$ is a nuclear Cartesian coordinate, $i,j,k$ are doubly occupied, $p$ is any MO, and superscript $x$ marks a skeleton derivative.

## Energy and variational conditions

**Energy (YOGS Eqs. 4.1-4.3).**

$$
E_{\text{el}} = 2\sum_ih_{ii} + \sum_{ij}\big[2(ii|jj) - (ij|ij)\big] = \sum_i(h_{ii} + \varepsilon_i),
$$

with the closed-shell Fock matrix ([[rhf]])

$$
F_{pq} = h_{pq} + \sum_k\big[2(pq|kk) - (pk|qk)\big].
$$

**Variational conditions.** $F_{ai} = 0$ for occupied $i$ and virtual $a$ (the Brillouin condition, [[brillouin-theorem]]). For canonical orbitals, also $F_{pq} = \delta_{pq}\varepsilon_p$.

## Differentiation

**Step 1: product rule (YOGS Eq. 4.8).**

$$
\frac{\partial E_{\text{el}}}{\partial x} = 2\sum_i\frac{\partial h_{ii}}{\partial x} + \sum_{ij}\Big[2\frac{\partial(ii|jj)}{\partial x} - \frac{\partial(ij|ij)}{\partial x}\Big].
$$

**Step 2: insert the MO-integral derivatives.** Each MO index contributes a $U$-term: $\partial h_{ii}/\partial x = h^x_{ii} + 2\sum_pU^x_{pi}h_{pi}$, and so on. Collecting all terms that multiply $U^x_{pi}$ gives exactly the Fock matrix (YOGS Eqs. 4.12-4.16):

$$
\frac{\partial E_{\text{el}}}{\partial x} = 2\sum_ih^x_{ii} + \sum_{ij}\big[2(ii|jj)^x - (ij|ij)^x\big] + 4\sum_p\sum_iU^x_{pi}F_{pi}.
$$

**Step 3: remove the response.** Split $p$ into virtual and occupied.

- **Virtual $p = a$.** $F_{ai} = 0$, so the occupied-virtual response $U^x_{ai}$ drops out. This is the only part that would need CPHF.
- **Occupied $p = j$.** $F_{ji}$ is symmetric, so only the symmetric part of $U^x_{ji}$ survives. By orthonormality that part is $-\tfrac12S^x_{ji}$:

$$
4\sum_{ij}U^x_{ji}F_{ji} = 2\sum_{ij}\big(U^x_{ji} + U^x_{ij}\big)F_{ij} = -2\sum_{ij}S^x_{ij}F_{ij}.
$$

**Result (YOGS Eq. 4.21, which uses canonical orbitals: $F_{ij} = \delta_{ij}\varepsilon_i$).**

$$
\frac{\partial E_{\text{el}}}{\partial x} = 2\sum_ih^x_{ii} + \sum_{ij}\big[2(ii|jj)^x - (ij|ij)^x\big] - 2\sum_{ij}S^x_{ij}F_{ij}
\;\xrightarrow{\ \text{canonical}\ }\;
\ldots - 2\sum_iS^x_{ii}\varepsilon_i .
$$

- **No CPHF.** The gradient needs no derivative of the MO coefficients. This is the $n = 0 \to 2n+1 = 1$ case of the 2n+1 rule.
- **Hidden response.** The $S^x$ term is what remains of the orbital response. It is there only because the basis moves: for a perturbation that leaves $S$ unchanged (an electric field) it vanishes, and the gradient becomes the Hellmann-Feynman expectation value.

## AO form

**Back-transform (YOGS Eqs. 4.22-4.25).** Use $P_{\mu\nu} = 2\sum_iC_{\mu i}C_{\nu i}$ and define the **energy-weighted density matrix**

$$
W_{\mu\nu} = 2\sum_{ij}C_{\mu i}F_{ij}C_{\nu j} = 2\sum_i\varepsilon_iC_{\mu i}C_{\nu i}\quad\text{(canonical)} .
$$

Then

$$
\frac{\mathrm dE}{\mathrm dx} = \sum_{\mu\nu}P_{\mu\nu}\frac{\partial h_{\mu\nu}}{\partial x}
+ \frac12\sum_{\mu\nu\lambda\sigma}\Big(P_{\mu\nu}P_{\lambda\sigma} - \tfrac12P_{\mu\lambda}P_{\nu\sigma}\Big)\frac{\partial(\mu\nu|\lambda\sigma)}{\partial x}
- \sum_{\mu\nu}W_{\mu\nu}\frac{\partial S_{\mu\nu}}{\partial x}
+ \frac{\partial V_{\text{nn}}}{\partial x}.
$$

**Interpretation.**

- **First term.** It contains the Hellmann-Feynman force (the operator derivative of $\hat V_{\text{ne}}$) and the basis-function part of $h$.
- **Second and third terms.** These, with the basis-function part of the first, are the **Pulay forces** ([[analytic-gradients-and-force-constants]]).
- **The $-\sum W S^x$ term.** It enforces orthonormality as the basis moves. Its weights are orbital energies because $\varepsilon_i$ are the Lagrange multipliers of the orthonormality constraint.

**Cost and practice.**

- **Density contraction.** Derivative integrals are contracted directly with $P$ and $W$; they are never transformed to the MO basis.
- **Unique integrals.** YOGS Eq. 4.26 restricts the sums to unique AO quadruples with the factors $(1 - \tfrac12\delta_{\mu\nu})$.
- **Atom ownership.** $\partial(\mu\nu|\lambda\sigma)/\partial X_A$ is nonzero only when at least one of the four functions sits on atom $A$. So the cost is a small multiple of one Fock build, independent of the number of coordinates.

## Worked example

!!! example "Water, R(OH) = 1.95 bohr, HOH = 110° (computed for this note)"
    The AO formula above, evaluated with PySCF derivative integrals, agrees with PySCF's own RHF gradient to $2\times10^{-15}$ (STO-3G) and $7\times10^{-15}$ (6-31G). The MO form (Eq. 4.21) agrees equally well. Contributions to two components ($E_h$/bohr):

    | Basis, component | $\sum Ph^x$ | two-electron | $-\sum WS^x$ | $V_{\text{nn}}^x$ | total |
    |---|---:|---:|---:|---:|---:|
    | STO-3G, $O_z$ | −5.314957 | 2.612579 | 0.276346 | 2.413471 | −0.012562 |
    | STO-3G, $H_{1y}$ | 4.083733 | −2.029919 | −0.176712 | −1.821378 | 0.055724 |
    | 6-31G, $O_z$ | −5.229001 | 2.439156 | 0.304223 | 2.413471 | −0.072151 |
    | 6-31G, $H_{1y}$ | 3.910312 | −1.828904 | −0.202691 | −1.821378 | 0.057339 |

    - **Cancellation.** The gradient is a cancellation of terms two orders of magnitude larger. Each term must be accurate to well below the size of the result, which is why derivative integrals are computed to the same precision as the energy integrals.
    - **The $W$ term.** It is 3 to 20 times larger than the gradient component it contributes to. Omitting it is not a small error.

```python
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
print(abs(grad - mf.nuc_grad_method().kernel()).max())   # about 3e-15
```

The derivative with respect to a nucleus is minus the derivative with respect to the electron coordinate of the functions centred on it, hence the minus signs on `ipovlp` and `ip1`. Building the full four-index derivative array is only sensible for tiny bases.

## Source

Yamaguchi, Osamura, Goddard and Schaefer, *A New Dimension to Quantum Chemistry* (Oxford University Press, New York, 1994), Ch. 4, Secs. 4.1-4.4, Eqs. (4.1)-(4.26), pp. 53-58. Equations read from the page images. The non-canonical form $-2\sum_{ij}S^x_{ij}F_{ij}$ is my intermediate step before YOGS's canonical Eq. 4.21. The pioneering papers cited by YOGS: P. Pulay, *Mol. Phys.* **17**, 197 (1969), doi:10.1080/00268976900100941; J. A. Pople, R. Krishnan, H. B. Schlegel and J. S. Binkley, *Int. J. Quantum Chem. Symp.* **13**, 225 (1979), doi:10.1002/qua.560160825 (DOI from an indexing site, to verify). Computations: PySCF 2.15, `gradients/rhf_grad_hess.py`, `gradients/extras.py`.
