---
id: mcscf-trust-region-and-augmented-hessian
title: MCSCF step control - the level-shifted Newton step, Levenberg-Marquardt trajectories, trust-radius updates, the Newton eigenvector method (NEO) and the augmented-Hessian method
summary: HJO restrict each MCSCF Newton step to a trust region ‖Pλ‖ ≤ h. Steps to the boundary are level-shifted Newton steps (E⁽²⁾ − μ)Pλ = −E⁽¹⁾. For a minimum take μ ≤ min(ε₁, 0); for the Kth state take the branch between the (K−1)th and Kth Hessian eigenvalues. The trust radius follows the ratio r of actual to predicted energy change. The same steps come from the eigenvectors of an augmented Hessian. The Kth eigenvector gives the Kth-state step, and α = 1 (the augmented-Hessian method) reduces to the CI eigenproblem. Recomputed: HJO's Fig. 12.1 model (Newton step 18.03, boundary solutions for h = 8, 16.13, 24) and the H₂/cc-pVDZ convergence from Hartree-Fock orbitals (Table 12.3). Unrestricted Newton lands on a saddle point 17.78 mE_h too high; the trust-region augmented Hessian reaches the minimum.
status: in-progress
kind: algorithm
level: advanced
tags: [mcscf, casscf, trust-region, level-shift, levenberg-marquardt, augmented-hessian, norm-extended-optimization, newton-method, step-control, excited-states]
prerequisites: [mcscf-parametrization-gradient-and-hessian, ci-optimization-newton-and-davidson]
related: [mcscf-second-order-optimization, scf-convergence-diis-and-newton, state-averaged-mcscf-and-configuration-rotations, upper-bounds-and-interlacing]
also: [07_Computational_Methods/Numerical_Optimization]
date: 2026-11-04
---

## Why restrict the Newton step

**The local model (HJO Sec. 12.3.1).** Each iteration expands the energy to second order:

$$
Q(\boldsymbol\lambda) = E^{(0)} + \mathbf E^{(1)\mathsf T}\boldsymbol\lambda + \tfrac12\boldsymbol\lambda^{\mathsf T}\mathbf E^{(2)}\boldsymbol\lambda .
$$

The Newton step $\mathbf E^{(2)}\boldsymbol\lambda = -\mathbf E^{(1)}$ is defined only up to the redundant direction $\boldsymbol\xi^{(0)}$ ([[mcscf-parametrization-gradient-and-hessian]]), so it is projected: $\mathbf P\boldsymbol\lambda = \boldsymbol\lambda$.

**Where Newton fails.** Close to the solution Newton converges quadratically. Far away, the model's stationary point need not resemble the real one, and in MCSCF it often does not. The step can be absurdly long, or go to a stationary point of the wrong type when the Hessian has the wrong number of negative eigenvalues.

## The level-shifted Newton step

**Trust region (HJO Sec. 12.3.2).** Optimize $Q$ only inside $\|\mathbf P\boldsymbol\lambda\|\le h$.

- **Newton step inside the region.** If it is shorter than $h$, take it. Always try it first, to keep quadratic convergence.
- **Otherwise go to the boundary.** For a minimum, go to the minimizer on the boundary. For an excited state, go to a suitable saddle point on it.

**Boundary points.** The Lagrangian with multiplier $\mu$ gives

$$
(\mathbf E^{(2)} - \mu\mathbf 1)\mathbf P\boldsymbol\lambda = -\mathbf E^{(1)},\qquad
\|\boldsymbol\lambda(\mu)\|^2 = \sum_i\frac{\phi_i^2}{(\varepsilon_i - \mu)^2},
$$

where $\varepsilon_i$ and $\phi_i$ are the Hessian eigenvalues and the gradient in the Hessian eigenbasis (the redundant zero eigenvalue omitted). The diagonalization is for analysis only; in practice the equations are solved iteratively.

**The step-length function (HJO Sec. 12.3.3).**

- **Shape.** It has $k+1$ branches separated by poles at the $k$ distinct eigenvalues, and tends to zero as $\mu\to\pm\infty$.
- **Number of boundary solutions.** At most $2k$: always one with $\mu<\varepsilon_1$ and one with $\mu>\varepsilon_k$, plus zero, one or two in each inner branch.
- **Levenberg-Marquardt trajectories.** The curves $\boldsymbol\lambda(\mu)$ traced as $\mu$ runs over each branch.
- **A too-long Newton step always has a solution with $\mu<0$.** If $\varepsilon_1<0$ this is the leftmost branch. If $\varepsilon_1>0$, lowering $\mu$ below zero shortens the step continuously.

!!! example "HJO Fig. 12.1 recomputed: $f = x^2 + 10y^2$ expanded at $(-15, 10)$ (computed for this note)"
    **Model.** Hessian eigenvalues 2 and 20; gradient $(-30, 200)$. The Newton step $(15, -10)$ has length 18.03.

    The middle branch $2<\mu<20$ has its minimum step length 16.13 at $\mu = 5.963$. That is why HJO chose $h = 16.13$: the trust circle there touches the middle branch at exactly one point.

    | Trust radius $h$ | Boundary solutions $\mu$ |
    |---:|---|
    | 8 | −7.312 (minimizer), 45.095 |
    | 16.13 | −0.346 (minimizer), 5.963 (double), 32.422 |
    | 24 | 0.616, 3.447, 11.595, 28.343 (Newton step lies inside) |

    - **h = 8.** There are only two solutions, one in each outer branch. The middle branch never comes down to 8.
    - **h = 24.** All four solutions exist ($2k = 4$), and the Newton step is acceptable.

## Choosing the level shift

**Ground states (HJO Sec. 12.3.4).** Require every mode to lower the energy. The rule is $\mu\le\min(\varepsilon_1, 0)$. Its solution is unique, though not guaranteed to be the global minimum on the boundary.

**Excited states (HJO Sec. 12.3.5).** For the first excited state:

- **Rule.** Raise the energy along the lowest mode and lower it along the others. The first-order condition is $\varepsilon_1<\mu<\varepsilon_2$; the second-order condition is $\varepsilon_1<2\mu<\varepsilon_2$.
- **When no solution exists.** Sometimes none satisfies both (in the model with $h = 8$, the branch $2<\mu<20$ is empty). Then take the solution for a larger radius and scale the step down.
- **Reliability.** Excited-state optimization is less robust. It may converge to a spurious state with misplaced negative eigenvalues, so always inspect the result.

**Updating the trust radius (HJO Sec. 12.3.6).** Compare the actual with the predicted energy change:

$$
r = \frac{E^{(0)}_{n+1} - E^{(0)}_n}{Q_n(\boldsymbol\lambda_n) - E^{(0)}_n} = 1 + O(\lambda_n).
$$

| $r$ | Action |
|---|---|
| $r > 0.75$ | $h_{n+1} = 1.2\,h_n$ |
| $0.25 < r < 0.75$ | keep $h$ |
| $0 < r < 0.25$ | $h_{n+1} = 0.7\,h_n$ |
| $r < 0$ | reject the step; retry with $h_n\to0.7\,h_n$ |

The scheme is not sensitive to these constants. What matters is that $h$ adapts.

## The Newton eigenvector method

**An eigenvalue problem (HJO Sec. 12.4.1).** Write the step in intermediate normalization, $\boldsymbol\Lambda = \boldsymbol\xi^{(0)} + \mathbf P\boldsymbol\lambda$. The model becomes a pure quadratic form, $Q = E^{(0)} + \tfrac12\boldsymbol\Lambda^{\mathsf T}\mathbf G\boldsymbol\Lambda$, with

$$
\mathbf G = \mathbf E^{(2)} + \boldsymbol\xi^{(0)}\mathbf E^{(1)\mathsf T} + \mathbf E^{(1)}\boldsymbol\xi^{(0)\mathsf T}.
$$

With multipliers for $\boldsymbol\Lambda^{\mathsf T}\mathbf O\boldsymbol\Lambda = 1$ (where $\mathbf O = \boldsymbol\xi^{(0)}\boldsymbol\xi^{(0)\mathsf T}$) and $\boldsymbol\Lambda^{\mathsf T}\mathbf P\boldsymbol\Lambda = h^2$, this gives

$$
\mathbf G\boldsymbol\Lambda = \nu\,\mathbf T(\alpha)\boldsymbol\Lambda,\qquad \mathbf T(\alpha) = \mathbf O + \alpha^2\mathbf P .
$$

Projecting with $\mathbf P$ recovers the level-shifted Newton equations with $\mu = \nu\alpha^2$.

**Symmetric form (HJO Sec. 12.4.2).** $\mathbf T^{\pm1/2}(\alpha) = \mathbf O + \alpha^{\pm1}\mathbf P$, since $\mathbf O$ and $\mathbf P$ are complementary projectors. Multiplying by $\alpha^2\mathbf T^{-1/2}$ on both sides turns the problem into an ordinary eigenproblem, $\mathbf G(\alpha)\boldsymbol\Lambda(\alpha) = \mu\boldsymbol\Lambda(\alpha)$ with $\boldsymbol\Lambda(\alpha) = \mathbf T^{1/2}\boldsymbol\Lambda$, of the "gradient-scaled" augmented Hessian

$$
\mathbf G(\alpha) = \mathbf E^{(2)} + \alpha\big(\boldsymbol\xi^{(0)}\mathbf E^{(1)\mathsf T} + \mathbf E^{(1)}\boldsymbol\xi^{(0)\mathsf T}\big).
$$

- **Scaling.** Each eigenvector is intermediately normalized.
- **Step.** It is $\boldsymbol\Lambda = \boldsymbol\xi^{(0)} + \alpha^{-1}\mathbf P\boldsymbol\Lambda(\alpha)$.
- **Step length.** $\alpha$ sets it: a larger $\alpha$ gives a shorter step.

**Choosing the eigenvector (NEO, HJO Sec. 12.4.3).** $\mathbf P\mathbf G(\alpha)\mathbf P = \mathbf E^{(2)}$. By the interlacing theorem ([[upper-bounds-and-interlacing]]), the eigenvalues of $\mathbf G(\alpha)$ interlace those of $\mathbf E^{(2)}$. So the $K$th eigenvector of $\mathbf G(\alpha)$ gives a step obeying the first-order rule for the $K$th state:

- the lowest eigenvector for the ground state;
- the second for the first excited state, and so on.

No separate search for the right $\mu$ interval is needed.

**Limits.**

- **$\alpha\to0$.** The method becomes numerically unstable as the gradient vanishes, so switch to the plain Newton step in the local region. For excited states the plain Newton step is always preferable there, since NEO would need all lower eigenvectors.
- **$\alpha\to\infty$.** Two eigenvalues, approximately $\pm\alpha\|\mathbf E^{(1)}\|$, run off to infinity. Their steps are infinitesimal steepest-descent and steepest-ascent steps, the $\mu\to\pm\infty$ ends of the level-shift picture.

**The augmented-Hessian method (HJO Sec. 12.4.4).** Fix $\alpha = 1$ and control the step length by scaling the eigenvector. Then

$$
{}^{cc}\mathbf G(1) = 2(\mathbf H - E^{(0)}\mathbf 1).
$$

With no orbital parameters, the method is exactly the CI eigenvalue problem, so it generalizes CI diagonalization to MCSCF.

## Convergence in practice: H₂

!!! example "HJO Tables 12.2-12.3 revisited: CASSCF(2,2)/cc-pVDZ, H₂ at 1.40 bohr (energy error / gradient norm per iteration; computed for this note)"
    **Setup.** My own one-step second-order optimizer in HJO's parametrization. Starting CI vector from the CAS diagonalization in the starting orbitals. Augmented-Hessian steps with $\alpha = 1$, trust radius 0.7, and the update rules above.

    | Start / method | It. 1 | It. 2 | It. 3 | It. 4 | It. 5 | Final |
    |---|---|---|---|---|---|---|
    | HF orbitals, augmented Hessian | 1.55e-2 / 1.8e-2 | 2.97e-3 / 1.2e-1 | 7.1e-5 / 7.1e-3 | 2.8e-7 / 1.0e-3 | 3e-12 / 1.4e-6 | minimum |
    | HJO Table 12.3 | 1.546e-2 / 1.83e-2 | 3.36e-3 / 1.05e-1 | 1.38e-4 / 1.38e-2 | 4.6e-7 / 1.42e-3 | 0 / 1.7e-6 | minimum |
    | HF orbitals, unrestricted Newton | 1.55e-2 / 1.8e-2 | 1.77e-2 / 2.4e-2 | 1.78e-2 / 2.6e-2 | 1.78e-2 / 2.2e-3 | 1.78e-2 / 3.2e-4 | saddle, +17.78 m$E_h$ |
    | MP2 natural orbitals, Newton | 2.77e-4 / 5.5e-2 | 1.0e-7 / 1.8e-4 | 0 / 6.1e-7 | | | minimum |
    | HJO Table 12.2 | 1.126e-4 / 3.31e-2 | 4e-8 / 3.0e-4 | 0 / 3.7e-7 | | | minimum |

    - **Hartree-Fock start.** It agrees with HJO's: error 0.01546 and gradient norm 0.0183. The first Hessian has one negative eigenvalue. The lowest augmented-Hessian eigenvector still steers into the local region, after which convergence is quadratic. My later iterations are close to, but not identical with, HJO's; the details of their NEO step control are not given.
    - **Unrestricted Newton.** It converges quadratically to a stationary point at $E_{\text{conv}} + 0.017780\,E_h$ with CI vector $(0.99996, -0.00938)$ and $1\sigma_u$ occupation 0.0002. These are HJO's "−1.129128 $E_h$, 18 m$E_h$ above the minimum, occupations 1.9998 and 0.0002". That point has one negative Hessian eigenvalue. It describes neither the ground nor the first excited state.
    - **MP2 natural orbitals.** They start in the local region, and three Newton steps converge. My starting error, 2.8e-4, is larger than HJO's 1.1e-4. I diagonalized the *unrelaxed* MP2 density; HJO do not say which density they used.

**Water (HJO Table 12.4).** The table caption says cc-pVDZ, but the text and the energy say cc-pVQZ. My valence CASSCF energies at the reference geometry:

- cc-pVQZ: −76.11653168 $E_h$ (HJO −76.11653159);
- cc-pVDZ: −76.07783559 $E_h$.

So the caption is a misprint. I did not reproduce the iteration history. HJO's first step (length 0.71) was rejected with $r = -0.73$ and retried with a radius of 0.47. After that came five Newton iterations: two or three global iterations followed by quadratic convergence, which they call typical.

**Lessons (HJO).**

- **Starting orbitals.** MP2 natural orbitals usually beat canonical HF orbitals, whose low virtuals are too diffuse for correlation.
- **Step control.** It is not optional. An unrestricted Newton optimization can converge, quadratically and convincingly, to the wrong kind of stationary point.

## Source

Helgaker, Jørgensen and Olsen, *Molecular Electronic-Structure Theory* (Wiley, Chichester, 2000), Secs. 12.3-12.4 and 12.5.5, pp. 610-621 and 628-630, Eqs. (12.3.1)-(12.4.30), Fig. 12.1, Tables 12.2-12.4. Recomputed for this note with PySCF 2.14 integrals and my own trust-region/augmented-Hessian driver (`hjo/c12/h2newton.py`, `hjo/c12/watcas.py`).
