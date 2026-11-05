---
id: eigenfunctions-of-hermitian-operators
title: Eigenfunctions of Hermitian operators; discrete and continuous spectra
summary: For normalizable eigenfunctions, Hermitian operators have real eigenvalues and orthogonal eigenfunctions for distinct eigenvalues (Gram–Schmidt within degenerate subspaces). Completeness is taken as an axiom. For continuous spectra (momentum, position) eigenfunctions are not in Hilbert space but are Dirac-orthonormal, ⟨f_p′|f_p⟩ = δ(p−p′), and complete in the integral sense. Derives f_p = e^{ipx/ħ}/√(2πħ), g_y = δ(x−y), and the de Broglie relation from them.
status: in-progress
kind: theory
level: intermediate
tags: [eigenvalues, eigenfunctions, spectrum, degeneracy, completeness, dirac-orthonormality, continuous-spectrum, momentum-eigenfunctions, griffiths]
prerequisites: [hilbert-space-and-hermitian-operators]
related: [generalized-statistical-interpretation, matrix-eigenvalue-problem, orthonormal-functions-and-operators, free-particle-and-wave-packets]
also: []
date: 2026-11-04
---

## Two kinds of spectrum

- **Discrete.** The eigenvalues are separated, and the eigenfunctions are normalizable, so they are physical states. Example: the oscillator Hamiltonian.
- **Continuous.** The eigenvalues fill a range, and the eigenfunctions are *not* normalizable. Only superpositions spread over a range of eigenvalues are physical. Example: the free-particle Hamiltonian.

Some operators have both, such as the finite-well Hamiltonian with its bound states and scattering continuum.

## Discrete spectra: two theorems

**Theorem 1.** The eigenvalues of a Hermitian operator are real.

*Proof.* Let $\hat Qf = qf$ with $f\in L^2$. Hermiticity gives $\langle f|\hat Qf\rangle = \langle\hat Qf|f\rangle$, that is $q\langle f|f\rangle = q^*\langle f|f\rangle$. Since $\langle f|f\rangle\neq0$, $q=q^*$.

**Theorem 2.** Eigenfunctions belonging to distinct eigenvalues are orthogonal.

*Proof.* Let $\hat Qf=qf$ and $\hat Qg=q'g$. Then $q'\langle f|g\rangle = \langle f|\hat Qg\rangle = \langle\hat Qf|g\rangle = q^*\langle f|g\rangle = q\langle f|g\rangle$. So $(q'-q)\langle f|g\rangle = 0$.

These two theorems are why stationary states of the infinite well and the oscillator came out orthogonal: they are eigenfunctions of a Hermitian $\hat H$ with distinct eigenvalues.

**Degeneracy.** Any combination of eigenfunctions with the same eigenvalue is again an eigenfunction (Griffiths Problem 3.7). Gram–Schmidt within each degenerate subspace produces an orthonormal set, so the eigenfunctions can always be *chosen* orthonormal.

Example (Problem 3.7b): $e^{\pm x}$ are eigenfunctions of $d^2/dx^2$ with eigenvalue 1, and $\cosh x$, $\sinh x$ are an orthogonal pair on $(-1,1)$.

**Completeness.** In finite dimensions, the eigenvectors of a Hermitian matrix span the space ([[matrix-eigenvalue-problem]]). The proof does not carry over to infinite dimensions. Following Dirac, Griffiths takes it as an **axiom**, or more precisely as a restriction on which Hermitian operators can represent observables:

> the eigenfunctions of an observable are complete.

In specific cases it is a theorem. Dirichlet's theorem covers the infinite-well sines, and for the oscillator see [[harmonic-oscillator-analytic-solution]].

## Continuous spectra

**Example 3.2: momentum.** Solve $-i\hbar f_p' = pf_p$:

$$
f_p(x) = Ae^{ipx/\hbar}.
$$

This is not square-integrable for any complex $p$, so $\hat p$ has no eigenfunctions in Hilbert space. For **real** $p$, however, the delta-function identity $\int e^{ikx}dx = 2\pi\delta(k)$ gives

$$
\int f_{p'}^*f_p\,dx = |A|^2\,2\pi\hbar\,\delta(p-p').
$$

The choice $A = 1/\sqrt{2\pi\hbar}$ yields **Dirac orthonormality**:

$$
f_p(x) = \frac{1}{\sqrt{2\pi\hbar}}e^{ipx/\hbar},\qquad \langle f_{p'}|f_p\rangle = \delta(p-p').
$$

**Completeness** becomes an integral:

$$
f(x) = \int c(p)f_p(x)\,dp,\qquad c(p) = \langle f_p|f\rangle .
$$

This is the Fourier transform (Plancherel's theorem in [[free-particle-and-wave-packets]]).

**De Broglie justified.** $f_p$ has wavelength $\lambda = 2\pi\hbar/p$, which is the de Broglie relation, now derived from $\hat p=-i\hbar\,d/dx$ rather than postulated. Strictly, no particle has a determinate momentum. The relation applies to normalizable packets with a narrow spread of $p$.

**Example 3.3: position.** $x\,g_y(x) = y\,g_y(x)$ for every $x$ forces $g_y$ to vanish except at $x=y$:

$$
g_y(x) = \delta(x-y),\qquad\langle g_{y'}|g_y\rangle = \delta(y-y').
$$

Completeness is trivial: $f(x) = \int f(y)\,\delta(x-y)\,dy$, so $c(y) = f(y)$.

**General statement.** For a continuous spectrum, the eigenfunctions with *real* eigenvalues are Dirac-orthonormalizable and complete, even though none of them lies in Hilbert space. That is all quantum mechanics needs. Griffiths (footnote 14) notes that eigenfunctions with non-real eigenvalues blow up at infinity. The real-eigenvalue family lives in the "suburbs" of Hilbert space: a rigged Hilbert space, where each member has a finite inner product with every member of $L^2$.

## Which Chapter 2 Hamiltonians have which spectrum (Griffiths Problem 3.9)

| Spectrum | Example (besides the oscillator, free particle and finite well) |
|---|---|
| Discrete only | infinite square well |
| Continuous only | delta-function *barrier*, potential step |
| Both | delta-function well (one bound state plus continuum) |

## Worked example

!!! example "Is the ground state of the infinite well a momentum eigenstate? (Griffiths Problem 3.10)"
    **No.** $\psi_1 = \sqrt{2/a}\sin(\pi x/a)$ is a superposition of $e^{\pm i\pi x/a}$: momenta $\pm\pi\hbar/a$ with equal weight, cut off by the walls.

    **Momentum distribution** ([[generalized-statistical-interpretation]], Griffiths Problem 3.34). $|\Phi_1(p)|^2$ is in fact peaked at $p=0$ and decays as $p^{-4}$. The sharp edges of the box mix in a broad range of momenta. As $n$ grows, the peaks move toward $\pm n\pi\hbar/a$:

    | $n$ | 1 | 2 | 5 | 10 |
    |---|---|---|---|---|
    | Most probable $|p|$ (units $\hbar/a$) | 0 | 5.26 | 15.32 | 31.22 |
    | $n\pi$ | 3.14 | 6.28 | 15.71 | 31.42 |

    **Second moment.** $\langle p^2\rangle = \int p^2|\Phi_n|^2dp$ converges only as $1/p_{\max}$. Extrapolating the cutoffs 400 and 800 gives $9.8697$, $39.4780$ and $88.8274$, against $(n\pi\hbar/a)^2 = 9.8696$, $39.4784$, $88.8264$.

## Source

Griffiths and Schroeter, *Introduction to Quantum Mechanics* (3rd ed., Cambridge University Press, 2018), Sec. 3.3, Eqs. (3.30)-(3.42), Theorems 1-2, Examples 3.2-3.3; Problems 3.7-3.10, 3.34; footnotes 11-14. Page numbers are not given because the PDF used is an e-book rendering without print pagination. The table of most probable momenta and the extrapolated $\langle p^2\rangle$ are computed answers to Problem 3.34, not quoted. Numbers from `griffiths/ch03_formalism.py` (section B).
