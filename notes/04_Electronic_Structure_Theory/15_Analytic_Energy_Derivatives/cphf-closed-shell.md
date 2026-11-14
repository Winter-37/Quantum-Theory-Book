---
id: cphf-closed-shell
title: Closed-shell coupled-perturbed Hartree-Fock (CPHF) equations - first and second order, nuclear and electric-field perturbations
summary: CPHF follows from differentiating the Brillouin condition F_ai = 0. For each perturbation x it is one linear system, Σ_bj M_ai,bj U^x_bj = B^x_ai, with M_ai,bj = (ε_a − ε_i)δ_abδ_ij + 4(ai|bj) − (ab|ij) − (aj|ib). M is the same for every perturbation: it is a quarter of the closed-shell orbital Hessian and equals A + B of static singlet RPA. Only the right-hand side depends on the perturbation. The occupied-occupied and virtual-virtual elements of U follow by convention, orbital-energy derivatives come out at no extra cost, and second-order CPHF has the same matrix. Verified for water: U against differentiated MOs, dε_i/dx against finite differences (10⁻⁷), and the static polarizability against finite field.
status: in-progress
kind: derivation
level: advanced
tags: [cphf, coupled-perturbed-hartree-fock, orbital-response, u-matrix, polarizability, linear-response, orbital-hessian]
prerequisites: [derivative-integrals-and-u-matrices, rhf, brillouin-theorem]
related: [rhf-analytic-hessian, z-vector-method, ci-analytic-gradient, generalized-fock-matrix-and-orbital-hessian, scf-second-order-and-stability, polarization-propagator-rpa, molecular-properties-and-response]
order: 50
date: 2026-11-07
---

Notation: [[derivative-integrals-and-u-matrices]]. Here $i,j,k,l$ are occupied, $a,b$ are virtual, $p,q$ are general MOs, $x,y$ are perturbations, and canonical RHF orbitals are assumed unless stated.

## First-order CPHF

**Condition to differentiate.** The RHF orbitals satisfy $F_{pq} = \delta_{pq}\varepsilon_p$ at every value of the perturbation, with ([[rhf-analytic-gradient]])

$$
F_{pq} = h_{pq} + \sum_k\big[2(pq|kk) - (pk|qk)\big].
$$

The occupied-virtual elements $F_{ai} = 0$ are the variational conditions. The rest are conventions defining canonical orbitals.

**Derivative of the Fock matrix (YOGS Eqs. 10.5-10.9).** Insert the MO-integral derivatives:

$$
\frac{\partial F_{pq}}{\partial x} = F^x_{pq} + \sum_m\big(U^x_{mp}F_{mq} + U^x_{mq}F_{pm}\big) + \sum_m\sum_kU^x_{mk}A_{pq,mk},
$$

where

$$
F^x_{pq} = h^x_{pq} + \sum_k\big[2(pq|kk)^x - (pk|qk)^x\big],
\qquad
A_{pq,rs} = 4(pq|rs) - (pr|qs) - (ps|qr).
$$

$F^x$ is the skeleton Fock derivative: integrals differentiated, MO coefficients held fixed.

**Eliminating the dependent elements (YOGS Eqs. 10.10-10.17).**

- **Fock terms.** With canonical orbitals and $U^x_{qp} = -U^x_{pq} - S^x_{pq}$, the second term is $\varepsilon_qU^x_{qp} + \varepsilon_pU^x_{pq} = -(\varepsilon_q - \varepsilon_p)U^x_{pq} - S^x_{pq}\varepsilon_q$.
- **Occupied-occupied part of the $A$-sum.** $A_{pq,kl}$ is symmetric in $k,l$, so only the symmetric part $-\tfrac12S^x_{kl}$ of $U^x_{kl}$ contributes:

$$
\sum_{kl}U^x_{kl}A_{pq,kl} = -\sum_{kl}S^x_{kl}\big[2(pq|kl) - (pk|ql)\big].
$$

**The CPHF equations (YOGS Eqs. 10.21-10.23).** Setting $\partial F_{ai}/\partial x = 0$ gives

$$
\sum_{bj}M_{ai,bj}U^x_{bj} = B^x_{ai},
$$

$$
M_{ai,bj} = (\varepsilon_a - \varepsilon_i)\delta_{ab}\delta_{ij} + 4(ai|bj) - (ab|ij) - (aj|ib),
$$

$$
B^x_{ai} = -F^x_{ai} + S^x_{ai}\varepsilon_i + \sum_{kl}S^x_{kl}\big[2(ai|kl) - (ak|il)\big].
$$

YOGS write the same equations with the opposite overall sign, $(\varepsilon_i - \varepsilon_a)U^x_{ai} - \sum A\,U = B^x_0$ with $B^x_0 = -B^x$. Their $A$ matrix in Ch. 18 includes the orbital-energy differences; here they are in $\mathbf M$.

**Properties.**

- **Dimension.** $n_{\text{occ}}n_{\text{virt}}$, independent of the perturbation. $3N$ nuclear perturbations need $3N$ right-hand sides with the same matrix.
- **Relation to other notes.**
    - $4\mathbf M$ is the closed-shell occupied-virtual orbital Hessian $E^{(2)}_{ai,bj}$ of [[generalized-fock-matrix-and-orbital-hessian]]. So CPHF is one Newton step on the perturbed energy, and $\mathbf M$ is positive definite exactly when the RHF solution is a stable minimum ([[scf-second-order-and-stability]]).
    - $\mathbf M$ is $\mathbf A + \mathbf B$ of singlet RPA ([[polarization-propagator-rpa]]): CPHF is the $\omega = 0$ limit of time-dependent Hartree-Fock.
- **Solution.** Iterative, with $\varepsilon_a - \varepsilon_i$ as preconditioner, and without building $\mathbf M$. The product $\mathbf{MU}$ needs only one AO Fock-like build per perturbation from the trial density $\sum_{ai}C_{\mu a}U_{ai}C_{\nu i}$. YOGS mention direct solution only for dimensions below about 1000.
- **Electric fields.** For $\hat h \to \hat h + F_k\hat r_k$ with field-independent basis functions, $S^F = 0$ and $F^F_{pq} = (r_k)_{pq}$, so $B^F_{ai} = -(r_k)_{ai}$ (YOGS Sec. 17.5, with the sign of the field perturbation as written here).

## Non-independent pairs and orbital-energy derivatives

**Occupied-occupied and virtual-virtual elements (YOGS Eq. 10.26).** If canonical orbitals are kept, set $\partial F_{pq}/\partial x = 0$ for $p\neq q$ inside one block:

$$
U^x_{pq} = \frac{1}{\varepsilon_q - \varepsilon_p}\Big[F^x_{pq} - S^x_{pq}\varepsilon_q - \sum_{kl}S^x_{kl}\big[2(pq|kl) - (pk|ql)\big] + \sum_{bj}U^x_{bj}A_{pq,bj}\Big].
$$

- **Degeneracy.** The formula breaks down for degenerate orbitals and becomes ill-conditioned for nearly degenerate ones.
- **When it is not needed.** RHF Hessians and gradients of methods invariant within the occupied and virtual spaces (CISD with all electrons correlated, for example) do not need these elements. Any choice obeying $U^x_{pq} + U^x_{qp} = -S^x_{pq}$ gives the same result ([[rhf-analytic-hessian]]).
- **When it is needed.** It matters when the orbital partition is not invariant: frozen-core correlated methods, and wave-function derivatives in canonical orbitals.

**Orbital-energy derivative (YOGS Eq. 10.25).** The diagonal of $\partial\mathbf F/\partial x$ costs nothing once $\mathbf U^x_{\text{vo}}$ is known:

$$
\frac{\partial\varepsilon_p}{\partial x} = F^x_{pp} - S^x_{pp}\varepsilon_p - \sum_{kl}S^x_{kl}\big[2(pp|kl) - (pk|pl)\big] + \sum_{bj}U^x_{bj}\big[4(pp|bj) - (pb|pj) - (pj|pb)\big].
$$

## Second-order CPHF

**Same matrix (YOGS Sec. 10.4, Eqs. 18.29-18.30).** Differentiating $\partial F_{ai}/\partial x = 0$ once more gives

$$
\sum_{bj}M_{ai,bj}U^{xy}_{bj} = B^{xy}_{ai}.
$$

The right-hand side contains second skeleton derivatives ($F^{xy}$, $S^{xy}$, and $\xi^{xy}$ from second-order orthonormality), products $\mathbf U^x\mathbf U^y$, and $\mathbf U^x\mathbf F^y$, $\mathbf U^x\mathbf A^y$ terms.

- **When needed.** $\mathbf U^{xy}$ is needed for fourth RHF derivatives and, without the Z-vector method, for second derivatives of CI energies.
- **Cost.** There are $3N(3N+1)/2$ right-hand sides, which is why the Z-vector reformulation matters ([[z-vector-method]]).

## Worked example

!!! example "Water, R(OH) = 1.95 bohr, HOH = 110°, 6-31G (computed for this note)"
    CPHF dimension $5\times8 = 40$. Eigenvalues of $\mathbf M$ lie between 0.327 and 21.6 $E_h$: positive definite, so the RHF solution is a stable minimum and every CPHF system is well posed.

    | Check | Result |
    |---|---|
    | $\partial F_{pq}/\partial x$ off-diagonal, canonical $\mathbf U^x$ | $\le 6\times10^{-15}$ |
    | $\mathbf U^x_{\text{vo}}$ vs finite-differenced canonical MOs (step $10^{-3}$) | $1.4\times10^{-7}$ |
    | $\partial\varepsilon_i/\partial x$ (Eq. 10.25) vs finite differences, all 9 coordinates | $1.2\times10^{-7}$ |
    | $\alpha_{zz} = -4\sum_{ai}U^{F_z}_{ai}(z)_{ai}$ | 4.771588 a.u. |
    | $\alpha_{zz}$ from finite field, $\pm10^{-3}$ a.u. | 4.771597 a.u. |
    | $\alpha_{xx}$, $\alpha_{yy}$ (CPHF) | 1.278815, 8.764620 a.u. |

    - **Polarizability.** The last rows use one CPHF solve per field direction. The small difference from finite field is the $O(F^2)$ error of the three-point formula. The small $\alpha_{xx}$ is the out-of-plane response; 6-31G has no polarization functions to describe it.
    - **Near-degenerate virtuals.** The virtual-virtual elements of $\mathbf U^x$ agree with finite differences only to $10^{-2}$ in this basis, because two virtuals are 0.014 $E_h$ apart. See [[derivative-integrals-and-u-matrices]].

```python
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
print(np.diag(alpha))                                   # 1.27881484 8.76462017 4.77158844
```

**Where the formula for $\alpha$ comes from.** $\partial E/\partial F_k = 2\sum_i(r_k)_{ii}$ is the RHF gradient for a perturbation with $S^F = 0$. Differentiating again with respect to $F_l$ and using $\sum_i\partial(r_k)_{ii}/\partial F_l = 2\sum_{ai}U^{F_l}_{ai}(r_k)_{ai}$ (the occupied-occupied part cancels) gives $\partial^2E/\partial F_k\partial F_l = 4\sum_{ai}U^{F_l}_{ai}(r_k)_{ai}$. Then $\alpha = -\partial^2E/\partial F^2$.

## Source

Yamaguchi, Osamura, Goddard and Schaefer, *A New Dimension to Quantum Chemistry* (Oxford University Press, New York, 1994), Ch. 10, Secs. 10.1-10.4, Eqs. (10.1)-(10.41), pp. 128-138; Sec. 17.5, pp. 332-335; Sec. 18.1-18.2, Eqs. (18.3)-(18.6) and (18.29)-(18.30), pp. 356-359. Equations read from the page images; signs rearranged so that $\mathbf M$ is positive definite. The CPHF method as cited by YOGS: J. Gerratt and I. M. Mills, *J. Chem. Phys.* **49**, 1719 (1968), doi:10.1063/1.1670299. The identification of $\mathbf M$ with the orbital Hessian and RPA $\mathbf A + \mathbf B$ is my own, checked against the formulas in the linked notes. Computations: PySCF 2.15, `gradients/rhf_grad_hess.py`, `gradients/deps.py`, `gradients/extras.py`.
