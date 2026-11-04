---
id: multipole-methods-and-integral-screening
title: Scaling of molecular integrals, Schwarz screening, classical versus nonclassical Coulomb integrals, and multipole methods up to the fast multipole method
summary: In large systems the significant overlap and kinetic integrals grow linearly and the significant two-electron integrals quadratically, not quartically. Most of the latter are classical interactions between non-overlapping distributions; only the nonclassical part, which decays as erfc, grows linearly. The Schwarz inequality |(ab|cd)| ≤ (ab|ab)^½(cd|cd)^½ lets codes skip negligible integrals. Classical integrals can be computed from multipole expansions, and the fast multipole method evaluates their total contribution in linear time. HJO's hydrogen-chain model (counts, 6.9 bohr cutoff, 3.2 bohr extent), the erfc ratio and the convergence of a bipolar multipole expansion were all checked numerically.
status: in-progress
kind: algorithm
level: advanced
tags: [integral-screening, schwarz-inequality, linear-scaling, multipole-expansion, fast-multipole-method, classical-coulomb, nonclassical-coulomb, extent, sparsity]
prerequisites: [electron-repulsion-integrals-md-os-rys, solid-harmonics-angular-basis]
related: [gaussian-overlap-distributions-and-one-electron-integrals, scf-procedure, coulomb-cusp-and-helium-expansions]
also: [04_Electronic_Structure_Theory/13_Integral_and_Algorithmic_Techniques/07_Algorithm_Complexity]
date: 2026-11-04
---

## How many integrals are significant? (HJO Sec. 9.12)

**HJO's model.** A linear chain of $n$ hydrogen atoms 1 bohr apart, each carrying one unnormalized $1s$ Gaussian of unit exponent. An integral is "significant" if larger than $10^{-10}$.

**Overlap and kinetic integrals.**

- **Decay.** $S_{ab} = (\pi/(a+b))^{3/2}\exp(-\tfrac{ab}{a+b}R_{AB}^2)$ falls off as a Gaussian in the separation.
- **Cutoff and crossover.** Beyond a fixed distance $d_s$ every overlap is negligible, so the matrix is banded and the number of significant elements grows **linearly** once $n$ exceeds about $d_s$. In the model, $d_s$ = 6.9 bohr, with the crossover near seven atoms.
- **Kinetic integrals.** These are combinations of overlaps of higher $l$ and behave the same way, crossing over slightly later.

**Two-electron integrals.** For $s$ functions,

$$
g_{abcd} = \frac{2\pi^{5/2}}{pq\sqrt{p+q}}K_{ab}K_{cd}F_0(\alpha R_{PQ}^2) = S_{ab}S_{cd}\,\frac{\operatorname{erf}(\sqrt\alpha R_{PQ})}{R_{PQ}}.
$$

- **Quadratic, not quartic.** $g_{abcd}$ is small only if $S_{ab}$ or $S_{cd}$ is small, so the significant count grows as (significant pairs)², i.e. **quadratically**, once the overlaps go linear.
- **No further gain in practice.** The $1/R_{PQ}$ tail would make the count linear only for separations of order $10^{10}$ bohr.

!!! example "HJO's hydrogen-chain model recomputed (computed for this note)"
    Unnormalized $e^{-r^2}$ on each of $n$ collinear centres 1 bohr apart, threshold $10^{-10}$:

    | $n$ | $S$ total | $S$ significant | $T$ significant | $g$ total | $g$ significant | nonclassical $g$ significant | Schwarz bound significant |
    |---:|---:|---:|---:|---:|---:|---:|---:|
    | 2 | 4 | 4 | 4 | 16 | 16 | 16 | 16 |
    | 4 | 16 | 16 | 16 | 256 | 256 | 256 | 256 |
    | 7 | 49 | 49 | 49 | 2 401 | 2 341 | 2 199 | 2 341 |
    | 10 | 100 | 88 | 94 | 10 000 | 7 228 | 4 926 | 7 348 |
    | 15 | 225 | 153 | 169 | 50 625 | 21 077 | 9 471 | 21 653 |
    | 20 | 400 | 218 | 244 | 160 000 | 41 792 | 14 016 | 43 408 |
    | 30 | 900 | 348 | 394 | 810 000 | 103 772 | 23 106 | 109 268 |
    | 40 | 1 600 | 478 | 544 | 2 560 000 | 193 152 | 32 196 | 204 928 |

    - **Overlap.** Significant overlaps grow by exactly 13 per atom ($2\times6 + 1$: neighbours within 6.89 bohr). The cutoff $\sqrt{2\ln[(\pi/2)^{3/2}/10^{-10}]}$ = 6.89 bohr matches HJO's 6.9.
    - **Nonclassical integrals** grow by a constant 909 per added atom from $n = 20$ to 40, i.e. linearly.
    - **All significant integrals.** Their count grows roughly as $n^2$ (doubling $n$ from 20 to 40 multiplies it by 4.6, still approaching the asymptotic factor 4). At $n = 40$ they are only 7.5% of all $n^4$ integrals.
    - **Schwarz bound.** It never fails (apart from underflow below $10^{-100}$), and it flags only 2-6% more integrals than are truly significant.

## Classical and nonclassical parts

**Splitting the integral.** Write $\operatorname{erf} = 1 - \operatorname{erfc}$:

$$
g_{abcd} = \underbrace{\frac{S_{ab}S_{cd}}{R_{PQ}}}_{\text{classical}} - \underbrace{S_{ab}S_{cd}\frac{\operatorname{erfc}(\sqrt\alpha R_{PQ})}{R_{PQ}}}_{\text{nonclassical}},\qquad
\frac{g^{\text{non}}}{g^{\text{cls}}} = -\operatorname{erfc}\Big(\sqrt{\tfrac{pq}{p+q}}R_{PQ}\Big)\quad(9.12.15).
$$

**Behaviour.**

- **Decay.** The nonclassical part decays faster than any overlap, so the number of significant nonclassical integrals grows linearly.
- **Small separations.** At small $R_{PQ}$ both parts diverge and the integral is their small difference.

**Extent of a Gaussian (HJO Eqs. 9.12.10-9.12.14).**

- **Definition.** For target accuracy $10^{-k}$, take $r_p = \operatorname{erfc}^{-1}(10^{-k})/\sqrt p$.
- **Classical test.** If $R_{PQ} > r_p + r_q$, then $\sqrt{pq/(p+q)}R_{PQ}\ge\operatorname{erfc}^{-1}(10^{-k})$ and the interaction is classical to that accuracy.
- **Model value.** In the model, $p = 2$ and $k = 10$ give $r_p$ = 3.23 bohr (HJO 3.2), so classical integrals appear beyond 6.4 bohr.

!!! example "The erfc ratio (computed for this note)"
    For two $s$ distributions with $p = q = 2$:

    | $R_{PQ}$ (bohr) | 1.0 | 2.0 | 3.2 | 4.0 | 6.4 |
    |---|---:|---:|---:|---:|---:|
    | $(g - g^{\text{cls}})/g^{\text{cls}}$ | −1.573e-1 | −4.678e-3 | −6.026e-6 | −1.542e-8 | (below double precision) |
    | $-\operatorname{erfc}(\sqrt\alpha R)$ | −1.573e-1 | −4.678e-3 | −6.026e-6 | −1.542e-8 | −1.4e-19 |

    The two rows agree to all digits shown.

**Consequence for algorithms.**

- **Nonclassical integrals** need MD, OS or Rys ([[electron-repulsion-integrals-md-os-rys]]); their number grows linearly.
- **Classical integrals** need only multipole moments. Their total contribution to the Coulomb matrix can even be obtained in linear time without forming individual integrals.

## The Schwarz inequality and screening (HJO Sec. 9.12.4)

**Positive definiteness.** Through the Fourier representation of $1/r_{12}$, the self-repulsion of any real charge distribution is

$$
J[\rho] = \frac1{2\pi^2}\int k^{-2}\lvert\tilde\rho(\mathbf k)\rvert^2\,\mathrm d\mathbf k\ge0 .
$$

So the matrix $g_{ab,cd}$ (pairs as row and column labels) is positive definite, and $(ab|cd)$ is an inner product. Cauchy-Schwarz then gives

$$
\lvert(ab|cd)\rvert\le(ab|ab)^{1/2}(cd|cd)^{1/2}.
$$

**Use in practice.** Precompute $Q_{ab} = (ab|ab)^{1/2}$ for all pairs (cost $\mathcal O(n^2)$), then skip any batch with $Q_{ab}Q_{cd}$ below threshold. This needs no geometry, works for any angular momentum, and costs nothing per skipped integral.

**Limitation.** The bound measures overlap only. It does not see the $1/R_{PQ}$ decay between distant pairs, so it cannot reduce the count below quadratic.

**Outside HJO (general knowledge, not from the book):** positive-definiteness of the ERI matrix is also what makes Cholesky decomposition and density fitting of it possible. Notes on those do not exist yet.

## Multipole expansion of a two-electron integral (HJO Sec. 9.13)

**Setting.** Write $\mathbf r_1 = \mathbf P + \mathbf r_{1P}$, $\mathbf r_2 = \mathbf Q + \mathbf r_{2Q}$ and $\mathbf R_{QP} = \mathbf Q - \mathbf P$. Where $\lvert\mathbf r_{1P} - \mathbf r_{2Q}\rvert < R_{QP}$, the partial-wave expansion of $1/r_{12}$ and the addition theorem for solid harmonics give the **bipolar multipole expansion** (9.13.19):

$$
g_{abcd} = \sum_{lm}\sum_{jk}q^{ab}_{lm}(\mathbf P)\,T_{lm,jk}(\mathbf R_{QP})\,q^{cd}_{jk}(\mathbf Q),\qquad
q^{ab}_{lm}(\mathbf P) = \int\Omega_{ab}(\mathbf r)R_{lm}(\mathbf r_P)\,\mathrm d\mathbf r .
$$

**Ingredients.**

- **Scaled solid harmonics.** $R_{lm} = r^lC_{lm}/\sqrt{(l-m)!(l+m)!}$ (regular) and $I_{lm} = \sqrt{(l-m)!(l+m)!}\,r^{-l-1}C_{lm}$ (irregular), with Racah-normalized $C_{lm}$ ([[solid-harmonics-angular-basis]]). Their addition theorem has no numerical factors: $R_{lm}(\mathbf u + \mathbf v) = \sum_{jk}R_{l-j,m-k}(\mathbf u)R_{jk}(\mathbf v)$.
- **Interaction matrix.** $T$ contains only irregular harmonics of $\mathbf R_{QP}$. All information about the distributions is in the moments.
- **Lowest order.** $q_{00} = S_{ab}$ gives the monopole term $S_{ab}S_{cd}/R_{PQ}$, the classical part above.

**Convergence (9.13.28-9.13.29).**

- **Truncation error.** It falls by a constant factor $\sim r_{12}/R_{QP}$ per order.
- **Asymptotic, not convergent.** Gaussian distributions always overlap a little, so the convergence condition never holds everywhere and the expansion is strictly asymptotic. It is useful as long as the overlapping region contributes less than the target error, which is exactly the extent criterion.

!!! example "Convergence of a multipole expansion for a (pₓ p_z | p_y d_xy)-type primitive integral (computed for this note)"
    **Setup.** Bra: $x_A$ and $z_B$ primitives ($a = 0.8$, $b = 0.6$; $A$ at the origin, $B = (1, 0.3, 0)$). Ket: $y_C$ and $x_Dy_D$ ($c = 0.7$, $d = 0.5$), both displaced by about $R$ along $z$. I expanded $1/\lvert\mathbf R + \mathbf r_{2Q} - \mathbf r_{1P}\rvert$ in Cartesian Taylor form to total order $L$, used the exact Cartesian moments of each overlap distribution about its own centre, and compared with the exact MD integral. Relative errors:

    | $R_{PQ}$ (bohr) | $L$ = 0 | 2 | 4 | 6 | 8 | 10 |
    |---:|---:|---:|---:|---:|---:|---:|
    | 4.3 | 1.0 | 0.40 | 4.2e-2 | 1.5e-5 | 1.5e-5 | 1.5e-5 |
    | 6.3 | 1.0 | 0.16 | 7.5e-3 | 1.8e-11 | 1.8e-11 | 1.8e-11 |
    | 8.3 | 1.0 | 0.090 | 2.3e-3 | 5e-16 | 7e-16 | 2e-16 |
    | 12.3 | 1.0 | 0.040 | 4.6e-4 | 3e-16 | 7e-16 | 3e-15 |

    - **Monopole.** The monopole term vanishes because $S_{ab} = 0$ for these functions.
    - **Termination.** The expansion stops at total order 5 ($= l_a + l_b + l_c + l_d$). An overlap distribution is a finite sum of Hermite Gaussians centred at $P$, and a Hermite Gaussian $\Lambda_{tuv}$ has only (traceless) multipoles of order $t + u + v$. This is the termination for one-centre distributions noted by HJO.
    - **What remains** beyond $L = 6$ is the **nonclassical** part: $1.5\times10^{-5}$ at 4.3 bohr, $10^{-11}$ at 6.3 bohr, and nothing above 8 bohr. The extent criterion predicts this behaviour: the residual drops by about $10^6$ between 4.3 and 6.3 bohr, which agrees within a factor of two with $\exp(-\alpha R^2)$, $\alpha = pq/(p+q) = 0.65$ (a drop of $9\times10^5$).

**Practical steps.**

- **Contracted integrals.** Moments are contracted first, so the expansion acts on contracted pairs.
- **Changing origin.** Moments are moved to a common origin with the translation matrix built from the addition theorem (HJO Secs. 9.13.3-9.13.4).
- **Real arithmetic.** Real versions of the moments and of the translation and interaction matrices avoid complex numbers (9.13.5-9.13.7).
- **Generating the harmonics.** The scaled harmonics are generated by recurrences like those of [[solid-harmonics-angular-basis]] (9.13.8).

## From the naive multipole method to the FMM (HJO Sec. 9.14)

HJO present the multipole methods for point charges first.

**Naive box method.**

- **Setup.** Divide space into equal boxes. Nearest neighbours (27 boxes in 3D, including the box itself) form the near field (NF) and are treated exactly. Well-separated boxes form the far field (FF) and interact through box multipole expansions.
- **Cost.** NF work is linear, but each box has $\mathcal O(N)$ FF boxes, so the total is still **quadratic** (with a small prefactor).

**Two-level method.** Group boxes into parents. Children of the parent's nearest neighbours that are well separated form the local far field (LFF). Everything farther is the remote far field (RFF), handled through the parent's field. This keeps the ratio of box size to distance roughly constant.

**Fast multipole method.** Build a hierarchy: level 0 is one box, level $l$ has $8^l$ boxes, and the deepest level is $S\approx\log_8N$. The hierarchy has $(8N-1)/7$ boxes in total, about 7/8 of them at the deepest level. For $10^6$ particles $S = 5$ gives about 30 particles per smallest box.

1. Form multipole moments of each deepest box.
2. Translate them upwards to all parents.
3. For each box, add the field of its $6^3 - 3^3 = 189$ LFF boxes.
4. Pass each parent's total far field down to its children as their RFF, and add their own LFF.
5. Contract each particle's moments with the far-field vector of its box.
6. Add near-field interactions explicitly.

Every step costs a fixed amount per box or particle, so the total cost is **linear in $N$**. Accuracy is controlled by the expansion order $L$ and the box size (10-100 particles per box).

**Continuous FMM (Sec. 9.14.4).** Gaussian distributions can interact nonclassically and vary in size, so the near field must depend on the extent.

- **Branches.** At each level the CFMM introduces branches with even near-field widths $Q_n$ (in boxes).
- **Assignment.** Each distribution goes to the branch with $Q_n = \max\big(Q_1, 2\lceil r_p/\Lambda_l\rceil\big)$, where $r_p = p^{-1/2}\operatorname{erfc}^{-1}(10^{-k})$ is its extent (the same definition as above) and $\Lambda_l$ the box size at level $l$. This guarantees that the far field contains only classical interactions.
- **Steps.** They are those of the FMM, with sums replaced by integrals over the Gaussians.
- **Cost (HJO).** It depends on the extents. If every Gaussian spans the whole system, nothing is far field and the cost reverts to explicit (quartic) integration. Linear scaling sets in only for systems much larger than the largest extent; in general the cost lies between explicit integration and the point-charge FMM.

## Source

Helgaker, Jørgensen and Olsen, *Molecular Electronic-Structure Theory* (Wiley, Chichester, 2000), Secs. 9.12-9.14, pp. 398-425, Eqs. (9.12.1)-(9.14.25), Figs. 9.12-9.16. The integral counts, cutoff distance, extent, erfc ratio, Schwarz test and multipole-convergence example were computed for this note (NumPy, SciPy, SymPy; my own MD code). The FMM description and the CFMM summary follow HJO and were not implemented.
