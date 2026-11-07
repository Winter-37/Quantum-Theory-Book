---
id: baker-campbell-hausdorff
title: Commutator algebra and the Baker-Campbell-Hausdorff expansion
summary: Commutator and anticommutator product rules, rank lowering of second-quantized commutators, the nested-commutator (Hadamard) series for exp(A) B exp(−A), and the BCH formula for log(exp(A) exp(B)). When the series terminate or collapse to matrix exponentials, and where quantum chemistry uses them - orbital rotations, the second-order MCSCF energy, coupled-cluster equations. Each identity checked numerically.
status: in-progress
kind: derivation
level: intermediate
tags: [bch, baker-campbell-hausdorff, hadamard-lemma, commutator, nested-commutators, similarity-transformation, operator-algebra]
prerequisites: [functions-of-matrices, matrices-and-determinants]
related: [orbital-rotations, mcscf-second-order-optimization, coupled-cluster-second-quantization, second-quantized-operators, spin-tensor-operators]
order: 60
date: 2026-11-03
---

## Why this note

Three results in second-quantized quantum chemistry rest on one tool:

1. The rotated creation operator $e^{\hat\kappa}a_q^\dagger e^{-\hat\kappa}$ ([[orbital-rotations]]).
2. The second-order energy expansion that defines MCSCF gradients and Hessians ([[mcscf-second-order-optimization]]).
3. The coupled-cluster similarity transform $e^{-\hat T}\hat He^{\hat T}$ ([[coupled-cluster-second-quantization]]).

In each case an exponential of an operator acts by conjugation, and the result is a series of nested commutators. Jørgensen and Simons use this series at the end of their Ch. 1 (Eq. 1.41) and throughout Ch. 2 (Eq. 2.24) and Ch. 4 (Eq. 4.13) without naming it. This note collects the algebra in one place.

Notation: $[A,B] = AB - BA$, $[A,B]_+ = AB + BA$. The nested commutators are $[A,B]_0 = B$ and $[A,B]_n = [A,[A,B]_{n-1}]$.

## Product rules (J-S Problem 1.1)

For any operators $A$, $B$, $C$:

$$
[AB, C] = A[B,C] + [A,C]B = A[B,C]_+ - [A,C]_+B,
$$

$$
[AB, C]_+ = [A,C]_+B + A[B,C] ,
$$

$$
[A_1A_2\cdots A_N, B] = \sum_{j=1}^{N}A_1\cdots A_{j-1}[A_j, B]A_{j+1}\cdots A_N .
$$

Each follows by adding and subtracting one term, e.g. $ABC - CAB = (ABC - ACB) + (ACB - CAB)$. The mixed commutator/anticommutator forms are the useful ones for fermion operators, because the elementary relations are anticommutators: $[a_r, a_s^\dagger]_+ = \delta_{rs}$, $[a_r, a_s]_+ = [a_r^\dagger, a_s^\dagger]_+ = 0$ ([[creation-and-annihilation-operators]]).

**Jacobi identity.** $[A,[B,C]] + [B,[C,A]] + [C,[A,B]] = 0$. With $B = H$ and $A = C = \lambda$ it gives $[\lambda,[H,\lambda]] = [[\lambda,H],\lambda]$. This is J-S Eq. (2.32), which lets the MCSCF Hessian be written with a symmetrized double commutator.

## Rank lowering (J-S Problem 1.2)

**Basic commutators.** Using the product rules with the anticommutators:

$$
[a_i^\dagger a_j, a_k^\dagger] = \delta_{jk}a_i^\dagger,
\qquad
[a_i^\dagger a_j, a_k] = -\delta_{ik}a_j,
$$

$$
[a_i^\dagger a_j, a_k^\dagger a_l] = \delta_{jk}a_i^\dagger a_l - \delta_{il}a_k^\dagger a_j ,
$$

$$
[a_i^\dagger a_j^\dagger a_la_k, a_r^\dagger] = \delta_{kr}a_i^\dagger a_j^\dagger a_l - \delta_{lr}a_i^\dagger a_j^\dagger a_k,
\qquad
[a_s, a_i^\dagger a_j^\dagger a_l]_+ = \delta_{si}a_j^\dagger a_l - \delta_{sj}a_i^\dagger a_l .
$$

**The rule.** Every elementary contraction removes one creator and one annihilator. A commutator of an operator string of $m$ creation/annihilation operators with one of $n$ has at most $m + n - 2$ operators. In J-S's three examples the particle rank is lowered by one, two and two:

- **Example 1.** $[i^\dagger j, k^\dagger l]$: two one-body operators give a one-body operator.
- **Example 2.** $[s, [i^\dagger j^\dagger lk, r^\dagger]]_+$: a two-body operator nested with two single operators gives a one-body operator.
- **Example 3.** $[r^\dagger s, [i^\dagger j, t^\dagger v]] = \delta_{jt}[r^\dagger s, i^\dagger v] - \delta_{iv}[r^\dagger s, t^\dagger j]$: three one-body operators give a one-body operator.

This lowering happens **at the operator level**, before any matrix element is taken. It is why commutator expressions stay compact ([[spin-tensor-operators]]).

## The nested-commutator (Hadamard) series

**Statement.** For operators (or matrices) $A$, $B$:

$$
e^{A}Be^{-A} = \sum_{n=0}^{\infty}\frac1{n!}[A,B]_n = B + [A,B] + \frac1{2!}[A,[A,B]] + \frac1{3!}[A,[A,[A,B]]] + \cdots
$$

**Proof.** Let $f(\lambda) = e^{\lambda A}Be^{-\lambda A}$. Then $f(0) = B$ and

$$
f'(\lambda) = e^{\lambda A}(AB - BA)e^{-\lambda A} = e^{\lambda A}[A,B]e^{-\lambda A},
\qquad
f^{(n)}(0) = [A,B]_n .
$$

The Taylor series of $f$ at $\lambda = 0$, evaluated at $\lambda = 1$, is the result. (This is often called the Hadamard lemma; physicists usually call it "the BCH expansion".)

**Two consequences.**

- **Products conjugate factor by factor:** $e^{A}B_1B_2e^{-A} = (e^AB_1e^{-A})(e^AB_2e^{-A})$. So it is enough to know how $e^A$ transforms single creation and annihilation operators.
- **Expectation values:** $\langle0|e^{-A}He^{A}|0\rangle = \langle0|H|0\rangle - \langle0|[A,H]|0\rangle + \tfrac12\langle0|[A,[A,H]]|0\rangle - \cdots$. This is the generating formula for gradients and Hessians.

## The BCH formula for products of exponentials

**Statement (general knowledge; not in J-S).** For small $A$, $B$, $e^Ae^B = e^Z$ with

$$
Z = A + B + \frac12[A,B] + \frac1{12}\big([A,[A,B]] - [B,[A,B]]\big) - \frac1{24}[B,[A,[A,B]]] + \cdots
$$

Every term beyond $A + B$ is a nested commutator, so $e^Ae^B = e^{A+B}$ whenever $[A,B] = 0$.

**Uses.** It tells when two parametrizations are equivalent to a given order. For example, $e^{i\hat\lambda}e^{i\hat S}$ (orbital rotation followed by state rotation) and $e^{i(\hat\lambda + \hat S)}$ agree to first order but differ at second order by $\tfrac12[i\hat\lambda, i\hat S]$. This is one reason J-S fix the order of the two exponentials in MCSCF (Eq. 2.18). The BCH formula is also behind the Trotter splitting $e^{A+B}\approx e^Ae^B$ used in time propagation and quantum algorithms.

## When the series collapses

**One-body generators on single operators.** If $\hat\kappa = \sum\kappa_{pq}a_p^\dagger a_q$, then $[\hat\kappa, a_q^\dagger] = \sum_p a_p^\dagger\kappa_{pq}$. Every nested commutator is again a linear combination of creation operators, and the series sums to a matrix exponential:

$$
e^{\hat\kappa}a_q^\dagger e^{-\hat\kappa} = \sum_p a_p^\dagger\,[e^{\boldsymbol\kappa}]_{pq}.
$$

This is J-S Eqs. (1.41)-(1.44), the last step of their Ch. 1. The operator problem on the $2^n$-dimensional Fock space is reduced to an $n\times n$ matrix exponential ([[orbital-rotations]]).

**Terminating series.** If $[A,B]_k = 0$ for some $k$, the series is a finite polynomial. In coupled-cluster theory, $\hat H$ has at most four operators and each commutator with the excitation operator $\hat T$ removes at least one, so $[\hat H, \hat T]_5 = 0$ ([[coupled-cluster-second-quantization]]).

**Two-by-two rotation (J-S Problem 1.5).** With $\boldsymbol\kappa = \begin{pmatrix}0 & -\kappa\\ \kappa & 0\end{pmatrix}$, $\boldsymbol\kappa^2 = -\kappa^2\mathbf 1$, so the exponential series splits into even and odd parts:

$$
e^{-\boldsymbol\kappa} = \mathbf 1\Big(1 - \frac{\kappa^2}{2!} + \cdots\Big) + \begin{pmatrix}0 & 1\\ -1 & 0\end{pmatrix}\Big(\kappa - \frac{\kappa^3}{3!} + \cdots\Big) = \begin{pmatrix}\cos\kappa & \sin\kappa\\ -\sin\kappa & \cos\kappa\end{pmatrix}.
$$

For $\kappa = 10^\circ$: $\cos\kappa = 0.985$, $\sin\kappa = 0.174$.

## The second-order energy of a unitary transformation

**Real orbital rotation.** For $|\tilde0\rangle = e^{\hat\kappa}|0\rangle$ with $\hat\kappa$ anti-Hermitian, the Hadamard series gives

$$
E(\kappa) = \langle0|e^{-\hat\kappa}\hat He^{\hat\kappa}|0\rangle = E_0 + \langle0|[\hat H, \hat\kappa]|0\rangle + \tfrac12\langle0|[[\hat H, \hat\kappa], \hat\kappa]|0\rangle + O(\kappa^3).
$$

**Gradient and Hessian.** With $\hat\kappa = \sum_{p>q}\kappa_{pq}(a_p^\dagger a_q - a_q^\dagger a_p)$, the linear term gives the gradient and the double commutator gives the Hessian. J-S's Eqs. (2.24)-(2.31) are this formula, with orbital and state rotations together and the double commutator symmetrized ([[mcscf-second-order-optimization]]).

**Why the expansion is exact in form.** The expansion is a Taylor series of an exactly unitary parametrization. Every truncation still describes a normalized state; only the energy model is approximate. That is what makes Newton steps on $\kappa$ well defined ([[scf-second-order-and-stability]]).

!!! example "Numerical checks (computed for this note)"
    - **Hadamard series.** Random $6\times6$ matrices ($A$ scaled by 0.3): $e^ABe^{-A}$ against the commutator series summed to 30 terms agrees to $1.3\times10^{-15}$.
    - **BCH formula.** Random $6\times6$ matrices scaled by 0.05: the error of $\log(e^Ae^B)$ against the BCH series truncated after first, second, third and fourth order is $1.3\times10^{-2}$, $6.0\times10^{-4}$, $2.5\times10^{-5}$ and $8.5\times10^{-7}$. Each order gains a factor of about 25.
    - **Rank lowering.** All of J-S's Problem 1.2 identities, checked as $16\times16$ Fock-space matrices (Jordan-Wigner), hold exactly.
    - **Jacobi form of Eq. (2.32).** $\langle0|[\lambda,[H,\lambda]]|0\rangle - \langle0|[[\lambda,H],\lambda]|0\rangle = 0$ to machine precision for random symmetric $H$, antisymmetric $\lambda$ and a random state.
    - **Problem 1.5.** $e^{-\boldsymbol\kappa}$ for $\kappa = 10^\circ$ is $\begin{pmatrix}0.9848 & 0.1736\\ -0.1736 & 0.9848\end{pmatrix}$.

```python
from scipy.linalg import expm, logm
comm = lambda X, Y: X @ Y - Y @ X
lhs = expm(A) @ B @ expm(-A)                    # Hadamard series
term = B.copy(); s = B.copy()
for n in range(1, 30):
    term = comm(A, term) / n; s = s + term      # term = [A,B]_n / n!
Z = logm(expm(A) @ expm(B)).real                # BCH
z3 = A + B + comm(A, B) / 2 + (comm(A, comm(A, B)) - comm(B, comm(A, B))) / 12
```

## Source

Jørgensen and Simons, *Second Quantization-Based Methods in Quantum Chemistry* (Academic Press, New York, 1981), Ch. 1, Sec. D, Eqs. (1.40)-(1.44), pp. 10-11; Problems and Solutions 1.1, 1.2 and 1.5, pp. 13-17; Ch. 2, Eqs. (2.24)-(2.32), p. 23; Ch. 4, Eq. (4.13), p. 93. The derivation of the Hadamard series and the BCH formula for $\log(e^Ae^B)$ are general knowledge, not from J-S. Numerical checks computed for this note.
