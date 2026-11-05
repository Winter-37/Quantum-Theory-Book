---
id: parity-and-parity-selection-rules
title: Parity, inversion symmetry and Laporte's rule
summary: The parity operator Π̂ψ(r) = ψ(−r) is Hermitian, unitary and its own inverse, with eigenvalues ±1. It flips r̂ and p̂, leaves L̂ and Ŝ alone, and so sorts operators into true vectors, pseudovectors, true scalars and pseudoscalars. If [Ĥ, Π̂] = 0, parity is conserved and stationary states can be chosen even or odd; central-potential states have parity (−1)^ℓ. Sandwiching Π̂ around an odd operator gives Laporte's rule. Checked on hydrogen: ⟨200|z|210⟩ = −3a, same-parity dipole elements vanish.
status: in-progress
kind: theory
level: intermediate
tags: [parity, inversion, laporte-rule, selection-rules, pseudovector, pseudoscalar, dipole-moment, hydrogen, griffiths]
prerequisites: [translation-operator-and-translational-symmetry, central-potentials-and-spherical-harmonics]
related: [rotation-operator-and-rotational-symmetry, rotational-selection-rules-and-wigner-eckart, symmetry-conservation-and-degeneracy, hydrogen-atom, exact-wave-function-properties-and-symmetry]
also: []
date: 2026-11-05
---

## The parity operator

**Definition.** In one dimension $\hat\Pi\psi(x) = \psi(-x)$; in three, $\hat\Pi\psi(\mathbf r) = \psi(-\mathbf r)$. Applying it twice is the identity, and $\langle f|\hat\Pi g\rangle = \int f^*(\mathbf r)g(-\mathbf r)\,d^3r = \langle\hat\Pi f|g\rangle$ (substitute $\mathbf r\to-\mathbf r$). Hence

$$
\hat\Pi^{-1} = \hat\Pi = \hat\Pi^\dagger .
$$

**Eigenvalues.** From $\hat\Pi^2 = 1$, any eigenvalue $\lambda$ satisfies $\lambda^2 = 1$, so $\lambda = \pm1$: even and odd functions.

**Geometry.** In 3D, inversion equals a mirror reflection through a plane followed by a rotation by $\pi$ about the normal to that plane (Problem 6.1a). In spherical coordinates $\mathbf r\to-\mathbf r$ is $(r,\theta,\phi)\to(r,\pi-\theta,\phi+\pi)$. In 2D, $(x,y)\to(-x,-y)$ is just a rotation by $\pi$, so "parity" is reserved for 1D and 3D.

## How operators transform

**Rule.** As for any unitary transformation ([[translation-operator-and-translational-symmetry]]), the transformed operator is $\hat Q' = \hat\Pi^\dagger\hat Q\hat\Pi$. Acting on a test function, $\hat\Pi^\dagger\hat x\hat\Pi f(x) = \hat\Pi[x f(-x)] = -x f(x)$, and similarly for $\hat p = -i\hbar\,d/dx$ because the chain rule supplies a sign. So

$$
\hat\Pi^\dagger\hat{\mathbf r}\hat\Pi = -\hat{\mathbf r},\qquad
\hat\Pi^\dagger\hat{\mathbf p}\hat\Pi = -\hat{\mathbf p},\qquad
\hat\Pi^\dagger\hat Q(\hat{\mathbf r},\hat{\mathbf p})\hat\Pi = \hat Q(-\hat{\mathbf r},-\hat{\mathbf p}).
$$

**Angular momentum is even.** $\hat{\mathbf L}' = (-\hat{\mathbf r})\times(-\hat{\mathbf p}) = \hat{\mathbf L}$ (Example 6.2). Spin is taken to behave the same way, $[\hat\Pi,\hat{\mathbf S}] = 0$. On a two-component spinor $\hat\Pi$ then commutes with all three Pauli matrices, so it is a multiple of the identity on spin space, and the conventional choice is $+1$: parity does not touch the spin part (Problem 6.12).

**Classification.** Combining the behaviour under parity with that under rotations ([[rotation-operator-and-rotational-symmetry]]):

| Type | Under parity | Under rotations | Examples |
|---|---|---|---|
| true vector | $\{\hat\Pi,\hat V_i\} = 0$ | $[\hat L_i,\hat V_j] = i\hbar\epsilon_{ijk}\hat V_k$ | $\hat{\mathbf r}$, $\hat{\mathbf p}$ |
| pseudovector | $[\hat\Pi,\hat V_i] = 0$ | $[\hat L_i,\hat V_j] = i\hbar\epsilon_{ijk}\hat V_k$ | $\hat{\mathbf L}$, $\hat{\mathbf S}$ |
| true scalar | $[\hat\Pi,\hat f] = 0$ | $[\hat L_i,\hat f] = 0$ | $\hat{\mathbf r}\cdot\hat{\mathbf r}$ |
| pseudoscalar | $\{\hat\Pi,\hat f\} = 0$ | $[\hat L_i,\hat f] = 0$ | $\hat{\mathbf p}\cdot\hat{\mathbf S}$ |

The anticommutator rows follow from $\hat\Pi^\dagger\hat V\hat\Pi = -\hat V$ by multiplying on the left by $\hat\Pi$ (Problem 6.9). With spin present, replace $\hat L_i$ by $\hat J_i = \hat L_i+\hat S_i$.

## Inversion symmetry and conservation

**Invariance.** $\hat H$ has inversion symmetry if $\hat\Pi^\dagger\hat H\hat\Pi = \hat H$, equivalently $[\hat H,\hat\Pi] = 0$. For $\hat H = \hat p^2/2m + V(\mathbf r)$ this means $V(-\mathbf r) = V(\mathbf r)$; every central potential qualifies.

**Consequences.**

- $\hat H$ and $\hat\Pi$ have a common eigenbasis, so the stationary states can be chosen even or odd (in a degenerate level, *chosen*; a single eigenfunction need not have definite parity).
- $\hat\Pi$ has no explicit time dependence, so $d\langle\hat\Pi\rangle/dt = (i/\hbar)\langle[\hat H,\hat\Pi]\rangle = 0$; by [[symmetry-conservation-and-degeneracy]] the probabilities of the outcomes $\pm1$ are constant too. An even initial state of the oscillator stays even forever (Griffiths Fig. 6.7, a $\xi^2e^{-\xi^2/2}$ packet).

**Central potentials.** With $\psi_{n\ell m} = R_{n\ell}(r)Y_\ell^m(\theta,\phi)$, only the angular factor feels the inversion, and

$$
Y_\ell^m(\pi-\theta,\phi+\pi) = (-1)^\ell\,Y_\ell^m(\theta,\phi)
\quad\Longrightarrow\quad
\hat\Pi\psi_{n\ell m} = (-1)^\ell\psi_{n\ell m}.
$$

The factor $(-1)^\ell$ comes from $e^{im\pi} = (-1)^m$ times the $(-1)^{\ell+m}$ of the associated Legendre function under $\cos\theta\to-\cos\theta$. The identity was checked numerically for all $|m|\le\ell\le3$ at random angles, using SciPy's Condon–Shortley harmonics ([[central-potentials-and-spherical-harmonics]]).

## Parity selection rules

**Derivation.** Let $\hat O$ be odd, $\hat\Pi^\dagger\hat O\hat\Pi = -\hat O$, and let $|a\rangle$, $|b\rangle$ have parities $\pi_a$, $\pi_b$. Then

$$
\langle b|\hat O|a\rangle = -\langle b|\hat\Pi^\dagger\hat O\hat\Pi|a\rangle = -\pi_b\pi_a\langle b|\hat O|a\rangle
\quad\Longrightarrow\quad
\langle b|\hat O|a\rangle = 0\ \text{ unless }\ \pi_a\pi_b = -1 .
$$

(Parities are real, so $\langle b|\hat\Pi^\dagger = \pi_b\langle b|$.)

**Laporte's rule.** The electric dipole operator $\hat{\mathbf p}_e = q\hat{\mathbf r}$ is odd. Between central-potential states,

$$
\langle n'\ell'm'|\hat{\mathbf p}_e|n\ell m\rangle = 0\quad\text{if } \ell+\ell' \text{ is even.}
$$

Electric-dipole transitions connect states of opposite parity only. For an even operator (any pseudovector such as $\hat{\mathbf L}$, or any true scalar) the rule reverses: matrix elements vanish unless $\ell+\ell'$ is even (Problem 6.11). Rotational selection rules then sharpen these ([[rotational-selection-rules-and-wigner-eckart]]).

**Permanent dipoles.** A nondegenerate state of definite parity has $\langle\hat{\mathbf p}_e\rangle = 0$ (take $a = b$). The hydrogen ground state therefore has no dipole moment, with no calculation needed (Problem 6.13a). A *degenerate* level can mix parities, and then a dipole is allowed.

!!! example "Hydrogen n = 2: a state with a dipole moment (Problems 6.13, 6.25)"
    **Laporte checks** (exact symbolic integrals with SymPy's hydrogen functions, $a$ = Bohr radius):

    - $\langle200|z|200\rangle = \langle210|z|210\rangle = \langle211|z|211\rangle = 0$;
    - all twelve $\langle21m'|r_i|21m\rangle$ with $m,m'\in\{1,0\}$ and $r_i = x,y,z$ vanish.

    **Mixed parity.** The one surviving element within $n=2$ needed here is

    $$
    \langle200|z|210\rangle = -3a .
    $$

    For $\psi = (\psi_{200}+\psi_{210})/\sqrt2$, the diagonal terms vanish by Laporte and the $x,y$ cross terms vanish by $\Delta m$ rules, so $\langle z\rangle = \mathrm{Re}\langle200|z|210\rangle = -3a$. With electron charge $q = -e$:

    $$
    \langle\hat{\mathbf p}_e\rangle = -e\langle\hat{\mathbf r}\rangle = +3ea\,\hat{\mathbf z}.
    $$

    This is the origin of the linear Stark effect in hydrogen (degenerate 2s–2p mixing).

    **Problem 6.25.** For $(\psi_{211}+\psi_{210})/\sqrt2$, both components have $\ell = 1$, so every term is a same-parity dipole element and $\langle\hat{\mathbf p}_e\rangle = 0$ exactly.

## Source

Griffiths and Schroeter, *Introduction to Quantum Mechanics* (3rd ed., Cambridge University Press, 2018), Sec. 6.4 (6.4.1–6.4.3), Eqs. (6.16)–(6.27), Example 6.2, Table 6.1 (classification table, reproduced in content), Fig. 6.7 (described); Problems 6.1, 6.8–6.13, 6.25. Page numbers are not given because the PDF used is an e-book rendering without print pagination. The $Y_\ell^m$ parity check and the hydrogen matrix elements are computed in `griffiths/ch06_symmetry.py` (section C). The Stark-effect remark is an addition.
