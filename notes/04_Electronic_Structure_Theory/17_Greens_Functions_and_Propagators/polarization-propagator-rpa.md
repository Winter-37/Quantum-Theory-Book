---
id: polarization-propagator-rpa
title: The polarization propagator - TDHF/RPA, stability, coupled Hartree-Fock, length-velocity equivalence and MCTDHF
summary: The polarization propagator ⟨⟨r;r⟩⟩_E has poles at excitation energies and residues equal to squared transition moments; its real part is the frequency-dependent polarizability. With an HF reference and particle-hole operators it becomes TDHF (RPA), a non-Hermitian eigenvalue problem that reduces to a Hermitian one of half the size. Instabilities (A±B not positive definite), equality with coupled Hartree-Fock at E = 0, length-velocity equivalence in a complete basis, the MCSCF extension, and the second-order (SOPPA-type) analysis. HeH⁺ problems and water and H₂ calculations recomputed.
status: in-progress
kind: theory
level: advanced
tags: [polarization-propagator, rpa, tdhf, excitation-energies, oscillator-strength, polarizability, stability, mctdhf, soppa]
prerequisites: [propagators-and-superoperators, scf-second-order-and-stability, molecular-properties-and-response]
related: [heh-plus-minimal-basis-model, mcscf-second-order-optimization, h2-dissociation-rhf-uhf, spin-tensor-operators]
order: 40
date: 2026-11-03
---

## The propagator and the polarizability

**Spectral form.** With $A = B = \mathbf r$ (number conserving), the propagator of [[propagators-and-superoperators]] is

$$
\langle\langle\mathbf r; \mathbf r\rangle\rangle_E = \sum_{m\ne0}\left[\frac{\langle0|\mathbf r|m\rangle\langle m|\mathbf r|0\rangle}{E - (E_m - E_0)} - \frac{\langle0|\mathbf r|m\rangle\langle m|\mathbf r|0\rangle}{E + (E_m - E_0)}\right].
$$

Poles at $\pm(E_m - E_0)$ are excitation energies; residues are squared transition moments.

**Polarizability.** Combining the two terms,

$$
\alpha(E) = -\langle\langle\mathbf r; \mathbf r\rangle\rangle_E = \sum_m\frac{2(E_m - E_0)\,|\langle0|\mathbf r|m\rangle|^2}{(E_m - E_0)^2 - E^2},
$$

the usual sum-over-states frequency-dependent polarizability (overall sign by convention).

**Other forms.** With $[\mathbf r, H] = i\mathbf p$ (a.u., complete basis), the equation of motion gives two more expressions: $\alpha$ from $i E^{-1}\langle\langle\mathbf p; \mathbf r\rangle\rangle_E$, and $\langle\langle\mathbf r; \mathbf r\rangle\rangle_E = E^{-2}\big(N + \langle\langle\mathbf p; \mathbf p\rangle\rangle_E\big)$. Here $N$ comes from $[\mathbf p, \mathbf r] = -i$ summed over electrons, the Thomas-Reiche-Kuhn sum rule. In a finite basis $[\mathbf r, H] = i\mathbf p$ fails, so these forms differ. The $E^{-1}$ and $E^{-2}$ factors make them unreliable near $E = 0$.

## TDHF (RPA)

**Choice.** HF reference and the particle-hole manifold $\{\mathbf Q^\dagger, \mathbf Q\} = \{a_m^\dagger a_\alpha, a_\alpha^\dagger a_m\}$ (virtual $m$, occupied $\alpha$). The superoperator matrices are

$$
\mathbf S = (\mathbf Q^\dagger|\mathbf Q^\dagger),\qquad \mathbf A = (\mathbf Q^\dagger|\hat H|\mathbf Q^\dagger),\qquad \mathbf B = (\mathbf Q^\dagger|\hat H|\mathbf Q),
$$

and the poles follow from

$$
\begin{pmatrix}\mathbf A & \mathbf B\\ \mathbf B & \mathbf A\end{pmatrix}\begin{pmatrix}\mathbf Z\\ \mathbf Y\end{pmatrix} = E\begin{pmatrix}\mathbf S & 0\\ 0 & -\mathbf S\end{pmatrix}\begin{pmatrix}\mathbf Z\\ \mathbf Y\end{pmatrix}.
$$

For spin orbitals $\mathbf S = \mathbf 1$, $A_{ai,bj} = (\varepsilon_a - \varepsilon_i)\delta_{ab}\delta_{ij} + \langle aj||ib\rangle$ and $B_{ai,bj} = \langle ab||ij\rangle$ in the common modern convention (general knowledge). J-S's $\mathbf B$ in Ch. 2 has the opposite sign, so their Hessian is $\mathbf A - \mathbf B$ where the modern one is $\mathbf A + \mathbf B$. The physics is the same.

**Halving the problem.** Adding and subtracting the two block rows, $(\mathbf A + \mathbf B)(\mathbf Z + \mathbf Y) = E\mathbf S(\mathbf Z - \mathbf Y)$ and $(\mathbf A - \mathbf B)(\mathbf Z - \mathbf Y) = E\mathbf S(\mathbf Z + \mathbf Y)$. Then

$$
\mathbf S^{-1}(\mathbf A + \mathbf B)\mathbf S^{-1}(\mathbf A - \mathbf B)(\mathbf Z - \mathbf Y) = E^2(\mathbf Z - \mathbf Y).
$$

If $\mathbf A - \mathbf B$ is positive definite, this becomes the Hermitian problem $(\mathbf A - \mathbf B)^{1/2}\mathbf S^{-1}(\mathbf A + \mathbf B)\mathbf S^{-1}(\mathbf A - \mathbf B)^{1/2}\mathbf X = E^2\mathbf X$, of the dimension of the particle-hole space. Eigenvectors come in pairs $(\mathbf Z, \mathbf Y)$ at $+\omega$ and $(\mathbf Y^*, \mathbf Z^*)$ at $-\omega$, normalized by $\mathbf Z^\dagger\mathbf S\mathbf Z - \mathbf Y^\dagger\mathbf S\mathbf Y = 1$. With $O_\lambda^\dagger = \mathbf Q^\dagger\mathbf Z_\lambda + \mathbf Q\mathbf Y_\lambda$, the propagator takes spectral form, $\langle\langle\mathbf r; \mathbf r\rangle\rangle_E = \sum_\lambda|(\mathbf r|O_\lambda^\dagger)|^2\big[(E - \omega_\lambda)^{-1} - (E + \omega_\lambda)^{-1}\big]$.

**Tamm-Dancoff limit (general knowledge).** Setting $\mathbf B = 0$ gives CIS. RPA adds de-excitation amplitudes $\mathbf Y$, i.e. ground-state correlation effects.

**Order.** TDHF is consistent through **first order** in the fluctuation potential. Diagrammatically it sums the infinite series of ring (bubble) diagrams (J-S Fig. 6.3).

## Stability

**Conditions.** If $\mathbf A - \mathbf B$ and $\mathbf A + \mathbf B$ are both positive definite, all $E^2 > 0$ and all excitation energies are real. If one is positive definite and the other not, some $E^2 < 0$: **imaginary** excitation energies, an RPA instability. If both are indefinite, negative excitation energies can occur; the reference is then a saddle point.

**Connection to the SCF Hessian.** $\mathbf A \mp \mathbf B$ are the Hessians of the HF energy for real and imaginary orbital rotations ([[scf-second-order-and-stability]]). An RPA instability means the HF solution is not a minimum for that kind of rotation:

- the dipole (singlet) propagator probes singlet instabilities;
- a triplet operator, such as the Fermi contact Hamiltonian ([[spin-tensor-operators]]), probes triplet (RHF→UHF) instabilities.

Triplet TDHF energies of closed shells are often poor or unstable for this reason.

!!! example "Triplet instability of STO-3G H₂ seen in RPA (computed for this note)"
    One particle-hole pair ($\sigma_g\to\sigma_u$). Triplet: $A - B = \Delta\varepsilon - J_{12} + K_{12}$ and $A + B = \Delta\varepsilon - J_{12} - K_{12}$ (modern convention, hartree).

    | R (bohr) | Singlet $\omega^2$ | Triplet $A - B$ | Triplet $A + B$ | Triplet $\omega^2$ |
    |---:|---:|---:|---:|---:|
    | 1.4 | 0.8648 | 0.7662 | 0.4036 | +0.3093 |
    | 2.0 | 0.4158 | 0.4747 | 0.0737 | +0.0350 |
    | 2.1 | 0.3725 | 0.4395 | 0.0316 | +0.0139 |
    | 2.2 | 0.3346 | 0.4070 | −0.0078 | −0.0032 |
    | 2.4 | 0.2716 | 0.3491 | −0.0797 | −0.0278 |

    The triplet $A + B$ is exactly $\varepsilon_2 - \varepsilon_1 - J_{12} - K_{12}$, the RHF→UHF stability quantity of [[scf-second-order-and-stability]] (0.4036 at 1.4 bohr). It changes sign at $R_c = 2.18$ bohr, where the triplet excitation energy becomes imaginary.

## E = 0: coupled Hartree-Fock

At $E = 0$, rotating the $(\mathbf Q^\dagger, \mathbf Q)$ basis by $\tfrac{1}{\sqrt2}\begin{pmatrix}1 & 1\\ 1 & -1\end{pmatrix}$ block-diagonalizes the matrix. Because $\mathbf r$ is real, $(\mathbf r|\mathbf Q) = -(\mathbf r|\mathbf Q^\dagger)$, and

$$
\langle\langle\mathbf r; \mathbf r\rangle\rangle_{E=0} \propto (\mathbf r|\mathbf Q)\,(\mathbf A - \mathbf B)_{\text{J-S}}^{-1}\,(\mathbf Q|\mathbf r),
$$

the coupled Hartree-Fock (CPHF) static polarizability of [[molecular-properties-and-response]].

## Length-velocity equivalence

**Statement.** The velocity form of the transition moment is $(\mathbf p|O_\lambda^\dagger) = -i\langle0|[[\mathbf r, H], O_\lambda^\dagger]|0\rangle$. Using Brillouin's theorem in the form $\langle0|[[\mathbf r, O_\lambda^\dagger], H]|0\rangle = 0$ and the RPA eigenvalue equation, J-S show that

$$
(\mathbf p|O_\lambda^\dagger) = -i\omega_\lambda\,(\mathbf r|O_\lambda^\dagger),
$$

so oscillator strengths in the length ($f = \tfrac23\omega|\langle\mathbf r\rangle|^2$) and velocity ($f = \tfrac2{3\omega}|\langle\mathbf p\rangle|^2$) forms are **equal**, provided $[\mathbf r, H] = i\mathbf p$ holds, i.e. in a complete basis.

**Unusual among approximations.** RPA has this property; CIS and most truncated CI do not. MCTDHF keeps it all the way from TDHF to the full CI limit.

!!! example "Water (Szabo geometry), TDHF singlets (computed for this note)"
    | Basis | $\omega$ (hartree) | $f$ length | $f$ velocity |
    |---|---|---|---|
    | 6-31G** | 0.3524, 0.4191, 0.4521, 0.5206 | 0.0207, 0, 0.1109, 0.0937 | 0.0588, 0, 0.1583, 0.0917 |
    | aug-cc-pVTZ | 0.3180, 0.3794, 0.4021 | 0.0474, 0, 0.0979 | 0.0477, 0, 0.0979 |

    - **Basis dependence.** In 6-31G** the two gauges differ by a factor of 3 for the lowest state; in aug-cc-pVTZ they agree to 1%.
    - **CIS (TDA) energies in 6-31G**:** 0.3549, 0.4220, 0.4551, 0.5249, 0.003-0.004 hartree above TDHF.
    - **TDHF and CPHF.** Summing $2|\langle0|z|\lambda\rangle|^2/\omega_\lambda$ over all 95 TDHF roots gives $\alpha_{zz}(0) = 5.0713$, identical to the CPHF value.

## HeH⁺ (J-S Problems 6.2-6.3)

!!! example "TDHF and MCTDHF for minimal-basis HeH⁺ (computed for this note; J-S in parentheses)"
    **TDHF.** One singlet particle-hole pair, with $A_{11} = 2.1467$ (2.1464) and $B_{11} = -0.2523$ (−0.2522), J-S convention.

    - Excitation energy 1.0659 (1.0657); $Z = 0.7083$, $Y = 0.0418$ (same).
    - Transition moment $(z|O^\dagger) = 2\langle1|z|2\rangle(Z - Y) = 0.7255$ (0.7255).
    - $\alpha_{zz}(0) = 0.9876$ (0.9878) and $\alpha_{zz}(0.1) = 0.9964$ (0.9965). The static value equals CHF (Problem 5.2).

    **MCTDHF.** Reference: the two-configuration MCSCF state. Manifold: $\{Q^\dagger, R^\dagger, Q, R\}$, i.e. the one orbital and one state rotation.

    - J-S's MCTDHF gives exactly the full-CI excitation energies (1.0225, 2.3295) and transition moments (0.7578, 0.0146 vs CI 0.7578, 0.0144).
    - The reason: the MCSCF state equals full CI here, and the manifold acting on it spans the remaining full-CI space.
    - Full CI with the printed integrals (this note): 1.0227, 2.3297; moments 0.7575, 0.0143; $\alpha_{zz}(0) = 1.1223$ (J-S MCTDHF 1.1234, CMCHF 1.1232); $\alpha_{zz}(0.1) = 1.1331$ (1.1344).

## Beyond TDHF

**MCTDHF (Yeager and Jørgensen; Dalgaard).** MCSCF reference and the MCSCF rotation operators $\{\mathbf Q^\dagger, \mathbf R^\dagger, \mathbf Q, \mathbf R\}$. The matrices $\mathbf A$, $\mathbf B$ are those of second-order MCSCF ([[mcscf-second-order-optimization]]). The metric now has an antisymmetric part $\boldsymbol\Delta$, and the reduced problem is $(\mathbf S - \boldsymbol\Delta)^{-1}(\mathbf A + \mathbf B)(\mathbf S + \boldsymbol\Delta)^{-1}(\mathbf A - \mathbf B)(\mathbf Z - \mathbf Y) = E^2(\mathbf Z - \mathbf Y)$.

- **Hermiticity.** The orbital-state coupling elements are not Hermitian for an approximate $|0\rangle$, since $\langle0|HQ|n\rangle - E_0\langle0|Q|n\rangle\ne0$. Hermiticity is imposed by letting $\hat H$ act on the orbital operators. With this choice, MCTDHF at $E = 0$ equals coupled MCHF, and length and velocity remain equivalent.
- **Stability.** Imaginary roots signal that the MCSCF state is not a minimum for that symmetry of perturbation.

**Second-order propagator (Oddershede; Nielsen, Jørgensen, Oddershede).** With an MP reference, the manifold $\{\mathbf T_2^\dagger, \mathbf T_4^\dagger\}$ (particle-hole and two-particle-two-hole operators), and partitioning, all poles and residues become consistent through second order. TDHF is the first-order member. This is the second-order polarization propagator approach (SOPPA, the modern name; general knowledge).

## Source

Jørgensen and Simons, *Second Quantization-Based Methods in Quantum Chemistry* (Academic Press, New York, 1981), Ch. 6, Sec. E, pp. 142-162, Eqs. (6.86)-(6.181); Problems 6.2-6.3 with Solutions, pp. 162-166. Water and H₂ numbers computed for this note with PySCF 2.14; HeH⁺ with J-S's integrals.
