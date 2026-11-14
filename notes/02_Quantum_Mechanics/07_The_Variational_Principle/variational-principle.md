---
id: variational-principle
title: The variational principle - the energy of any trial state bounds the ground state from above
summary: For any normalized trial state, the energy expectation value is an upper bound to the exact ground-state energy. Proof via eigenfunction expansion, matrix form, and three worked checks (delta potential, hydrogen, 2x2 matrix).
status: in-progress
kind: derivation
level: introductory
tags: [basics, variational, ground-state, upper-bound]
prerequisites: []
related: [hellmann-feynman-and-virial-theorems, upper-bounds-and-interlacing, linear-variation-method]
order: 10
date: 2026-10-31
---

## Statement

Let $\hat H$ be a time-independent Hamiltonian with exact eigenstates

$$
\hat H|\Phi_\alpha\rangle = E_\alpha|\Phi_\alpha\rangle,
\qquad E_0 \le E_1 \le E_2 \le \dots
$$

and let $|\tilde\Phi\rangle$ be **any** normalized state that obeys the same boundary conditions (usually: vanishes at infinity). Then

$$
\langle\tilde\Phi|\tilde\Phi\rangle = 1
\;\;\Longrightarrow\;\;
\langle\tilde\Phi|\hat H|\tilde\Phi\rangle \;\ge\; E_0 .
$$

Equality holds only if $|\tilde\Phi\rangle$ is a ground state of $\hat H$ (the exact $|\Phi_0\rangle$ if it is non-degenerate, up to a phase).

**Assumptions.** The eigenstates $\{|\Phi_\alpha\rangle\}$ are orthonormal and complete, and $\hat H$ is Hermitian with a spectrum bounded below. For simplicity the spectrum is written as discrete. Continuum states only turn $\sum_\alpha$ into $\sum_\alpha + \int$ and change nothing below.

## Proof

Orthonormality and completeness of the eigenstates are

$$
\langle\Phi_\alpha|\Phi_\beta\rangle = \delta_{\alpha\beta},
\qquad
\sum_\alpha |\Phi_\alpha\rangle\langle\Phi_\alpha| = 1 .
$$

Insert the identity twice into the normalization condition:

$$
1 = \langle\tilde\Phi|\tilde\Phi\rangle
= \sum_{\alpha\beta}\langle\tilde\Phi|\Phi_\alpha\rangle\langle\Phi_\alpha|\Phi_\beta\rangle\langle\Phi_\beta|\tilde\Phi\rangle
= \sum_\alpha |\langle\Phi_\alpha|\tilde\Phi\rangle|^2 .
$$

Write $c_\alpha = \langle\Phi_\alpha|\tilde\Phi\rangle$, so $\sum_\alpha |c_\alpha|^2 = 1$. The same insertion for the energy, using $\hat H|\Phi_\beta\rangle = E_\beta|\Phi_\beta\rangle$, gives

$$
\langle\tilde\Phi|\hat H|\tilde\Phi\rangle
= \sum_{\alpha\beta}\langle\tilde\Phi|\Phi_\alpha\rangle\langle\Phi_\alpha|\hat H|\Phi_\beta\rangle\langle\Phi_\beta|\tilde\Phi\rangle
= \sum_\alpha E_\alpha |c_\alpha|^2 .
$$

Since $E_\alpha \ge E_0$ for every $\alpha$ and $|c_\alpha|^2 \ge 0$,

$$
\langle\tilde\Phi|\hat H|\tilde\Phi\rangle
\;\ge\; E_0\sum_\alpha |c_\alpha|^2 = E_0 .
$$

Subtracting $E_0$ shows exactly where the error comes from:

$$
\langle\tilde\Phi|\hat H|\tilde\Phi\rangle - E_0
= \sum_{\alpha>0}\,(E_\alpha - E_0)\,|c_\alpha|^2 \;\ge\; 0 .
$$

The error is a weighted sum of excitation energies, with weights equal to the excited-state populations of the trial function. It vanishes only if every state with $E_\alpha > E_0$ has $c_\alpha = 0$. Note that $|c_\alpha|^2$ is quadratic in the amplitude of the error in $|\tilde\Phi\rangle$, so the energy error is **second order** in the wave-function error.

## Why it is useful: the variation method

The theorem says an approximate wave function always gives an energy that is too high. The energy is therefore a quality measure: the lower, the better. The **variation method** uses this directly. Take a normalized trial function $|\tilde\Phi(\lambda_1,\lambda_2,\dots)\rangle$ that depends on parameters, and minimize

$$
E(\boldsymbol\lambda) = \langle\tilde\Phi(\boldsymbol\lambda)|\hat H|\tilde\Phi(\boldsymbol\lambda)\rangle
$$

with respect to $\boldsymbol\lambda$. The minimum is the variational estimate of $E_0$, and it can never fall below the exact value.

If $|\tilde\Phi\rangle$ is not normalized, minimize the Rayleigh quotient instead:

$$
E[\tilde\Phi] = \frac{\langle\tilde\Phi|\hat H|\tilde\Phi\rangle}{\langle\tilde\Phi|\tilde\Phi\rangle} \ge E_0 .
$$

!!! warning "What the theorem does not say"
    It bounds the **energy**, not other properties. A lower energy does not guarantee a better dipole moment, density at a point, etc. It also applies to the ground state only (or the lowest state of each symmetry if the trial function is restricted to that symmetry).

## Matrix form

Expand the trial function in a finite orthonormal set $\{|\chi_i\rangle\}$ and let $\mathbf O$ be any Hermitian matrix (for the Hamiltonian, $O_{ij} = \langle\chi_i|\hat H|\chi_j\rangle$). For a column vector $\mathbf c$ with $\mathbf c^\dagger\mathbf c = 1$,

$$
\mathbf c^\dagger \mathbf O\, \mathbf c \;\ge\; \varepsilon_{\min}(\mathbf O),
$$

where $\varepsilon_{\min}$ is the lowest eigenvalue of $\mathbf O$. The proof is the same as above with the eigenvectors of $\mathbf O$ in place of $|\Phi_\alpha\rangle$. A finite basis is an incomplete expansion, so the lowest eigenvalue of $\mathbf O$ is itself an upper bound to $E_0$. This is the basis of the linear variation method (see [[linear-variation-method]]).

## Worked examples

!!! example "1D electron in a delta potential, Gaussian trial function"
    **Problem.** In atomic units, $\left(-\tfrac12\tfrac{\mathrm d^2}{\mathrm dx^2} - \delta(x)\right)|\Phi\rangle = E|\Phi\rangle$ has exact ground-state energy $E_0 = -0.5$ hartree. Use $\tilde\Phi(x) = N e^{-\alpha x^2}$ with $\alpha>0$.

    **Normalization.** $\int_{-\infty}^{\infty} e^{-2\alpha x^2}\,\mathrm dx = \sqrt{\pi/(2\alpha)}$, so
    $$
    N^2 = \sqrt{\frac{2\alpha}{\pi}} .
    $$

    **Kinetic energy.** $\tilde\Phi'' = (4\alpha^2x^2 - 2\alpha)\tilde\Phi$ and $\langle x^2\rangle = 1/(4\alpha)$, hence
    $$
    \langle \hat T\rangle = -\tfrac12\left(4\alpha^2\cdot\tfrac{1}{4\alpha} - 2\alpha\right) = \frac{\alpha}{2}.
    $$

    **Potential energy.** $\langle -\delta(x)\rangle = -|\tilde\Phi(0)|^2 = -N^2 = -\sqrt{2\alpha/\pi}$.

    **Minimize.**
    $$
    E(\alpha) = \frac{\alpha}{2} - \sqrt{\frac{2\alpha}{\pi}},
    \qquad
    \frac{\mathrm dE}{\mathrm d\alpha} = \frac12 - \frac{1}{\sqrt{2\pi\alpha}} = 0
    \;\Rightarrow\; \alpha_{\min} = \frac{2}{\pi}.
    $$
    Then
    $$
    E(\alpha_{\min}) = \frac1\pi - \frac2\pi = -\frac1\pi \approx -0.3183 \;>\; -0.5 ,
    $$
    so $-1/\pi$ is an upper bound to $E_0$, as the theorem requires. The error is about $0.18$ hartree because a Gaussian cannot reproduce the cusp of the exact solution $e^{-|x|}$.

!!! example "Hydrogen atom with a Gaussian trial function"
    **Problem.** $\left(-\tfrac12\nabla^2 - \tfrac1r\right)|\Phi\rangle = E|\Phi\rangle$, exact $E_0 = -0.5$ hartree. Use $\tilde\Phi(r) = N e^{-\alpha r^2}$.

    **Integrals used** (for $\alpha>0$, integer $m \ge 0$):
    $$
    \int_0^\infty r^{2m}e^{-\alpha r^2}\,\mathrm dr = \frac{(2m)!\,\pi^{1/2}}{2^{2m+1}\,m!\,\alpha^{m+1/2}},
    \qquad
    \int_0^\infty r^{2m+1}e^{-\alpha r^2}\,\mathrm dr = \frac{m!}{2\alpha^{m+1}} .
    $$

    **Normalization.** With $\mathrm d^3r = 4\pi r^2\,\mathrm dr$ and $m=1$, $\alpha\to2\alpha$:
    $$
    1 = 4\pi N^2\,\frac{\sqrt\pi}{4(2\alpha)^{3/2}}
    \;\Rightarrow\;
    N^2 = \left(\frac{2\alpha}{\pi}\right)^{3/2}.
    $$

    **Kinetic energy.** $\nabla^2 e^{-\alpha r^2} = (4\alpha^2r^2 - 6\alpha)e^{-\alpha r^2}$ and $\langle r^2\rangle = 3/(4\alpha)$, so
    $$
    \langle\hat T\rangle = -\tfrac12\left(3\alpha - 6\alpha\right) = \frac{3\alpha}{2}.
    $$

    **Potential energy.** With $m=0$, $\alpha\to2\alpha$:
    $$
    \left\langle\frac1r\right\rangle = 4\pi N^2\cdot\frac{1}{2(2\alpha)} = \frac{\pi N^2}{\alpha} = 2\sqrt{\frac{2\alpha}{\pi}} .
    $$

    **Minimize.**
    $$
    E(\alpha) = \frac{3\alpha}{2} - 2\sqrt{\frac{2\alpha}{\pi}},
    \qquad
    \frac{\mathrm dE}{\mathrm d\alpha} = \frac32 - \sqrt{\frac{2}{\pi\alpha}} = 0
    \;\Rightarrow\; \alpha_{\min} = \frac{8}{9\pi}.
    $$
    Then
    $$
    E(\alpha_{\min}) = \frac{4}{3\pi} - \frac{8}{3\pi} = -\frac{4}{3\pi} \approx -0.4244 \;>\; -0.5 .
    $$
    A single Gaussian recovers about 85% of the exact energy (the numerator $0.4244/0.5$), which is why contracted combinations of Gaussians are used in practice (see [[gaussian-basis-functions]]).

!!! example "2x2 symmetric matrix, rotation-angle trial vector"
    **Problem.** Let $\mathbf O = \begin{pmatrix} O_{11} & O_{12}\\ O_{12} & O_{22}\end{pmatrix}$ be real symmetric, and use the normalized trial vector $\mathbf c = (\cos\theta,\ \sin\theta)^{\mathsf T}$ (normalized for every $\theta$).

    **Energy function.**
    $$
    \omega(\theta) = \mathbf c^\dagger\mathbf O\,\mathbf c
    = O_{11}\cos^2\theta + O_{22}\sin^2\theta + 2O_{12}\sin\theta\cos\theta .
    $$
    With double-angle identities,
    $$
    \omega(\theta) = \frac{O_{11}+O_{22}}{2} + \frac{O_{11}-O_{22}}{2}\cos2\theta + O_{12}\sin2\theta .
    $$

    **Stationary points.**
    $$
    \frac{\mathrm d\omega}{\mathrm d\theta} = -(O_{11}-O_{22})\sin2\theta + 2O_{12}\cos2\theta = 0
    \;\Rightarrow\;
    \tan2\theta = \frac{2O_{12}}{O_{11}-O_{22}} .
    $$
    This has two solutions for $2\theta$ per period, one minimum and one maximum. Let $A = (O_{11}-O_{22})/2$, $B = O_{12}$, $R = \sqrt{A^2+B^2}$. The expression $A\cos2\theta + B\sin2\theta$ has its minimum $-R$ at $(\cos2\theta_0,\ \sin2\theta_0) = -(A,B)/R$.

    **Minimum value.**
    $$
    \omega(\theta_0) = \frac{O_{11}+O_{22}}{2} - \sqrt{\left(\frac{O_{11}-O_{22}}{2}\right)^2 + O_{12}^2}.
    $$
    This is exactly the lower root of the secular equation $\det(\mathbf O - \varepsilon\mathbf 1) = 0$, i.e. the lowest eigenvalue of $\mathbf O$.

    **Why this should have been anticipated.** The vectors $(\cos\theta,\sin\theta)^{\mathsf T}$ cover every normalized real direction in the two-dimensional space. The eigenvector of the lowest eigenvalue is one of them, so the "trial function" is already complete and the variational bound is saturated. In general the bound is only exact when the trial space contains the exact eigenvector.

## Source

Szabo and Ostlund, *Modern Quantum Chemistry*, Sec. 1.3.1 (The Variation Principle, pp. 31-32, Eqs. 1.148-1.152) and Exercises 1.18-1.20 (pp. 32-33). Edition and year: 2nd Edition, 1996.
