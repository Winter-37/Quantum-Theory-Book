---
id: spin-adapted-configurations
title: Restricted, spin-adapted, and unrestricted determinants
summary: Closed-shell restricted determinants are singlets; open-shell ones generally are not, but simple combinations (spin-adapted configurations) are. Singlet and triplet configurations from single and double excitations, unrestricted determinants, and spin contamination with the ⟨S²⟩ formula, checked on minimal-basis H2.
status: in-progress
kind: theory
level: intermediate
tags: [spin, spin-adaptation, csf, rhf, uhf, spin-contamination, singlet, triplet]
prerequisites: [spin-operators, spin-orbital-to-spatial-orbital]
related: [exact-wave-function-properties-and-symmetry, genealogical-coupling, minimal-basis-h2-model, excited-determinants, spin-orbitals-and-antisymmetry]
also: []
date: 2026-11-03
---

## Restricted determinants

From $K$ orthonormal spatial orbitals, **restricted** spin orbitals use the same spatial function for both spins: $\chi_{2i-1} = \psi_i\alpha$ and $\chi_{2i} = \psi_i\beta$. Bar notation writes $\bar\psi_i = \psi_i\beta$. In a restricted determinant each spatial orbital is empty, singly occupied (an **open shell**), or doubly occupied.

## Closed shells are singlets

A determinant with every occupied spatial orbital doubly occupied satisfies

$$
\hat{\mathcal S}^2|\psi_a\bar\psi_a\psi_b\bar\psi_b\cdots\rangle = 0 .
$$

**Proof sketch (Szabo Ex. 2.38).**

- Use $\hat{\mathcal S}^2 = \hat{\mathcal S}_-\hat{\mathcal S}_+ + \hat{\mathcal S}_z + \hat{\mathcal S}_z^2$, with $M_S = 0$ so the last two terms vanish.
- $\hat{\mathcal S}_+$ commutes with antisymmetrization and acts on one electron at a time.
- On $\psi\alpha$ it gives zero. On $\bar\psi_a = \psi_a\beta$ it gives $\psi_a\alpha$, producing a determinant with $\psi_a\alpha$ twice, which is zero.

The simplest case is the H$_2$ ground state:

$$
|1\bar1\rangle = \psi_1(\mathbf r_1)\psi_1(\mathbf r_2)\cdot2^{-1/2}\big[\alpha(1)\beta(2) - \beta(1)\alpha(2)\big],
$$

a symmetric space part times the singlet spin function. The doubly excited $|2\bar2\rangle$ is also a singlet.

## Open shells: spin-adapted configurations

Open-shell restricted determinants are $\hat{\mathcal S}^2$ eigenfunctions only when all open-shell electrons have parallel spin. For two electrons in $\psi_1$, $\psi_2$ (minimal-basis H$_2$ singles, [[minimal-basis-h2-model]]):

**High spin, already pure triplets.**

$$
|\bar2\bar1\rangle = -2^{-1/2}\big[\psi_1(1)\psi_2(2) - \psi_2(1)\psi_1(2)\big]\beta(1)\beta(2),
$$

$$
|12\rangle = 2^{-1/2}\big[\psi_1(1)\psi_2(2) - \psi_2(1)\psi_1(2)\big]\alpha(1)\alpha(2).
$$

These have $M_S = -1, +1$.

**$M_S = 0$, not pure.** $|\Psi_1^3\rangle = |2\bar1\rangle$ and $|\Psi_2^4\rangle = |1\bar2\rangle$ each mix singlet and triplet. Their normalized sum and difference are pure:

$$
|{}^1\Psi_1^2\rangle = 2^{-1/2}\big(|1\bar2\rangle + |2\bar1\rangle\big)
= 2^{-1/2}\big[\psi_1(1)\psi_2(2) + \psi_2(1)\psi_1(2)\big]\cdot2^{-1/2}\big[\alpha(1)\beta(2) - \beta(1)\alpha(2)\big],
$$

$$
|{}^3\Psi_1^2\rangle = 2^{-1/2}\big(|1\bar2\rangle - |2\bar1\rangle\big)
= 2^{-1/2}\big[\psi_1(1)\psi_2(2) - \psi_2(1)\psi_1(2)\big]\cdot2^{-1/2}\big[\alpha(1)\beta(2) + \beta(1)\alpha(2)\big].
$$

The singlet has a symmetric space part with an antisymmetric spin part, and the triplet has an antisymmetric space part with a symmetric spin part. Their product is antisymmetric in both cases. The three triplets ($M_S = 1, 0, -1$) share the same spatial factor (Szabo Ex. 2.39).

**Energies (Szabo Ex. 2.40).** Using the [[spin-orbital-to-spatial-orbital]] rules,

$$
\langle{}^1\Psi_1^2|\hat H|{}^1\Psi_1^2\rangle = h_{11} + h_{22} + J_{12} + K_{12},
\qquad
\langle{}^3\Psi_1^2|\hat H|{}^3\Psi_1^2\rangle = h_{11} + h_{22} + J_{12} - K_{12}.
$$

The triplet is lower by $2K_{12}$. Its antisymmetric space factor vanishes at $\mathbf r_1 = \mathbf r_2$, keeping the electrons apart and reducing their repulsion (Hund's rule). At $R = 1.4$ bohr (STO-3G) these are $-0.883577$ and $-1.246093$ hartree. Both agree with the eigenvalues of the second-quantized Hamiltonian in [[second-quantized-operators]], where the triplet appears threefold degenerate.

## General singlet configurations from a closed shell

For excitations from $|{}^1\Psi_0\rangle = |\cdots\psi_a\bar\psi_a\psi_b\bar\psi_b\cdots\rangle$, quoted without derivation:

**Singles.**

$$
|{}^1\Psi_a^r\rangle = 2^{-1/2}\big(|\Psi_a^r\rangle + |\Psi_{\bar a}^{\bar r}\rangle\big).
$$

This reduces to the H$_2$ result for $a = 1$, $r = 2$.

**Doubles** (Szabo Table 2.7):

| Electrons leave (spatial) | Electrons enter (spatial) | Singlet configurations |
|---|---|---|
| both $\psi_a$ | both $\psi_r$ | one: $|\Psi_{a\bar a}^{r\bar r}\rangle$ (closed shell, already pure) |
| both $\psi_a$ | $\psi_r$ and $\psi_s$ | one |
| $\psi_a$ and $\psi_b$ | both $\psi_r$ | one |
| $\psi_a$ and $\psi_b$ ($a\ne b$) | $\psi_r$ and $\psi_s$ ($r\ne s$) | **two** linearly independent singlets, labelled $^A$ and $^B$ |

The last case has two because four open shells admit two independent ways to couple to $S = 0$. Szabo quotes the explicit combinations, which are beyond this note and best taken from the book. Systematic construction of spin eigenfunctions is treated by Pauncz, *Spin Eigenfunctions* (Plenum, 1979), as cited by Szabo.

## Unrestricted determinants

Restricted orbitals are a real constraint. In Li ($1s^22s$) the $1s\alpha$ electron has an exchange interaction with $2s\alpha$ but $1s\beta$ does not, so the two $1s$ electrons feel different potentials. **Unrestricted** spin orbitals use different spatial sets for the two spins:

$$
\chi_{2i-1} = \psi_i^\alpha\alpha,
\qquad
\chi_{2i} = \psi_i^\beta\beta,
\qquad
\langle\psi_i^\alpha|\psi_j^\alpha\rangle = \langle\psi_i^\beta|\psi_j^\beta\rangle = \delta_{ij},
\qquad
\langle\psi_i^\alpha|\psi_j^\beta\rangle = S_{ij}^{\alpha\beta}.
$$

The $2K$ spin orbitals are still orthonormal ([[spin-orbitals-and-antisymmetry]], Ex. 2.1). Minimizing a single determinant with this extra freedom is UHF, which always gives an energy at or below RHF.

**Spin contamination.** An unrestricted determinant is not an $\hat{\mathcal S}^2$ eigenfunction, and it cannot be spin-adapted by combining a few determinants. It contains admixtures of **higher** multiplicities only:

- An approximate singlet mixes in triplet, quintet, and so on.
- An approximate doublet mixes in quartet, sextet, and so on.
- An approximate triplet mixes in quintet, and so on.

The expectation value, with $N^\alpha\ge N^\beta$, is

$$
\langle\hat{\mathcal S}^2\rangle_{\text{UHF}} = \langle\hat{\mathcal S}^2\rangle_{\text{exact}} + N^\beta - \sum_{i}^{N^\alpha}\sum_{j}^{N^\beta}|S_{ij}^{\alpha\beta}|^2,
\qquad
\langle\hat{\mathcal S}^2\rangle_{\text{exact}} = \frac{N^\alpha - N^\beta}{2}\left(\frac{N^\alpha - N^\beta}{2} + 1\right).
$$

$S_{ij}^{\alpha\beta}$ is the overlap between occupied $\alpha$ and occupied $\beta$ spatial orbitals. The excess is $\ge 0$ and vanishes only when every occupied $\beta$ orbital lies in the span of the occupied $\alpha$ orbitals.

!!! example "Two electrons in different orbitals (Szabo Ex. 2.41)"
    For $|K\rangle = |\psi_1^\alpha\bar\psi_1^\beta\rangle$ with $\langle\psi_1^\alpha|\psi_1^\beta\rangle = S_{11}^{\alpha\beta}$, the formula gives $\langle\hat{\mathcal S}^2\rangle = 0 + 1 - |S_{11}^{\alpha\beta}|^2$. This is zero, a pure singlet, only if $\psi_1^\beta = \psi_1^\alpha$ up to a phase.

!!! example "UHF H2 at stretched geometry"
    STO-3G, PySCF 2.14, UHF started from a broken-symmetry guess. Total energies in hartree:

    | $R$ (bohr) | $E_{\text{RHF}}$ | $E_{\text{UHF}}$ | $\langle\hat{\mathcal S}^2\rangle$ (PySCF) | $1 - |S_{11}^{\alpha\beta}|^2$ |
    |---:|---:|---:|---:|---:|
    | 1.4 | −1.116714 | −1.116714 | 0.000000 | 0.000000 |
    | 4.0 | −0.761082 | −0.935842 | 0.963988 | 0.963988 |

    Near equilibrium the UHF solution collapses to RHF, as Szabo notes for this model. At $R = 4$ bohr it breaks spin symmetry: the energy drops by 0.175 hartree towards two H atoms (STO-3G H atom $\approx -0.4666$ hartree), and the wave function is nearly an equal singlet-triplet mixture ($\langle\hat{\mathcal S}^2\rangle\approx1$). The formula and `mf.spin_square()` agree to machine precision.

## Source

Szabo and Ostlund, *Modern Quantum Chemistry* (Dover, 1996; reprint of the revised first edition, McGraw-Hill, 1989), Sec. 2.5.2-2.5.3, pp. 100-107, Eqs. (2.255)-(2.272), Table 2.7, Ex. 2.38-2.41. UHF numbers computed for this note.
