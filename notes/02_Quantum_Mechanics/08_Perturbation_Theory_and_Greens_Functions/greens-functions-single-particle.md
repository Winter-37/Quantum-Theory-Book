---
id: greens-functions-single-particle
title: Green's functions for single-particle problems - resolvents, poles, the Dyson-type integral equation and propagators
summary: The Green's function of a Hermitian operator is its resolvent (E − H)⁻¹. It solves inhomogeneous equations by one integration, has poles at the eigenvalues, and obeys G = G0 + G0 V G when H = H0 + V. Worked example - the attractive δ potential, whose single bound state (E = −1/2, φ = e^{−|x|}) appears as a pole of G - checked on a grid. Connection to the time-dependent propagator by Fourier transformation.
status: in-progress
kind: derivation
level: intermediate
tags: [greens-function, resolvent, dyson-equation, propagator, poles, delta-potential, integral-equation]
prerequisites: [matrix-eigenvalue-problem, orthonormal-functions-and-operators, functions-of-matrices]
related: [one-particle-greens-function, propagators-and-superoperators, rayleigh-schrodinger-perturbation-theory]
order: 20
date: 2026-11-03
---

## The Green's matrix

**Problem.** Solve $(E\mathbf 1 - \mathbf H_0)\mathbf a = \mathbf b$ for a Hermitian $N\times N$ matrix $\mathbf H_0$, a parameter $E$ and a given $\mathbf b$.

**Solution.** Define the Green's matrix (the **resolvent** of $\mathbf H_0$),

$$
\mathbf G_0(E) = (E\mathbf 1 - \mathbf H_0)^{-1},\qquad \mathbf a = \mathbf G_0(E)\,\mathbf b .
$$

Once $\mathbf G_0(E)$ is known, every right-hand side is a matrix multiplication away.

**Spectral form.** With $\mathbf H_0\mathbf c^\alpha = E_\alpha^{(0)}\mathbf c^\alpha$ ([[functions-of-matrices]]),

$$
\big(\mathbf G_0(E)\big)_{ij} = \sum_\alpha\frac{c_i^\alpha c_j^{\alpha*}}{E - E_\alpha^{(0)}} .
$$

Every element has a **pole** at each eigenvalue, and the residue is the product of eigenvector components. Locating the poles of $\mathbf G$ is equivalent to solving the eigenvalue problem.

**Adding a perturbation (Szabo Ex. 7.1).** For $\mathbf H = \mathbf H_0 + \mathbf V$, $\mathbf G = (E\mathbf 1 - \mathbf H_0 - \mathbf V)^{-1}$ satisfies

$$
\mathbf G(E) = \mathbf G_0(E) + \mathbf G_0(E)\,\mathbf V\,\mathbf G(E) .
$$

*Proof:* $\mathbf G^{-1} = \mathbf G_0^{-1} - \mathbf V$; multiply on the left by $\mathbf G_0$ and on the right by $\mathbf G$. Iterating gives $\mathbf G = \mathbf G_0 + \mathbf G_0\mathbf V\mathbf G_0 + \mathbf G_0\mathbf V\mathbf G_0\mathbf V\mathbf G_0 + \cdots$, the resolvent form of perturbation theory ([[rayleigh-schrodinger-perturbation-theory]]).

## The Green's function of a differential operator

**Problem.** $(E - \mathscr H_0)a(x) = b(x)$ for a Hermitian operator with eigenfunctions $\mathscr H_0\psi_\alpha = E_\alpha^{(0)}\psi_\alpha$. Expanding both sides in $\{\psi_\alpha\}$ gives $a_\alpha = b_\alpha/(E - E_\alpha^{(0)})$, so

$$
a(x) = \int dx'\,G_0(x, x'; E)\,b(x'),
\qquad
G_0(x, x'; E) = \sum_\alpha\frac{\psi_\alpha(x)\psi_\alpha^*(x')}{E - E_\alpha^{(0)}} .
$$

**Defining equation.** Setting $b(x) = \delta(x - x')$ shows that $G_0$ solves the equation with a point source:

$$
(E - \mathscr H_0)\,G_0(x, x'; E) = \delta(x - x'),
$$

the continuous analogue of $(E\mathbf 1 - \mathbf H_0)(E\mathbf 1 - \mathbf H_0)^{-1} = \mathbf 1$.

**Simplest example (Szabo Ex. 7.2).** For $d^2/dx^2$, $\tfrac{d^2}{dx^2}\tfrac12|x - x'| = \delta(x - x')$, so $a(x) = \tfrac12\int dx'\,|x - x'|\,b(x')$ solves $a'' = b$.

**Integral equation.** For $\mathscr H = \mathscr H_0 + V(x)$, writing $(E - \mathscr H_0)G = \delta + VG$ and applying $G_0$:

$$
G(x, x'; E) = G_0(x, x'; E) + \int dx''\,G_0(x, x''; E)\,V(x'')\,G(x'', x'; E).
$$

The matrix version $\mathbf G = \mathbf G_0 + \mathbf G_0\mathbf V\mathbf G$ is its representation in any complete basis. In abstract operator form, $\mathscr G_0 = (E - \mathscr H_0)^{-1}$ and $\mathscr G = (E - \mathscr H_0 - \mathscr V)^{-1}$ give $\mathscr G = \mathscr G_0 + \mathscr G_0\mathscr V\mathscr G$ directly. In the many-electron problem this is the **Dyson equation**, with an energy-dependent $\mathscr V$, the self-energy ([[one-particle-greens-function]]).

## Worked example: the attractive δ potential

**Setup.** $\mathscr H_0 = -\tfrac12 d^2/dx^2$ and $V(x) = -\delta(x)$. The free-particle Green's function (by Fourier transform and contour integration) is

$$
G_0(x, x'; E) = \frac{1}{i(2E)^{1/2}}\exp\big(i(2E)^{1/2}|x - x'|\big).
$$

**The integral equation becomes algebraic.** The δ function collapses the integral:

$$
G(x, x'; E) = G_0(x, x'; E) - G_0(x, 0; E)\,G(0, x'; E).
$$

Setting $x = 0$ gives $G(0, x'; E) = G_0(0, x'; E)/(1 + G_0(0, 0; E))$, so

$$
G(x, x'; E) = G_0(x, x'; E) - \frac{G_0(x, 0; E)\,G_0(0, x'; E)}{1 + G_0(0, 0; E)} .
$$

**Bound state from the pole.** $G$ diverges when $1 + G_0(0,0;E) = 0$, i.e. $i(2E)^{1/2} = -1$, $E = -\tfrac12$. The residue gives the eigenfunction (Szabo Ex. 7.4): $\phi(x) = e^{-|x|}$. This is an instance of the theorem that any attractive potential in one dimension binds at least one state.

!!! example "Numerical check on a grid (computed for this note)"
    Finite differences on $[-20, 20]$ with 4001 points, the δ function represented by $1/h$ at the origin:

    - **Bound state.** Lowest eigenvalue −0.49999; the eigenvector agrees with $e^{-|x|}$ to $10^{-4}$. The next eigenvalue (0.012) belongs to the discretized continuum.
    - **Dyson identity.** At $E = -0.3$, $\max|\mathbf G - \mathbf G_0 - \mathbf G_0\mathbf V\mathbf G| = 3.5\times10^{-14}$.
    - **Free Green's function.** At $E = -0.3$, $G_0(0, 0) = -1/(-2E)^{1/2} = -1.29099$ analytically against −1.29098 on the grid.

## From the time domain: propagators

**Time-dependent Green's function (Szabo Ex. 7.6).** If $i\,\partial_t G(x, x', t) = \mathscr H G(x, x', t)$ with $G(x, x', 0) = \delta(x - x')$, then

$$
\psi(x, t) = \int dx'\,G(x, x', t)\,\psi(x', 0)
$$

solves the time-dependent Schrödinger equation for any initial state. $G$ **propagates** the wave function, hence the name propagator. In operator form, $\mathscr G(t) = e^{-i\mathscr Ht}$.

**Energy domain.** The half-sided Fourier transform with a convergence factor,

$$
\mathscr G(E) = -i\lim_{\epsilon\to0^+}\int_0^\infty dt\,e^{iEt}e^{-\epsilon t}\,e^{-i\mathscr Ht} = (E - \mathscr H)^{-1},
$$

is the resolvent above. The many-body Green's functions of [[propagators-and-superoperators]] are built the same way, with creation and annihilation operators in place of $\psi$.

## Source

Szabo and Ostlund, *Modern Quantum Chemistry* (Dover, 1996; reprint of the revised first edition, McGraw-Hill, 1989), Sec. 7.1, pp. 381-387, Eqs. (7.1)-(7.25), Ex. 7.1-7.6. Grid calculation computed for this note.
