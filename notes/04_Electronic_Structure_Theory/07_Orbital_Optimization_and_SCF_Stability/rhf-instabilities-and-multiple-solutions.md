---
id: rhf-instabilities-and-multiple-solutions
title: Singlet and triplet instabilities of RHF wave functions, symmetry breaking, and multiple Hartree-Fock solutions - H₂, H₂O, the allyl radical and dissociated water
summary: An RHF state of a nondegenerate electronic state is always stationary under symmetry-breaking rotations, but not necessarily a minimum. Negative eigenvalues in the triplet block of the Hessian signal a spin-contaminated UHF solution of lower energy. Negative eigenvalues in non-totally-symmetric singlet blocks signal a spatially broken solution. HJO's examples were recomputed. Confirmed: the H₂/cc-pVQZ triplet onset (2.298 bohr), the water A₁ singlet minimum (0.060 E_h at 3.9 bohr), the allyl C₂ᵥ geometry and symmetry-breaking energies (0.012 and 4.16 mE_h), and the four RHF solutions of water at 8R. Disagreements: the water ³A₁ onset (2.47 bohr, not 2.64), the allyl B₂ onset (δ = −0.020, not −0.040 bohr), and the STO-3G H₂ exercise data.
status: in-progress
kind: theory
level: advanced
tags: [rhf, uhf, stability-analysis, triplet-instability, singlet-instability, symmetry-breaking, multiple-solutions, allyl-radical, coulson-fischer, hartree-fock]
prerequisites: [generalized-fock-matrix-and-orbital-hessian, uhf, h2-dissociation-rhf-uhf]
related: [scf-second-order-and-stability, scf-convergence-diis-and-newton, polarization-propagator-rpa, standard-models-h2-and-water, hartree-fock-csf-parametrization-and-canonical-conditions]
order: 70
date: 2026-11-04
---

## Symmetry-breaking rotations

**The two operators (HJO Sec. 10.10.1).** RHF uses the totally symmetric singlet generator $\hat\kappa^{\text{RHF}} = \sum_{p>q}{}^R\kappa^{0,0}_{pq}(\hat E_{pq} - \hat E_{qp})$. UHF adds the triplet ($M = 0$) generators and drops the spatial-symmetry restriction:

$$
\hat\kappa^{\text{UHF}} = \sum_{p>q}{}^R\kappa^{0,0}_{pq}(\hat E_{pq} - \hat E_{qp}) + \sum_{p>q}{}^R\kappa^{1,0}_{pq}(\hat T^{1,0}_{pq} - \hat T^{1,0}_{qp}),
$$

or equivalently separate $\alpha$ and $\beta$ rotation parameters. The extra parameters are the **symmetry-breaking rotations**. Only they can lower the energy below RHF.

**Stationary is not stable.**

- **Nondegenerate states are always stationary.** The gradient with respect to a symmetry-breaking rotation is zero by symmetry: a singlet bra, singlet $\hat H$, triplet operator and singlet ket contain no totally symmetric component.
- **Minimum or saddle point?** That is decided only by the Hessian, geometry by geometry.
- **Two blocks.** For nondegenerate states the Hessian splits into a singlet and a triplet block, each further split by irreducible representation. In canonical orbitals the closed-shell blocks are

$$
{}^1E^{(2)}_{ai,bj} = 4\big[\delta\delta(\varepsilon_a - \varepsilon_i) + 4g_{aibj} - g_{abij} - g_{ajib}\big],\qquad
{}^3E^{(2)}_{ai,bj} = 4\big[\delta\delta(\varepsilon_a - \varepsilon_i) - g_{abij} - g_{ajib}\big]
$$

([[generalized-fock-matrix-and-orbital-hessian]]).

**Triplet instabilities** (a negative triplet eigenvalue) are the common case when bonds stretch. They mean a spin-contaminated UHF state lies lower ([[h2-dissociation-rhf-uhf]]).

**Singlet instabilities** (a negative eigenvalue of a non-totally-symmetric singlet block) are rarer.

- **Meaning.** Several configurations are close in energy, and a spatially broken solution lies lower.
- **Geometry.** If a nuclear displacement has the same symmetry, the HF potential surface may acquire a spurious lower-symmetry minimum.

**Effect on properties.** At the onset of either instability the Hessian is singular, so response properties diverge:

- spin-spin coupling constants (triplet Fermi-contact perturbation) at triplet instabilities;
- force constants at singlet instabilities;
- RPA excitation energies that go to zero and then disappear ([[polarization-propagator-rpa]]).

**Degenerate states (HJO Sec. 10.10.3).**

- **Triplet states.** The gradient along triplet rotations need not vanish, so a lower spin-contaminated UHF state always exists, even if the RHF Hessian is positive.
- **Spatially degenerate states.** Likewise, e.g. C ³P, where $s$-$d$ mixing has a nonzero gradient and the HF solution slightly breaks atomic symmetry.

## H₂

!!! example "Triplet instability of H₂ (computed for this note)"
    I located the root of the lowest triplet Hessian eigenvalue ($\sigma_g\to\sigma_u$):

    | Basis | Onset $R$ (bohr) | HJO |
    |---|---:|---:|
    | cc-pVQZ | 2.2978 | 2.298 |
    | STO-3G ($\zeta_{\text H}$ = 1.24) | 2.1797 | 2.65 (Exercise 10.8) |

    - **cc-pVQZ.** The onset agrees with HJO, and the singlet block stays positive (1.78 $E_h$ at 2.0 bohr).
    - **STO-3G disagrees.** My onset matches [[h2-dissociation-rhf-uhf]] (2.180 bohr). HJO's Exercise 10.8 lists RHF data at 2.5-2.8 bohr ($E^{\text{HF}}$ = −0.922197, $\varepsilon_g$ = −0.443869, … at 2.5 bohr). Their triplet Hessian $4[\varepsilon_u - \varepsilon_g - g_{uugg} - g_{ugug}]$ vanishes near 2.65 bohr. Neither standard STO-3G ($\zeta$ = 1.24: $E$ = −0.965794, $\varepsilon_g$ = −0.395362 at 2.5 bohr) nor the unscaled $\zeta$ = 1 set (onset 2.302 bohr) reproduces those numbers. Their basis must differ from both, and I could not identify it.

## Water, C₂ᵥ stretch, cc-pVDZ (HOH = 110.565°)

!!! example "Lowest RHF Hessian eigenvalues by symmetry of the rotation (computed for this note, $E_h$)"
    | $R_{\text{OH}}$ (bohr) | singlet $A_1$ | singlet $B_2$ | triplet $A_1$ | triplet $B_2$ | triplet $B_1$ | triplet $A_2$ |
    |---:|---:|---:|---:|---:|---:|---:|
    | 1.8 | 1.724 | 1.995 | 1.246 | 1.452 | 1.105 | 1.448 |
    | 2.4 | 1.142 | 1.453 | 0.114 | 0.250 | 0.526 | 0.772 |
    | 2.6 | 0.943 | 1.284 | −0.183 | −0.052 | 0.377 | 0.589 |
    | 3.0 | 0.588 | 0.983 | −0.647 | −0.517 | 0.155 | 0.306 |
    | 3.4 | 0.302 | 0.744 | −0.979 | −0.849 | 0.014 | 0.107 |
    | 3.8 | 0.085 | 0.542 | −1.204 | −1.096 | −0.046 | −0.063 |
    | 3.9 | **0.060** | | | | | |

    - **Singlet block.** All singlet eigenvalues stay positive. The totally symmetric one has its minimum, 0.060 $E_h$ at 3.9 bohr, exactly as HJO state. This minimum comes from an avoided crossing with a second $^1A_1$ RHF solution: at 4.0-4.2 bohr PySCF converges to either, depending on the start, and a stability-following restart lowers the energy by 2-7 m$E_h$.
    - **Triplet onsets.** In order: $A_1$ at **2.473 bohr**, $B_2$ near 2.57, $B_1$ near 3.46, $A_2$ near 3.66.
    - **Disagreement.** HJO place the ³A₁ onset (RPA triplet $A_1$ excitation energy reaching zero) at 2.64 bohr. I confirmed my value independently. At 2.6 bohr, rotating the α and β orbitals oppositely along the lowest triplet eigenvector lowers the energy (−0.23 m$E_h$ at step 0.05, −3.8 m$E_h$ at 0.4), so the RHF state there is already unstable. The $(A - B)$ triplet matrix stays positive over the whole range, so it cannot explain HJO's number either. Since my singlet $A_1$ values, which use the same Hessian normalization, reproduce HJO's 0.060, I cannot account for the difference.

## The allyl radical: a singlet instability

**Background.** Unconstrained Hartree-Fock optimization gives allyl a $C_s$ minimum, contradicting experiment and better calculations. The ²A₂ RHF state, $6a_1^2\,4b_2^2\,1b_1^2\,1a_2^1$, has an unpaired electron in the nonbonding π orbital. Its lowest singlet B₂ Hessian eigenvalue, which shares the symmetry of the antisymmetric CC stretch, is negative around the equilibrium geometry.

!!! example "Allyl, ROHF/cc-pVDZ (computed for this note)"
    - **C₂ᵥ optimum** (geomeTRIC): $R_{\text{CC}}$ = 2.5980 bohr, CCC = 124.48° (HJO 2.5980 bohr, 124.49°), $E$ = −116.454889 $E_h$.
    - **Coordinate.** $\delta$ is the symmetric CC stretch: each terminal CH₂ is moved rigidly along its CC bond.
    - **Symmetry-broken solution.** I followed the B₂ instability with a spatially unrestricted ROHF (no point-group symmetry). It is 0.0124 m$E_h$ below the C₂ᵥ state at $\delta = 0$ and 4.160 m$E_h$ below it at $\delta$ = 0.4 bohr. HJO give "about 0.01" and 4.2 m$E_h$, so their "UHF" curve must be this spatially broken, spin-restricted solution. A spin-unrestricted UHF would lie much lower.
    - **The exact B₂ eigenvalue.** It falls monotonically: +0.0138 at $\delta$ = −0.1, −0.0033 at 0 and −0.0335 at +0.2 bohr. It crosses zero at $\delta$ = **−0.020 bohr** ($R_{\text{CC}}$ = 2.578), where HJO give −0.0395 bohr (2.5585). I computed it by finite differences of PySCF's analytic ROHF gradient over the 212 B₂ rotations. The overall scale of these eigenvalues depends on PySCF's gradient normalization, but the zero crossing does not. The conclusion is the same either way: the C₂ᵥ RHF solution is singlet-unstable at its own equilibrium.
    - **PySCF's ROHF Hessian is approximate.** The Hessian-vector product used in PySCF's ROHF second-order solver gave +0.040 at $\delta = 0$. The energy along that eigenvector curves downwards (−0.005), so for this purpose its ROHF Hessian is approximate and cannot be used for stability analysis.

**The double well (HJO Fig. 10.6).** Distorting along the antisymmetric stretch Δ gives two equivalent $C_s$ wells (²A″). The symmetric RHF state sits on a $C_s$ curve that keeps one negative A″ eigenvalue, and the two curves merge at |Δ| ≈ 0.03 bohr.

**Which to trust?** Neither state is "right". The symmetric one has the correct symmetry, the broken one the lower energy, and the gap is tiny compared with real excitation energies. The proper cure is a multiconfigurational wave function (HJO Sec. 12.8).

## Multiple solutions: water at 8R

**Why several solutions exist.** Far from equilibrium, several local minima of the HF energy coexist. Which one an SCF finds depends on the starting orbitals and the algorithm.

**HJO's example.** At 8 times the reference bond length the fragments no longer interact. Four closed-shell configurations are all true local minima:

!!! example "The four RHF minima of H₂O/cc-pVDZ at $8R_{\text{ref}}$ (HJO Table 10.5 recomputed)"
    | Configuration | Fragments | Mine ($E_h$) | HJO |
    |---|---|---:|---:|
    | O $1s^22s^22p^6$ | O²⁻ + 2H⁺ | −74.410875 | −74.410876 |
    | O $1s^22s^22p_x^2$, $H_{a_1}^2H_{b_2}^2$ | O²⁺ + 2H⁻ | −74.050033 | −74.050033 |
    | O $1s^22s^22p_z^22p_x^2$, $H_{b_2}^2$ | O + H⁻ + H | −75.393278 | −75.393278 |
    | O $1s^22s^22p_y^22p_x^2$, $H_{a_1}^2$ | O + H⁻ + H | −75.393278 | −75.393278 |

    - **Method.** Each solution was reached from a sum of fragment densities with a damped maximum-overlap SCF. All have vanishing occupied-virtual Fock elements ($<2\times10^{-15}$). A plain SCF from any of these guesses falls into a −75.393278 solution, possibly a $p_y\leftrightarrow p_x$ equivalent of the ones listed.
    - **None is the true limit.** None corresponds to the true dissociation products O(³P) + 2H(²S). The neutral O comes out as a ¹S/¹D mixture, and the H pair as the ionic/covalent mixture of [[h2-dissociation-rhf-uhf]]. The exact state has zero overlap with all four.
    - **At 3R.** HJO note several near-degenerate solutions; the physically sensible one, with O-H mixing in $3a_1$ and $1b_2$, is the highest of the three. The lowest RHF energy is not a reliable guide away from equilibrium.

## Source

Helgaker, Jørgensen and Olsen, *Molecular Electronic-Structure Theory* (Wiley, Chichester, 2000), Secs. 10.10-10.11, pp. 496-505, Eqs. (10.10.1)-(10.10.12), Figs. 10.2-10.6, Table 10.5, Exercise 10.8. All numbers marked as mine were computed for this note (PySCF 2.14, geomeTRIC 1.1, my own Hessian and stability code in `hjo/c10/instab.py`, `allyl*.py`, `multi*.py`). The allyl study is HJO's reference [26] (Paldus and Veillard), not consulted here.
