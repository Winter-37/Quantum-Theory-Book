---
id: rhf-analytic-hessian
title: The closed-shell RHF analytic Hessian - second derivatives from first-order CPHF
summary: Differentiating the RHF gradient once more brings in the first-order orbital response U^x but, by the 2n+1 rule, not U^xy. The second-order orthonormality condition removes U^xy, leaving YOGS Eq. 4.54. That is a skeleton second-derivative term plus terms bilinear in U^x and U^y, the skeleton Fock derivatives and the S^x matrices. Rearranged, the response part is −4 Σ_ai U^x_ai B^y_ai plus overlap-only terms, so only the occupied-virtual U from CPHF is needed. Checked against PySCF for water (5×10⁻⁹) and shown to be independent of the occupied-occupied and virtual-virtual convention for U.
status: in-progress
kind: derivation
level: advanced
tags: [analytic-hessian, force-constants, rhf, cphf, second-derivatives, 2n+1-rule]
prerequisites: [rhf-analytic-gradient, cphf-closed-shell, derivative-integrals-and-u-matrices]
related: [analytic-gradients-and-force-constants, cpci-and-ci-hessian, geometry-optimization]
order: 60
date: 2026-11-07
---

Notation: [[derivative-integrals-and-u-matrices]]. Here $i,j,k,l$ are occupied, $a,b$ virtual, $p,q$ general, and superscripts $x$, $xy$ mark skeleton derivatives. $F^x_{pq}$ is the skeleton Fock derivative and $A_{pq,rs} = 4(pq|rs) - (pr|qs) - (ps|qr)$, both as in [[cphf-closed-shell]].

## Derivation

**Start from the gradient before canonicalization (YOGS Eq. 4.16).**

$$
\frac{\partial E}{\partial x} = 2\sum_ih^x_{ii} + \sum_{ij}\big[2(ii|jj)^x - (ij|ij)^x\big] + 4\sum_p\sum_jU^x_{pj}F_{pj}.
$$

**Differentiate with respect to $y$ (YOGS Eqs. 4.38-4.49).** Three kinds of terms appear.

1. **Skeleton second derivatives.** $h^{xy}$, $(pq|rs)^{xy}$: the first two terms differentiated at fixed MO coefficients.
2. **U-terms from differentiating the skeleton integrals.** For example $\partial h^x_{ii}/\partial y = h^{xy}_{ii} + 2\sum_mU^y_{mi}h^x_{mi}$. These collect into $4\sum_{pj}U^y_{pj}F^x_{pj}$.
3. **Derivative of $4\sum U^x_{pj}F_{pj}$.** This needs $\partial U^x/\partial y = U^{xy} - U^yU^x$ ([[derivative-integrals-and-u-matrices]]) and $\partial F/\partial y$ from [[cphf-closed-shell]].

**Remove $U^{xy}$ (YOGS Eqs. 4.50-4.53).** $U^{xy}_{pj}$ appears only as $4\sum_{pj}U^{xy}_{pj}F_{pj}$. With $F_{aj} = 0$ and canonical $F_{ij} = \delta_{ij}\varepsilon_i$, this reduces to $4\sum_iU^{xy}_{ii}\varepsilon_i$. The diagonal of the second-order orthonormality condition gives $U^{xy}_{ii} = -\tfrac12(S^{xy}_{ii} + \eta^{xy}_{ii})$. No second-order CPHF is needed: the 2n+1 rule with $n = 1$.

**Result (YOGS Eq. 4.54).**

$$
\begin{aligned}
\frac{\partial^2E}{\partial x\,\partial y} ={}& 2\sum_ih^{xy}_{ii} + \sum_{ij}\big[2(ii|jj)^{xy} - (ij|ij)^{xy}\big] - 2\sum_iS^{xy}_{ii}\varepsilon_i + \frac{\partial^2V_{\text{nn}}}{\partial x\,\partial y}\\
&- 2\sum_i\eta^{xy}_{ii}\varepsilon_i
+ 4\sum_{p}\sum_j\big(U^y_{pj}F^x_{pj} + U^x_{pj}F^y_{pj}\big)\\
&+ 4\sum_p\sum_jU^x_{pj}U^y_{pj}\varepsilon_p
+ 4\sum_{pj}\sum_{ql}U^x_{pj}U^y_{ql}A_{pj,ql},
\end{aligned}
$$

with

$$
\eta^{xy}_{ii} = 2\sum_m\big(U^x_{im}U^y_{im} - S^x_{im}S^y_{im}\big).
$$

Here $p, q$ run over all MOs and $j, l$ over occupied ones.

- **First line: skeleton part.** It is $\partial^2E/\partial x\partial y$ with the MO coefficients frozen, the AO analogue of the gradient formula: $\sum P h^{xy} + \tfrac12\sum(PP - \tfrac12PP)(\mu\nu|\lambda\sigma)^{xy} - \sum W S^{xy}$.
- **Second and third lines: response part.** It is bilinear in first-order quantities.

**Compact form in independent pairs (my rearrangement).** Written in terms of the independent pairs only, the response part equals

$$
-4\sum_{ai}U^x_{ai}B^y_{ai}
+ 2\sum_{ij}S^x_{ij}S^y_{ij}(\varepsilon_i + \varepsilon_j)
+ \sum_{ijkl}S^x_{ij}S^y_{kl}A_{ij,kl}
- 2\sum_{ij}\big(S^x_{ij}F^y_{ij} + S^y_{ij}F^x_{ij}\big).
$$

- **Status of this form.** I did not take it from YOGS, and I have not derived it algebraically. I found it by least-squares fitting the response part of Eq. 4.54, minus $-4\,\mathbf U^{x\mathsf T}\mathbf B^y$, to four candidate overlap terms. The coefficients came out as the integers shown, and the form then reproduces Eq. 4.54 to $10^{-13}$ for all 81 elements in two bases. The derivation is still to do (or to check against Pople et al., 1979).
- **Reading.** $-4\,\mathbf U^{x\mathsf T}\mathbf B^y = -4\,\mathbf U^{x\mathsf T}\mathbf M\mathbf U^y$ is the familiar "relaxation lowers the curvature" term: it is negative semidefinite in the space of perturbations. The overlap-only terms appear because the basis moves.

## Cost

- **CPHF.** The Hessian needs $\mathbf U^x$ for every coordinate: $3N$ CPHF right-hand sides, all with the same $\mathbf M$. The Z-vector trick does not remove this, because the response part is quadratic in $\mathbf U$.
- **Integrals.** The skeleton part needs second-derivative integrals, contracted directly with $P$ and $W$ as in the gradient.
- **Comparison with finite differences.** The analytic Hessian costs a few times one gradient. A finite-difference Hessian from analytic gradients needs $6N$ gradients (central differences) and is limited by step-size noise.

## Worked example

!!! example "Water, R(OH) = 1.95 bohr, HOH = 110° (computed for this note)"
    - **Skeleton part.** Obtained by central differences (step $10^{-4}$ bohr) of the analytic skeleton gradient with $P$ and $W$ held at their reference values. That is the same as contracting analytic second-derivative integrals with fixed densities.
    - **Response part.** Eq. 4.54, with $\mathbf U^x$ from CPHF.

    | Check | STO-3G | 6-31G |
    |---|---:|---:|
    | max $\lvert$Eq. 4.54 − PySCF analytic Hessian$\rvert$ | $5.1\times10^{-9}$ | $4.8\times10^{-9}$ |
    | max $\lvert$compact form − Eq. 4.54 response part$\rvert$ | $1\times10^{-14}$ | $9\times10^{-14}$ |
    | largest Hessian element ($E_h$/bohr²) | 0.719 | 0.472 |

    - **Accuracy.** The $5\times10^{-9}$ deviation is the finite-difference error in the skeleton part.
    - **Convention independence.** In 6-31G, replacing the canonical occupied-occupied and virtual-virtual blocks of $\mathbf U^x$ by $-\tfrac12\mathbf S^x$ changes $\eta^{xy}$ and individual terms, but the Hessian is unchanged to $10^{-14}$.
    - **Size of the response.** For the O $z$,$z$ element (6-31G) the skeleton part is 0.23453 and the response part 0.08422, total 0.31874 $E_h$/bohr². The largest response element (0.289) exceeds the largest skeleton element (0.235). The orbital response is not a correction.

## Source

Yamaguchi, Osamura, Goddard and Schaefer, *A New Dimension to Quantum Chemistry* (Oxford University Press, New York, 1994), Ch. 4, Secs. 4.5-4.7, Eqs. (4.27)-(4.57), pp. 58-63. Equations read from the page images and converted to the notation above. The compact independent-pair form is my own rearrangement, verified numerically only. Original closed-shell analytic Hessian, as cited by YOGS: J. A. Pople, R. Krishnan, H. B. Schlegel and J. S. Binkley, *Int. J. Quantum Chem. Symp.* **13**, 225 (1979), doi:10.1002/qua.560160825 (DOI to verify). Computations: PySCF 2.15, `gradients/rhf_grad_hess.py`, `gradients/hessian_compact_check.py`.
