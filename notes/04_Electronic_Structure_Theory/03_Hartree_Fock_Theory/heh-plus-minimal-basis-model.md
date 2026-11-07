---
id: heh-plus-minimal-basis-model
title: Minimal-basis HeH⁺ - Jørgensen-Simons' worked problems, from first-order SCF to MCSCF and size consistency
summary: HeH⁺ in two Slater 1s functions (ζ = 1.6875, 1.0; R = 1.4 bohr) is the running example of J-S Ch. 2. With their integrals - corrected from the OCR text against the page images - this note reproduces Roothaan SCF (linear convergence), exp(κ) second-order SCF (quadratic), two- and three-configuration CI, the perturbative iterative CI solver, one-step second-order MCSCF (equal to full CI here), and the √n failure of DCI for n separated ions.
status: in-progress
kind: implementation
level: intermediate
tags: [heh+, minimal-basis, model-system, scf, second-order-scf, ci, mcscf, size-consistency, worked-example]
prerequisites: [rhf, scf-procedure, orbital-rotations]
related: [perturbation-theory-second-quantization, scf-second-order-and-stability, mcscf-second-order-optimization, ci-in-practice, size-consistency, minimal-basis-h2-model, molecular-properties-and-response, polarization-propagator-rpa, one-particle-greens-function]
order: 80
date: 2026-11-03
---

## The model

**System.** HeH⁺, two electrons, $R = 1.4$ bohr. Basis: Slater 1s on He ($\zeta = 1.6875$) and on H ($\zeta = 1.0$). Nuclear repulsion $Z_{\text{He}}Z_{\text{H}}/R = 2/1.4 = 1.428571$ hartree.

**Atomic integrals (J-S Problem 2.1, physicists' notation, 1 = 1s$_{\text{He}}$, 2 = 1s$_{\text{H}}$).**

| Integral | Value | Integral | Value |
|---|---:|---|---:|
| $S_{12}$ | 0.5784 | $\langle11|11\rangle$ | 1.0547 |
| $h_{11}$ | −2.6442 | $\langle11|21\rangle$ | 0.4744 |
| $h_{22}$ | −1.7201 | $\langle12|12\rangle$ | 0.5664 |
| $h_{12}$ | −1.5113 | $\langle22|11\rangle$ | 0.2469 |
| | | $\langle22|21\rangle$ | 0.3504 |
| | | $\langle22|22\rangle$ | 0.6250 |

**Checks on the data.** $\langle11|11\rangle = \tfrac58\zeta_{\text{He}} = 1.0547$ and $\langle22|22\rangle = \tfrac58\zeta_{\text{H}} = 0.6250$, the Slater 1s self-repulsions. In chemists' notation $\langle12|12\rangle = (11|22)$ is the Coulomb integral between the two atoms and $\langle22|11\rangle = (21|21)$ the exchange-type one.

**OCR warning.** The extracted text of this page swaps $h_{22}$ and $h_{12}$ and garbles several digits (e.g. the first Fock matrix). The values above were read from the page image and reproduce every number J-S quote.

**Precision.** J-S print 4-decimal integrals but quote energies to 8 decimals, so they used more precise integrals. With the printed ones, every energy below lies about $1\times10^{-4}$ hartree below theirs. Orbitals, orbital energies, Fock and Hessian elements agree to the printed digits.

## First-order SCF (J-S Problem 2.1)

**Procedure.** Roothaan iterations $\mathbf F\mathbf c = \mathbf S\mathbf c\,\varepsilon$ with $F_{\mu\nu} = h_{\mu\nu} + \sum_{\rho\sigma}P_{\rho\sigma}\big(2\langle\mu\rho|\nu\sigma\rangle - \langle\mu\rho|\sigma\nu\rangle\big)$ and $P_{\rho\sigma} = c_\rho c_\sigma$. Guess $\phi_1 = 1s_{\text{He}}$.

**First iteration.**

$$
\mathbf F = \begin{pmatrix}-1.5895 & -1.0369\\ -1.0369 & -0.8342\end{pmatrix},
\qquad
\varepsilon = -1.6048,\ -0.2348,
\qquad
\phi_1 = 0.9194\,1s_{\text{He}} + 0.1296\,1s_{\text{H}} .
$$

**Second iteration.** $\varepsilon_1 = -1.6470$, $\varepsilon_2 = -0.2290$, $\phi_1 = 0.9032\,1s_{\text{He}} + 0.1537\,1s_{\text{H}}$. Both match J-S.

**Converged.**

$$
\phi_1 = 0.9000\,1s_{\text{He}} + 0.1584\,1s_{\text{H}},\qquad
\phi_2 = 0.8323\,1s_{\text{He}} - 1.2156\,1s_{\text{H}},\qquad
\varepsilon_1 = -1.6563,\ \varepsilon_2 = -0.2289 ,
$$

$E_{\text{SCF}} = -2.843528$ hartree (J-S −2.843425). The sign of $\phi_2$ is opposite to J-S's; this flips the sign of integrals with an odd number of index 2.

**MO integrals at convergence (J-S Q12).**

| Integral | Value | Integral | Value |
|---|---:|---|---:|
| $\langle1|h|1\rangle$ | −2.6158 | $\langle11|11\rangle$ | 0.9596 |
| $\langle1|h|2\rangle$ | ∓0.1954 | $\langle11|21\rangle$ | ±0.1954 |
| $\langle2|h|2\rangle$ | −1.3154 | $\langle12|12\rangle$ | 0.6063 |
| | | $\langle12|21\rangle$ | 0.1262 |
| | | $\langle22|21\rangle$ | ±0.0046 |
| | | $\langle22|22\rangle$ | 0.6159 |

Note $\langle1|h|2\rangle = -\langle11|21\rangle$: the Brillouin condition $f_{12} = h_{12} + \langle11|21\rangle = 0$ at convergence.

**Two energy formulas (J-S Q2-Q6).**

- **Formula (B):** $E = 2\sum_k h_{kk} + \sum_{kl}(2\langle kl|kl\rangle - \langle kl|lk\rangle) + V_{nn}$.
- **Formula (C):** $E = \sum_k(\varepsilon_k + h_{kk}) + V_{nn}$.

The two agree only at self-consistency, because (C) assumes $F\phi_k = \varepsilon_k\phi_k$ for the orbitals used. During iterations neither is guaranteed to be an upper bound; only the converged expectation value is (J-S Q11).

**Convergence (J-S Q10).** J-S's listed energies are formula (C), evaluated with the new orbital energy and the new orbital. Recomputed: −2.800603, −2.835736, −2.842255, −2.843324, −2.843495, −2.843523, −2.843527 (J-S −2.8005, −2.8356, −2.842151, −2.843221, −2.843393, −2.843420, −2.843425).

- **J-S's errors** 0.001274, 0.000204, 0.000032, 0.000005 shrink by a factor of about 6 per step. That is linear (first-order) convergence; a quadratic method would have given $0.001274^2 = 1.6\times10^{-6}$ after the first of these steps.
- **The true expectation value** of each new determinant, formula (B), is lower and converges faster: −2.842197, −2.843492, −2.843527, errors $1.3\times10^{-3}$, $3.6\times10^{-5}$, $1\times10^{-6}$. It is still linear, with a ratio of about 0.03 per iteration for this easy case.

**Dissociation (J-S Q13).** $1\sigma^2$ dissociates correctly to He + H⁺, both electrons on He. Unlike H₂, a closed-shell single determinant is qualitatively right here.

## Second-order SCF with exp(−κ) (J-S Problem 2.2)

**Orthonormal start.** $\phi_1 = 1s_{\text{He}}$, and Schmidt orthogonalization gives $\phi_2 = -0.7090\,1s_{\text{He}} + 1.2259\,1s_{\text{H}}$. Then $E = -2.805129$ (J-S −2.8050), with MO integrals $h_{22} = -1.2870$, $h_{12} = 0.0222$, $\langle11|21\rangle = -0.1663$, $\langle12|12\rangle = 0.5567$, $\langle22|11\rangle = 0.0766$, $\langle22|21\rangle = 0.0170$, $\langle22|22\rangle = 0.6200$.

**Closed-shell gradient and Hessian.** For a closed shell the density matrices factorize, $\sum_\sigma\langle0|a_{r\sigma}^\dagger a_{s\sigma}|0\rangle = 2\delta_{rs}\nu_r$ and $\sum_{\sigma\sigma'}\langle0|a_{r\sigma}^\dagger a_{s\sigma'}^\dagger a_{t\sigma'}a_{u\sigma}|0\rangle = (4\delta_{ru}\delta_{st} - 2\delta_{rt}\delta_{su})\nu_r\nu_s$. The matrices of [[mcscf-second-order-optimization]] become (occupied $\alpha,\beta,\gamma$; virtual $m,n$):

$$
(A_{11})_{n\beta,m\alpha} = 2\Big[-h_{\alpha\beta}\delta_{mn} + h_{nm}\delta_{\alpha\beta} + \delta_{\alpha\beta}\sum_\gamma\big(2\langle n\gamma|m\gamma\rangle - \langle n\gamma|\gamma m\rangle\big) - \delta_{mn}\sum_\gamma\big(2\langle\alpha\gamma|\beta\gamma\rangle - \langle\alpha\gamma|\gamma\beta\rangle\big) + 2\langle n\alpha|\beta m\rangle - \langle n\alpha|m\beta\rangle\Big],
$$

$$
(B_{11})_{n\beta,m\alpha} = 2\big[\langle mn|\beta\alpha\rangle - 2\langle mn|\alpha\beta\rangle\big],
\qquad
W_{\alpha m} = 2\Big[h_{m\alpha} + \sum_\gamma\big(2\langle m\gamma|\alpha\gamma\rangle - \langle m\gamma|\gamma\alpha\rangle\big)\Big] .
$$

$W$ is twice the occupied-virtual Fock element: Brillouin's theorem is $W = 0$.

**Numbers.** $A_{11} = 1.8716$, $B_{11} = -0.1532$, $W = -0.2882$ (J-S 1.8713, −0.1530, −0.2880), so $\kappa = W/(A_{11} - B_{11}) = 0.1423$ in magnitude. A finite-difference derivative of the exactly rotated energy gives $dE/d\kappa = -0.5763 = 2W$ and $d^2E/d\kappa^2 = 4.0495 = 2(A_{11} - B_{11})$, confirming the formulas.

**Iterations.** Rotate with the $2\times2$ $e^{-\boldsymbol\kappa}$ of [[baker-campbell-hausdorff]], re-transform the integrals, repeat:

| Iteration | $E$ (this note) | $E$ (J-S) |
|---:|---:|---:|
| 0 | −2.80512857 | −2.80504513 |
| 1 | −2.84313838 | −2.84303574 |
| 2 | −2.84352780 | −2.84342526 |
| 3 | −2.84352782 | −2.84342527 |

The errors $3.8\times10^{-2}$, $3.9\times10^{-4}$, $2\times10^{-8}$ square at each step: **quadratic** convergence (J-S Q8). Each step costs an integral transformation; Roothaan steps are cheaper but need more of them.

## Configuration interaction (J-S Problems 2.3-2.5)

**Configurations.** With the converged SCF orbitals: $|1\sigma^2\rangle$, $|2\sigma^2\rangle$ and the singlet $|1\sigma2\sigma\rangle = 2^{-1/2}\big(|1\alpha2\beta| - |1\beta2\alpha|\big)$.

**Matrix elements (electronic).**

- $\langle1\sigma^2|H|1\sigma^2\rangle = 2h_{11} + \langle11|11\rangle = -4.2721$
- $\langle2\sigma^2|H|2\sigma^2\rangle = 2h_{22} + \langle22|22\rangle = -2.0148$
- $\langle1\sigma^2|H|2\sigma^2\rangle = \langle11|22\rangle = 0.1262$
- $\langle1\sigma^2|H|1\sigma2\sigma\rangle = \sqrt2\,(h_{12} + \langle11|21\rangle) = 0$, Brillouin
- $\langle2\sigma^2|H|1\sigma2\sigma\rangle = \sqrt2\,(h_{12} + \langle22|12\rangle) = \mp0.2698$
- $\langle1\sigma2\sigma|H|1\sigma2\sigma\rangle = h_{11} + h_{22} + \langle12|12\rangle + \langle12|21\rangle = -3.1987$

**Two-configuration CI (Problem 2.3).** $E = -4.2791$ and $-2.0078$, ground vector $(0.9985, -0.0556)$ (J-S −4.2790, (0.9984, −0.0556)). The ground state can be rewritten as a single **two-determinant** configuration with polarized orbitals $a^{1/2}\phi_1\pm b^{1/2}\phi_2$, $a = 0.9984$, $b = 0.0556$: the different-orbitals-for-different-spins form of a two-configuration function.

**Three-configuration (full) CI (Problem 2.4).** Eigenvalues −4.2793, −3.2566, −1.9497 (J-S −4.2792, −3.2567, −1.9497); ground vector $(0.9983, -0.0573, \mp0.0143)$. Total ground energy −2.85077 (J-S −2.8506). The $1\sigma2\sigma$ configuration does not couple to $1\sigma^2$ but enters through $2\sigma^2$.

**Perturbative iterative solution (Problem 2.5).** $\mathbf H^0$ = diagonal, $\mathbf c^{(k)} = (E - \mathbf H^0)^{-1}\mathbf V\mathbf c^{(k-1)}$ in intermediate normalization, $E = H_{11} + \sum_j V_{1j}c_j$. J-S damp the first step (average with $\mathbf c^0$) because the undamped iterates oscillate. Here: $E = -4.2756$, $-4.2791$, $-4.2792$, $-4.2793$ in iterations 1-4, with the vector converging to the CI eigenvector. The general method is in [[ci-in-practice]].

## One-step second-order MCSCF (J-S Problem 2.6)

**Setup.** Configurations $1\sigma^2$ and $2\sigma^2$. The parameters are one orbital rotation $\kappa$ ($1\leftrightarrow2$) and one state rotation $P$ between the two CI roots. Start from the SCF orbitals and the two-configuration CI states.

**First iteration (this note vs J-S).**

- **Gradient.** $\partial E/\partial\kappa = 0.0447$ ($= 2|W_{12}|$, J-S $W_{12} = -0.0224$) and $\partial E/\partial P = 0$, since the states come from a CI.
- **Hessian $(\mathbf A - \mathbf B)$.** Orbital-orbital 2.4009 (J-S $A_{12,21} - B_{12,21} = 2.1606 + 0.2400 = 2.4006$). Orbital-state coupling 0.4215 in magnitude (J-S $0.4020 + 0.0198 = 0.4218$). State-state 2.2714 ($= E_1 - E_0$ of the CI).
- **Step.** $|\kappa| = 0.0096$, $|P| = 0.0018$ (J-S 0.0097 and 0.0018).

**Energies.** −2.85055810 → −2.85077291 → −2.85077291 (J-S −2.85044942, −2.85066435, −2.85066436). The first value is the CI with SCF orbitals; one Newton step converges to $10^{-8}$.

**Interpretation (J-S Q5, Q7-Q9).**

- **Equal to full CI.** The converged two-configuration MCSCF energy equals the three-configuration full CI, −2.85077291. The $1\sigma2\sigma$ configuration is generated by the orbital rotation $\kappa$: two configurations plus one orbital parameter span the full CI space.
- **Three configurations.** If $1\sigma2\sigma$ is added to the MCSCF, the orbital rotation becomes **redundant**, and MCSCF = CI.
- **Two-step equivalence.** After the first iteration the one-step and two-step procedures give the same orbitals here, because the start already satisfies $\mathbf V = 0$. Later iterations differ, because the two-step method rediagonalizes the CI.

## n separated HeH⁺ ions (J-S Problem 2.7)

**DCI matrix.** $n$ noninteracting ions, reference $|\text{HF}\rangle$ plus the $n$ local doubles. With $B = \langle11|22\rangle = 0.1262$ and $C = E(2\sigma^2) - E(1\sigma^2) = 2.2573$, the same arrow-shaped matrix as for H₂ ([[size-consistency]]) gives

$$
E_{\text{corr}}(\text{DCI}, n) = \tfrac12\Big[C - \big(C^2 + 4nB^2\big)^{1/2}\Big],
$$

which grows as $\sqrt n$, not $n$.

!!! example "Size-consistency error of DCI (computed for this note)"
    | $n$ | $E_{\text{corr}}$ | per ion | % of $n\times$ monomer |
    |---:|---:|---:|---:|
    | 1 | −0.007030 | −0.007030 | 100.0 |
    | 2 | −0.014017 | −0.007009 | 99.7 |
    | 4 | −0.027865 | −0.006966 | 99.1 |
    | 10 | −0.068446 | −0.006845 | 97.4 |
    | 100 | −0.564199 | −0.005642 | 80.3 |
    | 1000 | −3.017762 | −0.003018 | 42.9 |

    - **Agreement with J-S.** J-S's solution table: −0.0684, −0.5637 and −3.0156 at n = 10, 100 and 1000, with errors 2.3, 19.5 and 56.9% (they divide by $n\times0.0070$).
    - **Not yet asymptotic.** $n = 100$ is not in the $\sqrt n$ regime: the 100→1000 ratio is 5.35, not $\sqrt{10} = 3.16$.
    - **Comparison (Bartlett and Purvis, quoted by J-S; literature).** DCI errors for $n$ H₂ molecules: 1.5, 4.8, 12.3, 48.0 and 79.1% for n = 2, 4, 10, 100, 1000. For He atoms: 0.8, 2.4, 6.5, 34.8 and 70.8%.
    - **Why HeH⁺ looks better (J-S Q5).** The two-function HeH⁺ model has a small correlation energy and a large excitation gap ($C = 2.26$ hartree). It therefore underestimates the size-consistency error that a realistic basis would show.

## Perturbation theory, coupled cluster, properties and propagators (J-S Problems 3.1-3.2, 4.1, 5.1-5.3, 6.1-6.3)

The later J-S chapters reuse this model. The worked results are in the notes on each method (all recomputed; J-S in parentheses):

| Quantity | Value (a.u.) | Note |
|---|---|---|
| Correlation energy: MP2, MP2 + MP3 | −0.005576, −0.006743 (−0.0056, −0.0067) | [[perturbation-theory-second-quantization]], [[linked-cluster-theorem]] |
| Correlation energy: linear CCD, CCD = 2×2 CI, full CI | −0.007052, −0.007030, −0.007245 (−0.0070, −0.0070, −0.0072) | [[coupled-cluster-second-quantization]] |
| Brillouin-Wigner second order, per ion, n = 1 and 1000 | −0.004169, −0.000017 | [[perturbation-theory-second-quantization]] |
| Full-CI excitation energies | 1.0227, 2.3297 (1.0225, 2.3295) | [[molecular-properties-and-response]] |
| Full-CI static polarizability $\alpha_{zz}$ | 1.1223 | [[molecular-properties-and-response]] |
| CHF polarizability | 0.9876 (0.9878) | [[molecular-properties-and-response]] |
| CMCHF polarizability | 1.1230 from J-S's matrices (1.1232) | [[molecular-properties-and-response]] |
| TDHF excitation energy, moment | 1.0659, 0.7255 (1.0657, 0.7255) | [[polarization-propagator-rpa]] |
| IP: Koopmans, second-order $\Sigma$, exact | 1.6563, 1.6351, 1.6348 | [[one-particle-greens-function]] |

## Code

```python
S = np.array([[1, .5784], [.5784, 1]]); h = np.array([[-2.6442, -1.5113], [-1.5113, -1.7201]])
# chemists' (pq|rs) from J-S physicists' values: <11|11>=(11|11), <11|21>=(12|11), <12|12>=(11|22),
# <22|11>=(21|21), <22|21>=(22|21), <22|22>=(22|22); fill with 8-fold symmetry into G[p,q,r,s]
def fock(c):
    P = np.outer(c, c)
    return h + 2*np.einsum("pqrs,rs->pq", G, P) - np.einsum("prqs,rs->pq", G, P), P
def energy(C):                                   # closed shell, occupied orbital in column 0
    F, P = fock(C[:, 0]); return np.sum(P*(h + F)) + 2/1.4
K = lambda k: np.array([[0, -k], [k, 0]])
for it in range(4):                              # second-order SCF on the single rotation angle
    f = lambda k: energy(C @ expm(K(k)))
    g = (f(1e-5) - f(-1e-5))/2e-5; H2 = (f(1e-5) - 2*f(0) + f(-1e-5))/1e-10
    C = C @ expm(K(-g/H2))
```

## Source

Jørgensen and Simons, *Second Quantization-Based Methods in Quantum Chemistry* (Academic Press, New York, 1981), Ch. 2, Problems 2.1-2.7, pp. 48-55, and Solutions, pp. 55-66. Integrals read from the page images (p. 49); all other numbers recomputed for this note and compared with J-S's solutions. Bartlett-Purvis DCI errors are literature values quoted by J-S (p. 55).
