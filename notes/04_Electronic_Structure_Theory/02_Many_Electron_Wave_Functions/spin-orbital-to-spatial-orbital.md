---
id: spin-orbital-to-spatial-orbital
title: From spin orbitals to spatial orbitals (integrating out spin)
summary: How spin-orbital integrals reduce to spatial integrals for restricted orbitals, the closed-shell energy E0 = 2Σh_aa + ΣΣ(2J_ab − K_ab), exchange lowering of parallel-spin pairs, the pseudo-classical bookkeeping of determinant energies, and the closed-shell MP2 formula as a worked conversion.
status: in-progress
kind: derivation
level: intermediate
tags: [spin-integration, closed-shell, rhf-energy, coulomb, exchange, mp2]
prerequisites: [slater-condon-rules, integral-notation]
related: [minimal-basis-h2-model, spin-adapted-configurations]
order: 60
date: 2026-11-03
---

## Restricted spin orbitals and bar notation

Restricted spin orbitals share one spatial function for both spins:

$$
\chi_i(\mathbf x) = \psi_j(\mathbf r)\alpha(\omega)\equiv\psi_j,
\qquad
\chi_i(\mathbf x) = \psi_j(\mathbf r)\beta(\omega)\equiv\bar\psi_j .
$$

A bar marks $\beta$. Integrating over $\omega$ uses only $\langle\alpha|\alpha\rangle = \langle\beta|\beta\rangle = 1$ and $\langle\alpha|\beta\rangle = 0$.

**One-electron integrals.** $h$ is spin-free:

$$
[\psi_i|h|\psi_j] = [\bar\psi_i|h|\bar\psi_j] = (\psi_i|h|\psi_j) = h_{ij},
\qquad
[\psi_i|h|\bar\psi_j] = 0 .
$$

**Two-electron integrals (chemists').** Each charge distribution $\chi^*\chi$ must have matching spins, or the integral vanishes:

$$
[ij|kl] \text{ (spin orbitals)} = (ij|kl) \text{ (spatial)}\times\delta_{\sigma_i\sigma_j}\,\delta_{\sigma_k\sigma_l}.
$$

So $[\psi_i\psi_j|\bar\psi_k\bar\psi_l] = (ij|kl)$, but $[\psi_i\bar\psi_j|\psi_k\bar\psi_l] = 0$. In physicists' notation, spins must match between positions 1 and 3 and between 2 and 4.

## Closed-shell determinant energy

A closed shell has $N/2$ spatial orbitals each doubly occupied:

$$
|\Psi_0\rangle = |\psi_1\bar\psi_1\cdots\psi_a\bar\psi_a\cdots\psi_{N/2}\bar\psi_{N/2}\rangle .
$$

Split the spin-orbital sums of [[slater-condon-rules]] into $\alpha$ and $\beta$ parts:

$$
\sum_a^N\chi_a = \sum_a^{N/2}\psi_a + \sum_a^{N/2}\bar\psi_a .
$$

- **One-electron part.** $\sum_a^N\langle a|h|a\rangle = 2\sum_a^{N/2}h_{aa}$.
- **Two-electron part.** In $\tfrac12\sum_{a,b}^N\big([aa|bb] - [ab|ba]\big)$ the Coulomb term survives for all four spin pairs, giving $4\cdot\tfrac12(aa|bb)$. The exchange term survives only for same-spin pairs, giving $2\cdot\tfrac12(ab|ba)$.

Hence

$$
E_0 = 2\sum_a^{N/2}h_{aa} + \sum_a^{N/2}\sum_b^{N/2}\big[2(aa|bb) - (ab|ba)\big]
= 2\sum_a^{N/2}h_{aa} + \sum_a^{N/2}\sum_b^{N/2}\big(2J_{ab} - K_{ab}\big),
$$

or in physicists' notation, $E_0 = 2\sum_a\langle a|h|a\rangle + \sum_{ab}\big(2\langle ab|ab\rangle - \langle ab|ba\rangle\big)$.

**Physical reading.** $h_{aa}$ is the mean kinetic plus nuclear-attraction energy of an electron in $\psi_a$. $J_{ab}$ is the Coulomb repulsion of charge clouds, and $K_{ab}$ is the exchange correction for same-spin pairs. Terms with $a=b$ give $2J_{aa} - K_{aa} = J_{aa}$, the repulsion of the two electrons sharing $\psi_a$. For minimal-basis H$_2$, $E_0 = 2h_{11} + J_{11}$ ([[minimal-basis-h2-model]]).

## Rules for any determinant (pseudo-classical bookkeeping)

The energy of any single determinant of restricted orbitals is:

1. $h_{ii}$ for each electron in $\psi_i$, whatever its spin.
2. $J_{ij}$ for **every** pair of electrons, one in $\psi_i$ and one in $\psi_j$ (including two electrons in the same $\psi_i$, which gives $J_{ii}$).
3. $-K_{ij}$ for every pair of electrons with **parallel** spins in different spatial orbitals.

!!! example "Parallel versus antiparallel spins (Szabo Eqs. 2.186-2.187, Ex. 2.22)"
    Two electrons in $\psi_1$ and $\psi_2$:
    $$
    E(\uparrow\downarrow) = \langle\psi_1\bar\psi_2|\hat H|\psi_1\bar\psi_2\rangle = h_{11} + h_{22} + J_{12},
    $$
    $$
    E(\uparrow\uparrow) = \langle\psi_1\psi_2|\hat H|\psi_1\psi_2\rangle = h_{11} + h_{22} + J_{12} - K_{12}.
    $$
    Since $K_{12}>0$, the parallel-spin determinant is lower. The Fermi hole keeps same-spin electrons apart and reduces their repulsion ([[slater-determinants]]).

    For contrast, the Hartree products $\psi_1(\mathbf r_1)\alpha(\omega_1)\psi_2(\mathbf r_2)\beta(\omega_2)$ and $\psi_1(\mathbf r_1)\beta(\omega_1)\psi_2(\mathbf r_2)\beta(\omega_2)$ both have energy $h_{11}+h_{22}+J_{12}$. A product has no exchange term, so its energy does not depend on the spins.

    With the minimal-basis H$_2$ numbers ($R = 1.4$ bohr, STO-3G): $h_{11}+h_{22}+J_{12} = -1.064835$ and $h_{11}+h_{22}+J_{12}-K_{12} = -1.246093$ hartree (electronic).

## Full CI of minimal-basis H2 in spatial form (Szabo Ex. 2.17, 2.21)

$$
\mathbf H = \begin{pmatrix} 2h_{11} + J_{11} & K_{12}\\ K_{12} & 2h_{22} + J_{22}\end{pmatrix}.
$$

The off-diagonal element is $\langle1\bar1||2\bar2\rangle = \langle1\bar1|2\bar2\rangle - \langle1\bar1|\bar22\rangle = (12|12) - 0$. For real orbitals $(12|12) = (12|21) = K_{12}$.

## Worked conversion: closed-shell MP2 (Szabo Ex. 2.18)

The second-order energy over spin orbitals is

$$
E_0^{(2)} = \frac14\sum_{abrs}\frac{|\langle ab||rs\rangle|^2}{\varepsilon_a + \varepsilon_b - \varepsilon_r - \varepsilon_s}.
$$

**Expand.** Write $|\langle ab||rs\rangle|^2 = |\langle ab|rs\rangle|^2 + |\langle ab|sr\rangle|^2 - 2\,\mathrm{Re}\,\langle ab|rs\rangle\langle rs|ba\rangle$. The two squared terms give equal sums after relabelling $r\leftrightarrow s$, so

$$
E_0^{(2)} = \frac12\sum_{abrs}\frac{|\langle ab|rs\rangle|^2 - \langle ab|rs\rangle\langle rs|ba\rangle}{\varepsilon_a+\varepsilon_b-\varepsilon_r-\varepsilon_s}.
$$

**Count spin cases.** Restricted orbitals have $\varepsilon_a = \varepsilon_{\bar a}$, and each spatial label carries a spin.

- $\langle ab|rs\rangle$ needs $\sigma_a = \sigma_r$ and $\sigma_b = \sigma_s$: 4 spin assignments.
- The product $\langle ab|rs\rangle\langle rs|ba\rangle$ needs all four spins equal: 2 assignments.

This gives

$$
E_0^{(2)} = \sum_{ab}^{N/2}\sum_{rs}^{K}{}'\ \frac{(ar|bs)\big[2(ra|sb) - (rb|sa)\big]}{\varepsilon_a+\varepsilon_b-\varepsilon_r-\varepsilon_s}.
$$

Here $a,b$ run over the occupied spatial orbitals $1..N/2$, $r,s$ over the virtual spatial orbitals $N/2+1..K$, and the integrals are chemists' notation. In physicists' notation the numerator is $\langle ab|rs\rangle\big(2\langle rs|ab\rangle - \langle rs|ba\rangle\big)$, the form printed in Szabo (p. 85). For real orbitals the two forms are identical term by term.

**Numerical check.** H$_2$O/STO-3G (O at the origin, H at $(0,\pm0.757,0.587)$ Å). The spin-orbital formula and the closed-shell formula both give $E^{(2)} = -0.035566818$ hartree, identical to PySCF `mp.MP2(mf).e_corr`.

## Source

Szabo and Ostlund, *Modern Quantum Chemistry* (Dover, 1996; reprint of the revised first edition, McGraw-Hill, 1989), Sec. 2.3.5-2.3.7, pp. 81-89, Eqs. (2.159)-(2.189), Ex. 2.17-2.23. Numbers computed with PySCF 2.14 for this note.
