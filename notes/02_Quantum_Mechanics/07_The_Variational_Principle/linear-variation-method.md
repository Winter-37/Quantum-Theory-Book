---
id: linear-variation-method
title: The linear variation method - the secular equation from a fixed basis
summary: Expanding the trial function in a fixed orthonormal basis turns energy minimization into diagonalizing the Hamiltonian matrix. Derivation with a Lagrange multiplier, meaning of all eigenvalues, and worked checks (excited-state bound, H atom in a field).
status: in-progress
kind: derivation
level: intermediate
tags: [basics, variational, linear-variation, secular-equation, matrix]
prerequisites: [variational-principle]
related: [upper-bounds-and-interlacing, matrix-eigenvalue-problem]
order: 30
date: 2026-10-31
---

## Setting and notation

Following Szabo and Ostlund, exact eigenvalues of $\hat H$ are written $\mathcal E_\alpha$ and eigenvalues obtained in a finite basis are written $E_\alpha$:

$$
\hat H|\Phi_\alpha\rangle = \mathcal E_\alpha|\Phi_\alpha\rangle,
\qquad \mathcal E_0 \le \mathcal E_1 \le \dots
$$

A trial function that depends on parameters has an energy $\langle\tilde\Phi|\hat H|\tilde\Phi\rangle$ that is a function of those parameters. In general this function is too complicated to minimize directly. If only **linear** variations are allowed, the problem reduces to matrix diagonalization.

Let $\{|\Psi_i\rangle\}_{i=1}^N$ be a **fixed** set of $N$ basis functions, assumed **real and orthonormal**:

$$
\langle\Psi_i|\Psi_j\rangle = \delta_{ij}.
$$

(The complex, non-orthogonal case is treated in Szabo Chapter 3.) The trial function is

$$
|\tilde\Phi\rangle = \sum_{i=1}^{N} c_i\,|\Psi_i\rangle ,
$$

with real coefficients $c_i$. The Hamiltonian matrix is

$$
H_{ij} = \langle\Psi_i|\hat H|\Psi_j\rangle .
$$

Since $\hat H$ is Hermitian and the basis is real, $\mathbf H$ is real symmetric: $H_{ij} = H_{ji}$.

## Derivation by constrained minimization

Normalization of the trial function and its energy are

$$
\langle\tilde\Phi|\tilde\Phi\rangle = \sum_{ij} c_i c_j\langle\Psi_i|\Psi_j\rangle = \sum_i c_i^2 = 1 ,
$$

$$
\langle\tilde\Phi|\hat H|\tilde\Phi\rangle = \sum_{ij} c_i c_j H_{ij} .
$$

We want the coefficients that minimize the energy. We cannot simply set $\partial\langle\tilde\Phi|\hat H|\tilde\Phi\rangle/\partial c_k = 0$ for all $k$, because the $c_k$ are not independent: the normalization constraint leaves only $N-1$ of them free.

**Lagrange multiplier.** Build

$$
\mathcal L(c_1,\dots,c_N,E) = \sum_{ij} c_i c_j H_{ij} - E\left(\sum_i c_i^2 - 1\right).
$$

On the normalized subspace the added term is zero, so $\mathcal L$ and the energy have their minimum at the same coefficients. Take $c_1,\dots,c_{N-1}$ as the independent ones (so $c_N$ is fixed by normalization). Then $\partial\mathcal L/\partial c_k = 0$ for $k=1,\dots,N-1$, but $\partial\mathcal L/\partial c_N$ is not automatically zero. The multiplier $E$ is still free, and we **choose** it so that this last derivative also vanishes:

$$
\frac{\partial\mathcal L}{\partial c_k} = 0, \qquad k = 1,\dots,N .
$$

Differentiating (the two terms of the double sum each contribute, and $H_{ij}=H_{ji}$):

$$
\frac{\partial\mathcal L}{\partial c_k}
= \sum_j c_j H_{kj} + \sum_i c_i H_{ik} - 2E c_k
= 2\left(\sum_j H_{kj}c_j - E c_k\right) = 0 .
$$

This gives $N$ equations, which in matrix form are

$$
\mathbf H\mathbf c = E\,\mathbf c .
\tag{1}
$$

This is the standard eigenvalue problem for the symmetric matrix $\mathbf H$.

**Meaning of the multiplier.** Multiplying the $k$-th equation by $c_k$ and summing gives $\mathbf c^{\mathsf T}\mathbf H\mathbf c = E\,\mathbf c^{\mathsf T}\mathbf c = E$. So $E$ is the energy of the trial function, not just a bookkeeping device.

## All $N$ solutions

A real symmetric $N\times N$ matrix has $N$ orthonormal eigenvectors $\mathbf c^\alpha$ with real eigenvalues, ordered $E_0 \le E_1 \le \dots \le E_{N-1}$:

$$
\mathbf H\mathbf c^\alpha = E_\alpha\mathbf c^\alpha,
\qquad
(\mathbf c^\alpha)^{\mathsf T}\mathbf c^\beta = \sum_i c_i^\alpha c_i^\beta = \delta_{\alpha\beta}.
$$

Collect them into the matrix $\mathbf C$ with $C_{i\alpha} = c_i^\alpha$ and the diagonal matrix $\mathbf E$ with $(\mathbf E)_{\alpha\beta} = E_\alpha\delta_{\alpha\beta}$. The $N$ equations combine into

$$
\mathbf H\mathbf C = \mathbf C\mathbf E .
\tag{2}
$$

So instead of one solution we get $N$ approximate states

$$
|\tilde\Phi_\alpha\rangle = \sum_{i=1}^N c_i^\alpha|\Psi_i\rangle = \sum_{i=1}^N C_{i\alpha}|\Psi_i\rangle,
\qquad \alpha = 0,1,\dots,N-1 .
$$

They are orthonormal:

$$
\langle\tilde\Phi_\alpha|\tilde\Phi_\beta\rangle
= \sum_{ij} c_i^\alpha c_j^\beta\,\delta_{ij}
= \sum_i c_i^\alpha c_i^\beta = \delta_{\alpha\beta},
$$

and diagonalize the Hamiltonian in the subspace:

$$
\langle\tilde\Phi_\beta|\hat H|\tilde\Phi_\alpha\rangle
= \sum_{ij} c_i^\beta H_{ij}c_j^\alpha
= (\mathbf c^\beta)^{\mathsf T}\mathbf H\mathbf c^\alpha
= E_\alpha\,\delta_{\alpha\beta}.
$$

Hence $E_\alpha$ is the expectation value of $\hat H$ in $|\tilde\Phi_\alpha\rangle$.

## What the eigenvalues mean

- **Ground state.** $E_0$ is the best approximation to the ground-state energy within the span of $\{|\Psi_i\rangle\}$, and by the variational principle (see [[variational-principle]])
$$
E_0 = \langle\tilde\Phi_0|\hat H|\tilde\Phi_0\rangle \;\ge\; \mathcal E_0 .
$$
- **Excited states.** The higher eigenvalues are also upper bounds: $E_\alpha \ge \mathcal E_\alpha$ for $\alpha = 1,2,\dots$. So $E_1$ bounds the first excited state from above, and so on. The case $\alpha=1$ is proved below. For general $\alpha$ the same idea is used, and a sharper statement (the eigenvalues can only go down as the basis grows) is the Hylleraas-Undheim-MacDonald theorem.

!!! note "Excited-state bound for the lowest excited state"
    Let $|\tilde\Phi'\rangle$ be normalized with $\langle\tilde\Phi'|\Phi_0\rangle = 0$, where $|\Phi_0\rangle$ is the **exact** ground state.

    **(a)** Expand in exact eigenstates, $c_\alpha = \langle\Phi_\alpha|\tilde\Phi'\rangle$. Orthogonality to $|\Phi_0\rangle$ means $c_0 = 0$, so
    $$
    \langle\tilde\Phi'|\hat H|\tilde\Phi'\rangle = \sum_{\alpha\ge1}\mathcal E_\alpha|c_\alpha|^2 \;\ge\; \mathcal E_1\sum_{\alpha\ge1}|c_\alpha|^2 = \mathcal E_1 .
    $$

    **(b)** Take $|\tilde\Phi'\rangle = x|\tilde\Phi_0\rangle + y|\tilde\Phi_1\rangle$ with the orthonormal states above. Normalization gives
    $$
    |x|^2 + |y|^2 = 1 .
    $$

    **(c)** Using $\langle\tilde\Phi_\alpha|\hat H|\tilde\Phi_\beta\rangle = E_\alpha\delta_{\alpha\beta}$ and $|y|^2 = 1-|x|^2$,
    $$
    \langle\tilde\Phi'|\hat H|\tilde\Phi'\rangle
    = E_0|x|^2 + E_1|y|^2
    = E_1 - |x|^2(E_1 - E_0).
    $$
    Now choose $x,y$ so that $|\tilde\Phi'\rangle$ is normalized and orthogonal to $|\Phi_0\rangle$. Part (a) gives $\mathcal E_1 \le E_1 - |x|^2(E_1-E_0)$, and since $E_1 \ge E_0$ the right side is at most $E_1$. Therefore
    $$
    E_1 \ge \mathcal E_1 .
    $$

## Equivalent route: projecting the Schrödinger equation

Equation (1) can also be reached without minimizing anything. Insert the expansion $|\Phi\rangle \approx \sum_j c_j|\Psi_j\rangle$ into $\hat H|\Phi\rangle = \mathcal E|\Phi\rangle$:

$$
\sum_j c_j\hat H|\Psi_j\rangle = \mathcal E\sum_j c_j|\Psi_j\rangle .
$$

Multiply from the left by $\langle\Psi_i|$ and replace $\mathcal E$ by $E$ (to remind us the expansion is approximate):

$$
\sum_j c_j\langle\Psi_i|\hat H|\Psi_j\rangle = E\sum_j c_j\langle\Psi_i|\Psi_j\rangle
\;\Longrightarrow\;
\sum_j H_{ij}c_j = E\,c_i ,
$$

which is the same as (1). If the basis were **complete** and orthonormal, $\mathbf H$ would be an infinite matrix whose eigenvalues are exactly those of $\hat H$. The linear variational method is therefore the same as solving the eigenvalue equation $\hat H|\Phi\rangle = \mathcal E|\Phi\rangle$ in the finite subspace spanned by $\{|\Psi_i\rangle\}_{i=1}^N$. This view carries over directly to the secular equation and to Roothaan-type equations later on.

!!! warning "Assumptions to keep in mind"
    Real, orthonormal basis functions and a real symmetric $\mathbf H$ are used above. With a non-orthogonal basis (overlap matrix $\mathbf S \ne \mathbf 1$) the equation becomes a generalized eigenvalue problem $\mathbf H\mathbf c = E\mathbf S\mathbf c$. The result $E_0 \ge \mathcal E_0$ still holds, but (1) no longer applies as written.

## Worked example: hydrogen atom in a uniform field

**Problem.** In atomic units, a hydrogen atom in a uniform field $F$ along $z$ has

$$
\hat H = \hat H_0 + F r\cos\theta,
\qquad
\hat H_0 = -\tfrac12\nabla^2 - \tfrac1r .
$$

Use the two-function basis of normalized eigenfunctions of $\hat H_0$:

$$
|1s\rangle = \pi^{-1/2}e^{-r},
\qquad
|2p_z\rangle = (32\pi)^{-1/2}\,r\,e^{-r/2}\cos\theta ,
$$

with $\hat H_0|1s\rangle = -\tfrac12|1s\rangle$ and $\hat H_0|2p_z\rangle = -\tfrac18|2p_z\rangle$.

!!! example "Matrix and secular equation"
    **Matrix elements.** The two functions are orthonormal. The diagonal elements of $\hat H_0$ are the eigenvalues above. The perturbation $Fr\cos\theta$ is odd under inversion, while $|1s\rangle$ and $|2p_z\rangle$ have opposite parity, so it has no diagonal elements and only couples the two functions:
    $$
    \mathbf H =
    \begin{pmatrix}
    -\tfrac12 & F M\\
    F M & -\tfrac18
    \end{pmatrix},
    \qquad
    M = \langle 1s|\,r\cos\theta\,|2p_z\rangle .
    $$

    **The integral.** Using $\mathrm d^3r = r^2\sin\theta\,\mathrm dr\,\mathrm d\theta\,\mathrm d\phi$, the angular part gives $\int\cos^2\theta\sin\theta\,\mathrm d\theta\,\mathrm d\phi = 4\pi/3$ and the radial part is $\int_0^\infty r^4 e^{-3r/2}\,\mathrm dr = 4!\,(2/3)^5$. Together with the normalization constants,
    $$
    M = \frac{1}{\pi^{1/2}(32\pi)^{1/2}}\cdot\frac{4\pi}{3}\cdot 24\left(\frac23\right)^5
    = \frac{128\sqrt2}{243} \approx 0.7449 .
    $$

    **Lowest eigenvalue.** For a $2\times2$ symmetric matrix the lower root of $\det(\mathbf H - E\mathbf 1)=0$ is
    $$
    E(F) = \frac{H_{11}+H_{22}}{2} - \sqrt{\left(\frac{H_{11}-H_{22}}{2}\right)^2 + H_{12}^2}
    = -\frac{5}{16} - \sqrt{\frac{9}{256} + M^2F^2}.
    $$
    At $F=0$ this gives $E(0) = -\tfrac5{16}-\tfrac3{16} = -\tfrac12$, the exact ground-state energy, as it must.

    **Expansion in $F$.** Using $(1+x)^{1/2}\simeq 1 + x/2$ with $\sqrt{9/256 + M^2F^2} = \tfrac{3}{16}\sqrt{1 + \tfrac{256}{9}M^2F^2}$:
    $$
    E(F) \simeq -\frac12 - \frac{8}{3}M^2F^2 .
    $$
    Comparing with $E(F) = E(0) - \tfrac12\alpha F^2 + \cdots$ gives the polarizability
    $$
    \alpha = \frac{16}{3}M^2 = \frac{2^{19}}{3^{11}} \approx 2.96 \ \text{(atomic units, bohr}^3\text{)} .
    $$
    The exact value is $4.5$, so two functions recover about 66% of it. The error comes from the truncated basis: the true response mixes in all higher $p$ states and the continuum. Because the energy is variational, $E(F)$ lies above the exact $\mathcal E(F)$ for every $F$, and hence $\alpha_{\text{approx}}$ underestimates the exact one.

Quick numerical check of the closed forms:

```python
import numpy as np

M = 128 * np.sqrt(2) / 243          # <1s| r cos(theta) |2pz>
alpha = 16 / 3 * M**2

def E_lowest(F):
    H = np.array([[-0.5, M * F],
                  [M * F, -0.125]])
    return np.linalg.eigvalsh(H)[0]

F = 0.01
print(E_lowest(F), -0.5 - 0.5 * alpha * F**2)   # -0.50014792  -0.50014798
print(alpha)                                     # 2.9596
```

## Source

Szabo and Ostlund, *Modern Quantum Chemistry*, Sec. 1.3.2 (The Linear Variational Problem, pp. 33-37, Eqs. 1.153-1.176) and Exercises 1.21-1.22 (pp. 36-38). Edition and year: add here.
