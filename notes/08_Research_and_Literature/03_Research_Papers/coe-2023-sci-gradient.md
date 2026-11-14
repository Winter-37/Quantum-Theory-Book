---
id: coe-2023-sci-gradient
title: Coe 2023 - Analytic gradients for selected configuration interaction
summary: Derives analytic nuclear gradients for a selected-CI wave function on RHF orbitals. Because a truncated determinant list is not invariant to occupied-occupied or virtual-virtual rotations, CPHF responses are needed for every orbital pair; they fold into one modified Z-vector solve. Orbital pairs in different irreps of an abelian group are shown not to contribute, so symmetry degeneracies cause no singularities. Validated against a seminumerical gradient; MCCI gradients approach FCI quality with a small fraction of the determinants.
kind: paper
status: in-progress
tags: [selected-CI, MCCI, analytic-gradients, CPHF, z-vector, degeneracies, symmetry, PySCF]
prerequisites: []
related: [selected-ci-analytic-gradient, ci-analytic-gradient, z-vector-method, sample-based-quantum-diagonalization]
order: 25
authors: J. P. Coe
journal: Journal of Chemical Theory and Computation 19, 874-886
year: 2023
doi: 10.1021/acs.jctc.2c01062
date: 2026-11-09
---

## Research problem

**Gradients for compact CI.** Selected CI reaches near-FCI energies with a small fraction of the determinants, without choosing an active space. For geometry optimization or dynamics it needs analytic gradients.

**Why it is harder than CISD.** A CISD energy with all electrons correlated is invariant to oo and vv rotations, so only occupied-virtual CPHF responses enter. A selected-CI energy is not invariant to any rotation.

- **The cost.** Responses are needed for all orbital pairs.
- **The worry.** Those responses carry $1/(\varepsilon_q-\varepsilon_p)$ factors that look singular at degeneracies.

## Method

**Wave function.** Monte Carlo CI (MCCI): configurations are added at random and removed when $|c_I|$ falls below a cutoff $c_{\min}$, repeated to convergence. The gradient theory applies to any selected CI.

**Fully numerical gradients.** Coe argues against them:

- **Cost.** They need $O(3N_A)$ selected-CI runs.
- **Accuracy.** They are step-size dependent.
- **Stochastic selection.** It adds noise to every displaced run.

**Seminumerical gradients.** One selected-CI run; the RDMs are fixed and only the MO integrals are differenced, using SCF runs at displaced geometries. Cost $O(3N_AM^5)$, still step-dependent. Used as the reference for the analytic method.

**Analytic gradients.**

- **The gradient.** RDMs contracted with derivative integrals, plus the orbital-response term $2\sum_{tp}F_{tp}U^{X}_{tp}$ (Eq. 7). It is rearranged with orthonormality into $2\sum_{t>p}\Delta F_{tp}U_{tp} - \sum\tilde F S^X$ (Eq. 11).
- **Response for every pair.** The vo pairs come from CPHF (Eq. 12). The oo and vv pairs come from the same equations rearranged with a $1/(\varepsilon_q-\varepsilon_p)$ factor (Eq. 13).
- **One solve.** Via Handy-Schaefer, with a modified Lagrangian $\Delta F'$ that absorbs the oo/vv pairs (Eqs. 14-16).
- **AO evaluation.** Back-transformed densities, so the per-coordinate cost is $O(M^4)$ (Eqs. 17-18).

## Mathematical contributions

Restated and derived in the notebook's notation in [[selected-ci-analytic-gradient]]; the key equations there are:

$$
U^x_{pq} = \frac{F^x_{pq} - \varepsilon_qS^x_{pq} + \sum_k\sum_{l\in\rm occ}U^x_{kl}A_{pq,kl}}{\varepsilon_q-\varepsilon_p}\quad(\text{oo, vv}),
\qquad
l'_{ai} = 2(X_{ai}-X_{ia}) + 2\sum_{p>q}\frac{X_{pq}-X_{qp}}{\varepsilon_q-\varepsilon_p}A_{pq,ai}.
$$

**Symmetry result (Sec. 2.4, Eqs. 20-21).** For $\Psi$ of definite irrep and orbitals of definite irreps in an abelian group, $F_{tp}=0$ whenever $t$ and $p$ belong to different irreps. Such pairs drop out regardless of their energy gap.

## Implementation

- **Integrals and SCF.** AO derivative integrals from Libcint through PySCF; RHF orbitals and energies from PySCF.
- **Wave functions.** MCCI program for the wave functions; an efficient selected-CI 2-RDM algorithm (Coe et al., JCTC 2022).
- **Determinants.** Slater determinants, not CSFs, so a different $M_s=0$ spin state can be converged on at dissociation.
- **Numerical threshold.** $|\Delta F_{tp}| < 10^{-8}$ is set to zero.
- **FCI reference gradients.** From full-space MCSCF in MOLPRO.

## Results

**Validation against the seminumerical gradient.** In each case it converges to the analytic value as the step shrinks.

- **CO.** 6-31G, two frozen orbitals, 3 bohr. The CPHF contribution is about 1.2% of the gradient.
- **CO, cc-pVTZ.**
    - **Near-degeneracy.** The smallest relevant gap was $3\times10^{-3}$ $E_h$.
    - **Hellmann-Feynman.** The operator-only force gave −0.027 (O) and 0.071 (C) $E_h$/bohr, far from the full gradient.
- **NH$_3$.** Distortions of 0.01 Å and $10^{-3}$ Å from trigonal planar, which leave gaps down to $1.3\times10^{-4}$ $E_h$. Without CPHF the gradient is up to 4.4 times too small. The seminumerical step needed to drop to about $10^{-6}$ bohr.
- **H$_4$, H$_6$, CH$_4$.** Slightly distorted square H$_4$, distorted hexagonal H$_6$ (and H$_6$ with a ghost atom), and distorted CH$_4$: all agree.

**Accuracy against FCI.** RMSE of the gradient over a bond-length scan ($E_h$/bohr), with the mean number of determinants:

| System | HF | MCCI $c_{\min}=10^{-3}$ | MCCI $5\times10^{-4}$ | MCCI $2\times10^{-4}$ | FCI space |
|---|---:|---:|---:|---:|---:|
| CO, 6-31G | $3.28\times10^{-2}$ | $5.25\times10^{-3}$ (2220) | $3.30\times10^{-3}$ (5087) | $1.47\times10^{-3}$ (15024) | 4 777 056 |
| NH$_3$ ground, 6-31G | $1.57\times10^{-2}$ | $9.90\times10^{-4}$ (1649) | $5.85\times10^{-4}$ (3550) | $2.48\times10^{-4}$ (8381) | 254 561 |
| NH$_3$ 1st excited $A_1$ | — | $1.42\times10^{-3}$ (2526) | $1.15\times10^{-3}$ (5295) | $2.62\times10^{-4}$ (12129) | 254 561 |
| H$_4$ square, cc-pVDZ | $5.15\times10^{-2}$ | $7.10\times10^{-4}$ (512) | $2.27\times10^{-3}$ (765) | $9.74\times10^{-4}$ (1347) | 5050 |
| H$_6$ hexagonal, cc-pVDZ | $8.68\times10^{-3}$ | $3.53\times10^{-4}$ (1305) | $1.80\times10^{-4}$ (2527) | $2.17\times10^{-4}$ (7131) | about 2.1 million |
| CH$_4$, 6-31G | $1.48\times10^{-2}$ | $1.33\times10^{-3}$ (2560) | $2.30\times10^{-3}$ (5509) | $2.02\times10^{-4}$ (14692) | 828 944 |

(Tables 1-6. Frozen orbitals: two for CO, one for NH$_3$ and CH$_4$.)

**The pattern.** The gradient is not variational: the error does not always fall as the cutoff is lowered (H$_4$, H$_6$, CH$_4$). At the tightest cutoff the error is one to two orders of magnitude below HF.

## Limitations

- **Small molecules and bases.** Minimal to triple-zeta; RHF orbitals only. No orbital optimization, no open shells, no excited states beyond one NH$_3$ example.
- **Symmetry argument.** It relies on the degeneracies splitting into different irreps of the abelian subgroup. This held for the molecules tested; it is not shown in general.
- **Near-degeneracies within one irrep.** These are tested only down to gaps of about $10^{-4}$-$10^{-5}$ $E_h$. The paper does not discuss what the fixed-list surface does when such a gap closes along a path.
- **Determinants.** Slater determinants, not CSFs, cause spin-state switching at long bond lengths.
- **No geometry optimizations.** Only gradients along scans.

## Relevance

- **Theory.** Source for [[selected-ci-analytic-gradient]], which extends [[ci-analytic-gradient]] and [[z-vector-method]] to lists that are not invariant to any rotation.
- **SQD.** At fixed sampled list, the gradient of an SQD energy is this gradient ([[sample-based-quantum-diagonalization]]).

## My observations

- **The non-variational behaviour.** It is a reminder that a tighter selection does not guarantee a better gradient. This matters for any convergence study of SQD gradients.
- **Translational sum rule.** In the notebook's own test ([[selected-ci-analytic-gradient]], worked example), dropping the oo/vv response leaves the net force exactly zero but produces a net torque. Rotational invariance, not translational, is the check that detects the missing term.
