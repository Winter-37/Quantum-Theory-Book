---
id: ci-optimization-newton-and-davidson
title: Optimizing CI wave functions - the projected parametrization, Newton's method as Rayleigh-quotient inverse iteration, cubic convergence, and quasi-Newton/Davidson steps with subspace collapse
summary: HJO parametrize the CI state as (C⁽⁰⁾ + P̂c)/norm with P̂ = 1 − |0⟩⟨0|, which makes the normalization redundancy constant. The gradient 2(H − E⁽⁰⁾)C⁽⁰⁾, the Hessian 2P(H − E⁽⁰⁾)P and the vanishing of all odd derivatives at a stationary point follow. Newton's method is inverse iteration with the Rayleigh quotient and converges cubically. Replacing H by a diagonal H₀ gives the quasi-Newton step, and dropping one term gives Davidson's step, which degrades as H₀ → H. Reproduced: HJO Table 11.4 for water CISD/cc-pVDZ (all four subspace variants at R_ref and 2R_ref). For Table 11.3 the exact Rayleigh iteration converges faster than HJO's numbers at R_ref, and at 2R_ref it reaches an excited CISD root, a known property of the method.
status: in-progress
kind: algorithm
level: advanced
tags: [configuration-interaction, davidson-method, inverse-iteration, rayleigh-quotient, newton-method, quasi-newton, cubic-convergence, eigenvalue-problem, cisd]
prerequisites: [linear-variation-method, matrix-eigenvalue-problem, cisd]
related: [ci-size-extensivity-and-excitation-levels, determinant-strings-and-direct-ci, ci-in-practice, scf-convergence-diis-and-newton, upper-bounds-and-interlacing]
order: 100
date: 2026-11-04
---

## A parametrization with a fixed redundancy

**The problem (HJO Sec. 11.4).** $|C\rangle = \sum_iC_i|i\rangle/\sqrt{\mathbf C^{\mathsf T}\mathbf C}$ is normalized for every $\mathbf C$. However, the redundant direction of $\mathbf C^{(0)} + \mathbf c$ is $\mathbf C^{(0)} + \mathbf c$ itself, which moves with $\mathbf c$.

**HJO's fix.** Use the projector $\hat P = 1 - |0\rangle\langle0|$ and write

$$
|\mathbf c\rangle = \frac{|0\rangle + \hat P|c\rangle}{\sqrt{1 + \langle c|\hat P|c\rangle}},\qquad
E(\mathbf c) = \frac{E^{(0)} + 2\mathbf c^{\mathsf T}\mathbf P\mathbf H\mathbf C^{(0)} + \mathbf c^{\mathsf T}\mathbf P\mathbf H\mathbf P\mathbf c}{1 + \mathbf c^{\mathsf T}\mathbf P\mathbf c}.
$$

Now the redundancy is always $\mathbf C^{(0)}$. Applying $\hat P$ reduces any state to a canonical form.

**Derivatives at $\mathbf c = 0$.**

$$
\mathbf E^{(1)} = 2(\mathbf H - E^{(0)}\mathbf 1)\mathbf C^{(0)},\qquad
\mathbf E^{(2)} = 2\mathbf P(\mathbf H - E^{(0)}\mathbf 1)\mathbf P .
$$

Higher derivatives obey HJO's recursion (11.4.26). In particular, if the gradient vanishes, all odd derivatives vanish (11.4.27). These results hold for the expectation value of any Hermitian operator.

## Newton = inverse iteration with the Rayleigh quotient

**The step (HJO Sec. 11.5.1).** The Hessian is singular along $\mathbf C^{(0)}$. Adding $\alpha\mathbf C^{(0)}\mathbf C^{(0)\mathsf T}$ and inverting with the Sherman-Morrison formula gives a Newton step orthogonal to $\mathbf C^{(0)}$ and independent of $\alpha$. The new vector is

$$
\mathbf C\propto(\mathbf H - E^{(0)}\mathbf 1)^{-1}\mathbf C^{(0)},\qquad E^{(0)} = \mathbf C^{(0)\mathsf T}\mathbf H\mathbf C^{(0)} .
$$

This is the Rayleigh method.

**Convergence (HJO Sec. 11.5.2).**

- **Generic Newton.** The error after a step is quadratic in the old error, with coefficient $\mathbf E^{(2)-1}\mathbf E^{(3)}$.
- **CI is better.** For the CI energy function, the third derivative at the solution is itself linear in the error (11.5.23). The method therefore converges **cubically**.

**Practical properties.**

- **Choice of root.** Holding $E^{(0)}$ fixed converges to the eigenvalue closest to it, so a scan over $E^{(0)}$ recovers a spectrum.
- **Excited states.** The rate is the same for excited states as for the ground state.
- **Cost.** Every macro-iteration needs a linear solve, i.e. many $\mathbf H\mathbf c$ products.

## Quasi-Newton and Davidson steps

**Quasi-Newton step (HJO Eq. 11.5.24).** Replace $(\mathbf H - E^{(0)})^{-1}$ by $(\mathbf H_0 - E^{(0)})^{-1}$, usually with $\mathbf H_0$ the diagonal of $\mathbf H$:

$$
\mathbf c = -(\mathbf H_0 - E^{(0)})^{-1}\Big[\mathbf r - \frac{\mathbf C^{(0)\mathsf T}(\mathbf H_0 - E^{(0)})^{-1}\mathbf r}{\mathbf C^{(0)\mathsf T}(\mathbf H_0 - E^{(0)})^{-1}\mathbf C^{(0)}}\mathbf C^{(0)}\Big],\qquad \mathbf r = (\mathbf H - E^{(0)})\mathbf C^{(0)} .
$$

Each iteration needs only one product $\mathbf H\mathbf C^{(0)}$, and the step is orthogonal to $\mathbf C^{(0)}$.

**Davidson's step.** Dropping the second term gives $\mathbf c_{\text{dav}} = -(\mathbf H_0 - E^{(0)})^{-1}\mathbf r$.

- **Trap.** As $\mathbf H_0\to\mathbf H$, the step tends to $-\mathbf C^{(0)}$ and produces no new direction. Improving the preconditioner can therefore slow Davidson down.
- **Contrast.** The full quasi-Newton step tends to the cubically convergent Newton step instead.

**Subspaces.** Rather than updating $\mathbf C^{(0)} + \mathbf c$, keep the last few eigenvector approximations together with the new correction vector. Diagonalize $\mathbf H$ in that subspace, collapsing to a fixed size to save storage.

!!! example "HJO Table 11.4 recomputed: quasi-Newton with diagonal $\mathbf H_0$, water CISD/cc-pVDZ from the HF determinant (energy error, $E_h$; computed for this note)"
    **Setup.** Spin-orbital determinant basis (32 016 parameters), HOH = 110.565°. "Subspace 1" adds $\mathbf c$ directly. Otherwise the new vector is the lowest eigenvector in the span of the last $k-1$ approximations and $\mathbf c$.

    | Iter. | 1 ($R_{\text{ref}}$) | 2 | 3 | all | 1 ($2R_{\text{ref}}$) | 2 | 3 | all |
    |---:|---:|---:|---:|---:|---:|---:|---:|---:|
    | 1 | 0.20580 | 0.20580 | 0.20580 | 0.20580 | 0.29194 | 0.29194 | 0.29194 | 0.29194 |
    | 2 | 0.02372 | 0.00660 | 0.00660 | 0.00660 | 0.25524 | 0.05129 | 0.05129 | 0.05129 |
    | 3 | 0.00641 | 0.00044 | 0.00026 | 0.00026 | 0.59423 | 0.00896 | 0.00576 | 0.00576 |
    | 4 | 0.00142 | 0.00005 | 0.00002 | 0.00002 | 0.41107 | 0.00267 | 0.00149 | 0.00149 |
    | 5 | 0.00038 | 0.00001 | 0.00000 | 0.00000 | 0.49789 | 0.00115 | 0.00057 | 0.00057 |
    | 6 | 0.00010 | 0.00000 | | | 0.60058 | 0.00062 | 0.00013 | 0.00012 |
    | 8 | 0.00001 | | | | 0.72577 | 0.00021 | 0.00001 | 0.00001 |
    | 14 | | | | | (diverges) | 0.00001 | | |

    - **Agreement.** Apart from the divergent simple-update column at $2R_{\text{ref}}$ (wandering 0.4-1.0 $E_h$ in both), everything matches HJO to $\pm1\times10^{-5}$. HJO print 0.02373 at iteration 2, and 0.00013 in the "all" column at iteration 6.
    - **Davidson step, subspace 2.** At $R_{\text{ref}}$: 0.00660, 0.00042, 0.00008, 0.00002. At $2R_{\text{ref}}$: 0.05129, 0.00807, 0.00250, …, $10^{-5}$ after 15 iterations. This is slightly slower than quasi-Newton, as HJO describe.

!!! example "Newton (Rayleigh) iterations from the HF determinant (HJO Table 11.3; computed for this note)"
    I solved $(\mathbf H - E^{(0)})\mathbf x = \mathbf C^{(0)}$ with MINRES to $10^{-14}$ in each macro-iteration.

    | Iter. | $R_{\text{ref}}$ (mine) | HJO | $2R_{\text{ref}}$ (mine) | HJO |
    |---:|---:|---:|---:|---:|
    | 1 | 0.2057981357 | 0.2057981191 | 0.2919387078 | 0.2919278031 |
    | 2 | 0.0008299755 | 0.1031691961 | 0.1362111277 | 0.2888220715 |
    | 3 | 0.0000000002 | 0.0000739193 | 0.1144507200 | 0.0557665473 |
    | 4 | 0.0000000000 | 0.0000000000 | … → 0.2026484 | 0.0010645471 |

    - **$R_{\text{ref}}$.** My iterations show the cubic law: $8.3\times10^{-4}\to2\times10^{-10}$, compared with $(8.3\times10^{-4})^3\approx6\times10^{-10}$.
    - **$2R_{\text{ref}}$.** $E_{\text{HF}}$ lies closer to an excited CISD eigenvalue, $E_{\text{CISD}} + 0.2026$, than to the ground state. Exact inverse iteration therefore converges to that root, which HJO's remark about converging to "the eigenvalue closest to $E^{(0)}$" predicts.
    - **Difference from HJO.** HJO's printed sequences (about 50% error reduction in the first step, then convergence to the ground state at $2R_{\text{ref}}$) must include some step control or approximate linear solves that they do not describe. I could not reproduce them.
    - **Converged energies.** They agree: correlation −205.798 and −291.939 m$E_h$.

**Cost comparison (HJO).** Newton needs the fewest macro-iterations, but each one is about ten times dearer than a quasi-Newton or Davidson iteration. The latter are therefore the methods of choice. Newton remains useful for excited states and for targeting a given energy.

## Source

Helgaker, Jørgensen and Olsen, *Molecular Electronic-Structure Theory* (Wiley, Chichester, 2000), Secs. 11.4-11.5, pp. 540-550, Eqs. (11.4.1)-(11.5.26), Tables 11.3-11.4. Recomputed for this note with PySCF 2.14 GCISD contractions and my own Newton, quasi-Newton and Davidson drivers (`hjo/c11/table113.py`).
