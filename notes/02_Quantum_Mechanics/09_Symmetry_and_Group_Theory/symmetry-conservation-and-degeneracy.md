---
id: symmetry-conservation-and-degeneracy
title: Symmetry, conservation laws and degeneracy (with the Runge–Lenz vector and Kramers' theorem)
summary: If [Ĥ, Q̂] = 0 and Q̂ has no explicit time dependence, both ⟨Q⟩ and the full outcome distribution of Q are constant. One symmetry operator, or several commuting ones, does not force degeneracy; two that do not commute with each other do. Applications: the 2ℓ+1 degeneracy of central potentials, the free particle, the 2D square well (whose ψ₊ and ψ₋ belong to different D₄ irreps, so their degeneracy needs a further symmetry), hydrogen's n² from the Runge–Lenz vector (constants c_nℓ derived and checked), and time reversal with Kramers' degeneracy (checked on a random spin-½ Hamiltonian).
status: in-progress
kind: theory
level: intermediate
tags: [conservation-laws, degeneracy, accidental-degeneracy, runge-lenz-vector, hydrogen-degeneracy, time-reversal, kramers-degeneracy, antiunitary, point-group, griffiths]
prerequisites: [rotation-operator-and-rotational-symmetry, generalized-statistical-interpretation]
related: [translation-operator-and-translational-symmetry, parity-and-parity-selection-rules, heisenberg-picture-and-time-translation, hydrogen-atom, exact-wave-function-properties-and-symmetry, spin-one-half]
also: []
date: 2026-11-05
---

## What "conserved" means in quantum mechanics

**Two definitions.** A system generally has no definite value of $Q$ before or after a process, so "conserved" can mean:

1. $\langle Q\rangle$ is independent of time;
2. the probability of every outcome $q_n$ is independent of time.

**Theorem.** Let $\partial\hat Q/\partial t = 0$ and $[\hat Q,\hat H] = 0$. Then both hold.

**Proof.**

- Definition 1 follows from $d\langle Q\rangle/dt = (i/\hbar)\langle[\hat H,\hat Q]\rangle$.
- For definition 2, choose a common eigenbasis, $\hat H\psi_n = E_n\psi_n$ and $\hat Q\psi_n = q_n\psi_n$. Then $\Psi(t) = \sum_mc_me^{-iE_mt/\hbar}\psi_m$, and

$$
P(q_n) = \Big|\sum_m c_me^{-iE_mt/\hbar}\langle\psi_n|\psi_m\rangle\Big|^2 = |c_n|^2,
$$

which does not depend on $t$. If $q_n$ is degenerate, sum $|c_i|^2$ over its eigenvectors; the argument is unchanged.

**Symmetries and conservation laws.**

| Symmetry | Conserved quantity |
|---|---|
| continuous translation | momentum ([[translation-operator-and-translational-symmetry]]) |
| rotation | angular momentum ([[rotation-operator-and-rotational-symmetry]]) |
| inversion | parity ([[parity-and-parity-selection-rules]]) |
| time translation | energy ([[heisenberg-picture-and-time-translation]]) |

A discrete translation conserves only crystal momentum.

## Why symmetry produces degeneracy

**Basic step.** If $[\hat H,\hat Q] = 0$ and $\hat H\psi_n = E_n\psi_n$, then $\hat H(\hat Q\psi_n) = \hat Q\hat H\psi_n = E_n(\hat Q\psi_n)$. So $\hat Q\psi_n$ is a stationary state with the same energy.

**One symmetry is not enough.** $\hat Q\psi_n$ may simply be $\psi_n$ again, up to a factor. Choosing the eigenbasis of $\hat H$ to diagonalize $\hat Q$ makes this happen for every state. The oscillator commutes with parity, but each eigenstate maps to $\pm$ itself, so parity alone produces no degeneracy. The same holds for any set of mutually commuting symmetries.

**Non-commuting symmetries force degeneracy.** Let $[\hat H,\hat Q] = [\hat H,\hat\Lambda] = 0$ but $[\hat Q,\hat\Lambda]\neq0$. Take $\psi$ a common eigenstate of $\hat H$ and $\hat Q$. If every such $\psi$ were also an eigenstate of $\hat\Lambda$, the three operators would share a complete eigenbasis and $\hat Q$, $\hat\Lambda$ would commute, which is false. So for some level, $\hat\Lambda\psi$ is a different state with the same energy, and that level is degenerate.

!!! example "Central potentials: 2ℓ + 1 (Example 6.3)"
    **Argument.** $[\hat H,\hat L_\pm] = 0$, so $\hat H(\hat L_\pm\psi_{n\ell m}) = E_n\hat L_\pm\psi_{n\ell m}$. Since $\hat L_\pm\psi_{n\ell m}\propto\psi_{n\ell,m\pm1}$ with a nonzero coefficient except at the ends of the ladder, every $m$ in a multiplet has the same energy. (The radial equation does not contain $m$, so this was known; the point is that rotational invariance is the reason.)

    **Normal degeneracy.** $2\ell+1$. Symmetry fixes the size of each degenerate set, not where it falls in the spectrum: the infinite spherical well shows $1,3,5,7,1,9,\ldots$

    **Excess degeneracy** signals more symmetry: hydrogen has $n^2$ and the 3D oscillator has $(n+1)(n+2)/2$. A degeneracy whose symmetry is not identified is called *accidental*, but usually a hidden symmetry is responsible.

!!! example "Free particle in 1D (Problem 6.18)"
    **Two symmetries.** $\hat H = \hat p^2/2m$ commutes with translations and with parity, but these do not commute with each other: $\hat\Pi\hat T(a) = \hat T(-a)\hat\Pi$.

    **Translation basis.** Momentum eigenstates $f_p(x) = e^{ipx/\hbar}/\sqrt{2\pi\hbar}$ diagonalize $\hat T$, and parity maps $f_p\to f_{-p}$.

    **Parity basis.** $\cos(px/\hbar)/\sqrt{\pi\hbar}$ and $\sin(px/\hbar)/\sqrt{\pi\hbar}$ diagonalize $\hat\Pi$, and $\hat T(a)$ mixes them.

    **Conclusion.** Either way, the pair $\pm p$ is degenerate. Both symmetries are needed: translations alone would not tie $f_p$ to $f_{-p}$.

## The square well and hidden symmetry (Problem 6.33)

**States.** A 2D infinite well of side $L$, centred at the origin, has

$$
\psi_{ab}(x,y) = \frac2L\sin\!\left[\frac{a\pi}{L}\!\left(x-\frac L2\right)\right]\sin\!\left[\frac{b\pi}{L}\!\left(y-\frac L2\right)\right],\qquad
E_{ab} = \frac{\pi^2\hbar^2}{2mL^2}(a^2+b^2).
$$

$\psi_{ab}$ and $\psi_{ba}$ are degenerate.

**(a) Rotation by $+90°$.** $(\hat R\psi)(x,y) = \psi(y,-x)$. Using $\sin[n\pi(-u-\tfrac12)] = (-1)^{n+1}\sin[n\pi(u-\tfrac12)]$:

$$
\hat R\,\psi_{ab} = (-1)^{b+1}\psi_{ba}.
$$

This was confirmed on a grid for $(a,b) = (1,2)$, $(2,3)$, $(5,7)$ and $(2,4)$. The constant depends on the sign convention of the sine factors; with the book's $(x-L/2)$ form it is $(-1)^{b+1}$.

**(b) Symmetric combinations.** For $\psi_\pm = (\psi_{ab}\pm\psi_{ba})/\sqrt2$,

$$
\hat R\psi_\pm = \frac{(-1)^{b+1}\psi_{ba}\pm(-1)^{a+1}\psi_{ab}}{\sqrt2},
$$

which is $\pm(-1)^{a+1}\psi_\pm$ exactly when $a$ and $b$ have the same parity.

!!! example "(c) The symmetry group of the square, D₄, for (a, b) = (5, 7)"
    **Method.** Apply all eight operations of the square (rotations $E$, $C_4$, $C_2$, $C_4^3$; reflections $\sigma_x$, $\sigma_y$ across the bisectors of the sides; $\sigma_d$, $\sigma_d'$ across the diagonals) on a grid. Both $\psi_\pm$ come back as exact multiples of themselves, with these eigenvalues:

    | | $E$ | $C_4$ | $C_2$ | $C_4^3$ | $\sigma_x$ | $\sigma_y$ | $\sigma_d$ | $\sigma_d'$ | irrep |
    |---|---|---|---|---|---|---|---|---|---|
    | $\psi_+$ | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | $A_1$ |
    | $\psi_-$ | 1 | −1 | 1 | −1 | 1 | 1 | −1 | −1 | $B_1$ (like $x^2-y^2$) |

    **Reading.** The two degenerate states lie in different one-dimensional irreps. No operation of the square connects them, so the degeneracy is not explained by the geometric symmetry.

    **The hidden symmetry.** It is separability: $\hat H = \hat H_x+\hat H_y$, and $\hat H_x$ is itself conserved. $\hat H_x$ does not commute with the $90°$ rotation, and $\psi_{57} = (\psi_++\psi_-)/\sqrt2$ is its eigenstate. By the non-commuting-symmetries argument above, the pair $\{\psi_+,\psi_-\}$ must be degenerate. (This identification is my reading; Griffiths only asks for the existence of an additional symmetry.)

## Hydrogen: the Runge–Lenz vector (Problem 6.34)

**The vector.** The Coulomb problem conserves the Laplace–Runge–Lenz vector

$$
\hat{\mathbf M} = \frac{\hat{\mathbf p}\times\hat{\mathbf L}-\hat{\mathbf L}\times\hat{\mathbf p}}{2m} + V(r)\,\mathbf r,\qquad V = -\frac{k}{r},\quad k = \frac{e^2}{4\pi\epsilon_0}.
$$

**Algebra.**

- $[\hat H,\hat M_i] = 0$, and $\hat{\mathbf M}$ is a vector operator: $[\hat L_i,\hat M_j] = i\hbar\epsilon_{ijk}\hat M_k$.
- $[\hat M_i,\hat M_j] = -i\hbar\,\epsilon_{ijk}\hat L_k\,(2\hat H/m)$.
- $\hat M^2 = k^2 + (2\hat H/m)(\hat L^2+\hbar^2)$ and $\hat{\mathbf M}\cdot\hat{\mathbf L} = 0$.

**Why it raises $\ell$.** $\hat M_+$ and $\hat L_\pm$ do not commute, so further degeneracy is forced. By Problem 6.19, $\hat M_+\psi_{n\ell\ell} = c_{n\ell}\,\psi_{n,\ell+1,\ell+1}$, which stays at the same energy because $\hat M$ commutes with $\hat H$.

**The constants $c_{n\ell}$.**

- Applying $\hat{\mathbf M}\cdot\hat{\mathbf L} = 0$ to $\psi_{n\ell\ell}$ gives $\hat M_z\psi_{n\ell\ell} = -\tfrac{1}{\sqrt2}\tfrac{1}{\sqrt{\ell+1}}c_{n\ell}\,\psi_{n,\ell+1,\ell}$.
- Applying $\hat M^2$ gives $\hat M_-\hat M_+\psi_{n\ell\ell} = k^2[1-(\ell+1)^2/n^2]\psi_{n\ell\ell}-\hat M_z^2\psi_{n\ell\ell}$.
- Take the expectation value in $\psi_{n\ell\ell}$, with $\langle\hat M_-\hat M_+\rangle = \|\hat M_+\psi\|^2 = |c_{n\ell}|^2$ and $\langle\hat M_z^2\rangle = \|\hat M_z\psi\|^2 = |c_{n\ell}|^2/2(\ell+1)$:

$$
|c_{n\ell}|^2 = k^2\,\frac{2(\ell+1)}{2\ell+3}\left[1-\frac{(\ell+1)^2}{n^2}\right].
$$

This vanishes only for $\ell = n-1$. Starting from $\psi_{n00}$, $\hat M_+$ climbs $\ell = 0,1,\ldots,n-1$, and $\hat L_-$ fills in each multiplet. Together they connect all $\sum_{\ell=0}^{n-1}(2\ell+1) = n^2$ states (Griffiths Fig. 6.9 draws this for $n=3$). The phase of $c_{n\ell}$ is convention-dependent.

!!! example "Direct check in atomic units (ħ = m = k = 1)"
    **Method.** $\hat{\mathbf M}$ was applied symbolically to SymPy's hydrogen functions in Cartesian form, using $\hat{\mathbf p}\times\hat{\mathbf L}-\hat{\mathbf L}\times\hat{\mathbf p} = 2\hat{\mathbf p}\times\hat{\mathbf L}-2i\hbar\hat{\mathbf p}$. The ratio to the target state was evaluated at two unrelated points.

    | $n$, $\ell$ | $c_{n\ell}$ computed | $\lvert c\rvert$ from the formula | $\hat M_z\psi$ coefficient | book form $-c/\sqrt{2(\ell+1)}$ |
    |---|---|---|---|---|
    | 2, 0 | −0.707107 | 0.707107 | 0.500000 | 0.500000 |
    | 3, 0 | −0.769800 | 0.769800 | 0.544331 | 0.544331 |
    | 3, 1 | −0.666667 | 0.666667 | 0.333333 | 0.333333 |
    | 2, 1 and 3, 2 | $\hat M_+\psi = 0$ ($\ell = n-1$) | 0 | | |

    The ratios are constant in space (the same at both points), which confirms that $\hat M_+$ maps onto the single state predicted. The negative sign is the phase in SymPy's Condon–Shortley convention.

## Time reversal and Kramers degeneracy (Problems 6.36–6.37)

**Spinless particles.** Time reversal reverses motion, not time: $\hat\Theta\Psi(x,t) = \Psi^*(x,t)$. Then $\hat x' = \hat x$ and $\hat p' = -\hat p$, since $-i\hbar\,d/dx$ changes sign under conjugation. $\hat\Theta$ is **antiunitary** (antilinear, $\hat\Theta(c\psi) = c^*\hat\Theta\psi$). The invariance condition, from "evolve, reverse, evolve, return", is $[\hat\Theta,\hat H] = 0$.

**Consequences for spinless systems.**

- If $\psi_n$ is stationary, so is $\psi_n^*$ with the same energy. A nondegenerate level can therefore be chosen real.
- Plane waves map $e^{ipx/\hbar}\to e^{-ipx/\hbar}$.
- Hydrogen states map $\psi_{n\ell m}\to\psi_{n\ell m}^* = (-1)^m\psi_{n\ell,-m}$ (Condon–Shortley), the same energy with reversed $L_z$.
- A magnetic field breaks the symmetry: reversing the velocity reverses the Lorentz force, and the particle does not retrace its orbit.

**Spin ½.** Spin must also flip, and Griffiths' choice (6.84) is $\hat\Theta\binom ab = \binom{-b^*}{a^*}$. Then $\hat\Theta^2 = -1$.

**Kramers' theorem.** Suppose $\hat\Theta\psi = c\psi$. Then $\hat\Theta^2\psi = \hat\Theta(c\psi) = c^*\hat\Theta\psi = |c|^2\psi$, which contradicts $\hat\Theta^2 = -1$. So $\psi$ and $\hat\Theta\psi$ are distinct, and every level of a time-reversal-invariant Hamiltonian is at least doubly degenerate. The same holds for any odd number of spin-½ particles. (The book prints "Kramer's degeneracy"; the name is Kramers.)

!!! example "Random matrices"
    **Spin-½.** A random complex Hermitian $12\times12$ Hamiltonian for six orbitals with spin was symmetrized as $\tfrac12(H+\Theta H\Theta^{-1})$, with $\Theta = (\mathbb 1\otimes\begin{smallmatrix}0&-1\\1&0\end{smallmatrix})K$. Every eigenvalue is exactly paired:

    $$
    -7.490437\ (\times2),\ -5.345897\ (\times2),\ -2.019963\ (\times2),\ 0.502883\ (\times2),\ 2.773705\ (\times2),\ 4.990042\ (\times2).
    $$

    **Spinless.** A random real symmetric $6\times6$ matrix, also time-reversal invariant, has no pairing. There $\hat\Theta^2 = +1$, and the theorem does not apply.

    This is why odd-electron molecules without a magnetic field always have degenerate (Kramers) doublets, even when spin–orbit coupling is included.

## Source

Griffiths and Schroeter, *Introduction to Quantum Mechanics* (3rd ed., Cambridge University Press, 2018), Secs. 6.3, 6.6, 6.8.2 (energy conservation), Eqs. (6.15), (6.39), (6.82)–(6.84), Example 6.3, Figs. 6.9–6.11 (described); Problems 6.18, 6.33, 6.34, 6.36, 6.37. Page numbers are not given because the PDF used is an e-book rendering without print pagination. The square-well group analysis, the Runge–Lenz constants and the Kramers check are computed in `griffiths/ch06_symmetry.py` (sections E, G, I). The closed form for $|c_{n\ell}|$ is my solution of Problem 6.34 and is confirmed by the direct computation. The $D_4$ irrep labels, the separability explanation and the remark on odd-electron molecules are additions.
