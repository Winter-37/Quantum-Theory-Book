---
id: periodic-table-and-term-symbols
title: The periodic table, configurations, Hund's rules and term symbols
summary: Aufbau in the hydrogenic picture (shells of 2n²) modified by screening (ℓ-ordering, 4s before 3d). Covers spectroscopic notation, LS term symbols ^{2S+1}L_J, the terms of p², p³ and d² by microstate counting, Hund's three rules with their exchange-symmetry rationale, and an automated reproduction of every ground term in Griffiths Table 5.1 (Z = 1–36), plus dysprosium ⁵I₈.
status: in-progress
kind: theory
level: intermediate
tags: [periodic-table, aufbau, screening, electron-configuration, term-symbols, russell-saunders, hunds-rules, microstates, griffiths]
prerequisites: [helium-atom-independent-particle-model, addition-of-angular-momenta]
related: [hydrogen-atom, spin-adapted-configurations, uhf, rhf]
order: 50
date: 2026-11-05
---

## Shells, screening and the order of filling

**Hydrogenic counting.** Without repulsion, electrons occupy hydrogenic orbitals $(n,\ell,m)$ with two spins each. Shell $n$ holds $2n^2$ electrons (2, 8, 18, 32, ...). The real row lengths (2, 8, 8, 18, 18, 32, ...) differ because of repulsion.

**Screening.** Inner electrons partly cancel the nuclear charge seen by outer ones. Low-$\ell$ orbitals penetrate the core (their density near the nucleus goes as $r^{2\ell}$), so they see more of $Ze$ and are more tightly bound. Within a shell, **energy increases with $\ell$**.

**Order of filling.** This gives 2s before 2p and 3s before 3p. By argon the effect is strong enough that 4s (K, Ca) fills before 3d (Sc–Zn), followed by 4p (Ga–Kr). Similar intrusions happen in later rows.

**Notation.** $\ell = 0,1,2,3,4,\ldots$ are written $s, p, d, f, g, \ldots$ (alphabetical after $f$, skipping $j$). A configuration such as carbon's $(1s)^2(2s)^2(2p)^2$ lists $n\ell$ with occupation exponents. It says nothing about which $m$ values are used, or how the spins and orbital momenta couple.

## Term symbols

**LS coupling.** In Russell–Saunders coupling, the open-shell electrons combine to total $L$, total $S$ and grand total $J$ ($|L-S|\le J\le L+S$):

$$
^{2S+1}L_J,\qquad L = 0,1,2,3,\ldots \to S, P, D, F, \ldots
$$

For example, carbon's ground state is $^3P_0$: $S=1$, $L=1$, $J=0$.

**Closed subshells** contribute $L = S = 0$, so only open subshells matter.

**Which terms a configuration allows.** Enumerate the Pauli-allowed **microstates** $(M_L, M_S)$ and peel off multiplets from the top. Computed here:

| Configuration | Terms |
|---|---|
| $p^2$ (C, Si, ...) | $^1D$, $^3P$, $^1S$ |
| $p^3$ (N, P, ...) | $^2D$, $^2P$, $^4S$ |
| $d^2$ (Ti, ...) | $^1G$, $^3F$, $^1D$, $^3P$, $^1S$ |

**Why $p^2$ has no $^3D$** (Problem 5.18b). The top of the $L=2$ ladder, $M_L = 2$, puts both electrons in $m=1$. That spatial state is symmetric, so it can only pair with the spin singlet. $^1D$ exists; $^3D$ does not.

## Hund's rules

These are empirical rules for the ground term, in this order (Problem 5.18):

1. **Maximum $S$.** Parallel spins require an antisymmetric spatial state, which keeps electrons apart and lowers the repulsion (the exchange hole, [[bosons-fermions-and-exchange-forces]]). For helium it predicts orthohelium below parahelium ([[helium-atom-independent-particle-model]]).
2. **Then maximum $L$.** Electrons orbiting in the same sense avoid each other better.
3. **Then $J$.** $J = |L-S|$ if the subshell is at most half filled; $J = L+S$ if it is more than half filled. This follows from the sign of the effective spin–orbit coupling for holes versus particles.

**Algorithm.** For $\ell^n$:

- fill $m_\ell = \ell,\ell-1,\ldots$ with spin up first, then spin down;
- $S = \tfrac12(n_\uparrow-n_\downarrow)$;
- $L = |\sum m_\ell|$;
- choose $J$ by rule 3.

!!! example "Automated check against Griffiths Table 5.1 (Z = 1–36)"
    The algorithm above was applied to the open subshells of each configuration in Table 5.1. For chromium, $(4s)(3d)^5$, all six spins are parallel: $S = 3$ and $L = 0$.

    **Result.** All 36 ground terms agree with the table, with no mismatches. Selected entries:

    | Element | Configuration | Ground term |
    |---|---|---|
    | B | $(\mathrm{He})(2s)^2(2p)$ | $^2P_{1/2}$ |
    | C | $(\mathrm{He})(2s)^2(2p)^2$ | $^3P_0$ |
    | N | $(\mathrm{He})(2s)^2(2p)^3$ | $^4S_{3/2}$ |
    | O | $(\mathrm{He})(2s)^2(2p)^4$ | $^3P_2$ (more than half filled, so $J = L+S$) |
    | Sc | $(\mathrm{Ar})(4s)^2(3d)$ | $^2D_{3/2}$ |
    | Cr | $(\mathrm{Ar})(4s)(3d)^5$ | $^7S_3$ |
    | Mn | $(\mathrm{Ar})(4s)^2(3d)^5$ | $^6S_{5/2}$ |
    | Fe | $(\mathrm{Ar})(4s)^2(3d)^6$ | $^5D_4$ |
    | Ni | $(\mathrm{Ar})(4s)^2(3d)^8$ | $^3F_4$ |
    | Cu | $(\mathrm{Ar})(4s)(3d)^{10}$ | $^2S_{1/2}$ |

    **Dysprosium** (Problem 5.19). The configuration $[\mathrm{Xe}]4f^{10}6s^2$ gives $S = 2$, $L = 6$ and, since the shell is more than half filled, $J = L+S = 8$: $^5I_8$, matching the quoted ground state.

**Caveats.**

- Hund's rules predict the ground term of a *given* configuration. They do not predict which configuration is lowest: Cr and Cu take one 4s electron into 3d, and this anomaly is an input here.
- LS coupling degrades for heavy atoms, where spin–orbit coupling competes (jj coupling).
- Griffiths notes the rules are empirical. Their first-rule rationale (reduced repulsion) is the usual textbook story; detailed analyses attribute much of the triplet stabilization to changes in electron–nucleus attraction. That refinement is mentioned here, not developed.

**Link to quantum chemistry.** A high-spin open-shell determinant (all unpaired spins parallel) is an eigenfunction of $S^2$ with $S = S_{\max}$. Lower-spin terms need combinations of determinants ([[spin-adapted-configurations]]). This is one reason high-spin ROHF/UHF references are the natural starting point for open-shell atoms.

## Source

Griffiths and Schroeter, *Introduction to Quantum Mechanics* (3rd ed., Cambridge University Press, 2018), Sec. 5.2.2, Eqs. (5.44)-(5.45), Table 5.1; Problems 5.17-5.19. Page numbers are not given because the PDF used is an e-book rendering without print pagination. The microstate decompositions and the Hund's-rule check are computed in `griffiths/ch05_identical.py` (section E). The remark on the mechanism behind Hund's first rule is my addition; no specific reference is given here, and it should be checked before relying on it.
