---
id: koopmans-theorem
title: Koopmans' theorem
summary: With frozen Hartree-Fock orbitals, the energy to remove an electron from χ_a is −ε_a and the energy gained by adding one to χ_r is −ε_r. Derivation from the Slater-Condon rules, the error balance (relaxation vs correlation), and computed STO-3G to 6-31G** values for small molecules.
status: in-progress
kind: derivation
level: intermediate
tags: [hartree-fock, koopmans, ionization-potential, electron-affinity, orbital-energies]
prerequisites: [fock-operator, slater-condon-rules]
related: [hartree-fock-equations, hf-closed-shell-basis-set-trends, one-particle-greens-function, ionization-potentials-second-order-self-energy, hartree-fock-csf-parametrization-and-canonical-conditions]
also: []
date: 2026-11-03
---

## Statement

Let $|{}^N\Psi_0\rangle$ be the $N$-electron Hartree-Fock determinant with canonical orbital energies $\varepsilon_i$ ([[fock-operator]]).

**Ionization.** Remove an electron from occupied $\chi_a$, keeping all other spin orbitals unchanged:

$$
\mathrm{IP}_a = {}^{N-1}E_a - {}^NE_0 = -\varepsilon_a .
$$

**Attachment.** Add an electron to virtual $\chi_r$, again with unchanged orbitals:

$$
\mathrm{EA}_r = {}^NE_0 - {}^{N+1}E^r = -\varepsilon_r .
$$

Here $|{}^{N-1}\Psi_a\rangle$ and $|{}^{N+1}\Psi^r\rangle$ are single determinants built from the $N$-electron Hartree-Fock orbitals.

## Derivation

Use the Case 1 [[slater-condon-rules]] for each determinant. Every term containing the removed (or added) orbital changes; all others cancel.

**Ionization.**

$$
{}^NE_0 - {}^{N-1}E_a = \langle a|h|a\rangle + \tfrac12\sum_b\langle ab||ab\rangle + \tfrac12\sum_b\langle ba||ba\rangle = \langle a|h|a\rangle + \sum_b^N\langle ab||ab\rangle = \varepsilon_a .
$$

The term $b=a$ is zero.

**Attachment (Szabo Ex. 3.6).**

$$
{}^NE_0 - {}^{N+1}E^r = -\langle r|h|r\rangle - \sum_b^N\langle rb||rb\rangle = -\varepsilon_r .
$$

**Double ionization (Szabo Ex. 3.5).** Removing electrons from $\chi_c$ and $\chi_d$ costs

$$
-\varepsilon_c - \varepsilon_d + \langle cd|cd\rangle - \langle cd|dc\rangle .
$$

The pair interaction is counted in both $\varepsilon_c$ and $\varepsilon_d$, so it must be added back once.

## Why it works for IPs, and fails for EAs

Two approximations are made.

1. **Frozen orbitals.** The ion is described with the neutral's orbitals. A separate Hartree-Fock calculation on the ion (ΔSCF) would relax them and lower the ion's energy. Relaxation alone therefore makes $-\varepsilon_a$ **too large** an IP.
2. **No correlation.** The $N$-electron system has more electron pairs, hence more correlation energy, than the $(N-1)$-electron ion. Correlation alone therefore makes the Hartree-Fock IP **too small**.

For ionization the two errors have opposite signs and partly cancel, so Koopmans IPs of valence orbitals are often within about 1 eV of experiment. For electron affinities both errors push the same way, so Koopmans EAs are poor. A negative $\varepsilon_r$ in a modest basis may simply reflect a diffuse-function artefact.

**Where it fails qualitatively.**

- **N$_2$ (Szabo Table 3.16).** Koopmans' theorem predicts the wrong ordering of the two lowest ionized states ($^2\Pi_u$ vs $^2\Sigma_g^+$).
- **Core ionizations** (standard result, not from Szabo). Relaxation dominates and the error is many eV.

## Worked examples

!!! example "HeH⁺, STO-3G (Szabo Sec. 3.5.3)"
    At $R = 1.4632$ bohr ($\zeta_{\text{He}} = 2.0925$, $\zeta_{\text{H}} = 1.24$):

    | Quantity | Orbital energy | Koopmans prediction |
    |---|---:|---:|
    | occupied $\varepsilon_1$ | −1.5975 hartree | IP = 1.5975 hartree = 43.5 eV |
    | virtual $\varepsilon_2$ | −0.0617 hartree | EA = 0.0617 hartree = 1.7 eV |

    The positive EA means the frozen-orbital model binds an extra electron. It does not mean HeH is stable: He + H$^+$ binds an electron much more strongly. Recomputed with the SCF code in [[scf-procedure]].

!!! example "First Koopmans IPs, Szabo's standard molecules (hartree)"
    $-\varepsilon_{\text{HOMO}}$ from RHF at the geometries of Szabo Table 3.10, Cartesian $d$ functions, PySCF 2.14:

    | Molecule | STO-3G | 4-31G | 6-31G* | 6-31G** |
    |---|---:|---:|---:|---:|
    | H$_2$ | 0.578 | 0.596 | 0.596 | 0.595 |
    | N$_2$ | 0.539 | 0.621 | 0.612 | 0.612 |
    | CO | 0.446 | 0.549 | 0.548 | 0.548 |
    | CH$_4$ | 0.520 | 0.544 | 0.546 | 0.545 |
    | NH$_3$ | 0.353 | 0.414 | 0.421 | 0.421 |
    | H$_2$O | 0.391 | 0.500 | 0.498 | 0.497 |
    | FH | 0.464 | 0.628 | 0.629 | 0.627 |

    STO-3G underestimates valence IPs badly. The split-valence and polarized sets agree with each other to about 0.01 hartree. Compare Szabo Tables 3.14-3.17 for his values and the experimental numbers.

## Why the canonical orbitals are the right ones, and ΔSCF (Helgaker, Jørgensen and Olsen)

**Diagonal elements.** HJO first note that, in any set of orbitals satisfying the HF conditions, $f_{ii}$ equals the IP for removing an electron from $\phi_i$ with frozen orbitals (Eq. 10.5.2).

**Why canonical orbitals.** The ionized state can be expanded as $\sum_ic_ia_{i\sigma}|\text{HF}\rangle$ and optimized variationally. The resulting CI matrix is

$$
\langle\text{HF}|a^\dagger_{i\sigma}\hat Ha_{j\sigma}|\text{HF}\rangle = E^{\text{HF}}\delta_{ij} - f_{ji},
$$

so the cationic states diagonalize the occupied block of $\mathbf f$. In the canonical basis this block is already diagonal. The canonical occupied orbitals are therefore the best frozen-orbital description of ionization, and the virtual canonical orbitals that of electron attachment.

**Not for excitations.** Virtual canonical orbitals are not the best orbitals for excitations, because an excited electron moves in the field of $N-1$ electrons.

**ΔSCF.** Relaxing the ion's orbitals gives $\text{IP}^{\Delta\text{SCF}} = E^{N-1}_{\text{HF}} - E^N_{\text{HF}}$. Relaxation always lowers the ion's energy, so ΔSCF IPs are always below Koopmans IPs.

!!! example "H₂O and N₂ ionization potentials, Koopmans versus ΔSCF (HJO Tables 10.1-10.3 recomputed, $E_h$)"
    **Method.** Cation states are open-shell ROHF. Core and inner-valence holes are kept by the maximum-overlap method; outer holes use symmetry-constrained occupations. Geometries are optimized at the RHF level in each basis, as in HJO. Water uses cc-pCVXZ on O and cc-pVXZ on H.

    **H₂O, cc-pVDZ, at HJO's reference geometry (Table 10.1):**

    | | $1b_2$ | $3a_1$ | $1b_1$ |
    |---|---:|---:|---:|
    | Koopmans | 0.7002 | 0.5510 | 0.4895 |
    | ΔSCF (mine) | 0.6432 | 0.4666 | 0.3945 |
    | ΔSCF (HJO) | 0.6433 | **0.4464** | 0.3945 |
    | FCI (HJO, quoted) | 0.6836 | 0.5027 | 0.4350 |

    **H₂O, cc-pCVQZ (optimized $R$ = 1.7756 bohr, 106.22°):**

    | | $1a_1$ | $2a_1$ | $1b_2$ | $3a_1$ | $1b_1$ |
    |---|---:|---:|---:|---:|---:|
    | Koopmans | 20.556 | 1.358 | 0.728 | 0.582 | 0.509 |
    | ΔSCF | 19.813 | 1.266 | 0.658 | 0.489 | 0.410 |
    | Experiment (HJO, quoted) | 19.83 | 1.18 | 0.676 | 0.540 | 0.463 |

    **N₂, cc-pCVQZ (optimized $R$ = 2.0136 bohr):**

    | | $1\sigma_g$ | $1\sigma_u$ | $2\sigma_g$ | $2\sigma_u$ | $1\pi_u$ | $3\sigma_g$ |
    |---|---:|---:|---:|---:|---:|---:|
    | Koopmans | 15.670 | 15.666 | 1.494 | 0.768 | 0.627 | 0.637 |
    | ΔSCF | 15.400 | 15.394 | 1.400 | 0.732 | 0.575 | 0.588 |
    | Experiment (HJO, quoted) | 15.06 | 15.06 | 1.37 | 0.684 | 0.617 | 0.570 |

    - **Agreement.** The cc-pCVDZ and cc-pCVTZ rows also match HJO's Tables 10.2 and 10.3 to ±0.001 $E_h$ (the $\pi_u$ ΔSCF to 0.001).
    - **Misprint in Table 10.1.** The one disagreement is the $3a_1$ ΔSCF value. I get 0.4666 by both maximum-overlap and symmetry-constrained ROHF (UHF gives 0.4634). In Table 10.2 the same ionization has Koopmans − ΔSCF = 0.084 at cc-pCVDZ, exactly my 0.5510 − 0.4666, whereas HJO's 0.4464 implies 0.105. I take 0.4464 to be a transposition of 0.4664.
    - **Knock-on effect.** HJO's "correlation corrections of 40-56 m$E_h$" (FCI − ΔSCF) then become 40, 36 and 41 m$E_h$.

**HJO's conclusions.**

- **Relaxation.** It is large for core holes (0.27 $E_h$ in N₂, 0.74 in H₂O) and below 0.1 $E_h$ for valence holes. Relative to the IP it matters more for valence holes, e.g. 24% for the water $1b_1$.
- **Basis-set limit.** Both methods converge to it within a few m$E_h$ by cc-pCVQZ, while the errors against experiment reach 0.73 $E_h$.
- **Correlation.** Its contribution changes sign from one ionization to another.
- **Core IPs.** ΔSCF is better.
- **Valence IPs.** Koopmans and ΔSCF bracket experiment for water.
- **N₂ ordering.** Both methods put the $1\pi_u$ ionization below $3\sigma_g$, the wrong order. Experimentally $3\sigma_g$ is lower: 0.570 against 0.617.

## Source

Szabo and Ostlund, *Modern Quantum Chemistry* (Dover, 1996; reprint of the revised first edition, McGraw-Hill, 1989), Sec. 3.3.1, pp. 123-128, Eqs. (3.71)-(3.97), Ex. 3.5-3.6; Sec. 3.7.2, pp. 194-200. Tables computed for this note. Helgaker, Jørgensen and Olsen, *Molecular Electronic-Structure Theory* (Wiley, Chichester, 2000), Sec. 10.5, pp. 454-458, Eqs. (10.5.1)-(10.5.17), Tables 10.1-10.3; their values recomputed with PySCF 2.14, experimental and FCI values quoted.
