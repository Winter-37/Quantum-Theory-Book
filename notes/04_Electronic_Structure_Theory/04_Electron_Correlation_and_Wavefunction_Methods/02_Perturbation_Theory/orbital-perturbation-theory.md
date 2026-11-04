---
id: orbital-perturbation-theory
title: Orbital perturbation theory - one-particle perturbations and the Hückel resonance-energy series
summary: When both H0 and V are sums of one-particle operators, the N-electron perturbation series is the sum of the series for each occupied orbital energy. Occupied-occupied terms cancel, so E(2) = Σ v_ar v_ra/(ε_a − ε_r) and E(3) has a particle and a hole term. Applied to cyclic polyenes this gives E(2) = Nβ/4, E(3) = 0 except for benzene, E(4) = Nβ/64, and for benzene a slowly oscillating series whose partial sums are computed here to twelfth order.
status: in-progress
kind: derivation
level: intermediate
tags: [perturbation-theory, one-particle-perturbation, huckel, resonance-energy, convergence]
prerequisites: [rayleigh-schrodinger-perturbation-theory, slater-determinants]
related: [one-particle-hamiltonian-models, mp2, linked-cluster-theorem]
also: []
date: 2026-11-03
---

## Setting

**Partition.** $\mathscr H_0 = \sum_i h_0(i)$ and $\mathscr V = \sum_i v(i)$, both one-body. The physical example is a molecule in a uniform electric field, $\mathscr V = \mathbf F\cdot\sum_i\mathbf r_i$, treated starting from Hartree-Fock orbitals; another is the Hückel model of [[one-particle-hamiltonian-models]].

**Zeroth order.** $|\Psi_0\rangle$ is the determinant of the $N$ lowest eigenfunctions of $h_0$, $h_0\chi_i^{(0)} = \varepsilon_i^{(0)}\chi_i^{(0)}$. Holes are $a,b,c,\ldots$, particles $r,s,t,\ldots$. Then

$$
E_0^{(0)} = \sum_a\varepsilon_a^{(0)}, \qquad E_0^{(1)} = \sum_a v_{aa}, \qquad E_0 = \langle\Psi_0|\mathscr H|\Psi_0\rangle = E_0^{(0)} + E_0^{(1)} .
$$

## The shortcut: perturb each orbital

The exact ground state is the determinant of the $N$ lowest eigenfunctions of $h_0 + v$, with energy $\mathscr E_0 = \sum_a\varepsilon_a$. So expand each **orbital energy** by ordinary RS theory ([[rayleigh-schrodinger-perturbation-theory]]) and add:

$$
\varepsilon_a = \varepsilon_a^{(0)} + v_{aa} + \sum_{r}\frac{v_{ar}v_{ra}}{\varepsilon_a^{(0)} - \varepsilon_r^{(0)}} + \sum_{b\ne a}\frac{v_{ab}v_{ba}}{\varepsilon_a^{(0)} - \varepsilon_b^{(0)}} + \cdots
$$

**Hole-hole terms cancel.** Summed over $a$, the last term is $X = \sum_{a\ne b}v_{ab}v_{ba}/(\varepsilon_a^{(0)} - \varepsilon_b^{(0)})$. Swapping the dummy labels $a\leftrightarrow b$ gives $X = -X$, so $X = 0$. The occupied orbitals can mix among themselves without changing the determinant. Hence

$$
E_0^{(2)} = \sum_{ar}\frac{v_{ar}v_{ra}}{\varepsilon_a^{(0)} - \varepsilon_r^{(0)}}
\qquad\Big(\text{closed shell: } 2\sum_{ar}^{N/2}\Big).
$$

**Same result from N-electron RS theory (Szabo Ex. 6.3).** In $\sum_n|\langle\Psi_0|\mathscr V|n\rangle|^2/(E_0^{(0)} - E_n^{(0)})$ only singles $|\Psi_a^r\rangle$ couple, with element $v_{ar}$ and denominator $\varepsilon_a^{(0)} - \varepsilon_r^{(0)}$.

**Third order (Szabo Ex. 6.4).** Using $\langle\Psi_a^r|\mathscr V - E_0^{(1)}|\Psi_b^s\rangle = v_{rs}\delta_{ab} - v_{ba}\delta_{rs}$ for $(a,r)\ne(b,s)$,

$$
E_0^{(3)} = \sum_{ars}\frac{v_{ar}v_{rs}v_{sa}}{(\varepsilon_a^{(0)} - \varepsilon_r^{(0)})(\varepsilon_a^{(0)} - \varepsilon_s^{(0)})}
- \sum_{abr}\frac{v_{ra}v_{ab}v_{br}}{(\varepsilon_a^{(0)} - \varepsilon_r^{(0)})(\varepsilon_b^{(0)} - \varepsilon_r^{(0)})}.
$$

The first is a "particle" term (the excited electron scatters among virtuals), the second a "hole" term (the hole scatters among occupied orbitals). The renormalization term $B^{(3)}$ of general RS theory has been absorbed; nothing grows like $N^2$. For a closed shell each sum gets a factor 2 and runs over spatial orbitals.

## Diagrams

**Szabo Sec. 6.4.** The same expressions follow from diagrams with hole lines ($a,b,\ldots$, arrows down) and particle lines ($r,s,\ldots$, arrows up). Each dot is a one-body vertex $\langle\text{in}|v|\text{out}\rangle$, each gap between dots gives $\sum\varepsilon_{\text{holes}} - \sum\varepsilon_{\text{particles}}$, and the sign is $(-1)^{h+l}$. Second order is one bubble (one hole, one particle). Third order has two diagrams, a particle line with an extra dot and a hole line with an extra dot; the hole diagram has two hole lines, hence the minus sign above. Only linked diagrams occur.

## Cyclic polyenes

**Setting.** As in [[one-particle-hamiltonian-models]]: $N = 4\nu + 2$ carbons, zeroth order $= N/2$ ethylenic units with bonding $|i\rangle$ at $\alpha+\beta$ and antibonding $|i^*\rangle$ at $\alpha-\beta$, so every particle-hole gap is $\varepsilon_i^{(0)} - \varepsilon_{j^*}^{(0)} = 2\beta$. The perturbation couples neighbouring units only:

$$
\langle i|v|(i\pm1)^*\rangle = \pm\beta/2,\qquad \langle i|v|i\pm1\rangle = \beta/2,\qquad \langle i^*|v|(i\pm1)^*\rangle = -\beta/2,
$$

and $\langle i|v|i^*\rangle = 0$. The exact resonance energy is $E_R = \beta\big(4/\sin(\pi/N) - N\big)$: $2\beta$ for benzene, $\to 0.2732N\beta$ for large $N$.

**Second order.**

$$
E^{(2)} = 2\sum_{i,j}\frac{\langle i|v|j^*\rangle\langle j^*|v|i\rangle}{2\beta} = \frac1\beta\sum_i\Big[(\beta/2)^2 + (-\beta/2)^2\Big] = \frac{N\beta}{4}.
$$

Benzene: $1.5\beta$ (75% of exact). Large $N$: $0.25/0.2732 = 91.5\%$ of exact.

**Path counting.** For fixed $i$, $\sum_j\langle i|v|j^*\rangle\langle j^*|v|i\rangle$ is the sum over paths $i\to j^*\to i$ of the product of the matrix elements met. Only $j = i\pm1$ are reachable, each path worth $\beta^2/4$.

**Third order.** The particle term needs paths $i\to j^*\to k^*\to i$. Since $v$ moves one unit per step, three steps cannot return to $i$, unless the ring is so small that $(i+2)^* = (i-1)^*$. That happens only for benzene ($N/2 = 3$). Hence

$$
E^{(3)} = 0\ (N > 6), \qquad E^{(3)}(\text{benzene}) = \tfrac34\beta .
$$

For benzene each of the two terms is $\tfrac38\beta$ (Szabo Eq. 6.54, Ex. 6.5).

**Fourth order (Szabo Ex. 6.7, by diagrams).** $E^{(4)} = N\beta/64$. Through fourth order $E_R\approx(1/4 + 1/64)N\beta = 0.2656N\beta$, 97% of the large-$N$ exact value.

## Convergence for benzene

**Alternating-bond model (Szabo Ex. 6.6).** Let the bonds alternate between $\beta_1 = \beta$ and $\beta_2 = x\beta$. Diagonalizing the $6\times6$ Hückel matrix gives

$$
\mathscr E_0 = 6\alpha + 2(\beta_1 + \beta_2) - 4\big(\beta_1^2 + \beta_2^2 - \beta_1\beta_2\big)^{1/2},
\qquad
E_R(x) = 4\beta\Big(\tfrac x2 - 1 + (1 + x^2 - x)^{1/2}\Big).
$$

$x = 0$ is the localized reference and $x = 1$ is benzene. The coefficient of $x^n$ is the $n$th-order energy.

!!! example "Perturbation series for benzene (computed for this note)"
    Taylor coefficients of $E_R(x)$, in units of β, and partial sums at $x = 1$ (exact 2):

    | $n$ | $E^{(n)}$ | Sum through $n$ |
    |---:|---:|---:|
    | 2 | 3/2 | 1.5000 |
    | 3 | 3/4 | 2.2500 |
    | 4 | 3/32 | 2.3438 |
    | 5 | −15/64 | 2.1094 |
    | 6 | −57/256 | 1.8867 |
    | 7 | −21/512 | 1.8457 |
    | 8 | 867/8192 | 1.9515 |
    | 9 | 1893/16384 | 2.0671 |
    | 10 | 1581/65536 | 2.0912 |
    | 11 | −8283/131072 | 2.0280 |
    | 12 | −76953/1048576 | 1.9546 |

    - **Through fourth order** the series overshoots (2.34β, 117%), as Szabo notes; the higher orders oscillate slowly back towards 2.
    - **Cause.** The expansion parameter is $x = 1$; the first-order coefficient vanishes and the series is that of a square root whose nearest singularities ($1 + x^2 - x = 0$, $|x| = 1$) lie on the unit circle, so convergence at $x=1$ is slow (the convergence radius statement is general knowledge, not from Szabo).
    - **The coefficients** agree with Szabo's $E^{(2)} = \tfrac32\beta$, $E^{(3)} = \tfrac34\beta$ and $E^{(4)} = \tfrac{3}{32}\beta = N\beta/64$. Szabo generates higher orders with a Gegenbauer-polynomial recursion; here the series was expanded symbolically instead.

    **Third-order formula check.** For a random 7-orbital one-body model with 3 occupied orbitals, the two-term $E^{(3)}$ above agrees with a numerical Taylor fit of the exact energy to $2\times10^{-6}$ (fit error).

**Lesson.** Perturbation theory works better for the large polyenes (97% at fourth order) than for benzene, where the three-unit ring creates extra low-order paths. Convergence is governed by how good the zeroth-order picture is, not by the size of the system.

## Source

Szabo and Ostlund, *Modern Quantum Chemistry* (Dover, 1996; reprint of the revised first edition, McGraw-Hill, 1989), Sec. 6.3, pp. 338-347, Eqs. (6.30)-(6.55), Ex. 6.3-6.7; Sec. 6.4, pp. 348-350. Series table computed for this note with SymPy.
