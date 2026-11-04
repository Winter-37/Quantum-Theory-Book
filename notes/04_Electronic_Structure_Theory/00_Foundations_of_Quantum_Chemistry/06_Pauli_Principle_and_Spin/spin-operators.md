---
id: spin-operators
title: Spin operators for one and many electrons
summary: One-electron spin operators and ladder operators acting on α and β, their 2x2 matrices, the many-electron total spin S² = S₋S₊ + S_z + S_z², why exact states are spin eigenfunctions, and why every determinant is an S_z eigenfunction but not necessarily an S² eigenfunction.
status: in-progress
kind: theory
level: introductory
tags: [spin, angular-momentum, s-squared, ladder-operators, multiplicity]
prerequisites: [spin-orbitals-and-antisymmetry, slater-determinants]
related: [spin-adapted-configurations]
also: []
date: 2026-11-03
---

## One electron

The spin $\hat{\mathbf s} = \hat s_x\mathbf i + \hat s_y\mathbf j + \hat s_z\mathbf k$ obeys ($\hbar = 1$)

$$
[\hat s_x,\hat s_y] = \mathrm i\hat s_z,\qquad
[\hat s_y,\hat s_z] = \mathrm i\hat s_x,\qquad
[\hat s_z,\hat s_x] = \mathrm i\hat s_y,
\qquad
\hat s^2 = \hat s_x^2 + \hat s_y^2 + \hat s_z^2 .
$$

States are labelled by $\hat s^2|s,m_s\rangle = s(s+1)|s,m_s\rangle$ and $\hat s_z|s,m_s\rangle = m_s|s,m_s\rangle$. For an electron $s = \tfrac12$ and $|\tfrac12,\tfrac12\rangle = |\alpha\rangle$, $|\tfrac12,-\tfrac12\rangle = |\beta\rangle$:

$$
\hat s^2|\alpha\rangle = \tfrac34|\alpha\rangle,\quad \hat s^2|\beta\rangle = \tfrac34|\beta\rangle,
\qquad
\hat s_z|\alpha\rangle = \tfrac12|\alpha\rangle,\quad \hat s_z|\beta\rangle = -\tfrac12|\beta\rangle,
$$

$$
\hat s_x|\alpha\rangle = \tfrac12|\beta\rangle,\quad \hat s_x|\beta\rangle = \tfrac12|\alpha\rangle,
\qquad
\hat s_y|\alpha\rangle = \tfrac{\mathrm i}{2}|\beta\rangle,\quad \hat s_y|\beta\rangle = -\tfrac{\mathrm i}{2}|\alpha\rangle .
$$

**Ladder operators** $\hat s_\pm = \hat s_x \pm \mathrm i\hat s_y$ shift $m_s$ by $\pm1$:

$$
\hat s_+|\alpha\rangle = 0,\quad \hat s_+|\beta\rangle = |\alpha\rangle,
\qquad
\hat s_-|\alpha\rangle = |\beta\rangle,\quad \hat s_-|\beta\rangle = 0 .
$$

(Check: $\hat s_+|\beta\rangle = \tfrac12|\alpha\rangle + \mathrm i(-\tfrac{\mathrm i}{2})|\alpha\rangle = |\alpha\rangle$.)

From the commutators, $\hat s_+\hat s_- = \hat s_x^2 + \hat s_y^2 - \mathrm i[\hat s_x,\hat s_y] = \hat s_x^2 + \hat s_y^2 + \hat s_z$, and similarly for $\hat s_-\hat s_+$. Hence

$$
\hat s^2 = \hat s_+\hat s_- - \hat s_z + \hat s_z^2 = \hat s_-\hat s_+ + \hat s_z + \hat s_z^2 .
$$

!!! example "2x2 matrices in the basis {α, β} (Szabo Ex. 2.33)"
    $$
    \mathbf s_z = \tfrac12\begin{pmatrix}1&0\\0&-1\end{pmatrix},\quad
    \mathbf s_+ = \begin{pmatrix}0&1\\0&0\end{pmatrix},\quad
    \mathbf s_- = \begin{pmatrix}0&0\\1&0\end{pmatrix},\quad
    \mathbf s^2 = \tfrac34\begin{pmatrix}1&0\\0&1\end{pmatrix}.
    $$
    Check the identity: $\mathbf s_-\mathbf s_+ = \operatorname{diag}(0,1)$, $\mathbf s_z = \operatorname{diag}(\tfrac12,-\tfrac12)$, $\mathbf s_z^2 = \operatorname{diag}(\tfrac14,\tfrac14)$. The sum is $\operatorname{diag}(\tfrac34,\tfrac34) = \mathbf s^2$. Likewise $\mathbf s_+\mathbf s_- - \mathbf s_z + \mathbf s_z^2 = \operatorname{diag}(1,0) + \operatorname{diag}(-\tfrac12,\tfrac12) + \tfrac14\mathbf 1 = \tfrac34\mathbf 1$.

    $[\hat s^2,\hat s_z] = 0$ (Szabo Ex. 2.34) follows from $[\hat s_x^2,\hat s_z] = \hat s_x[\hat s_x,\hat s_z] + [\hat s_x,\hat s_z]\hat s_x = -\mathrm i(\hat s_x\hat s_y + \hat s_y\hat s_x)$ and $[\hat s_y^2,\hat s_z] = +\mathrm i(\hat s_y\hat s_x + \hat s_x\hat s_y)$, which cancel.

## Many electrons

The total spin is the vector sum, so its components and ladder operators are one-electron sums:

$$
\hat{\mathcal S}_\lambda = \sum_{i=1}^N\hat s_\lambda(i)\ \ (\lambda = x,y,z),
\qquad
\hat{\mathcal S}_\pm = \sum_{i=1}^N\hat s_\pm(i).
$$

The square $\hat{\mathcal S}^2 = \hat{\mathcal S}\cdot\hat{\mathcal S} = \sum_{ij}\hat{\mathbf s}(i)\cdot\hat{\mathbf s}(j)$ contains one-electron terms ($i=j$) and two-electron terms ($i\ne j$), and satisfies the same identity:

$$
\hat{\mathcal S}^2 = \hat{\mathcal S}_+\hat{\mathcal S}_- - \hat{\mathcal S}_z + \hat{\mathcal S}_z^2 = \hat{\mathcal S}_-\hat{\mathcal S}_+ + \hat{\mathcal S}_z + \hat{\mathcal S}_z^2 .
$$

**Exact states are spin eigenfunctions.** The nonrelativistic Hamiltonian contains no spin, so $[\hat H,\hat{\mathcal S}^2] = 0 = [\hat H,\hat{\mathcal S}_z]$, and exact eigenstates can be chosen with

$$
\hat{\mathcal S}^2|\Phi\rangle = S(S+1)|\Phi\rangle,
\qquad
\hat{\mathcal S}_z|\Phi\rangle = M_S|\Phi\rangle .
$$

$S = 0,\tfrac12,1,\tfrac32,\dots$ gives multiplicity $2S+1$: singlet, doublet, triplet, quartet, and so on. Approximate wave functions need not be pure spin states, but it is often useful to constrain them to be.

Two general facts behind this:

- **Szabo Ex. 2.35.** If $[\hat{\mathcal A},\hat H] = 0$ and $\hat H|\Phi\rangle = E|\Phi\rangle$, then $\hat H(\hat{\mathcal A}|\Phi\rangle) = E\,\hat{\mathcal A}|\Phi\rangle$. For a nondegenerate $E$ this forces $\hat{\mathcal A}|\Phi\rangle\propto|\Phi\rangle$. With degeneracy, combinations can be chosen that are simultaneous eigenfunctions.
- **Szabo Ex. 2.36.** If $\hat{\mathcal A}$ is Hermitian, commutes with $\hat H$, and $\hat{\mathcal A}|\Psi_i\rangle = a_i|\Psi_i\rangle$ with $a_1\ne a_2$, then
$$
a_1\langle\Psi_1|\hat H|\Psi_2\rangle = \langle\Psi_1|\hat{\mathcal A}\hat H|\Psi_2\rangle = \langle\Psi_1|\hat H\hat{\mathcal A}|\Psi_2\rangle = a_2\langle\Psi_1|\hat H|\Psi_2\rangle,
$$
so $\langle\Psi_1|\hat H|\Psi_2\rangle = 0$. Singlet and triplet configurations never mix through $\hat H$, which is why CI can be done one spin symmetry at a time.

## Determinants and spin

**Every determinant is an $\hat{\mathcal S}_z$ eigenfunction (Szabo Ex. 2.37).** $\hat{\mathcal S}_z$ is symmetric in the electron labels, so it commutes with antisymmetrization. On each Hartree product it gives $\tfrac12$ per $\alpha$ and $-\tfrac12$ per $\beta$ spin orbital. With $N^\alpha$ and $N^\beta$ the numbers of $\alpha$ and $\beta$ spin orbitals,

$$
\hat{\mathcal S}_z|\chi_i\chi_j\cdots\chi_k\rangle = \tfrac12(N^\alpha - N^\beta)\,|\chi_i\chi_j\cdots\chi_k\rangle = M_S\,|\chi_i\cdots\chi_k\rangle .
$$

**It is not necessarily an $\hat{\mathcal S}^2$ eigenfunction.** Whether a determinant is pure in $S$ depends on its spatial orbitals. Closed-shell restricted determinants are singlets, high-spin open shells are pure, and most other open-shell or unrestricted determinants are not (see [[spin-adapted-configurations]]).

**Second-quantized forms.** For spin orbitals $\psi_p\alpha$, $\psi_p\beta$ with annihilators $a_{p\alpha}$, $a_{p\beta}$ over orthonormal spatial orbitals $p$:

$$
\hat{\mathcal S}_z = \tfrac12\sum_p(\hat n_{p\alpha} - \hat n_{p\beta}),
\qquad
\hat{\mathcal S}_+ = \sum_p a_{p\alpha}^\dagger a_{p\beta},
\qquad
\hat{\mathcal S}_- = \sum_p a_{p\beta}^\dagger a_{p\alpha}.
$$

This form (standard, e.g. Helgaker-Jørgensen-Olsen Ch. 2) is what codes use to evaluate $\langle\hat{\mathcal S}^2\rangle$.

## Source

Szabo and Ostlund, *Modern Quantum Chemistry* (Dover, 1996; reprint of the revised first edition, McGraw-Hill, 1989), Sec. 2.5.1, pp. 97-100, Eqs. (2.240)-(2.254), Ex. 2.32-2.37. The second-quantized spin operators are standard results not taken from Szabo.
