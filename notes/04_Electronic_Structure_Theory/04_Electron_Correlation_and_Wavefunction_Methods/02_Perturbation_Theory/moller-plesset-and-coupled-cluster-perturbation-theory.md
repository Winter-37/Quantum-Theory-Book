---
id: moller-plesset-and-coupled-cluster-perturbation-theory
title: Møller-Plesset and coupled-cluster perturbation theory (HJO 14.2-14.4) - the fluctuation potential, MP wave functions by excitation level, CCPT amplitudes order by order, termwise size-extensivity, the CCPT Lagrangian, and closed-shell MP2, MP3 and MP4 for water recomputed
summary: With the Fock operator as H₀, the perturbation is the fluctuation potential Φ. HJO derive MPn energies from coupled-cluster perturbation theory (CCPT), expanding the linked CC equations in orders of Φ, ε_μ t_μ⁽ⁿ⁾ = −⟨μ|[e^{−T}Φe^{T}]⁽ⁿ⁻¹⁾|HF⟩. Doubles appear at first order; singles, triples and disconnected quadruples at second. The energies are size-extensive term by term, and a CCPT Lagrangian restores the 2n + 1 rule. Since CCSD is exact through third order and its fourth-order energy is MP4(SDQ), I extracted MP2, MP3 and MP4(SDQ) for water/cc-pVDZ as Taylor coefficients of CCSD with the two-electron integrals scaled by λ, and added the MP4 triples from (T) evaluated with MP1 amplitudes. This reproduces HJO's MP2 and MP3 errors exactly and MP4 at 2R_ref exactly; at R_ref my MP4 error is 0.001060 against HJO's 0.001069.
status: in-progress
kind: theory
level: advanced
tags: [moller-plesset, mp2, mp3, mp4, coupled-cluster-perturbation-theory, fluctuation-potential, size-extensivity, lagrangian, epstein-nesbet]
prerequisites: [rspt-wigner-rule-and-hylleraas-functional, coupled-cluster-hierarchy-and-size-extensivity]
related: [mp2, mp3, linked-cluster-theorem, perturbation-theory-second-quantization, mp-convergence-intruders-analytic-continuation, perturbative-triples-cc2-cc3, coupled-cluster-optimization-and-lagrangian]
also: [04_Electronic_Structure_Theory/04_Electron_Correlation_and_Wavefunction_Methods/02_Perturbation_Theory/MP4]
date: 2026-11-04
---

## The Møller-Plesset partitioning

**Zero-order operator (HJO Sec. 14.2.1).** In canonical orbitals, $\hat f = \sum_P\varepsilon_Pa^\dagger_Pa_P$.

- **Perturbation.** The fluctuation potential $\hat\Phi = \hat H - \hat f - h_{\text{nuc}}$, the difference between instantaneous and mean-field repulsion.
- **Zero-order states.** The HF determinant and all excited determinants. $\hat f|\mu\rangle = (E^{(0)} + \varepsilon_\mu)|\mu\rangle$, where $\varepsilon_\mu$ is the sum of virtual minus occupied orbital energies, and $[\hat f, \hat\tau_\mu] = \varepsilon_\mu\hat\tau_\mu$.
- **Low orders.** $E^{(0)} + E^{(1)} = E_{\text{HF}}$. $E^{(1)} = \langle\hat\Phi\rangle$ is minus the electron-repulsion energy, which matters for convergence ([[mp-convergence-intruders-analytic-continuation]]).
- **Epstein-Nesbet alternative.** It keeps all occupation-conserving parts of $\hat H$ in $\hat H_0$. It is used occasionally but has been less successful.

**MP wave functions (HJO Secs. 14.2.2-14.2.6).**

- **First order.** $|\text{MP1}\rangle$ contains only doubles, $t^{AB(1)}_{IJ} = -g_{AIBJ}^{\text{antisym}}/\varepsilon^{AB}_{IJ}$.
- **Second order.** $|\text{MP2}\rangle$ adds singles, triples and the *disconnected* quadruples $\tfrac12(\hat T_2^{(1)})^2$.
- **Size-extensivity.** As in general RSPT, the energies are extensive order by order but not term by term in the 2n + 1 form ([[rspt-wigner-rule-and-hylleraas-functional]]).

## Coupled-cluster perturbation theory

**Ansatz (HJO Secs. 14.3.1-14.3.2).** Take $|\text{CC}\rangle = e^{\hat T}|\text{HF}\rangle$ with the *full* cluster operator, expand $\hat T = \sum_n\hat T^{(n)}$ in orders of $\hat\Phi$, and use the canonical-form CC equations of [[coupled-cluster-optimization-and-lagrangian]]:

$$
\varepsilon_\mu t^{(1)}_\mu = -\langle\mu|\hat\Phi|\text{HF}\rangle,\qquad
\varepsilon_\mu t^{(2)}_\mu = -\langle\mu|[\hat\Phi,\hat T^{(1)}]|\text{HF}\rangle,\qquad
\varepsilon_\mu t^{(3)}_\mu = -\langle\mu|[\hat\Phi,\hat T^{(2)}] + \tfrac12[[\hat\Phi,\hat T^{(1)}],\hat T^{(1)}]|\text{HF}\rangle .
$$

**First appearance of each excitation level (HJO Table 14.2).**

- **Doubles:** first order.
- **Singles:** second order, because of the Brillouin theorem.
- **Triples:** second order.
- **$n$-fold excitations in general:** order $n-1$, by the rank rules of [[coupled-cluster-hierarchy-and-size-extensivity]].

**Wave-function corrections (HJO Sec. 14.3.3).** Expanding the exponential gives $|0^{(1)}\rangle = \hat T^{(1)}|\text{HF}\rangle$ and $|0^{(2)}\rangle = (\hat T^{(2)} + \tfrac12\hat T^{(1)2})|\text{HF}\rangle$. These are the MP wave functions, obtained without the long RSPT manipulations.

**Energies and extensivity (HJO Secs. 14.3.4-14.3.5).**

- **Energy.** $E^{(n)} = \langle\text{HF}|\hat\Phi(\hat T_2^{(n-1)} + \tfrac12[\hat T_1\hat T_1]^{(n-1)})|\text{HF}\rangle$.
- **Extensivity.** The amplitude equations are linked commutators, so $\hat T^{(n)}$ separates additively for noninteracting systems. The energies are therefore extensive *term by term*.

**CCPT Lagrangian (HJO Secs. 14.3.6-14.3.9).** With multipliers $\bar t^{(n)}$, the energy obeys the 2n + 1 rule for amplitudes and 2n + 2 for multipliers, and stays termwise extensive:

$$
E^{(4)} = \langle\bar t^{(1)}|[\hat\Phi,\hat T^{(2)}]|\text{HF}\rangle + \ldots
$$

- **Order 2 and 3.** Only connected doubles contribute.
- **Order 4.** Singles and triples enter.
- **Order 5.** Disconnected quadruples appear through the multipliers (HJO Table 14.3).

## Closed-shell MP energies

**Spin-adapted expressions (HJO Sec. 14.4).** With the biorthogonal basis of [[closed-shell-ccsd-t1-transformation]]:

$$
E^{(2)} = \sum_{aibj}t^{ab(1)}_{ij}L_{iajb},\qquad t^{ab(1)}_{ij} = -\frac{g_{aibj}}{\varepsilon_a + \varepsilon_b - \varepsilon_i - \varepsilon_j} .
$$

$E^{(3)}$ needs the second-order doubles. $E^{(4)}$ splits into singles (S), doubles (D), triples (T) and quadruples (Q) contributions. Its triples part is the dominant cost: $O^3V^4$, i.e. $n^7$.

**MP4(SDQ).** It omits the triples. It is the fourth-order estimate of the CCSD energy (HJO Eq. 14.4.83).

!!! example "MP series for water/cc-pVDZ from λ-scaled CCSD (computed for this note; $E - E_{\text{FCI}}$ in $E_h$ with HJO's FCI)"
    **Method.** Scale all two-electron integral blocks by λ but keep the Fock matrix, so that $\hat H(\lambda) = \hat f + \lambda\hat\Phi$. Then $E_{\text{CCSD}}(\lambda) = \lambda^2E^{(2)} + \lambda^3E^{(3)} + \lambda^4E^{(4)}_{\text{SDQ}} + O(\lambda^5)$.

    - **Fit.** A degree-8 to degree-10 polynomial fit on 12 values of $|\lambda|\le0.1$-0.3 is stable to $10^{-10}$ in $E^{(2)}$ and $E^{(4)}_{\text{SDQ}}$.
    - **Triples.** $E^{(4)}_T$ is PySCF's (T) formula evaluated with $t_1 = 0$ and MP1 doubles.

    | | $R_{\text{ref}}$ | $2R_{\text{ref}}$ |
    |---|---:|---:|
    | $E^{(2)}$ (fit / direct MP2) | −0.20469002 / −0.20469002 | −0.30922413 / −0.30922413 |
    | $E^{(3)}$ | −0.00669214 | +0.01436682 |
    | $E^{(4)}_{\text{SDQ}}$ | −0.00235768 | −0.03400973 |
    | $E^{(4)}_T$ | −0.00302152 | −0.01904089 |
    | MP2 error (HJO) | 0.013131 (0.013131) | 0.054730 (0.054730) |
    | MP3 error (HJO) | 0.006439 (0.006439) | 0.069096 (0.069096) |
    | MP4 error (HJO) | 0.001060 (**0.001069**) | 0.016046 (0.016046) |

    - **Agreement.** Five of the six errors agree with HJO (their Table 5.12) to the last digit.
    - **Open discrepancy.** At $R_{\text{ref}}$ my MP4 is 9 µ$E_h$ lower than HJO's. Neither piece looks suspect: the $2R_{\text{ref}}$ value agrees exactly by the same method, and the fit is stable. It could be a misprint; I cannot tell.
    - **The stretched molecule.** $E^{(3)}$ is *positive* at $2R_{\text{ref}}$, so MP3 is worse than MP2. Large singles and triples make up the fourth order.

## Source

Helgaker, Jørgensen and Olsen, *Molecular Electronic-Structure Theory* (Wiley, Chichester, 2000), Secs. 14.2-14.4, pp. 739-769, Eqs. (14.2.1)-(14.4.83), Tables 14.2-14.3; MP reference values from Table 5.12 (p. 194). Recomputed for this note with PySCF 2.14 (RCCSD with scaled integrals, MP2, `ccsd_t`) in `hjo/c14/mpn.py` and `hjo/c14/fitchk.py`.
