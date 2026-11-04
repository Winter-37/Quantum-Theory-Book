---
id: rayleigh-schrodinger-perturbation-theory
title: Rayleigh-Schrödinger perturbation theory - energies through fourth order, the two-state model, diagrams and resummation
summary: Derivation of the RS energy expressions with intermediate normalization, E(n) = ⟨i|V|Ψ(n−1)⟩, explicit E(2) and E(3), the two-state model expanded to fourth order (including the renormalization term), Szabo's two-state diagram rules, the geometric summation of diagonal diagrams as a shifted denominator (repartitioning), and an exact order-by-order recursion checked numerically.
status: in-progress
kind: derivation
level: intermediate
tags: [perturbation-theory, rayleigh-schrodinger, intermediate-normalization, diagrams, partitioning, resummation]
prerequisites: [linear-variation-method, matrix-eigenvalue-problem, dirac-notation]
related: [perturbation-theory-second-quantization, mp2, mp3, orbital-perturbation-theory, linked-cluster-theorem, iepa]
also: []
date: 2026-11-03
---

## Setup

**Problem.** Solve $\mathscr H|\Phi_i\rangle = (\mathscr H_0 + \mathscr V)|\Phi_i\rangle = \mathscr E_i|\Phi_i\rangle$ when the eigenpairs of $\mathscr H_0$ are known, $\mathscr H_0|i\rangle = E_i^{(0)}|i\rangle$, and $\mathscr V$ is "small".

**Ordering parameter.** Write $\mathscr H = \mathscr H_0 + \lambda\mathscr V$ and expand

$$
\mathscr E_i = E_i^{(0)} + \lambda E_i^{(1)} + \lambda^2E_i^{(2)} + \cdots,
\qquad
|\Phi_i\rangle = |i\rangle + \lambda|\Psi_i^{(1)}\rangle + \lambda^2|\Psi_i^{(2)}\rangle + \cdots,
$$

setting $\lambda = 1$ at the end. $E_i^{(n)}$ is the $n$th-order energy.

**Intermediate normalization.** Choose $\langle i|\Phi_i\rangle = 1$ (possible unless the exact state is orthogonal to $|i\rangle$). Since this holds for every $\lambda$, all corrections are orthogonal to the reference: $\langle i|\Psi_i^{(n)}\rangle = 0$ for $n\ge1$.

## Order-by-order equations

Equating powers of $\lambda$:

$$
\begin{aligned}
\mathscr H_0|i\rangle &= E_i^{(0)}|i\rangle,\\
\mathscr H_0|\Psi_i^{(1)}\rangle + \mathscr V|i\rangle &= E_i^{(0)}|\Psi_i^{(1)}\rangle + E_i^{(1)}|i\rangle,\\
\mathscr H_0|\Psi_i^{(2)}\rangle + \mathscr V|\Psi_i^{(1)}\rangle &= E_i^{(0)}|\Psi_i^{(2)}\rangle + E_i^{(1)}|\Psi_i^{(1)}\rangle + E_i^{(2)}|i\rangle,
\end{aligned}
$$

and in general $(E_i^{(0)} - \mathscr H_0)|\Psi_i^{(n)}\rangle = \mathscr V|\Psi_i^{(n-1)}\rangle - \sum_{k=1}^{n}E_i^{(k)}|\Psi_i^{(n-k)}\rangle$.

**Energies.** Multiplying by $\langle i|$ and using the orthogonality:

$$
E_i^{(0)} = \langle i|\mathscr H_0|i\rangle,\qquad
E_i^{(1)} = \langle i|\mathscr V|i\rangle,\qquad
E_i^{(n)} = \langle i|\mathscr V|\Psi_i^{(n-1)}\rangle\quad(n\ge2).
$$

**First-order wave function.** Expand in the complete set $\{|n\rangle\}$, excluding $n = i$: $|\Psi_i^{(1)}\rangle = \sum_n{}'|n\rangle\langle n|\Psi_i^{(1)}\rangle$ with $\langle n|\Psi_i^{(1)}\rangle = \langle n|\mathscr V|i\rangle/(E_i^{(0)} - E_n^{(0)})$. Hence

$$
E_i^{(2)} = \sum_n{}'\frac{\langle i|\mathscr V|n\rangle\langle n|\mathscr V|i\rangle}{E_i^{(0)} - E_n^{(0)}} = \sum_n{}'\frac{|V_{in}|^2}{E_i^{(0)} - E_n^{(0)}} .
$$

For the ground state every denominator is negative, so $E_0^{(2)}\le0$.

**Third order.** Expanding $|\Psi_i^{(2)}\rangle$ the same way and using the $n = 2$ equation:

$$
E_i^{(3)} = A_i^{(3)} + B_i^{(3)},
\qquad
A_i^{(3)} = \sum_{n,m}{}'\frac{V_{in}V_{nm}V_{mi}}{(E_i^{(0)} - E_n^{(0)})(E_i^{(0)} - E_m^{(0)})},
\qquad
B_i^{(3)} = -V_{ii}\sum_n{}'\frac{|V_{in}|^2}{(E_i^{(0)} - E_n^{(0)})^2}.
$$

$B^{(3)}$ is the **renormalization term**. For a large system it is the piece that grows too fast with system size and must cancel against part of $A^{(3)}$ ([[linked-cluster-theorem]]).

**$(2n+1)$ rule (general knowledge, not from Szabo).** $|\Psi^{(n)}\rangle$ determines the energy through order $2n+1$. For example, $E^{(3)} = \langle\Psi^{(1)}|\mathscr V - E^{(1)}|\Psi^{(1)}\rangle$, which is the same expression as above.

## The two-state model

**Exact answer.** With $\mathscr H_0 = \operatorname{diag}(E_1^{(0)}, E_2^{(0)})$, $E_1^{(0)} < E_2^{(0)}$, and $\mathscr V$ with elements $V_{11}, V_{12}, V_{21}, V_{22}$, the lower eigenvalue is

$$
\mathscr E_1 = \tfrac12\Big[E_1^{(0)} + V_{11} + E_2^{(0)} + V_{22} - \Big(\big(E_2^{(0)} - E_1^{(0)} + V_{22} - V_{11}\big)^2 + 4V_{12}V_{21}\Big)^{1/2}\Big].
$$

**Taylor expansion.** Scale every $V$ by $\lambda$, expand the square root and the inverse, and collect powers. With $\Delta E = E_1^{(0)} - E_2^{(0)} < 0$:

$$
E^{(1)} = V_{11},\qquad
E^{(2)} = \frac{V_{12}V_{21}}{\Delta E},\qquad
E^{(3)} = \frac{V_{12}V_{22}V_{21}}{\Delta E^2} - \frac{V_{11}V_{12}V_{21}}{\Delta E^2},
$$

$$
E^{(4)} = \frac{V_{12}V_{22}V_{22}V_{21}}{\Delta E^3} - 2\frac{V_{11}V_{12}V_{22}V_{21}}{\Delta E^3} + \frac{V_{11}^2V_{12}V_{21}}{\Delta E^3} - \frac{(V_{12}V_{21})^2}{\Delta E^3}.
$$

The general RS formulas with the single intermediate state $|n\rangle = |2\rangle$ reproduce $E^{(1)}$-$E^{(3)}$ term by term, as they must: both are Taylor expansions in $\lambda$.

!!! example "Numerical check (computed for this note)"
    $E_1^{(0)} = 0$, $E_2^{(0)} = 1$, $V_{11} = 0.10$, $V_{22} = -0.05$, $V_{12} = V_{21} = 0.20$.

    - **Formulas above:** $E^{(1)} = 0.1$, $E^{(2)} = -0.04$, $E^{(3)} = -0.006$, $E^{(4)} = 0.0007$; sum 0.054700.
    - **Exact recursion below:** identical through fourth order, then $E^{(5)} = 0.000585$, $E^{(6)} = 0.0000678$, $E^{(7)} = -0.0000450$.
    - **Exact eigenvalue:** 0.055293. The partial sums 0.0547, 0.055285, 0.055353, 0.055308 oscillate into it.
    - **Without** the $-(V_{12}V_{21})^2/\Delta E^3$ term, $E^{(4)}$ would be −0.0009 instead of 0.0007.

## Diagrams for the two-state problem

Szabo introduces a pictorial bookkeeping that later becomes the Goldstone/Hugenholtz diagrams of many-body theory.

**Drawing.** A dot stands for $\mathscr V$, a line with a downward arrow for state $|1\rangle$ (a "hole line") and an upward arrow for $|2\rangle$ (a "particle line"). For order $n$:

1. Place $n$ dots in a vertical column.
2. Join them with one continuous line so that each dot has one line in and one line out. Only connected (linked) diagrams are drawn.
3. Draw all topologically distinct ways, then put arrows on the line in every allowed way and label down-lines 1 and up-lines 2. A first-order closed circle counts as a hole line.

**Translation rules.**

1. Each dot contributes $\langle\text{label in}|\mathscr V|\text{label out}\rangle$.
2. Each gap between adjacent dots contributes a denominator $\sum(\text{hole labels}) - \sum(\text{particle labels})$ of zeroth-order energies, summed over the lines that the cut crosses.
3. The sign is $(-1)^{h+l}$, where $h$ is the number of hole lines and $l$ the number of closed loops.

The diagrams with a hole line crossing a gap carry denominators such as $2E_1^{(0)} - 2E_2^{(0)}$; they generate the renormalization terms, including the $-(V_{12}V_{21})^2/\Delta E^3$ term of $E^{(4)}$. For $N$ states the particle lines are labelled $n, m, \ldots = 2,\ldots,N$ and summed independently.

## Resummation = repartitioning

**Geometric series.** In the two-state problem take the second-order diagram and add dots on the particle and hole lines in all possible ways (diagonal insertions only). The values form a geometric series:

$$
\frac{V_{12}V_{21}}{\Delta E}\Big[1 + \frac{V_{22} - V_{11}}{\Delta E} + \Big(\frac{V_{22} - V_{11}}{\Delta E}\Big)^2 + \cdots\Big]
= \frac{V_{12}V_{21}}{(E_1^{(0)} + V_{11}) - (E_2^{(0)} + V_{22})}.
$$

**Interpretation.** Summing this class to infinite order gives the second-order expression with a **shifted denominator**. Equivalently, it is plain second-order theory with the repartitioned zeroth-order Hamiltonian

$$
\mathscr H_0' = \begin{pmatrix}E_1^{(0)} + V_{11} & 0\\ 0 & E_2^{(0)} + V_{22}\end{pmatrix},
\qquad
\mathscr V' = \begin{pmatrix}0 & V_{12}\\ V_{21} & 0\end{pmatrix}.
$$

For $N$ states the same summation gives $\sum_n{}'|V_{1n}|^2/\big((E_1^{(0)} + V_{11}) - (E_n^{(0)} + V_{nn})\big)$. Applied to the many-electron problem with the Hartree-Fock reference, this is exactly the Epstein-Nesbet pair formula ([[iepa]], [[linked-cluster-theorem]]).

## Exact recursion to any order

The order-$n$ equation gives a direct algorithm when $\mathscr H_0$ is diagonal in the chosen basis:

$$
|\Psi^{(n)}\rangle = (E_0^{(0)} - \mathscr H_0)^{-1}\mathcal Q\Big[\mathscr V|\Psi^{(n-1)}\rangle - \sum_{k=1}^{n}E^{(k)}|\Psi^{(n-k)}\rangle\Big],
\qquad
E^{(n+1)} = \langle 0|\mathscr V|\Psi^{(n)}\rangle,
$$

with $\mathcal Q = 1 - |0\rangle\langle0|$. (The $k = n$ term vanishes after projection; it is kept for clarity.)

```python
psi = [np.zeros(dim) for _ in range(N)]; E = [0.0] * N
psi[0][ref] = 1.0; E[0] = H0d[ref]; E[1] = V[ref, ref]
denom = E[0] - H0d; denom[ref] = np.inf          # resolvent, reference excluded
for n in range(1, N - 1):
    rhs = V @ psi[n - 1] - sum(E[k] * psi[n - k] for k in range(1, n + 1))
    psi[n] = rhs / denom; psi[n][ref] = 0.0
    E[n + 1] = V[ref] @ psi[n]
```

Run in the full determinant space of a molecule with $\mathscr H_0$ = sum of Fock operators, this generates the Møller-Plesset series to any order; the water results are in [[mp3]].

## Source

Szabo and Ostlund, *Modern Quantum Chemistry* (Dover, 1996; reprint of the revised first edition, McGraw-Hill, 1989), Sec. 6.1, pp. 322-326, Eqs. (6.1)-(6.23); Sec. 6.2, pp. 327-338, Table 6.1 rules, Eqs. (6.25)-(6.29). The $(2n+1)$ remark is general knowledge. Numerical examples computed for this note.
