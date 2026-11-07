---
id: one-particle-hamiltonian-models
title: Many-electron methods applied to one-particle Hamiltonians - relaxation energy and Hückel resonance energy
summary: For a Hamiltonian with only one-body terms the exact answer is a single determinant, so every many-electron method can be tested against an exact result. Singles play the role of doubles, doubles the role of quadruples, and CCA becomes exact because c_ab^rs = c_a^r c_b^s − c_a^s c_b^r holds identically. Szabo's SCI, IEPA, L-CCA, CEPA and CCA equations, the relaxation energy as a trace, and the cyclic-polyene resonance energy computed for several ring sizes.
status: in-progress
kind: comparison
level: intermediate
tags: [relaxation-energy, huckel, resonance-energy, thouless, ccsd, size-consistency, model-hamiltonian]
prerequisites: [coupled-pair-approximations, slater-determinants, matrix-eigenvalue-problem]
related: [coupled-cluster-doubles, orbital-perturbation-theory, iepa, size-consistency]
order: 30
date: 2026-11-03
---

## Why study a problem without correlation

**The model.** Take an $N$-electron Hamiltonian made only of one-particle terms,

$$
\mathscr H = \mathscr H_0 + \mathscr V = \sum_i h_0(i) + \sum_i v(i).
$$

The zeroth-order determinant $|\Psi_0\rangle$ is built from the $N$ lowest eigenfunctions $\chi_i^{(0)}$ of $h_0$, with $E_0 = \langle\Psi_0|\mathscr H|\Psi_0\rangle = \sum_a(\varepsilon_a^{(0)} + v_{aa})$.

**The exact answer is trivial.** Since $\mathscr H$ is also a sum of one-body terms, diagonalize $h_0 + v$, and the exact ground state is the determinant of its $N$ lowest eigenfunctions with $\mathscr E_0 = \sum_a\varepsilon_a$. The **relaxation energy** $E_R = \mathscr E_0 - E_0$ is the analogue of the correlation energy.

**Why bother.** Applying CI, pair and cluster theories to this problem is the "hard way", but every result can be compared with the exact one, and the algebra is short enough to see the structure. The orbital picture is exact here, and a good many-electron theory should know that.

**Dictionary.** Because $\mathscr H$ is one-body:

| Real many-electron problem | One-particle model |
|---|---|
| correlation energy | relaxation energy |
| doubles carry the energy | singles carry the energy |
| quadruples ≈ products of doubles | doubles = products of singles |
| pair energies $e_{ab}$ | "particle" energies $e_a$ |
| 18-term product | 2-term product |

## Exact relaxation energy as a trace

**Partitioned eigenvalue problem.** Expand an exact orbital in the zeroth-order orbitals and split occupied $(A)$ and virtual $(B)$ blocks:

$$
\begin{pmatrix}\mathbf H_{AA} & \mathbf H_{AB}\\ \mathbf H_{BA} & \mathbf H_{BB}\end{pmatrix}
\begin{pmatrix}\mathbf c_A\\ \mathbf c_B\end{pmatrix} = \varepsilon\begin{pmatrix}\mathbf c_A\\ \mathbf c_B\end{pmatrix},
\qquad
(\mathbf H_{AA})_{ab} = \varepsilon_a^{(0)}\delta_{ab} + v_{ab},\ \ (\mathbf H_{BA})_{rb} = v_{rb},
$$

and similarly for the other blocks. The exact energy is the sum of the $N$ lowest eigenvalues, so $E_R = \operatorname{tr}(\boldsymbol\varepsilon_A - \mathbf H_{AA})$.

**Reformulation with one matrix.** Let $\mathbf U$ diagonalize the matrix and define $\mathbf C_{BA} = \mathbf U_{BA}\mathbf U_{AA}^{-1}$. Two of the four block equations then give (Szabo Eqs. 5.96, 5.98)

$$
E_R = \operatorname{tr}\mathbf H_{AB}\mathbf C_{BA},
\qquad
\mathbf H_{BA} + \mathbf H_{BB}\mathbf C_{BA} - \mathbf C_{BA}\mathbf H_{AA} - \mathbf C_{BA}\mathbf H_{AB}\mathbf C_{BA} = 0 .
$$

The second equation is quadratic in $\mathbf C_{BA}$ and must be solved iteratively. For a $1\times1$ occupied block it reduces to the familiar intermediate-normalized eigenvalue equation for the lowest root.

**Element form.** With $c_a^r = (\mathbf C_{BA})_{ra}$:

$$
E_R = \sum_{br} v_{br}c_b^r,
\qquad
v_{ra} + \sum_s(\varepsilon_r^{(0)}\delta_{rs} + v_{rs})c_a^s - \sum_b c_b^r(\varepsilon_b^{(0)}\delta_{ab} + v_{ba}) - \sum_{bs}c_b^r v_{bs}c_a^s = 0 .
$$

(General knowledge, not from Szabo: $\mathbf C_{BA}$ is the Thouless parametrization of a determinant relative to $|\Psi_0\rangle$, and the quadratic equation is the condition that the occupied space of $h_0+v$ is invariant.)

## The many-electron methods

**Matrix elements (Szabo Ex. 5.14).** Between determinants, a one-body operator connects only determinants differing by one spin orbital. In particular $\langle\Psi_0|\mathscr H|\Psi_a^r\rangle = v_{ar}$, $\langle\Psi_0|\mathscr H|\Psi_{ab}^{rs}\rangle = 0$, and $\langle\Psi_a^r|\mathscr H|\Psi_{ab}^{rs}\rangle = v_{bs}$.

**Full CI hierarchy.** The relaxation energy depends only on singles, $E_R = \sum_{bs}v_{bs}c_b^s$. The singles equation contains the doubles $c_{ab}^{rs}$, and so on.

**The five truncations** (Szabo Table 5.5). Writing $\mathcal L_a^r(\mathbf c) = v_{ra} + \sum_s(\varepsilon_r^{(0)}\delta_{rs} + v_{rs})c_a^s - \sum_b(\varepsilon_a^{(0)}\delta_{ab} + v_{ba})c_b^r$:

| Method | Singles equation | Analogue of |
|---|---|---|
| SCI | $\mathcal L_a^r = E_R\,c_a^r$ | DCI |
| IEPA | same as SCI with only $b = a$ coupling and $E_R\to e_a$ | IEPA |
| L-CCA | $\mathcal L_a^r = 0$ | L-CCD |
| CEPA | $\mathcal L_a^r = e_a\,c_a^r$ | CEPA |
| CCA | $\mathcal L_a^r = \sum_{bs}c_b^r v_{bs}c_a^s$ | CCD |

with $e_a = \sum_s v_{as}c_a^s$ and $E_R = \sum_a e_a$ in every case.

**CCA is exact.** The CCA closure is $c_{ab}^{rs} = c_a^rc_b^s - c_a^sc_b^r$. Substituting it into the doubles terms of the singles equation and cancelling the $E_R c_a^r$ term gives exactly the quadratic equation of the previous section with $c_a^r = (\mathbf C_{BA})_{ra}$. So CCA reproduces the exact relaxation energy for **any** one-particle Hamiltonian, however poor the starting determinant.

**Why the closure is exact.** The exact ground state is a single determinant of orbitals $\chi_a = \sum_b\chi_b^{(0)}U_{ba} + \sum_r\chi_r^{(0)}U_{ra}$. Expanding that determinant in zeroth-order determinants and normalizing so that $\langle\Psi_0|\Phi_0\rangle = 1$ gives singles coefficients $c_a^r = (\mathbf U_{BA}\mathbf U_{AA}^{-1})_{ra}$ and doubles coefficients that are $2\times2$ minors, $c_{ab}^{rs} = c_a^rc_b^s - c_a^sc_b^r$. Higher coefficients are larger minors. In second quantization, a single determinant is $e^{\hat T_1}|\Psi_0\rangle$ exactly (general knowledge; Thouless's theorem).

!!! example "Two electrons, three virtuals (Szabo Eqs. 5.121-5.123)"
    Let $|\chi_1\rangle = |\chi_1^{(0)}\rangle + a_3|\chi_3^{(0)}\rangle + a_4|\chi_4^{(0)}\rangle$ and $|\chi_2\rangle = |\chi_2^{(0)}\rangle + b_3|\chi_3^{(0)}\rangle + b_4|\chi_4^{(0)}\rangle$. Expanding $|\chi_1\chi_2\rangle$ by multilinearity of the determinant gives singles coefficients $c_1^3 = a_3$, $c_1^4 = a_4$, $c_2^3 = b_3$, $c_2^4 = b_4$, and the double

    $$
    c_{12}^{34} = a_3b_4 - a_4b_3 = c_1^3c_2^4 - c_1^4c_2^3 .
    $$

## Cyclic polyenes in Hückel theory

**Model.** A ring of $N = 4\nu + 2$ carbons, one $\pi$ electron each, orthonormal $p$ orbitals, $h_{\mu\mu} = \alpha$, $h_{\mu,\mu\pm1} = \beta$ (both negative). The Hückel orbital energies are $\varepsilon_j = \alpha + 2\beta\cos(2\pi j/N)$, and the closed-shell ground-state energy is

$$
\mathscr E_0 = N\alpha + \frac{4\beta}{\sin(\pi/N)} .
$$

**Zeroth order.** $N/2$ isolated ethylenic units, each with bonding $|i\rangle$ ($\alpha+\beta$) and antibonding $|i^*\rangle$ ($\alpha-\beta$) orbitals, so $E_0 = N\alpha + N\beta$. The perturbation consists of the $\pm\beta/2$ couplings between neighbouring units.

**Resonance energy.** $E_R = \mathscr E_0 - E_0 = \beta\big(4/\sin(\pi/N) - N\big)$. For benzene $E_R = 2\beta$. For large $N$, $E_R\to(4/\pi - 1)N\beta = 0.2732N\beta$: proportional to $N$, so only size-consistent methods can work.

**Benzene by hand (Szabo).**

- **SCI.** $E_R = \tfrac12(\sqrt{13} - 1)\beta = 1.303\beta$ (65%). For general $N$, with only the configurations that touch $|\Psi_0\rangle$, $E_R(\text{SCI}) = \big((1 + N/2)^{1/2} - 1\big)\beta \propto\sqrt N$, the analogue of DCI's failure.
- **IEPA.** All six "particle" energies are equal. Each particle function mixes $|\Psi_0\rangle$ with one combination of singles, with coupling $2^{-1/2}\beta$ and excitation energy $-\tfrac32\beta$, so $e^2 + \tfrac32\beta e - \tfrac12\beta^2 = 0$ and $E_R = 6e = \tfrac64(\sqrt{17} - 3)\beta = 1.685\beta$ (84%).
- **L-CCA.** Setting $E_R = 0$ in the SCI equation: $3\beta$ (150%).
- **CEPA.** Replacing $E_R$ by $e$: $2e^2 - 2\beta e - \beta^2 = 0$, $E_R = 3(\sqrt3 - 1)\beta = 2.196\beta$ (110%).
- **CCA.** Exact, $2\beta$.

!!! example "Resonance energies computed for this note (units of β)"
    Each method was solved numerically in the full space of single excitations of the ethylenic determinant, using the equations of the table above.

    | $N$ | Exact | SCI | IEPA | CEPA | L-CCA | CCA |
    |---:|---:|---:|---:|---:|---:|---:|
    | 6 | 2.0000 | 1.3028 | 1.6847 | 2.1962 | 3 | 2.0000 |
    | 10 | 2.9443 | 1.5712 | 2.3868 | 3.2001 | 5 | 2.9443 |
    | 14 | 3.9758 | 1.9218 | 3.3070 | 4.2389 | 7 | 3.9758 |
    | 30 | 8.2671 | 3.0782 | 7.0820 | 8.7912 | 15 | 8.2671 |

    - **Benzene** reproduces Szabo Table 5.6: 1.303, 1.685, 2.196, 3 and 2.
    - **IEPA for N = 10** is 2.387, the "exact IEPA" value of Szabo Ex. 5.19b (2.387β), 6% above the simpler estimate $0.2247N\beta = 2.247\beta$ that ignores singles which reach $|\Psi_0\rangle$ only through other singles.
    - **SCI for N = 10** is 1.571 in the full singles space. Szabo's restricted formula $(\sqrt{1+N/2} - 1)\beta$ gives 1.449; the extra singles do not change the $\sqrt N$ trend.
    - **L-CCA** gives exactly $N\beta/2$ in this model, 50 to 80% too large.
    - **CEPA** overshoots by 6 to 10%, IEPA gives 81 to 86% of exact, and CCA is exact to machine precision.

**Caveat (Szabo).** The model is harder than real correlation because the zeroth-order picture (alternate bonds switched off) is poor. DCI for a real six-electron molecule recovers far more than 65% of the correlation energy. The table illustrates structure, not accuracy for molecules.

## Source

Szabo and Ostlund, *Modern Quantum Chemistry* (Dover, 1996; reprint of the revised first edition, McGraw-Hill, 1989), Sec. 5.3, pp. 297-318, Eqs. (5.72)-(5.159), Tables 5.5 (p. 307) and 5.6 (p. 318), Ex. 5.13-5.21. The Thouless remarks are general knowledge. The resonance-energy table was computed for this note.
