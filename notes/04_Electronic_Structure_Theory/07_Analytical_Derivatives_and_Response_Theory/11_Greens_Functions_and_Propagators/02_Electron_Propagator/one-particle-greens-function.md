---
id: one-particle-greens-function
title: The one-particle many-body Green's function (electron propagator) - Dyson equation and self-energy
summary: The one-particle Green's function of an N-electron system has poles at ionization potentials and electron affinities. The Hartree-Fock Green's function has poles at orbital energies (Koopmans). The exact one obeys the Dyson equation with an energy-dependent self-energy Σ(E), whose second-order term is given explicitly. Analytic solutions for minimal-basis H2 (the IP is shifted by exactly the second-order correlation energy) and HeH⁺ (correlation and orbital relaxation), and J-S's superoperator derivation, with the HeH⁺ problem recomputed.
status: in-progress
kind: theory
level: advanced
tags: [greens-function, electron-propagator, self-energy, dyson-equation, ionization-potential, electron-affinity, koopmans]
prerequisites: [greens-functions-single-particle, koopmans-theorem, mp2]
related: [ionization-potentials-second-order-self-energy, propagators-and-superoperators, heh-plus-minimal-basis-model, minimal-basis-h2-model]
also: [04_Electronic_Structure_Theory/08_Electronic_and_Molecular_Properties/01_Electronic_Energies, 04_Electronic_Structure_Theory/04_Electron_Correlation_and_Wavefunction_Methods/02_Perturbation_Theory]
date: 2026-11-03
---

## From orbitals to a many-body Green's function

**Hartree-Fock Green's function (HFGF).** The Fock operator is a one-particle operator, so by analogy with [[greens-functions-single-particle]],

$$
G_0(\mathbf x, \mathbf x'; E) = \sum_i\frac{\chi_i(\mathbf x)\chi_i^*(\mathbf x')}{E - \varepsilon_i},
\qquad
\mathbf G_0(E) = (E\mathbf 1 - \boldsymbol\varepsilon)^{-1}
$$

in the basis of HF spin orbitals, occupied and virtual. Its poles are the orbital energies. By Koopmans' theorem ([[koopmans-theorem]]), $-\varepsilon_c$ approximates an ionization potential and $-\varepsilon_r$ an electron affinity.

**What Koopmans misses.** Write the exact IP for removing an electron from $\chi_c$:

$$
-\text{IP} = {}^N\mathscr E_0 - {}^{N-1}\mathscr E_0(c) = \varepsilon_c - {}^{N-1}E_R(c) + \big({}^NE_{\text{corr}} - {}^{N-1}E_{\text{corr}}(c)\big).
$$

Two corrections are missing:

- **Orbital relaxation** ${}^{N-1}E_R$ (negative), because the $N$-electron orbitals are not optimal for the ion;
- **the difference in correlation energy** between the $N$ and $N-1$ electron systems.

The electron affinity is analogous.

**Exact Green's function (Szabo Ex. 7.8).** With $|{}^N\Phi_0\rangle$ the exact ground state and $|{}^{N\pm1}\Phi_k\rangle$ the states of the ions,

$$
G_{ij}(E) = \sum_m\frac{\langle{}^N\Phi_0|a_j^\dagger|{}^{N-1}\Phi_m\rangle\langle{}^{N-1}\Phi_m|a_i|{}^N\Phi_0\rangle}{E - ({}^N\mathscr E_0 - {}^{N-1}\mathscr E_m)} + \sum_p\frac{\langle{}^N\Phi_0|a_i|{}^{N+1}\Phi_p\rangle\langle{}^{N+1}\Phi_p|a_j^\dagger|{}^N\Phi_0\rangle}{E - ({}^{N+1}\mathscr E_p - {}^N\mathscr E_0)} .
$$

The "many-body" Green's function has poles at **differences** of eigenvalues, $-\text{IP}_m$ and $-\text{EA}_p$. Its residues are the products of overlap amplitudes (pole strengths). Replacing the exact states by $|\Psi_0\rangle$, $a_c|\Psi_0\rangle$ and $a_r^\dagger|\Psi_0\rangle$ recovers $\mathbf G_0$.

## Dyson equation and self-energy

**Dyson's construction.** The exact $\mathbf G(E)$ obeys

$$
\mathbf G(E) = \mathbf G_0(E) + \mathbf G_0(E)\,\boldsymbol\Sigma(E)\,\mathbf G(E),
$$

the same form as the single-particle equation, with an **energy-dependent effective potential** $\boldsymbol\Sigma(E)$, the self-energy. Everything is a matrix in the orbital basis, of dimension equal to the number of spin orbitals: a one-particle picture that is formally exact.

**Second-order self-energy.** In perturbation theory $\boldsymbol\Sigma = \boldsymbol\Sigma^{(2)} + \boldsymbol\Sigma^{(3)} + \cdots$; the first correction is second order, as for the energy ([[mp2]]):

$$
\Sigma_{ij}^{(2)}(E) = \frac12\sum_{a,rs}\frac{\langle rs||ia\rangle\langle ja||rs\rangle}{E + \varepsilon_a - \varepsilon_r - \varepsilon_s} + \frac12\sum_{ab,r}\frac{\langle ab||ir\rangle\langle jr||ab\rangle}{E + \varepsilon_r - \varepsilon_a - \varepsilon_b} .
$$

The first sum has 2p1h intermediate states (two particles and one hole), the second 2h1p. For a closed shell, over spatial orbitals,

$$
\Sigma_{ij}^{(2)}(E) = \sum_{a,rs}\frac{\langle ia|rs\rangle\big(2\langle rs|ja\rangle - \langle rs|aj\rangle\big)}{E + \varepsilon_a - \varepsilon_r - \varepsilon_s} + \sum_{ab,r}\frac{\langle ir|ab\rangle\big(2\langle ab|jr\rangle - \langle ab|rj\rangle\big)}{E + \varepsilon_r - \varepsilon_a - \varepsilon_b} .
$$

**Solving the Dyson equation.** $\mathbf G(E) = (E\mathbf 1 - \boldsymbol\varepsilon - \boldsymbol\Sigma(E))^{-1}$, so the poles are the roots of

$$
\det\big(E\mathbf 1 - \boldsymbol\varepsilon - \boldsymbol\Sigma(E)\big) = 0 .
$$

Three levels of approximation:

1. **Neglect the off-diagonal elements:** $E = \varepsilon_i + \Sigma_{ii}(E)$, one equation per orbital.
2. **Iterate it to self-consistency** in $E$ (the "diagonal Dyson" solution).
3. **Simplest of all:** evaluate $\Sigma$ at the Koopmans energy, $E_i\approx\varepsilon_i + \Sigma_{ii}^{(2)}(\varepsilon_i)$.

The last is analysed in [[ionization-potentials-second-order-self-energy]]. Because $\Sigma(E)$ has poles of its own, the equation has additional roots: shake-up states, ionization accompanied by excitation.

## Minimal-basis H₂: correlation only

**Setup.** One occupied (1) and one virtual (2) orbital ([[minimal-basis-h2-model]]). Only integrals with even numbers of 1s and 2s survive, so $\boldsymbol\Sigma^{(2)}$ is diagonal:

$$
\Sigma_{11}^{(2)}(E) = \frac{K_{12}^2}{E + \varepsilon_1 - 2\varepsilon_2},
\qquad
\Sigma_{22}^{(2)}(E) = \frac{K_{12}^2}{E + \varepsilon_2 - 2\varepsilon_1}.
$$

**Exact answer in the basis.** H₂⁺ has no correlation, and its optimal orbitals are those of H₂ by symmetry ($h_{12} = 0$). So ${}^{N-1}\mathscr E_0 = h_{11}$ and

$$
-\text{IP} = \varepsilon_1 + {}^NE_{\text{corr}} .
$$

**Lowest order.** $\Sigma_{11}^{(2)}(\varepsilon_1) = K_{12}^2/2(\varepsilon_1 - \varepsilon_2) = {}^NE^{(2)}$: the Green's function corrects Koopmans' IP by the second-order correlation energy.

**Exact roots of $E = \varepsilon_1 + \Sigma_{11}^{(2)}(E)$.** The quadratic gives

$$
E_\mp = \varepsilon_1 + (\varepsilon_2 - \varepsilon_1) \mp \big((\varepsilon_2 - \varepsilon_1)^2 + K_{12}^2\big)^{1/2}.
$$

$E_-$ is the IP pole. It has the structure of the exact correlation energy $\Delta - (\Delta^2 + K_{12}^2)^{1/2}$ with $\Delta\to\varepsilon_2 - \varepsilon_1$: exact at second order, approximate beyond. $E_+$ approximates electron capture into an excited state of H₂⁻ (Szabo Ex. 7.9).

**Third order (Szabo Ex. 7.10).** Adding $\Sigma^{(3)}$, which has an energy-independent part, and evaluating at $\varepsilon_1$ gives $\varepsilon_1 + E^{(2)} + E^{(3)}$, the MBPT correlation energy through third order ([[mp3]]).

**Numbers (STO-3G, R = 1.4 bohr; computed for this note).** Koopmans 0.578, $\Sigma^{(2)}(\varepsilon)$ 0.591, Dyson root 0.591, full CI 0.599 hartree (Szabo Table 7.2).

## Minimal-basis HeH⁺: correlation and relaxation

**Relaxation now exists.** Without symmetry, $h_{12}\ne0$. Brillouin's theorem gives $f_{12} = h_{12} + \langle11|12\rangle = 0$, so $h_{12} = -\langle11|12\rangle$. Diagonalizing $\mathbf h$ for HeH²⁺ gives ${}^{N-1}\mathscr E_0 = h_{11} + {}^{N-1}E_R$, and to lowest order

$$
{}^{N-1}E_R^{(2)} = \frac{|\langle11|12\rangle|^2}{\varepsilon_1 - \varepsilon_2}.
$$

**Green's function.** $\Sigma_{11}^{(2)}(E) = K_{12}^2/(E + \varepsilon_1 - 2\varepsilon_2) + |\langle11|12\rangle|^2/(E + \varepsilon_2 - 2\varepsilon_1)$. At $E = \varepsilon_1$:

$$
\varepsilon_1' = \varepsilon_1 + {}^NE^{(2)} - {}^{N-1}E_R^{(2)} ,
$$

which contains both missing effects to second order (Szabo Eq. 7.68).

!!! example "HeH⁺ with J-S's integrals (J-S Problem 6.1, Szabo Sec. 7.3; computed for this note)"
    SCF data of [[heh-plus-minimal-basis-model]]: $\varepsilon_1 = -1.6563$, $\varepsilon_2 = -0.2289$.

    | Quantity (hartree) | This note | J-S |
    |---|---:|---:|
    | Koopmans IP | 1.6563 | 1.6562 |
    | IP from $\Sigma^{(2)}(\varepsilon_1)$ | 1.6351 | 1.6350 |
    | IP from the iterated diagonal Dyson equation | 1.6355 | |
    | Exact IP in the basis, $E(\text{HeH}^{2+}) - E(\text{HeH}^+)$ | 1.6348 | |
    | Koopmans EA ($-\varepsilon_2$) | 0.2289 | 0.2289 |
    | EA from $\Sigma^{(2)}(\varepsilon_2)$ | 0.2234 | 0.2233 |

    **Decomposition.** ${}^NE^{(2)} = -0.0056$ and ${}^{N-1}E_R^{(2)} = -0.0267$. Relaxation dominates and lowers the IP; correlation of the neutral raises it.

    **Other roots.** The equation also has shake-up roots near $E\approx\varepsilon_1 - 2\varepsilon_2$ and $\varepsilon_2 - 2\varepsilon_1$, from the poles of $\Sigma$ (J-S Q5).

## The same object in Jørgensen and Simons

**Definition.** J-S define the electron propagator as the superoperator matrix element $G_{rs}(E) = \langle\langle a_r^\dagger; a_s\rangle\rangle_E = (a_s^\dagger|(E\hat 1 + \hat H)^{-1}|a_r^\dagger)$ ([[propagators-and-superoperators]]). Its spectral form has exactly the IP and EA poles above, up to an overall sign convention for $E$.

**Koopmans level.** With $|0\rangle$ = HF and the operator manifold $\{a_\alpha^\dagger, a_p^\dagger\}$ (occupied and virtual), the superoperator matrix is diagonal, $(a_j^\dagger|E\hat1 + \hat H|a_k^\dagger) = (E + \varepsilon_j)\delta_{jk}$. The propagator is the HFGF, with all pole strengths equal to 1.

**Order analysis.** Add the 2h1p and 2p1h operators $\{a_p^\dagger a_q^\dagger a_\alpha, a_\alpha^\dagger a_\beta^\dagger a_p\}$ as a second block and partition (J-S Eqs. 6.56-6.61):

$$
\mathbf P(E) = \mathbf A - \mathbf C^\dagger\mathbf M^{-1}\mathbf C .
$$

$\mathbf A_1 = \mathbf A_2 = 0$ and $\mathbf C_0 = 0$, so Koopmans' theorem is correct through **first order**, and $-\mathbf C_1^\dagger\mathbf M_0^{-1}\mathbf C_1$ is exactly $\boldsymbol\Sigma^{(2)}(E)$ (J-S Eq. 6.79). Third order adds $\mathbf A_3$ and further terms (Eq. 6.83). In practice second-order propagators are good to about ±0.5 eV and third-order ones to about ±0.3 eV (J-S's assessment).

## Source

Szabo and Ostlund, *Modern Quantum Chemistry* (Dover, 1996; reprint of the revised first edition, McGraw-Hill, 1989), Sec. 7.2-7.3, pp. 387-398, Eqs. (7.26)-(7.68), Ex. 7.7-7.12. Jørgensen and Simons, *Second Quantization-Based Methods in Quantum Chemistry* (Academic Press, New York, 1981), Ch. 6, Sec. D, pp. 134-142, Eqs. (6.46)-(6.85); Problem 6.1 with Solution, pp. 162-163. Numbers recomputed for this note.
