---
id: position-momentum-and-energy-representations
title: State vectors and their position, momentum and energy representations
summary: The state |S(t)⟩ is a vector in Hilbert space. Ψ(x,t) = ⟨x|S⟩, Φ(p,t) = ⟨p|S⟩ and c_n(t) = ⟨n|S⟩ are its components in three bases. Covers resolutions of the identity (discrete and continuous), projection operators, operators as matrices, x and p in each representation, the transformation Ψ → Φ by inserting 1 = ∫|x⟩⟨x|dx, functions of operators, and a two-level system solved exactly. Companion to the finite-dimensional dirac-notation note.
status: in-progress
kind: theory
level: intermediate
tags: [dirac-notation, representations, position-space, momentum-space, energy-basis, resolution-of-identity, projection-operator, two-level-system, spectral-decomposition, griffiths]
prerequisites: [generalized-statistical-interpretation, dirac-notation]
related: [change-of-basis, orthonormal-functions-and-operators, functions-of-matrices, baker-campbell-hausdorff, harmonic-oscillator-ladder-operators]
also: []
date: 2026-11-04
---

## Scope

[[dirac-notation]] and [[change-of-basis]] cover kets, bras, matrix representations and unitary basis changes in a finite $N$-dimensional space. This note adds what Griffiths Sec. 3.6 brings beyond that: continuous bases (position and momentum), the three standard representations of one state, and operators acting between them.

## One vector, three sets of components

The state of the system is a vector $|\mathcal S(t)\rangle$ in Hilbert space, independent of any basis. Its components in the eigenbases of $\hat x$, $\hat p$ and $\hat H$ are:

$$
\Psi(x,t) = \langle x|\mathcal S(t)\rangle,\qquad
\Phi(p,t) = \langle p|\mathcal S(t)\rangle,\qquad
c_n(t) = \langle n|\mathcal S(t)\rangle .
$$

Here $|x\rangle$, $|p\rangle$ and $|n\rangle$ are the eigenvectors of $\hat x$, $\hat p$ and $\hat H$, with $\langle x|p\rangle = f_p(x) = e^{ipx/\hbar}/\sqrt{2\pi\hbar}$. The three sets carry the same information, just as a 2D arrow has different components along rotated axes. Calling $\Psi(x,t)$ "the state" is shorthand for "the state in the position basis".

## Resolutions of the identity

**Orthonormality and completeness** for a discrete and a continuous basis:

$$
\langle e_m|e_n\rangle = \delta_{mn},\quad \sum_n|e_n\rangle\langle e_n| = 1;
\qquad
\langle e_z|e_{z'}\rangle = \delta(z-z'),\quad \int|e_z\rangle\langle e_z|\,dz = 1 .
$$

**The three standard ones:**

$$
1 = \int dx\,|x\rangle\langle x|,\qquad 1 = \int dp\,|p\rangle\langle p|,\qquad 1 = \sum_n|n\rangle\langle n| .
$$

Applying each to $|\mathcal S\rangle$ gives the three expansions, for example $|\mathcal S\rangle = \int\Psi(x,t)\,|x\rangle\,dx$.

**Projection operators.** For a normalized $|\alpha\rangle$, $\hat P = |\alpha\rangle\langle\alpha|$ picks out the component along $|\alpha\rangle$.

- $\hat P^2 = \hat P$, so the eigenvalues are 0 and 1 (Problem 3.23).
- The vectors along $|\alpha\rangle$ have eigenvalue 1; everything orthogonal to it has eigenvalue 0.
- A resolution of the identity is a sum of projectors onto a complete orthonormal set.

## Operators in a basis

**Matrix elements.** $Q_{mn} = \langle e_m|\hat Q|e_n\rangle$. If $|\beta\rangle = \hat Q|\alpha\rangle$, the components obey $b_m = \sum_nQ_{mn}a_n$.

**Hermiticity.** A Hermitian operator has a Hermitian matrix in every orthonormal basis, $Q_{mn} = Q_{nm}^*$ (Problem 3.24).

**Position and momentum in each representation.**

| | Position basis | Momentum basis |
|---|---|---|
| $\hat x$ | $x$ | $i\hbar\,\partial/\partial p$ |
| $\hat p$ | $-i\hbar\,\partial/\partial x$ | $p$ |

**Precise statement.** $\langle x|\hat x|\mathcal S\rangle = x\Psi(x,t)$ and $\langle p|\hat x|\mathcal S\rangle = i\hbar\,\partial\Phi/\partial p$. "What is the position operator?" has no basis-free answer in the form of a formula.

**Spectral decomposition and functions of operators.** If $\hat Q|e_n\rangle = q_n|e_n\rangle$ with a complete orthonormal set, then

$$
\hat Q = \sum_nq_n|e_n\rangle\langle e_n|,\qquad f(\hat Q) = \sum_nf(q_n)\,|e_n\rangle\langle e_n|
$$

(Problem 3.27). This agrees with the power-series definition $e^{\hat Q} = \sum_k\hat Q^k/k!$, as in [[functions-of-matrices]].

Example of power-series action (Problem 3.28): with $\hat D = d/dx$, $\sin(\hat D)\,x^5 = 5x^4 - 10x^2 + 1$. Only finitely many terms survive on a polynomial.

## Changing representation by inserting the identity

**Position to momentum** (Example 3.9). Insert $1 = \int dx\,|x\rangle\langle x|$:

$$
\Phi(p,t) = \langle p|\mathcal S\rangle = \int\langle p|x\rangle\langle x|\mathcal S\rangle\,dx = \frac{1}{\sqrt{2\pi\hbar}}\int e^{-ipx/\hbar}\Psi(x,t)\,dx .
$$

This is the Fourier transform of [[generalized-statistical-interpretation]], obtained in one line.

**The position operator in the momentum basis** (Example 3.10). Insert $1$ to the right of $\hat x$ and use $\hat x|x\rangle = x|x\rangle$:

$$
\langle p|\hat x|\mathcal S\rangle = \int x\,\langle p|x\rangle\,\Psi\,dx = i\hbar\frac{\partial}{\partial p}\int\langle p|x\rangle\Psi\,dx = i\hbar\frac{\partial\Phi}{\partial p}.
$$

**Position to energy** (Problem 3.30). $c_n(t) = \int\psi_n^*(x)\,\Psi(x,t)\,dx$, which is Fourier's trick again, with $\langle n|x\rangle = \psi_n^*(x)$.

## Worked example

!!! example "Two-level system (Griffiths Example 3.8)"
    **Setup.** In the basis $|1\rangle,|2\rangle$, take

    $$
    \mathsf H = \begin{pmatrix}h & g\\ g & h\end{pmatrix}
    $$

    with $g$ and $h$ real, and start in $|1\rangle$.

    **Eigenpairs.** $E_\pm = h\pm g$ and $|s_\pm\rangle = (1,\pm1)^{\rm T}/\sqrt2$. Then $|1\rangle = (|s_+\rangle+|s_-\rangle)/\sqrt2$.

    **Time evolution.** Attach the phases $e^{-iE_\pm t/\hbar}$:

    $$
    |\mathcal S(t)\rangle = e^{-iht/\hbar}\begin{pmatrix}\cos(gt/\hbar)\\ -i\sin(gt/\hbar)\end{pmatrix},
    \qquad P_2(t) = \sin^2(gt/\hbar).
    $$

    The system oscillates fully between $|1\rangle$ and $|2\rangle$ at angular frequency $2g/\hbar$. Griffiths (footnote 34) notes this as a crude model of neutrino oscillations, with the off-diagonal $g$ mixing the flavours. In chemistry the same structure describes a symmetric double well, where tunnelling splits the two localized states by $2g$.

    **Numerical check** ($h=1$, $g=0.3$). $e^{-i\mathsf Ht}$ by matrix exponential agrees with the closed form to $3\times10^{-16}$ at $t = 0.7$ and $3.1$, where $P_2 = 0.043456$ and $0.642595$.

    **Problem 3.25.** $\hat H = \epsilon\left(|1\rangle\langle1|-|2\rangle\langle2|+|1\rangle\langle2|+|2\rangle\langle1|\right)$ has eigenvalues $\pm\sqrt2\,\epsilon$.

## Source

Griffiths and Schroeter, *Introduction to Quantum Mechanics* (3rd ed., Cambridge University Press, 2018), Sec. 3.6, Eqs. (3.77)-(3.110), Examples 3.8-3.10, Fig. 3.3 (described); Problems 3.23-3.28, 3.30; footnotes 27-38. Page numbers are not given because the PDF used is an e-book rendering without print pagination. The double-well remark and the $\sin(\hat D)x^5$ result are additions, the latter checked with SymPy from the power series. Numbers from `griffiths/ch03_formalism.py` (section E).
