---
id: orbital-angular-momentum
title: Orbital angular momentum; eigenvalues by ladder operators
summary: Commutation relations [L_x, L_y] = iħL_z and cyclic, with [L², L] = 0. The ladder operators L± give the spectrum L² = ħ²ℓ(ℓ+1), L_z = ħm, with ℓ integer or half-integer, plus the normalization factors ħ√((ℓ∓m)(ℓ±m+1)). In spherical coordinates L_z = −iħ∂/∂φ and L² is (minus ħ² times) the angular Laplacian, so its eigenfunctions are the spherical harmonics; orbital ℓ must be an integer. Includes the vector-model caveat, conservation for central forces, and the rigid rotor applied to CO.
status: in-progress
kind: derivation
level: intermediate
tags: [angular-momentum, commutation-relations, ladder-operators, spherical-harmonics, rigid-rotor, rotational-spectroscopy, conservation, griffiths]
prerequisites: [generalized-uncertainty-principle, central-potentials-and-spherical-harmonics, harmonic-oscillator-ladder-operators]
related: [spin-one-half, addition-of-angular-momenta, hydrogen-atom, spin-operators, energy-time-uncertainty-principle]
also: []
date: 2026-11-04
---

## Commutation relations

**Definition.** Classically $\mathbf L = \mathbf r\times\mathbf p$, so

$$
L_x = yp_z - zp_y,\qquad L_y = zp_x - xp_z,\qquad L_z = xp_y - yp_x .
$$

**Computing $[L_x,L_y]$.** Using $[r_i,p_j] = i\hbar\delta_{ij}$, only the pairs $(y,p_y)$ and $(x,p_x)$ fail to commute:

$$
[L_x,L_y] = yp_x[p_z,z] + xp_y[z,p_z] = i\hbar(xp_y - yp_x) = i\hbar L_z .
$$

Cyclic permutation gives the full set:

$$
[L_x,L_y] = i\hbar L_z,\qquad [L_y,L_z] = i\hbar L_x,\qquad [L_z,L_x] = i\hbar L_y .
$$

**Consequences.**

- The components are incompatible: $\sigma_{L_x}\sigma_{L_y}\ge\frac\hbar2|\langle L_z\rangle|$ ([[generalized-uncertainty-principle]]).
- $L^2 = L_x^2+L_y^2+L_z^2$ commutes with each component, $[L^2,\mathbf L] = 0$, so $L^2$ and one component (conventionally $L_z$) have simultaneous eigenstates.

## Eigenvalues from the algebra alone

**Ladder operators.** Define $L_\pm = L_x\pm iL_y$. Then

$$
[L_z,L_\pm] = \pm\hbar L_\pm,\qquad [L^2,L_\pm] = 0 .
$$

**Raising and lowering.** If $L^2f = \lambda f$ and $L_zf = \mu f$, then $L_\pm f$ has the same $\lambda$ and $L_z$ eigenvalue $\mu\pm\hbar$.

**The ladder has a top and a bottom.** $\langle L_z^2\rangle$ cannot exceed $\langle L^2\rangle$, so there is a top state $f_t$ with $L_+f_t = 0$ and a bottom state $f_b$ with $L_-f_b = 0$. Use

$$
L_\pm L_\mp = L^2 - L_z^2 \pm \hbar L_z .
$$

Write $L_zf_t = \hbar\ell f_t$ at the top and $L_zf_b = \hbar\bar\ell f_b$ at the bottom.

- At the top: $\lambda = \hbar^2\ell(\ell+1)$.
- At the bottom: $\lambda = \hbar^2\bar\ell(\bar\ell-1)$.

These agree only for $\bar\ell = -\ell$. The ladder steps by 1 from $-\ell$ to $\ell$, so $2\ell$ is an integer:

$$
L^2f_\ell^m = \hbar^2\ell(\ell+1)f_\ell^m,\qquad L_zf_\ell^m = \hbar mf_\ell^m,\qquad
\ell = 0,\tfrac12,1,\tfrac32,\ldots,\quad m = -\ell,\ldots,\ell .
$$

**Normalization factors** (Problem 4.21), using $L_\mp = L_\pm^\dagger$:

$$
L_\pm f_\ell^m = \hbar\sqrt{\ell(\ell+1)-m(m\pm1)}\;f_\ell^{m\pm1} = \hbar\sqrt{(\ell\mp m)(\ell\pm m+1)}\;f_\ell^{m\pm1}.
$$

**Check.** Matrices built from these factors satisfy $[J_x,J_y] = iJ_z$ to $2\times10^{-15}$, with $J^2 = j(j+1)\mathbf 1$, for $j = \tfrac12,1,\tfrac32,2,\tfrac52,3$. The same algebra serves spin ([[spin-one-half]]).

**The vector-model caveat.** $\sqrt{\ell(\ell+1)}>\ell$ for $\ell>0$, so $\mathbf L$ can never point along $z$. $L_x$ and $L_y$ are not merely unknown; they have no definite values when $L_z$ does. Pictures of vectors on cones are mnemonics only.

## Eigenfunctions: back to spherical harmonics

**Operators in spherical coordinates.** With $\mathbf L = -i\hbar\,\mathbf r\times\nabla$:

$$
L_z = -i\hbar\frac{\partial}{\partial\phi},\qquad
L_\pm = \pm\hbar e^{\pm i\phi}\left(\frac{\partial}{\partial\theta}\pm i\cot\theta\frac{\partial}{\partial\phi}\right),
$$

$$
L^2 = -\hbar^2\left[\frac{1}{\sin\theta}\frac{\partial}{\partial\theta}\left(\sin\theta\frac{\partial}{\partial\theta}\right)+\frac{1}{\sin^2\theta}\frac{\partial^2}{\partial\phi^2}\right].
$$

**Spherical harmonics.** The eigenvalue equation for $L^2$ *is* the angular equation of [[central-potentials-and-spherical-harmonics]], so $f_\ell^m = Y_\ell^m$. Orthogonality of the $Y_\ell^m$ then follows from hermiticity of $L^2$ and $L_z$ (distinct eigenvalues).

**Checks.**

- With Griffiths's phases, the differential $L_\pm$ satisfies $L_\pm Y_\ell^m = \hbar\sqrt{(\ell\mp m)(\ell\pm m+1)}\,Y_\ell^{m\pm1}$ exactly, for all $\ell\le3$.
- $L^2Y_\ell^m = \hbar^2\ell(\ell+1)Y_\ell^m$ (SymPy, numerical residual below $10^{-12}$).
- Example (Problem 4.26): $L_+Y_2^1 = 2\hbar Y_2^2$, with $Y_2^2 = \sqrt{15/32\pi}\,\sin^2\theta\,e^{2i\phi}$.

**Kinetic energy split.** The TISE becomes

$$
\frac{1}{2mr^2}\left[-\hbar^2\frac{\partial}{\partial r}\left(r^2\frac{\partial}{\partial r}\right)+L^2\right]\psi + V\psi = E\psi .
$$

For a central potential, $H$, $L^2$ and $L_z$ are mutually compatible (Problem 4.22). Hence the labels $(n,\ell,m)$.

**Half-integers.** The algebra allows half-integer $\ell$, but separation of variables does not. Single-valuedness in $\phi$ forces integer $m$, so *orbital* angular momentum is always integral. The half-integer representations are realized by spin.

## Conservation (Problem 4.23)

**Torque law.** $\frac{d}{dt}\langle\mathbf L\rangle = \langle\mathbf N\rangle$ with $\mathbf N = \mathbf r\times(-\nabla V)$.

**Central potentials.** For a central potential the torque vanishes and $\langle\mathbf L\rangle$ is conserved. This is the generalized Ehrenfest theorem with $[H,\mathbf L] = 0$ ([[energy-time-uncertainty-principle]]).

**Useful commutators.**

$$
[L_z,x] = i\hbar y,\quad [L_z,y] = -i\hbar x,\quad [L_z,z] = 0,\quad
[L_z,p_x] = i\hbar p_y,\quad [L_z,p_y] = -i\hbar p_x,\quad [L_z,r^2] = [L_z,p^2] = 0 .
$$

## Rigid rotor (Problem 4.27)

**Energies.** For a diatomic with fixed bond length $r_e$, moment of inertia $I = \mu r_e^2$, the energy is $L^2/2I$:

$$
E_\ell = \frac{\hbar^2}{2I}\ell(\ell+1),\qquad \psi = Y_\ell^m(\theta,\phi),\qquad\text{degeneracy }2\ell+1 .
$$

**Spectrum.** Transitions $\ell\to\ell-1$ give lines at $\nu = \hbar\ell/2\pi I$: equally spaced by $\Delta\nu = \hbar/2\pi I = 2B$ (in frequency units).

!!! example "Carbon monoxide"
    Masses ¹²C = 12.000000 u and ¹⁶O = 15.994915 u give $\mu = 6.8562$ u. With $r_e = 1.1283$ Å:

    $$
    \Delta\nu = \frac{\hbar}{2\pi I} = 115.80\ \text{GHz} = 3.8627\ \text{cm}^{-1},\qquad B = 1.9314\ \text{cm}^{-1}.
    $$

    **Inverse.** Reading a spacing of about 3.86 cm⁻¹ off a CO far-infrared spectrum, as Griffiths asks with his Fig. 4.13, gives $r = 1.129$ Å. This is how bond lengths come out of microwave spectroscopy. The value 3.86 cm⁻¹ is my approximate reading and the input to the inverse step, not a quoted datum.

## Source

Griffiths and Schroeter, *Introduction to Quantum Mechanics* (3rd ed., Cambridge University Press, 2018), Sec. 4.3, Eqs. (4.95)-(4.133), Figs. 4.11-4.13 (described); Problems 4.21-4.27. Page numbers are not given because the PDF used is an e-book rendering without print pagination. The CO numbers use the atomic masses above and the experimental $r_e$ (standard value, not from Griffiths). All checks are in `griffiths/ch04_3d.py` (section D).
