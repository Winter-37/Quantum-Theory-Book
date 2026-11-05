---
id: helium-atom-independent-particle-model
title: "Helium in the independent-particle model: parahelium and orthohelium"
summary: The helium Hamiltonian. Dropping electron–electron repulsion gives hydrogenic product states with Z = 2 and a ground state of 8E₁ = −108.8 eV, against the measured −78.975 eV. First-order inclusion of ⟨e²/4πε₀r₁₂⟩ = (5/2)|E₁| = 34.0 eV improves this to −74.8 eV. Excited states split into singlet parahelium and triplet orthohelium, with triplets lower by exchange. Also covers doubly excited (autoionizing) states, He⁺, and lithium in the same model.
status: in-progress
kind: theory
level: introductory
tags: [helium, two-electron-atom, independent-particle-model, electron-repulsion, parahelium, orthohelium, exchange-splitting, autoionization, lithium, griffiths]
prerequisites: [hydrogen-atom, exchange-symmetry-spin-and-symmetrization-principle]
related: [periodic-table-and-term-symbols, coulomb-cusp-and-helium-expansions, variational-principle, hartree-fock-equations, electron-correlation]
also: [03_Quantum_Chemistry/01_Atomic_Structure]
date: 2026-11-05
---

## Hamiltonian

For an atom with nuclear charge $Ze$ and $Z$ electrons:

$$
\hat H = \sum_{j=1}^{Z}\left[-\frac{\hbar^2}{2m}\nabla_j^2-\frac{1}{4\pi\epsilon_0}\frac{Ze^2}{r_j}\right]+\frac12\frac{1}{4\pi\epsilon_0}\sum_{j\neq k}\frac{e^2}{|\mathbf r_j-\mathbf r_k|}.
$$

The factor $\tfrac12$ corrects for double counting. Only hydrogen is exactly solvable. For helium ($Z=2$) the equation is two hydrogenic Hamiltonians with nuclear charge $2e$ plus the repulsion $e^2/4\pi\epsilon_0|\mathbf r_1-\mathbf r_2|$, and that last term is the whole difficulty.

## Ignoring the repulsion

**Product states.** The equation separates into products of hydrogenic functions with $Z = 2$: Bohr radius $a/2$ and energies $4E_n$ ([[hydrogen-atom]]). Hence

$$
E = 4(E_n+E_{n'}),\qquad
\psi_0 = \psi_{100}(\mathbf r_1)\psi_{100}(\mathbf r_2) = \frac{8}{\pi a^3}e^{-2(r_1+r_2)/a},\qquad
E_0 = 8E_1 = -108.85\ \text{eV}.
$$

**Spin.** $\psi_0$ is spatially symmetric, so the spin state must be the singlet. The real ground state is indeed a singlet.

**Comparison with experiment.** Griffiths quotes $-78.975$ eV. The 30 eV error is the neglected positive repulsion.

## First-order repulsion (Griffiths Problem 5.15)

**Integral.** In $\psi_0$, put the polar axis along $\mathbf r_1$ and integrate over $\mathbf r_2$ first. The angular integral of $1/|\mathbf r_1-\mathbf r_2|$ gives $1/\max(r_1,r_2)$, and the remaining radial integrals give

$$
\left\langle\frac{1}{|\mathbf r_1-\mathbf r_2|}\right\rangle = \frac{5}{4a}.
$$

This was confirmed symbolically.

**Energy.**

$$
V_{ee} = \frac{e^2}{4\pi\epsilon_0}\frac{5}{4a} = \frac52|E_1| = 34.01\ \text{eV},
\qquad E_0+V_{ee} = -74.83\ \text{eV}.
$$

This overshoots the experimental value: the frozen $Z=2$ orbitals are too compact. Letting the effective charge relax is the variational fix ($-77.5$ eV, Griffiths Ch. 8; [[variational-principle]]). The remaining error is electron correlation ([[electron-correlation]], [[coulomb-cusp-and-helium-expansions]]).

## Excited states: parahelium and orthohelium

**Configurations.** Low excited states put one electron in $\psi_{100}$ and one in $\psi_{n\ell m}$. Doubly excited states lie above the He⁺ + e⁻ threshold (see the next section). The two orbitals can be combined two ways:

- **Parahelium:** symmetric space with the spin singlet.
- **Orthohelium:** antisymmetric space with the spin triplet.

**Ordering.** The antisymmetric spatial function keeps the electrons apart (exchange hole, [[bosons-fermions-and-exchange-forces]]), so their repulsion is smaller. **Orthohelium levels lie below the corresponding parahelium levels**, as observed (Griffiths Fig. 5.1). This is Hund's first rule in its simplest setting.

**First-order exchange splitting.** For the configuration $1s\,n\ell$:

$$
E_\pm = E^{(0)} + J \pm K,\qquad
J = \left\langle\psi_a\psi_b\left|\tfrac{e^2}{4\pi\epsilon_0r_{12}}\right|\psi_a\psi_b\right\rangle,\quad
K = \left\langle\psi_a\psi_b\left|\tfrac{e^2}{4\pi\epsilon_0r_{12}}\right|\psi_b\psi_a\right\rangle .
$$

The upper sign is the singlet. For real orbitals $K>0$ (a standard result, not shown in Griffiths Ch. 5), so the triplet lies $2K$ below the singlet. These $J$ and $K$ are the Coulomb and exchange integrals of [[hartree-fock-equations]].

## Doubly excited states and He⁺ (Griffiths Problem 5.13)

**Both electrons in $n=2$.** Without repulsion the energy is $2\times4E_2 = 2E_1 = -27.2$ eV. This is above the He⁺ ground state ($4E_1 = -54.4$ eV). One electron can drop to 1s and eject the other with kinetic energy **27.2 eV**: **autoionization**. Repulsion shifts these numbers, but the picture stands.

**He⁺.** It is hydrogenic with $Z=2$, so $1/\lambda = 4\mathcal R(1/n_f^2-1/n_i^2)$.

## Lithium in the same model (Griffiths Problem 5.16)

**Configuration.** Pauli blocks a third 1s electron, so the ground configuration is $1s^2\,2s$.

**Energy.** Without repulsion,

$$
E = 9\left(2E_1+\tfrac14E_1\right) = -275.5\ \text{eV}.
$$

**Antisymmetrization.** A two-dimensional Slater determinant of $1s\!\uparrow$ and $1s\!\downarrow$, extended by $2s$ ([[exchange-symmetry-spin-and-symmetrization-principle]]).

**Degeneracy.** 2, from the spin of the 2s electron. Without repulsion, 2s and 2p are degenerate. Screening by the 1s pair, which is part of the neglected repulsion, is what selects 2s ([[periodic-table-and-term-symbols]]).

## Source

Griffiths and Schroeter, *Introduction to Quantum Mechanics* (3rd ed., Cambridge University Press, 2018), Secs. 5.2-5.2.1, Eqs. (5.36)-(5.43), Fig. 5.1 (described); Problems 5.13-5.16. Page numbers are not given because the PDF used is an e-book rendering without print pagination. The experimental $-78.975$ eV is quoted from Griffiths and not independently checked. The first-order $J\pm K$ formula and the sign of $K$ are standard results added here, not taken from Griffiths Ch. 5. Numbers are recomputed in `griffiths/ch05_identical.py` (section D).
