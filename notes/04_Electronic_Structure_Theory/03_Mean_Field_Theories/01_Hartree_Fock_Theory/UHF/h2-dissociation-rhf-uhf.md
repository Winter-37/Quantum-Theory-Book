---
id: h2-dissociation-rhf-uhf
title: The H2 dissociation problem - RHF failure and the UHF solution
summary: In minimal-basis H2 the RHF determinant dissociates to a 50/50 mixture of covalent and ionic structures and its energy goes to the wrong limit. A one-parameter UHF (rotation angle θ) breaks spin symmetry beyond an instability point, reaches the correct energy limit, but becomes a 50% triplet-contaminated wave function. Stability analysis and recomputed STO-3G curves.
status: in-progress
kind: derivation
level: intermediate
tags: [hartree-fock, rhf, uhf, dissociation, symmetry-breaking, stability, static-correlation, coulson-fischer]
prerequisites: [uhf, minimal-basis-h2-model, spin-adapted-configurations]
related: [standard-models-h2-and-water, rhf, excited-determinants, scf-second-order-and-stability, mp2]
also: [04_Electronic_Structure_Theory/04_Electron_Correlation_and_Wavefunction_Methods/01_Electron_Correlation/Static_Correlation]
date: 2026-11-03
---

## Why RHF fails

In minimal-basis H$_2$ the RHF orbital is $\psi_1 = [2(1+S_{12})]^{-1/2}(\phi_1 + \phi_2)$ ([[minimal-basis-h2-model]]). Expanding the spatial part of $|\psi_1\bar\psi_1\rangle$:

$$
\psi_1(1)\psi_1(2) \propto \underbrace{\phi_1(1)\phi_2(2) + \phi_2(1)\phi_1(2)}_{\text{covalent, H}\cdot\ \cdot\text{H}} + \underbrace{\phi_1(1)\phi_1(2) + \phi_2(1)\phi_2(2)}_{\text{ionic, H}^-\text{H}^+} .
$$

Covalent and ionic structures always enter with equal weight. At large $R$ the ionic part should vanish, but RHF cannot remove it. The RHF energy therefore goes to the average of two H atoms and H$^-$ + H$^+$.

In the same basis as $R\to\infty$:

$$
E_{\text{RHF}}(\infty) = 2E_{\text{H}} + \tfrac12(\phi_1\phi_1|\phi_1\phi_1),
$$

which is too high by half the one-centre repulsion. For STO-3G this error is $0.7746/2 = 0.387$ hartree. The approach is slow, because the ionic component carries a $-1/(2R)$ attraction; at $R = 60$ bohr the RHF energy is still 0.008 hartree below this limit.

Full CI fixes this by mixing in $|\psi_2\bar\psi_2\rangle$, which cancels the ionic part (static correlation).

## One-parameter UHF

The only freedom in this basis is a rotation between $\psi_1$ and $\psi_2$, taken in opposite directions for the two spins:

$$
\psi_1^\alpha = \cos\theta\,\psi_1 + \sin\theta\,\psi_2,
\qquad
\psi_1^\beta = \cos\theta\,\psi_1 - \sin\theta\,\psi_2,
\qquad
0\le\theta\le45^\circ .
$$

- $\theta = 0$ is RHF.
- $\theta = 45^\circ$ puts $\alpha$ entirely on atom 1 and $\beta$ on atom 2.

Both sets are orthonormal (Szabo Ex. 3.42).

**Energy and its curvature.** The energy $E(\theta) = \langle\psi_1^\alpha\bar\psi_1^\beta|\hat H|\psi_1^\alpha\bar\psi_1^\beta\rangle$ is even in $\theta$, so $\theta = 0$ is always stationary. Its curvature there is

$$
E''(0) = 4\big(h_{22} - h_{11} - J_{11} + J_{12} - 2K_{12}\big),
$$

checked against a finite-difference second derivative to $10^{-7}$.

- **Short bonds.** $E''(0) > 0$, so RHF is a local minimum and no UHF solution exists.
- **Long bonds.** $E''(0) < 0$, so RHF becomes a **maximum** along $\theta$ and the energy drops by breaking spin symmetry.
- **Crossover.** The point where $E''(0) = 0$ is the **RHF→UHF instability point** (Coulson-Fischer point).

**Wave function.** Expanding the determinant (Szabo Eq. 3.381):

$$
|\psi_1^\alpha\bar\psi_1^\beta\rangle = \cos^2\theta\,|\psi_1\bar\psi_1\rangle - \sin^2\theta\,|\psi_2\bar\psi_2\rangle - \sqrt2\cos\theta\sin\theta\,|{}^3\Psi_1^2\rangle,
$$

where $|{}^3\Psi_1^2\rangle$ is the $M_S = 0$ triplet configuration ([[spin-adapted-configurations]]).

- **What it does well.** The doubly excited singlet enters with a negative sign, which is what full CI uses to remove the ionic part.
- **What it costs.** In a single determinant this comes bundled with a triplet. Since $\hat{\mathcal S}^2$ gives 2 on the triplet and 0 on the singlets,
$$
\langle\hat{\mathcal S}^2\rangle = 2\cdot2\cos^2\theta\sin^2\theta = \sin^2 2\theta .
$$
- **The limit.** As $R\to\infty$, $\theta\to45^\circ$ and the wave function becomes $|\phi_1\bar\phi_2\rangle$: 50% singlet and 50% triplet (Szabo Ex. 3.44). The correct singlet would be $2^{-1/2}(|\phi_1\bar\phi_2\rangle + |\phi_2\bar\phi_1\rangle)$.

## STO-3G numbers

$\zeta = 1.24$ throughout. $\theta$ is found by minimizing $E(\theta)$ directly. FCI is the 2x2 CI of [[minimal-basis-h2-model]]. Total energies in hartree; $2E_{\text{H}} = -0.933164$ in this basis.

| $R$ (bohr) | $\theta$ | $E_{\text{RHF}}$ | $E_{\text{UHF}}$ | $E_{\text{FCI}}$ | $\langle\hat{\mathcal S}^2\rangle_{\text{UHF}}$ |
|---:|---:|---:|---:|---:|---:|
| 1.4 | 0° | −1.116714 | −1.116714 | −1.137276 | 0 |
| 2.0 | 0° | −1.049171 | −1.049171 | −1.088496 | 0 |
| 2.5 | 20.77° | −0.965794 | −0.979948 | −1.030474 | 0.440 |
| 3.0 | 30.82° | −0.885275 | −0.951018 | −0.985157 | 0.774 |
| 4.0 | 39.53° | −0.761082 | −0.935842 | −0.943778 | 0.964 |
| 6.0 | 44.24° | −0.645077 | −0.933227 | −0.933402 | 0.999 |

**Observations.**

- $\theta = 39.5^\circ$ at $R = 4.0$ bohr agrees with Szabo Ex. 3.43. The $\langle\hat{\mathcal S}^2\rangle = \sin^22\theta$ value at 4.0 bohr matches PySCF `spin_square()` (0.963988).
- The instability point computed from $E''(0) = 0$ is $R_c = 2.180$ bohr. Szabo states "in the vicinity of 2.3 a.u."; his value was read from the tabulated integrals of his Appendix D. This note's value is the root of the analytic $E''(0)$ with PySCF integrals.
- RHF is already 0.29 hartree too high at 4 bohr. UHF follows FCI within 8 mHa there and reaches the atomic limit.

## Lessons

- **Symmetry breaking is a diagnostic.** Breaking spin symmetry recovers the right energy at dissociation, but the wave function is wrong (contaminated). Using UHF as a reference near dissociation complicates CI and perturbation theory.
- **The proper fix is multireference.** Static correlation needs at least two configurations (CASSCF/MCSCF) or a symmetry-restored method.
- **Not specific to H₂.** Similar instabilities appear whenever closed-shell bonds are stretched. The onset can be at or even before equilibrium for multiple bonds. Checking SCF stability (the orbital Hessian) is good practice.

## Source

Szabo and Ostlund, *Modern Quantum Chemistry* (Dover, 1996; reprint of the revised first edition, McGraw-Hill, 1989), Sec. 3.8.7, pp. 221-229, Eqs. (3.355)-(3.382), Figs. 3.17-3.19, Ex. 3.42-3.44. All numbers computed for this note.
