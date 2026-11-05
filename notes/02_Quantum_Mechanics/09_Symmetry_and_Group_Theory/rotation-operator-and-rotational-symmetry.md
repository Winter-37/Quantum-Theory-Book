---
id: rotation-operator-and-rotational-symmetry
title: The rotation operator, vector operators and angular-momentum conservation
summary: R̂_n(φ) = exp(−iφ n·L̂/ħ), so angular momentum generates rotations. Infinitesimal rotations explain why the transformed position operator looks like 1 − δ times a generator; compounding N small rotations recovers the finite rotation matrix. A vector operator is defined by [L̂_i, V̂_j] = iħε_ijk V̂_k, a scalar by [L̂_i, f̂] = 0. Central potentials conserve L, and H, L², L_z form a complete set. All ladder commutators (6.50)–(6.54) and Problem 6.19 are checked symbolically; the Wigner d-matrix and spin-½ rotations (sign flip at 2π) are checked numerically.
status: in-progress
kind: derivation
level: intermediate
tags: [rotation-operator, generator, vector-operator, scalar-operator, wigner-d-matrix, spinor-rotation, angular-momentum-conservation, complete-set-of-commuting-observables, griffiths]
prerequisites: [translation-operator-and-translational-symmetry, orbital-angular-momentum, spin-one-half]
related: [parity-and-parity-selection-rules, rotational-selection-rules-and-wigner-eckart, symmetry-conservation-and-degeneracy, central-potentials-and-spherical-harmonics, addition-of-angular-momenta, spin-tensor-operators, functions-of-matrices]
also: []
date: 2026-11-05
---

## Rotations about the z axis

**Definition.** A counterclockwise rotation of a function by $\varphi$ about $z$ is

$$
\hat R_z(\varphi)\psi(r,\theta,\phi) = \psi(r,\theta,\phi-\varphi).
$$

**Generator.** $\hat L_z = -i\hbar\,\partial/\partial\phi$, so the same Taylor argument as for translations ([[translation-operator-and-translational-symmetry]]) gives

$$
\hat R_z(\varphi) = e^{-i\varphi\hat L_z/\hbar}.
$$

On an eigenfunction this is just a phase: $\hat R_z(\varphi)Y_\ell^m = e^{-im\varphi}Y_\ell^m$.

**Transforming $\hat x$.** For an infinitesimal angle $\delta$, $\hat R\approx1-i\delta\hat L_z/\hbar$ and

$$
\hat x' = \hat R^\dagger\hat x\hat R \approx \hat x + \frac{i\delta}{\hbar}[\hat L_z,\hat x] = \hat x-\delta\hat y,
\qquad \hat y' = \hat y+\delta\hat x,\qquad \hat z' = \hat z,
$$

using $[\hat L_z,\hat x] = i\hbar\hat y$ and $[\hat L_z,\hat y] = -i\hbar\hat x$. This is the first-order form of the familiar matrix

$$
\mathsf D_z(\varphi) = \begin{pmatrix}\cos\varphi&-\sin\varphi&0\\ \sin\varphi&\cos\varphi&0\\0&0&1\end{pmatrix}.
$$

**From infinitesimal to finite (Problem 6.14).** The $2\times2$ block of $N$ rotations by $\varphi/N$ is $\mathsf M^N$ with $\mathsf M = \begin{pmatrix}1&-\varphi/N\\ \varphi/N&1\end{pmatrix}$. The eigenvalues of $\mathsf M$ are $1\pm i\varphi/N$, and $(1\pm i\varphi/N)^N\to e^{\pm i\varphi}$. Transforming back gives exactly the $\cos/\sin$ block.

Numerically, for $\varphi = 0.83$, $\max|\mathsf M^N-\mathsf D|$ is $2.5\times10^{-2}$, $2.5\times10^{-3}$ and $2.5\times10^{-5}$ for $N = 10$, $100$, $10^4$: first-order convergence in $1/N$.

## Rotations in three dimensions

**General axis.** For a unit vector $\mathbf n$,

$$
\hat R_{\mathbf n}(\varphi) = \exp\!\left[-\frac{i\varphi}{\hbar}\,\mathbf n\cdot\hat{\mathbf L}\right].
$$

Angular momentum is the **generator of rotations**.

**Vector operators.** A three-component operator is a **vector operator** if it transforms like $\hat{\mathbf r}$, $\hat{\mathbf V}' = \hat R^\dagger\hat{\mathbf V}\hat R = \mathsf D\hat{\mathbf V}$ with the same $3\times3$ matrix $\mathsf D$. Taking the infinitesimal form, this is equivalent to

$$
[\hat L_i,\hat V_j] = i\hbar\,\epsilon_{ijk}\hat V_k,
$$

which serves as the working definition. $\hat{\mathbf r}$, $\hat{\mathbf p}$ and $\hat{\mathbf L}$ itself all satisfy it; this was checked symbolically on an arbitrary function $F(x,y,z)$.

**Scalar operators.** A scalar is unchanged by rotations: $[\hat L_i,\hat f] = 0$. Then $\hat R^\dagger\hat f\hat R = \hat f$ for finite rotations as well (Problem 6.15), since $\hat f$ commutes with every power of $\mathbf n\cdot\hat{\mathbf L}$.

The parity behaviour (true versus pseudo) is independent of this classification; see the table in [[parity-and-parity-selection-rules]].

**Ladder components.** With $\hat V_\pm = \hat V_x\pm i\hat V_y$ the definition becomes

$$
[\hat L_z,\hat V_z] = 0,\quad
[\hat L_z,\hat V_\pm] = \pm\hbar\hat V_\pm,\quad
[\hat L_\pm,\hat V_\pm] = 0,\quad
[\hat L_\pm,\hat V_z] = \mp\hbar\hat V_\pm,\quad
[\hat L_\pm,\hat V_\mp] = \pm2\hbar\hat V_z .
$$

These are Eqs. (6.50)–(6.54); every sign was verified for $\hat{\mathbf V} = \hat{\mathbf r}$ and $\hat{\mathbf p}$. They are used in [[rotational-selection-rules-and-wigner-eckart]].

**Problem 6.19.** Further,

$$
[\hat L^2,\hat V_\pm] = 2\hbar^2\hat V_\pm \pm 2\hbar\hat V_\pm\hat L_z \mp 2\hbar\hat V_z\hat L_\pm ,
$$

also verified symbolically. Acting on a state with $m = \ell$ (so $\hat L_+\psi = 0$), $\hat V_+\psi$ is either zero or an eigenstate with $(\ell+1,\ell+1)$: $\hat V_+$ raises both quantum numbers. This is the step used for the Runge–Lenz vector in [[symmetry-conservation-and-degeneracy]].

### Rotating angular-momentum eigenstates

**Statement.** $\hat L^2$ commutes with every $\hat L_i$, so a rotation never changes $\ell$; it only mixes the $2\ell+1$ values of $m$ (Problem 6.17):

$$
\hat R_{\mathbf n}(\varphi)\psi_{n\ell m} = \sum_{m'}D^{(\ell)}_{m'm}\psi_{n\ell m'} .
$$

For a rotation by $\beta$ about $y$, $D^{(\ell)}_{m'm} = d^{(\ell)}_{m'm}(\beta)$, the Wigner small-$d$ matrix.

!!! example "Numerical check of the d-matrix (ℓ = 2, β = 0.7)"
    **Method.** Each $Y_2^m$ is rotated actively, $(\hat R\psi)(\mathbf r) = \psi(\mathsf R^{-1}\mathbf r)$, on a $40\times40$ Gauss–Legendre $\times$ uniform-$\phi$ grid. The result is projected onto $Y_2^{m'}$ and onto $\ell = 1$ and $\ell = 3$.

    **Result.**

    - The projections reproduce SymPy's $d^{(2)}_{m'm}(0.7)$ (`Rotation.d`) to $8\times10^{-15}$ for all 25 entries.
    - The leakage to $\ell = 1, 3$ is $6\times10^{-17}$.

    This confirms both the statement that $\ell$ is preserved and the active-rotation sign convention used here.

## Spin-½ rotations (Problem 6.32)

**Pauli identity.** For ordinary vectors $\mathbf a$, $\mathbf b$, $(\mathbf a\cdot\boldsymbol\sigma)(\mathbf b\cdot\boldsymbol\sigma) = \mathbf a\cdot\mathbf b + i(\mathbf a\times\mathbf b)\cdot\boldsymbol\sigma$. Hence $(\mathbf n\cdot\boldsymbol\sigma)^2 = 1$, and the exponential series splits into even and odd parts. With $\hat{\mathbf S} = (\hbar/2)\boldsymbol\sigma$:

$$
\mathsf R_{\mathbf n}(\varphi) = e^{-i\varphi\,\mathbf n\cdot\boldsymbol\sigma/2}
= \cos\frac\varphi2\,\mathbb 1 - i\sin\frac\varphi2
\begin{pmatrix}\cos\theta & \sin\theta\,e^{-i\phi}\\ \sin\theta\,e^{i\phi} & -\cos\theta\end{pmatrix},
$$

where $(\theta,\phi)$ are the polar angles of $\mathbf n$.

**Checks** (with $\theta = 1.1$, $\phi = 0.4$, $\varphi = 2.3$):

- the closed form agrees with `expm` to $3\times10^{-16}$ and is unitary;
- $\mathsf R_z^\dagger\hat S_x\mathsf R_z = \cos\varphi\,\hat S_x - \sin\varphi\,\hat S_y$, the same $\mathsf D_z$ as for $\hat{\mathbf r}$, so spin is a vector operator;
- $\mathsf R_x(\pi)|{\uparrow}\rangle = -i|{\downarrow}\rangle$: the up spin is turned down, up to a phase;
- $\mathsf R_z(2\pi) = -\mathbb 1$.

**The surprise.** A full turn multiplies every spinor by $-1$; it takes $4\pi$ to return to the identity. Overall phases are unobservable, but the relative phase is observable in interference experiments in which only one beam is rotated. This half-angle behaviour is why half-integer $j$ has no counterpart in orbital angular momentum, where $e^{-2\pi i m} = 1$.

## Rotational invariance and conservation of angular momentum

**Invariance.** For $V(\mathbf r) = V(r)$, $[\hat H,\hat R_{\mathbf n}(\varphi)] = 0$ for every axis and angle. The infinitesimal case gives

$$
[\hat H,\hat{\mathbf L}] = 0
\quad\Longrightarrow\quad
\frac{d\langle\hat{\mathbf L}\rangle}{dt} = 0 .
$$

Angular-momentum conservation follows from rotational invariance, and so do the time-independent probability distributions of each component.

**Complete set.** $\hat H$, $\hat L^2$ and $\hat L_z$ commute pairwise, so the eigenstates can be labelled $\psi_{n\ell m}$:

$$
\hat H\psi_{n\ell m} = E_{n\ell}\psi_{n\ell m},\qquad \hat L^2\psi_{n\ell m} = \ell(\ell+1)\hbar^2\psi_{n\ell m},\qquad \hat L_z\psi_{n\ell m} = m\hbar\psi_{n\ell m}.
$$

For bound states of any central potential, $(n,\ell,m)$ specifies the state uniquely ([[central-potentials-and-spherical-harmonics]]). The non-commutativity of $\hat L_x$, $\hat L_y$ and $\hat L_z$ is what forces the $(2\ell+1)$-fold degeneracy ([[symmetry-conservation-and-degeneracy]]).

## Source

Griffiths and Schroeter, *Introduction to Quantum Mechanics* (3rd ed., Cambridge University Press, 2018), Sec. 6.5 (6.5.1–6.5.2), Eqs. (6.28)–(6.38), Table 6.1, Fig. 6.4 (described); Sec. 6.7.2, Eqs. (6.50)–(6.54); Problems 6.14–6.17, 6.19, 6.22(a), 6.32. Page numbers are not given because the PDF used is an e-book rendering without print pagination. The symbolic commutator checks, the d-matrix projection and the spin-½ matrices are computed in `griffiths/ch06_symmetry.py` (section D). The remark on observability of the $2\pi$ sign is an addition: it refers to neutron-interferometry experiments of the 1970s, for which no specific reference is given here (to verify).
