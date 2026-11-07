---
id: spin-one-half
title: "Spin 1/2: spinors, Pauli matrices, measurements and magnetic fields"
summary: Intrinsic angular momentum obeys the same algebra as L but allows half-integer s. Spin 1/2 is a two-component spinor with S = (ħ/2)σ; covers the Pauli algebra σ_jσ_k = δ_jk + iε_jklσ_l, measurement of S_x and of S along an arbitrary axis, why the components are incompatible, spin 1 and general-s matrices, Larmor precession in a static field, a spin in an oscillating field, and the Stern–Gerlach experiment as state preparation and measurement.
status: in-progress
kind: theory
level: intermediate
tags: [spin, spin-one-half, pauli-matrices, spinor, stern-gerlach, larmor-precession, magnetic-moment, gyromagnetic-ratio, griffiths]
prerequisites: [orbital-angular-momentum, generalized-statistical-interpretation]
related: [addition-of-angular-momenta, spin-operators, position-momentum-and-energy-representations, generalized-uncertainty-principle]
order: 50
date: 2026-11-04
---

## Spin as intrinsic angular momentum

**What spin is.** Besides orbital $\mathbf L$, elementary particles carry an intrinsic angular momentum $\mathbf S$. It is not motion of parts: a classical spinning electron would need a surface speed far above $c$ (Problem 4.28).

**Algebra.** Only the commutation relations are postulated:

$$
[S_x,S_y] = i\hbar S_z\quad(\text{and cyclic}),\qquad
S^2|s\,m\rangle = \hbar^2s(s+1)|s\,m\rangle,\qquad S_z|s\,m\rangle = \hbar m|s\,m\rangle,
$$

$$
S_\pm|s\,m\rangle = \hbar\sqrt{s(s+1)-m(m\pm1)}\;|s\,(m\pm1)\rangle .
$$

The ladder argument of [[orbital-angular-momentum]] then allows $s = 0,\tfrac12,1,\tfrac32,\ldots$. Since the eigenvectors are not functions of angles, nothing excludes half-integers.

**$s$ is fixed per species.** Pions have $s=0$; electrons, protons, neutrons and quarks $\tfrac12$; photons 1; $\Delta$ baryons $\tfrac32$. By contrast, $\ell$ can change.

The second-quantized many-electron spin operators ($S^2$ of a determinant, $S_\pm$ on $\alpha/\beta$) are in [[spin-operators]].

## Spin 1/2

**State.** A general state is a normalized two-component **spinor**:

$$
\chi = \begin{pmatrix}a\\b\end{pmatrix} = a\chi_+ + b\chi_-,\qquad |a|^2+|b|^2 = 1 .
$$

**Matrices.** From the action on $\chi_\pm$:

$$
\mathsf S = \frac\hbar2\boldsymbol\sigma,\qquad
\sigma_x = \begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
\sigma_y = \begin{pmatrix}0&-i\\i&0\end{pmatrix},\quad
\sigma_z = \begin{pmatrix}1&0\\0&-1\end{pmatrix},\qquad
\mathsf S^2 = \frac34\hbar^2\mathbf 1 .
$$

$\mathsf S_+ = \hbar\begin{pmatrix}0&1\\0&0\end{pmatrix}$ and $\mathsf S_- = \hbar\begin{pmatrix}0&0\\1&0\end{pmatrix}$ are not Hermitian, so they are not observables.

**Pauli algebra** (Problem 4.29, checked numerically):

$$
\sigma_j\sigma_k = \delta_{jk}\mathbf 1 + i\sum_l\epsilon_{jkl}\sigma_l .
$$

Hence $\sigma_j^2 = \mathbf 1$, $\{\sigma_j,\sigma_k\} = 2\delta_{jk}$ and $[\sigma_j,\sigma_k] = 2i\epsilon_{jkl}\sigma_l$.

**Measuring $S_x$.** The eigenvalues of $\mathsf S_x$ are $\pm\hbar/2$, with eigenspinors $\chi_\pm^{(x)} = (1,\pm1)^{\rm T}/\sqrt2$. Expanding

$$
\chi = \frac{a+b}{\sqrt2}\chi_+^{(x)} + \frac{a-b}{\sqrt2}\chi_-^{(x)}
$$

gives $P(+\hbar/2) = \tfrac12|a+b|^2$.

**Arbitrary axis** $\hat r = (\sin\theta\cos\phi, \sin\theta\sin\phi, \cos\theta)$ (Problem 4.33). With $\mathsf S_r = \hat r\cdot\mathsf S$:

$$
\chi_+^{(r)} = \begin{pmatrix}\cos(\theta/2)\\ e^{i\phi}\sin(\theta/2)\end{pmatrix},\qquad
\chi_-^{(r)} = \begin{pmatrix}e^{-i\phi}\sin(\theta/2)\\ -\cos(\theta/2)\end{pmatrix},
$$

with eigenvalues $\pm\hbar/2$. Every spinor is "spin up" along some axis, which is the Bloch-sphere picture of a qubit.

## Measurement examples

!!! example "Griffiths Example 4.2"
    $\chi = \frac{1}{\sqrt6}\begin{pmatrix}1+i\\2\end{pmatrix}$.

    | Measurement | Outcome | Probability |
    |---|---|---|
    | $S_z$ | $+\hbar/2$ | $1/3$ |
    | $S_z$ | $-\hbar/2$ | $2/3$ |
    | $S_x$ | $+\hbar/2$ | $\tfrac12|3+i|^2/6 = 5/6$ |
    | $S_x$ | $-\hbar/2$ | $1/6$ |

    Hence $\langle S_x\rangle = \hbar/3$, which equals $\chi^\dagger\mathsf S_x\chi$.

!!! example "Problem 4.30: $\chi = A\begin{pmatrix}3i\\4\end{pmatrix}$"
    **Normalization and expectation values.** $A = 1/5$:

    $$
    \langle S_x\rangle = 0,\qquad \langle S_y\rangle = -\tfrac{12}{25}\hbar,\qquad \langle S_z\rangle = -\tfrac{7}{50}\hbar .
    $$

    **Spreads.** $\sigma_{S_x} = \tfrac12\hbar$, $\sigma_{S_y} = \tfrac{7}{50}\hbar$, $\sigma_{S_z} = \tfrac{12}{25}\hbar$.

    **Uncertainty.** $\sigma_{S_x}\sigma_{S_y} = 0.0700\,\hbar^2 = \tfrac\hbar2|\langle S_z\rangle|$: the $S_x$–$S_y$ uncertainty relation is saturated here. For a pure spin-½ state the stronger Schrödinger–Robertson form is always an equality ([[generalized-uncertainty-principle]]).

**Incompatibility in practice.** A particle in $\chi_+$ has a definite $S_z$ but no definite $S_x$. Measuring $S_x$ and getting $+\hbar/2$ leaves it in $\chi_+^{(x)}$. A subsequent $S_z$ measurement is then 50/50: the first measurement's information is gone. Griffiths uses this as the cleanest setting for the conceptual puzzles of measurement.

## Higher spins (Problems 4.34, 4.62)

**Matrix elements.** For spin $s$, in the basis $m = s,\ldots,-s$:

$$
(\mathsf S_z)_{mm'} = \hbar m\,\delta_{mm'},\qquad
(\mathsf S_\pm)_{m'm} = \hbar\sqrt{s(s+1)-m(m\pm1)}\;\delta_{m',m\pm1}.
$$

$\mathsf S_x$ and $\mathsf S_y$ follow from $\mathsf S_\pm$.

**Spin 1:**

$$
\mathsf S_x = \frac{\hbar}{\sqrt2}\begin{pmatrix}0&1&0\\1&0&1\\0&1&0\end{pmatrix},\quad
\mathsf S_y = \frac{\hbar}{\sqrt2}\begin{pmatrix}0&-i&0\\i&0&-i\\0&i&0\end{pmatrix},\quad
\mathsf S_z = \hbar\begin{pmatrix}1&0&0\\0&0&0\\0&0&-1\end{pmatrix}.
$$

**Check.** The construction satisfies the commutation relations with $S^2 = s(s+1)\hbar^2\mathbf 1$ for $s = \tfrac12$ to 3.

## Spin in a magnetic field

**Hamiltonian.** A spinning charge has magnetic moment $\boldsymbol\mu = \gamma\mathbf S$, where $\gamma$ is the gyromagnetic ratio. Its energy in a field is $H = -\boldsymbol\mu\cdot\mathbf B$, so for a particle at rest

$$
\mathsf H = -\gamma\,\mathbf B\cdot\mathsf S .
$$

**Larmor precession** (Example 4.3). Take $\mathbf B = B_0\hat k$, so $\mathsf H = -\gamma B_0\mathsf S_z$ with $E_\pm = \mp\gamma B_0\hbar/2$; the moment parallel to the field is lower in energy. Starting from $\chi(0) = (\cos\tfrac\alpha2,\sin\tfrac\alpha2)^{\rm T}$:

$$
\langle\mathbf S\rangle(t) = \frac\hbar2\left(\sin\alpha\cos\gamma B_0t,\ -\sin\alpha\sin\gamma B_0t,\ \cos\alpha\right).
$$

$\langle\mathbf S\rangle$ keeps its angle $\alpha$ to $\mathbf B$ and precesses at the **Larmor frequency** $\omega = \gamma B_0$, as classically: this is Ehrenfest's theorem for torques. Matrix-exponential propagation reproduces the formula to $10^{-6}$ (printed precision) at $t = 0$, 1 and 2.5.

**Oscillating field** (Problem 4.36). For $\mathbf B = B_0\cos(\omega t)\,\hat k$, $\mathsf H(t)$ commutes with itself at different times, so

$$
\chi(t) = \exp\!\left[\frac{i\gamma B_0}{2\omega}\sin(\omega t)\,\sigma_z\right]\chi(0).
$$

Starting in $\chi_+^{(x)}$:

$$
P\big(S_x = -\tfrac\hbar2\big) = \sin^2\!\left(\frac{\gamma B_0}{2\omega}\sin\omega t\right).
$$

Direct integration of the Schrödinger equation agrees to $10^{-8}$. A complete flip requires $\gamma B_0/2\omega\ge\pi/2$, i.e. $B_0\ge\pi\omega/\gamma$.

**Stern–Gerlach** (Example 4.4). An inhomogeneous field $\mathbf B = -\alpha x\,\hat\imath + (B_0+\alpha z)\,\hat k$ exerts a force $\mathbf F = \nabla(\boldsymbol\mu\cdot\mathbf B)$. The $x$ component averages out under fast Larmor precession about $B_0\hat k$, leaving $F_z = \gamma\alpha S_z$. A beam therefore splits into $2s+1$ discrete streams: two for silver atoms, whose net spin is that of the single outer electron. This is the prototype of both **state preparation** (select one stream) and **measurement** (record which stream).

## Source

Griffiths and Schroeter, *Introduction to Quantum Mechanics* (3rd ed., Cambridge University Press, 2018), Secs. 4.4.1-4.4.2, Eqs. (4.134)-(4.170), Examples 4.2-4.4, Figs. 4.14-4.15 (described); Problems 4.28-4.36, 4.62. Page numbers are not given because the PDF used is an e-book rendering without print pagination. Problem answers and the Bloch-sphere and qubit remark are worked or added here, and the numerical checks are in `griffiths/ch04_3d.py` (section E).
