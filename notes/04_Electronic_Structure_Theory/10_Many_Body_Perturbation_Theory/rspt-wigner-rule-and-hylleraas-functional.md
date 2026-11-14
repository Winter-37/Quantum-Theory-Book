---
id: rspt-wigner-rule-and-hylleraas-functional
title: Rayleigh-Schrödinger perturbation theory (HJO 14.1) - the order-by-order recursion, Wigner's 2n + 1 rule from a variational Lagrangian, the 2n + 2 rule for multipliers, the Hylleraas functional, and size-extensivity order by order but not term by term
summary: In intermediate normalization the RSPT master equation (H₀ − E⁽⁰⁾)|n⟩ = −U|n−1⟩ + Σ E⁽ᵏ⁾|n−k⟩ determines every correction, with E⁽ⁿ⁾ = ⟨0|U|n−1⟩. Making the energy a Lagrangian, whose multipliers equal the wave-function corrections, yields Wigner's 2n + 1 rule. Examples are E⁽³⁾ = ⟨1|U − E⁽¹⁾|1⟩ and E⁽⁴⁾ = ⟨1|U − E⁽¹⁾|2⟩ − E⁽²⁾⟨1|1⟩. The even orders are minima of Hylleraas functionals, with errors quadratic in the trial-function error. RSPT is size-extensive order by order, but individual 2n + 1 terms are not. Checked numerically: the 2n + 1 formulas against the recursion (10⁻¹⁷), the Hylleraas error versus the standard-expression error, and the 6-31G Møller-Plesset series of two noninteracting H₂ to 10th order. In the dimer, the two E⁽⁴⁾ terms are each off by ±0.231 mE_h from twice the monomer value but cancel exactly.
status: in-progress
kind: derivation
level: advanced
tags: [perturbation-theory, rayleigh-schrodinger, wigner-2n+1-rule, hylleraas-functional, lagrangian, size-extensivity, intermediate-normalization]
prerequisites: [perturbation-theory-second-quantization, linear-variation-method]
related: [moller-plesset-and-coupled-cluster-perturbation-theory, mp-convergence-intruders-analytic-continuation, linked-cluster-theorem, coupled-cluster-optimization-and-lagrangian, mp2]
order: 60
date: 2026-11-04
---

## The recursion

**Partitioning (HJO Sec. 14.1.1).** $\hat H = \hat H_0 + \hat U$, with known eigenstates of $\hat H_0$. Expand $|0\rangle = \sum_k|0^{(k)}\rangle$ and $E = \sum_kE^{(k)}$.

- **Intermediate normalization.** $\langle0^{(0)}|0^{(k)}\rangle = 0$ for $k > 0$.
- **Master equation.** Order $n$ gives

$$
(\hat H_0 - E^{(0)})|0^{(n)}\rangle = -\hat U|0^{(n-1)}\rangle + \sum_{k=1}^nE^{(k)}|0^{(n-k)}\rangle,\qquad E^{(n)} = \langle0^{(0)}|\hat U|0^{(n-1)}\rangle .
$$

- **Solving it.** The right-hand side has no $|0^{(0)}\rangle$ component, so $(\hat H_0 - E^{(0)})^{-1}$ padded by $\hat P = 1 - |0^{(0)}\rangle\langle0^{(0)}|$ is well defined:

$$
|0^{(1)}\rangle = -\hat P(\hat H_0 - E^{(0)})^{-1}\hat P\,\hat U|0^{(0)}\rangle,\qquad
|0^{(2)}\rangle = -\hat P(\hat H_0 - E^{(0)})^{-1}\hat P(\hat U - E^{(1)})|0^{(1)}\rangle,\ \ldots
$$

- **Cost profile.** The wave function to order $n-1$ gives the energy to order $n$.
- **Brillouin-Wigner alternative.** It iterates on the exact energy instead and is not size-extensive (HJO Exercise 14.1).

## Wigner's 2n + 1 rule

**Lagrangian (HJO Sec. 14.1.2).** In matrix form, with $\mathbf H(\alpha) = \mathbf H_0 + \alpha\mathbf U$ and $\mathbf C(\alpha) = \mathbf C^{(0)} + \mathbf P\mathbf C(\alpha)$, the energy is $E = \mathbf C^{(0)\mathsf T}\mathbf H\mathbf C$, constrained by $\mathbf P(\mathbf H - E)\mathbf C = 0$. Adding multipliers $\bar{\mathbf C}$ gives

$$
L = \mathbf C^{(0)\mathsf T}\mathbf H\mathbf C^{(0)} + \alpha(\mathbf C + \bar{\mathbf C})^{\mathsf T}\mathbf P\mathbf U\mathbf C^{(0)} + \bar{\mathbf C}^{\mathsf T}\mathbf P(\mathbf H - E)\mathbf P\mathbf C .
$$

- **Symmetry.** $L$ is symmetric in $\mathbf C$ and $\bar{\mathbf C}$. Both obey the same stationarity equations, so $\bar{\mathbf C}^{(k)} = \mathbf C^{(k)}$ order by order.
- **Elimination.** A function that is both linear and stationary in a parameter cannot depend on it. So every vector that enters $L^{(n)}$ only linearly can be dropped, provided no other dropped vector shares a term with it.
- **Result.** The wave function to order $n$ fixes the energy to order $2n+1$. The multipliers obey the stronger $2n+2$ rule; that does not help here, since multipliers and wave function coincide, but it matters for derivatives.

$$
\begin{aligned}
E^{(3)} &= \mathbf C^{(1)\mathsf T}(\mathbf U - E^{(1)})\mathbf C^{(1)},\\
E^{(4)} &= \mathbf C^{(1)\mathsf T}(\mathbf U - E^{(1)})\mathbf C^{(2)} - E^{(2)}\mathbf C^{(1)\mathsf T}\mathbf C^{(1)},\\
E^{(5)} &= \mathbf C^{(2)\mathsf T}(\mathbf U - E^{(1)})\mathbf C^{(2)} - 2E^{(2)}\mathbf C^{(1)\mathsf T}\mathbf C^{(2)} - E^{(3)}\mathbf C^{(1)\mathsf T}\mathbf C^{(1)} .
\end{aligned}
$$

**Not bounds.** These expressions are not variational in the upper-bound sense. Stationarity of the Lagrangian concerns only its parameters.

## The Hylleraas functional

**Definition (HJO Sec. 14.1.3).** Keep the $2n$-th order Lagrangian variational in $\mathbf C^{(n)}$ only, with the lower orders fixed. For $n = 1$:

$$
J^{(2)}[\tilde{\mathbf C}] = 2\tilde{\mathbf C}^{\mathsf T}\mathbf U\mathbf C^{(0)} + \tilde{\mathbf C}^{\mathsf T}(\mathbf H_0 - E^{(0)})\tilde{\mathbf C},\qquad \tilde{\mathbf C}\perp\mathbf C^{(0)} .
$$

- **Minimum.** For a ground state the Hessian $2(\mathbf H_0 - E^{(0)})$ is positive semidefinite. The minimizer is $\mathbf C^{(n)}$ and the minimum value is $E^{(2n)}$.
- **Error behaviour.** If $\tilde{\mathbf C} = \mathbf C^{(n)} + \boldsymbol\delta$, the Hylleraas error is $\boldsymbol\delta^{\mathsf T}(\mathbf H_0 - E^{(0)})\boldsymbol\delta\ge0$, quadratic. The 2n + 1 expressions give an error linear in $\boldsymbol\delta$, of either sign.
- **Use.** The trial correction may be nonlinearly parametrized, for example with explicitly correlated pair functions.

!!! example "Checks on a random 40 × 40 problem (computed for this note)"
    - **2n + 1 formulas.** Against the recursion, the differences are $2\times10^{-18}$, $9\times10^{-18}$ and $3\times10^{-18}$ for $E^{(3)}$, $E^{(4)}$ and $E^{(5)}$.
    - **Error scaling.** For $\tilde{\mathbf C}^{(1)} = \mathbf C^{(1)} + \epsilon\mathbf d$ with $\epsilon = 10^{-1}, 10^{-2}, 10^{-3}$:
      - Hylleraas error: $+5.07\times10^{-2}$, $+5.07\times10^{-4}$, $+5.07\times10^{-6}$, quadratic and positive;
      - standard expression $\langle0|U|\tilde1\rangle$: $-6.4\times10^{-3}$, $-6.4\times10^{-4}$, $-6.4\times10^{-5}$, linear.

## Size-extensivity: order by order, not term by term

**Separable systems (HJO Sec. 14.1.4).** Take $\hat H_0 = \hat H_{0,A} + \hat H_{0,B}$ and $\hat U = \hat U_A + \hat U_B$.

- **First-order wave function.** $|0^{(1)}_{AB}\rangle = |0^{(1)}_A0^{(0)}_B\rangle + |0^{(0)}_A0^{(1)}_B\rangle$. It contains just the terms of the product function that are correct to first order; it is not a product itself.
- **Energies.** $E^{(1)}$, $E^{(2)}$ and $E^{(3)}$ come out additive. In $E^{(3)}$ this happens only after non-extensive pieces such as $\langle0^{(1)}_A|0^{(1)}_A\rangle\langle0^{(0)}_B|\hat U_B|0^{(0)}_B\rangle$ cancel.
- **The pattern.** RSPT is extensive order by order, but its 2n + 1 terms are not individually extensive. Dropping single terms is therefore dangerous.
- **The cure.** The $n+1$ form is termwise extensive if the corrections have the product structure $|0^{(n)}_{AB}\rangle = \sum_k|0^{(n-k)}_A0^{(k)}_B\rangle$. Coupled-cluster perturbation theory provides exactly that ([[moller-plesset-and-coupled-cluster-perturbation-theory]]).

!!! example "Møller-Plesset series of two noninteracting H₂ (6-31G, 1.4 bohr, 200 bohr apart) from an exact RSPT recursion in the full determinant space (computed for this note)"
    | $n$ | $E^{(n)}$, monomer | $E^{(n)}$, dimer | dimer − 2 × monomer |
    |---:|---:|---:|---:|
    | 2 | −0.0173904570 | −0.0347809142 | $-3\times10^{-10}$ |
    | 3 | −0.0052092593 | −0.0104185183 | $2\times10^{-10}$ |
    | 4 | −0.0016050491 | −0.0032100981 | $7\times10^{-11}$ |
    | 6 | −0.0001585069 | −0.0003170138 | $-2\times10^{-11}$ |
    | 10 | −0.0000010767 | −0.0000021534 | $-1\times10^{-12}$ |

    - **The two $E^{(4)}$ terms.** In the dimer, $\langle1|U - E^{(1)}|2\rangle = -0.00367281$ and $-E^{(2)}\langle1|1\rangle = +0.00046271$. Twice the monomer values are $-0.00344145$ and $+0.00023135$, so each term is off by $\mp0.000231$ $E_h$, and the errors cancel exactly.
    - **Residuals.** The tiny remaining differences (and a $2.7\times10^{-7}$ shift between $E^{(0)}$ and $E^{(1)}$, which cancels in their sum) come from the $1/R$ interaction at 200 bohr.

## Source

Helgaker, Jørgensen and Olsen, *Molecular Electronic-Structure Theory* (Wiley, Chichester, 2000), Sec. 14.1, pp. 725-739, Eqs. (14.1.1)-(14.1.97), Table 14.1. Recomputed for this note with NumPy (`hjo/c14/rspt.py`) and PySCF 2.14 FCI σ-vectors in my own RSPT recursion (`hjo/c14/rsptsep.py`).
