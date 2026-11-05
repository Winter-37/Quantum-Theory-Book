---
id: generalized-uncertainty-principle
title: The generalized uncertainty principle and the minimum-uncertainty wave packet
summary: Proof of the Robertson inequality σ_A²σ_B² ≥ (⟨[A,B]⟩/2i)² from the Schwarz inequality, Heisenberg's σxσp ≥ ħ/2 as a special case, compatible versus incompatible observables, the stronger Schrödinger–Robertson form with the anticommutator term, and the derivation that the minimum-uncertainty states are exactly the gaussians. Includes commutator identities and random-matrix checks of both inequalities.
status: in-progress
kind: derivation
level: intermediate
tags: [uncertainty-principle, robertson, schrodinger-robertson, commutator, compatible-observables, minimum-uncertainty, gaussian, schwarz-inequality, griffiths]
prerequisites: [hilbert-space-and-hermitian-operators, generalized-statistical-interpretation]
related: [de-broglie-and-heisenberg-uncertainty, energy-time-uncertainty-principle, harmonic-oscillator-coherent-states, baker-campbell-hausdorff]
also: []
date: 2026-11-04
---

## Proof

**Setup.** For observables $A$ and $B$ in state $\Psi$, define

$$
f \equiv (\hat A-\langle A\rangle)\Psi,\qquad g \equiv (\hat B-\langle B\rangle)\Psi .
$$

By hermiticity, $\sigma_A^2 = \langle f|f\rangle$ and $\sigma_B^2 = \langle g|g\rangle$.

**Step 1: Schwarz.**

$$
\sigma_A^2\sigma_B^2 = \langle f|f\rangle\langle g|g\rangle \ge |\langle f|g\rangle|^2 .
$$

**Step 2: keep only the imaginary part.** For any complex $z$, $|z|^2 = (\mathrm{Re}\,z)^2+(\mathrm{Im}\,z)^2 \ge (\mathrm{Im}\,z)^2 = \left[\tfrac{1}{2i}(z-z^*)\right]^2$. With $z = \langle f|g\rangle$:

$$
\sigma_A^2\sigma_B^2 \ge \left(\frac{1}{2i}\left[\langle f|g\rangle-\langle g|f\rangle\right]\right)^2 .
$$

**Step 3: evaluate.** Expanding with hermiticity and treating $\langle A\rangle$, $\langle B\rangle$ as numbers gives $\langle f|g\rangle = \langle\hat A\hat B\rangle - \langle A\rangle\langle B\rangle$ and $\langle g|f\rangle = \langle\hat B\hat A\rangle - \langle A\rangle\langle B\rangle$. Their difference is $\langle[\hat A,\hat B]\rangle$:

$$
\boxed{\ \sigma_A^2\sigma_B^2 \ge \left(\frac{1}{2i}\langle[\hat A,\hat B]\rangle\right)^2\ }
$$

**The right side is non-negative.** $[\hat A,\hat B]$ is anti-Hermitian, so its expectation value is purely imaginary and the quantity in parentheses is real.

**Heisenberg as a special case.** With $[x,\hat p]=i\hbar$, $\sigma_x\sigma_p\ge\hbar/2$. This is the result stated in [[de-broglie-and-heisenberg-uncertainty]], now proved.

## Compatible and incompatible observables

**Incompatible** observables have non-commuting operators, and the principle applies to every such pair. They cannot share a complete set of eigenfunctions (Problem 3.16): a complete common set would give $[\hat A,\hat B]f=0$ for every $f$ in the space.

**Compatible** observables commute and do admit a complete set of simultaneous eigenfunctions. Examples are $\hat H$, $\hat L^2$ and $\hat L_z$ for hydrogen. The matrix analogue is that commuting Hermitian matrices are simultaneously diagonalizable.

**How the laboratory enforces it.** A sharp position measurement collapses $\Psi$ to a spike, which contains a broad range of momenta. A subsequent momentum measurement then collapses it to a long sinusoid, erasing the position information. Only a common eigenstate would survive both collapses unchanged. Griffiths (footnote 21) notes that Bohr and Heisenberg's disturbance accounts have been questioned in recent work.

## The stronger Schrödinger–Robertson form (Griffiths Problem 3.43)

Step 2 discarded $(\mathrm{Re}\,z)^2$. Keeping it, and defining

$$
\hat C = -i[\hat A,\hat B],\qquad \hat D = \hat A\hat B+\hat B\hat A - 2\langle A\rangle\langle B\rangle,
$$

gives

$$
\sigma_A^2\sigma_B^2 \ge \tfrac14\left(\langle C\rangle^2 + \langle D\rangle^2\right).
$$

$\hat D$ measures the correlation between $A$ and $B$. For a two-level system the inequality is an equality for every pure state.

!!! example "Random-matrix check"
    **Robertson.** Over 20000 random $4\times4$ Hermitian pairs $(\hat A,\hat B)$ and random states:

    - $\min[\sigma_A^2\sigma_B^2 - \tfrac14\langle C\rangle^2] = 0.0211 \ge 0$;
    - $\min[\sigma_A^2\sigma_B^2 - \tfrac14(\langle C\rangle^2+\langle D\rangle^2)] = 0.0059 \ge 0$.

    **Spin-1/2, $\hat S_x$ and $\hat S_y$.** Over 2000 random states the Schrödinger–Robertson bound holds with equality to $5\times10^{-17}$.

## Minimum-uncertainty states

**Conditions for equality.** Equality needs equality at both inequality steps.

- **Schwarz** is an equality iff $g = cf$ for some complex $c$.
- **Dropping $\mathrm{Re}\,z$** is free iff $\mathrm{Re}\langle f|g\rangle = \mathrm{Re}(c\langle f|f\rangle) = 0$. Since $\langle f|f\rangle$ is real, $c = ia$ with $a$ real.

**Position–momentum case.** The condition $g = iaf$ reads

$$
\left(-i\hbar\frac{d}{dx} - \langle p\rangle\right)\Psi = ia\left(x-\langle x\rangle\right)\Psi,
$$

whose solution (Problem 3.17) is

$$
\Psi(x) = A\,e^{-a(x-\langle x\rangle)^2/2\hbar}\,e^{i\langle p\rangle x/\hbar}.
$$

**Result.** The minimum-uncertainty states are exactly the Gaussians, at any centre, with any mean momentum and any width ($a>0$ for normalizability). This explains why the oscillator ground state and the free Gaussian packet at $t=0$ both hit $\hbar/2$. The statement is instantaneous: the Gaussian packet saturates the bound only at $t=0$ and spreads afterwards (footnote 22).

**Grid check** ($\hbar=1$): three Gaussians with different $(a,\langle x\rangle,\langle p\rangle)$ give $\sigma_x\sigma_p = 0.49999$, $0.49999$ and $0.49993$.

## Useful commutator identities (Griffiths Problems 3.14, 3.29)

$$
[\hat A+\hat B,\hat C] = [\hat A,\hat C]+[\hat B,\hat C],\qquad
[\hat A\hat B,\hat C] = \hat A[\hat B,\hat C]+[\hat A,\hat C]\hat B,
$$

$$
[x^n,\hat p] = i\hbar nx^{n-1},\qquad [f(x),\hat p] = i\hbar f'(x),\qquad [\hat H,\hat a_\pm] = \pm\hbar\omega\,\hat a_\pm .
$$

If $\hat C = [\hat A,\hat B]$ commutes with both $\hat A$ and $\hat B$:

$$
[\hat A^n,\hat B] = n\hat A^{n-1}\hat C,\qquad e^{\hat A+\hat B} = e^{\hat A}e^{\hat B}e^{-\hat C/2}.
$$

The second is the special case of [[baker-campbell-hausdorff]] that holds for $x$ and $\hat p$. It is checked here with $3\times3$ Heisenberg-algebra matrices: error $6\times10^{-17}$.

**Problem 3.15.** With $A = x$ and $B = H$, $[x,\hat H] = i\hbar\hat p/m$ gives

$$
\sigma_x\sigma_H\ge\frac{\hbar}{2m}|\langle p\rangle| .
$$

The bound is empty for stationary states, where $\langle p\rangle = 0$. For a displaced, boosted Gaussian in an oscillator: $0.64996\ge0.59999$.

## Source

Griffiths and Schroeter, *Introduction to Quantum Mechanics* (3rd ed., Cambridge University Press, 2018), Secs. 3.5.1-3.5.2, Eqs. (3.59)-(3.70), (3.115); Problems 3.14-3.17, 3.29, 3.43; footnotes 19-22. Page numbers are not given because the PDF used is an e-book rendering without print pagination. The random-matrix and grid checks are computations for this note, in `griffiths/ch03_formalism.py` (sections C and E).
