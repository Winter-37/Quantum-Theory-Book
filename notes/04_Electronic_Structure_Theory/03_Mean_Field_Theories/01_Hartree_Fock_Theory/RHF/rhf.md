---
id: rhf
title: Restricted closed-shell Hartree-Fock and the Roothaan equations
summary: Integrating out spin for a closed shell gives the spatial Fock operator f = h + Σ_a (2J_a − K_a). Expanding the orbitals in K basis functions turns it into the generalized matrix eigenvalue problem FC = SCε, with the density matrix P, the Fock matrix F(P), and the energy E0 = ½ Σ P(H + F). Worked STO-3G H2 values.
status: in-progress
kind: derivation
level: intermediate
tags: [hartree-fock, rhf, roothaan-hall, closed-shell, density-matrix, fock-matrix, lcao]
prerequisites: [hartree-fock-equations, fock-operator, spin-orbital-to-spatial-orbital]
related: [scf-procedure, basis-orthogonalization, uhf, population-analysis, minimal-basis-h2-model, gaussian-basis-functions]
also: []
date: 2026-11-03
---

## Closed-shell spatial equations

A closed-shell determinant has $N/2$ doubly occupied spatial orbitals,

$$
|\Psi_0\rangle = |\psi_1\bar\psi_1\cdots\psi_a\bar\psi_a\cdots\psi_{N/2}\bar\psi_{N/2}\rangle .
$$

Insert $\chi = \psi\alpha$ into $f\chi = \varepsilon\chi$ ([[fock-operator]]), multiply by $\alpha^*$, and integrate over spin. The sum over occupied spin orbitals splits into $\alpha$ and $\beta$ halves:

- **Coulomb.** Both halves contribute, giving $2J_a$.
- **Exchange.** Only the same-spin half contributes, giving $K_a$.

The **closed-shell Fock operator** is

$$
f(\mathbf r_1) = h(\mathbf r_1) + \sum_a^{N/2}\big[2J_a(\mathbf r_1) - K_a(\mathbf r_1)\big],
\qquad
f\,\psi_j = \varepsilon_j\psi_j ,
$$

with spatial Coulomb and exchange operators

$$
J_a(1)\psi(1) = \Big[\int\mathrm d\mathbf r_2\,\psi_a^*(2)r_{12}^{-1}\psi_a(2)\Big]\psi(1),
\qquad
K_a(1)\psi(1) = \Big[\int\mathrm d\mathbf r_2\,\psi_a^*(2)r_{12}^{-1}\psi(2)\Big]\psi_a(1).
$$

**Orbital energies and total energy (Szabo Ex. 3.9).**

$$
\varepsilon_i = h_{ii} + \sum_a^{N/2}\big(2J_{ia} - K_{ia}\big),
\qquad
E_0 = 2\sum_a h_{aa} + \sum_{ab}\big(2J_{ab} - K_{ab}\big) = \sum_a^{N/2}\big(h_{aa} + \varepsilon_a\big).
$$

## Introducing a basis: the Roothaan equations

Expand each spatial MO in $K$ known basis functions $\{\phi_\mu\}$, which are generally not orthogonal:

$$
\psi_i(\mathbf r) = \sum_{\mu=1}^{K}C_{\mu i}\,\phi_\mu(\mathbf r),
\qquad i = 1,\dots,K .
$$

Substitute into $f\psi_i = \varepsilon_i\psi_i$, multiply by $\phi_\mu^*$ and integrate:

$$
\sum_\nu F_{\mu\nu}C_{\nu i} = \varepsilon_i\sum_\nu S_{\mu\nu}C_{\nu i}
\qquad\Longleftrightarrow\qquad
\mathbf F\mathbf C = \mathbf S\mathbf C\boldsymbol\varepsilon ,
$$

with

$$
S_{\mu\nu} = \int\mathrm d\mathbf r_1\,\phi_\mu^*(1)\phi_\nu(1),
\qquad
F_{\mu\nu} = \int\mathrm d\mathbf r_1\,\phi_\mu^*(1)f(1)\phi_\nu(1),
$$

$\mathbf C$ the $K\times K$ coefficient matrix (MOs in columns), and $\boldsymbol\varepsilon$ diagonal. These are the **Roothaan (Roothaan-Hall) equations**. Orthonormal MOs require

$$
\mathbf C^\dagger\mathbf S\mathbf C = \mathbf 1
$$

(Szabo Ex. 3.10). For $\mathbf S = \mathbf 1$ the problem reduces to an ordinary eigenvalue problem. Otherwise orthogonalize first ([[basis-orthogonalization]]).

## The density matrix

The total closed-shell electron density is

$$
\rho(\mathbf r) = 2\sum_a^{N/2}|\psi_a(\mathbf r)|^2 = \sum_{\mu\nu}P_{\mu\nu}\,\phi_\mu(\mathbf r)\phi_\nu^*(\mathbf r),
\qquad
P_{\mu\nu} = 2\sum_a^{N/2}C_{\mu a}C_{\nu a}^* .
$$

$\int\rho = N$ becomes

$$
\operatorname{tr}(\mathbf{PS}) = \sum_{\mu\nu}P_{\mu\nu}S_{\nu\mu} = N .
$$

$\rho(\mathbf r)$ is also the expectation value of $\hat\rho(\mathbf r) = \sum_i\delta(\mathbf r_i - \mathbf r)$ (Szabo Ex. 3.11).

**Idempotency (Szabo Ex. 3.12).** From $\mathbf C^\dagger\mathbf{SC} = \mathbf 1$ restricted to occupied columns,

$$
\mathbf{PSP} = 2\mathbf P ,
$$

so $\tfrac12\mathbf P$ is idempotent in the metric $\mathbf S$. It projects onto the occupied space, the defining property of a single-determinant density.

## The Fock matrix

The Fock operator depends on the orbitals only through $\mathbf P$ (Szabo Ex. 3.13):

$$
f(\mathbf r_1) = h(\mathbf r_1) + \tfrac12\sum_{\lambda\sigma}P_{\lambda\sigma}\int\mathrm d\mathbf r_2\ \phi_\sigma^*(2)\,\big(2 - \mathscr P_{12}\big)\,r_{12}^{-1}\,\phi_\lambda(2),
$$

where $\mathscr P_{12}$ swaps electrons 1 and 2 in what follows. In matrix form, with chemists' integrals ([[integral-notation]]):

$$
F_{\mu\nu} = H_{\mu\nu}^{\text{core}} + G_{\mu\nu},
\qquad
G_{\mu\nu} = \sum_{\lambda\sigma}P_{\lambda\sigma}\Big[(\mu\nu|\sigma\lambda) - \tfrac12(\mu\lambda|\sigma\nu)\Big],
$$

$$
H_{\mu\nu}^{\text{core}} = T_{\mu\nu} + \sum_A V_{\mu\nu}^{A},
\qquad
T_{\mu\nu} = \int\phi_\mu^*\big(-\tfrac12\nabla^2\big)\phi_\nu,
\qquad
V_{\mu\nu}^{A} = \int\phi_\mu^*\Big(-\frac{Z_A}{|\mathbf r - \mathbf R_A|}\Big)\phi_\nu .
$$

$\mathbf H^{\text{core}}$ is computed once. $\mathbf G$ needs the two-electron integrals and the current $\mathbf P$, so $\mathbf F = \mathbf F(\mathbf P)$ and the Roothaan equations are **nonlinear**: they must be solved by iteration ([[scf-procedure]]).

**Integral count (Szabo Ex. 3.14).** For real basis functions, $(\mu\nu|\lambda\sigma)$ has 8-fold permutational symmetry. With $n = K(K+1)/2$ unique pairs, the number of unique integrals is $n(n+1)/2$. For $K = 100$ this is $5050\cdot5051/2 = 12\,753\,775\approx K^4/8$. Their evaluation and contraction dominate the cost of conventional Hartree-Fock, formally $O(K^4)$.

## Energy

$$
E_0 = \tfrac12\sum_{\mu\nu}P_{\nu\mu}\big(H_{\mu\nu}^{\text{core}} + F_{\mu\nu}\big),
\qquad
E_{\text{tot}} = E_0 + \sum_{A<B}\frac{Z_AZ_B}{R_{AB}} .
$$

This is the matrix form of $\sum_a(h_{aa} + \varepsilon_a)$.

!!! example "STO-3G H₂ at R = 1.4 bohr (Szabo Sec. 3.5.2, Ex. 3.22-3.27)"
    Basis: one STO-3G 1s on each H ($\zeta = 1.24$). AO integrals from PySCF (hartree):

    | Integral | Value |
    |---|---:|
    | $S_{12}$ | 0.6593 |
    | $H_{11}^{\text{core}}$ | −1.1204 |
    | $H_{12}^{\text{core}}$ | −0.9584 |
    | $(11|11)$ | 0.7746 |
    | $(11|22)$ | 0.5697 |
    | $(21|11)$ | 0.4441 |
    | $(21|21)$ | 0.2970 |

    **Coefficients.** Symmetry fixes the MOs: $\psi_{1,2} = [2(1\pm S_{12})]^{-1/2}(\phi_1\pm\phi_2)$. So $P_{\mu\nu} = (1+S_{12})^{-1} = 0.6027$ for all four elements, and $\operatorname{tr}(\mathbf{PS}) = 2$.

    **One-electron H₂⁺ orbital energies (Ex. 3.23).** $(H_{11}+H_{12})/(1+S_{12}) = -1.2528$ and $(H_{11}-H_{12})/(1-S_{12}) = -0.4756$.

    **Converged Fock matrix (Ex. 3.25).** $F_{11} = F_{22} = -0.3655$, $F_{12} = -0.5939$.

    **Orbital energies (Ex. 3.26).**
    $$
    \varepsilon_1 = \frac{F_{11}+F_{12}}{1+S_{12}} = -0.5782,
    \qquad
    \varepsilon_2 = \frac{F_{11}-F_{12}}{1-S_{12}} = +0.6703 .
    $$

    **Energy (Ex. 3.27).**
    $$
    E_0 = \frac{F_{11}+H_{11}+F_{12}+H_{12}}{1+S_{12}} = -1.8310,
    \qquad
    E_{\text{tot}} = E_0 + \frac{1}{1.4} = -1.1167 .
    $$

    All values match Szabo's to four decimals and the MO-based numbers in [[minimal-basis-h2-model]]. They were checked with an independent Szabo-style SCF code; $\mathbf{PSP} = 2\mathbf P$ holds to $10^{-15}$.

!!! example "Bond length and exponent of STO-3G H₂ (Szabo Tables 3.2, 3.3)"
    **Bond-length scan** ($\zeta = 1.24$), total energy in hartree:

    | $R$ (bohr) | 1.32 | 1.34 | 1.36 | 1.38 | 1.40 |
    |---|---:|---:|---:|---:|---:|
    | $E_{\text{tot}}$ | −1.11731 | −1.11750 | −1.11745 | −1.11718 | −1.11671 |

    The minimum is at $R_e = 1.346$ bohr.

    **Exponent scan** at $R = 1.4$ bohr:

    | $\zeta$ | 1.0 | 1.1 | 1.2 | 1.3 |
    |---|---:|---:|---:|---:|
    | $E_{\text{tot}}$ | −1.08164 | −1.11089 | −1.11912 | −1.10714 |

    The optimum is $\zeta = 1.190$, larger than the free-atom value 1.0. The bonded electron cloud is contracted. Szabo prints −1.11672 at 1.40 bohr; the last-digit difference comes from integral precision.

## Source

Szabo and Ostlund, *Modern Quantum Chemistry* (Dover, 1996; reprint of the revised first edition, McGraw-Hill, 1989), Sec. 3.4.1-3.4.4, pp. 131-142, Eqs. (3.112)-(3.157), Ex. 3.9-3.14; Sec. 3.5.2, pp. 159-168, Ex. 3.22-3.27. Numbers recomputed for this note.
