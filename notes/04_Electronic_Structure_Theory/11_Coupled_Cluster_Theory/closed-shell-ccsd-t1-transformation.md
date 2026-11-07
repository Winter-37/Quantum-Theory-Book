---
id: closed-shell-ccsd-t1-transformation
title: Closed-shell CCSD - singlet cluster operators, the energy Σ(t_ij^ab + t_i^a t_j^b)L_iajb, the T1-transformed Hamiltonian, the biorthogonal projection basis, the norm of the CCSD state, and the O²V⁴ cost
summary: For a closed-shell singlet, HJO write T̂₁ = Σt_i^a E_ai and T̂₂ = ½Σt_ij^ab E_ai E_bj with spin-free amplitudes. The energy is E_HF + Σ(t_ij^ab + t_i^a t_j^b)(2g_iajb − g_ibja). Absorbing exp(T̂₁) into the integrals, with X = C(1 − t₁ᵀ) and Y = C(1 + t₁), turns CCSD into CCD-like algebra with nonsymmetric integrals. A biorthogonal bra basis ⟨ab ij| = ⅓⟨ij ab| + ⅙⟨ji ab| simplifies projection, and the singles-plus-doubles part of the norm is 1 + 2Σ(t_i^a)² + Σ(2τ − τᵀ)τ. Checked for water/cc-pVDZ: Eq. (13.7.18) and the T1-transformed energy reproduce PySCF's CCSD energies to 10⁻⁹ E_h, and the norm formula equals my spin-orbital enumeration exactly.
status: in-progress
kind: derivation
level: advanced
tags: [ccsd, closed-shell, spin-adaptation, t1-transformation, biorthogonal-basis, integral-transformation, computational-cost]
prerequisites: [coupled-cluster-hierarchy-and-size-extensivity, spin-tensor-operators]
related: [coupled-cluster-optimization-and-lagrangian, eom-ccsd-and-size-extensivity, coupled-cluster-variants-brueckner-qcisd-open-shell, density-based-hartree-fock]
order: 80
date: 2026-11-04
---

## Singlet cluster operators

**Spin adaptation (HJO Sec. 13.7.1).** For a singlet, $\hat T$ must commute with $\hat S_\pm$ and $\hat S_z$.

- **Singles.** This forces equal α and β amplitudes, $\hat T_1 = \sum_{ai}t_i^a\hat E_{ai}$.
- **Doubles.** $\hat T_2 = \tfrac12\sum_{aibj}t_{ij}^{ab}\hat E_{ai}\hat E_{bj}$ with $t_{ij}^{ab} = t_{ji}^{ba}$. This uses the singlet excitation operators $\hat E_{pq} = \sum_\sigma a^\dagger_{p\sigma}a_{q\sigma}$.

**Energy (HJO Sec. 13.7.2).** Only $[[\hat H, \hat E_{ai}], \hat E_{bj}]$ survives on $|\text{HF}\rangle$. With $L_{pqrs} = 2g_{pqrs} - g_{psrq}$,

$$
E_{\text{CCSD}} = E_{\text{HF}} + \sum_{aibj}\big(t_{ij}^{ab} + t_i^at_j^b\big)L_{iajb} .
$$

Only the combination $\tau_{ij}^{ab} = t_{ij}^{ab} + t_i^at_j^b$ appears. This is the closed-shell form of $\hat T_2 + \tfrac12\hat T_1^2$.

## The T1-transformed Hamiltonian

**Absorbing the singles (HJO Secs. 13.7.3-13.7.4).** Write $e^{-\hat T}\hat He^{\hat T} = e^{-\hat T_2}\tilde H e^{\hat T_2}$ with $\tilde H = e^{-\hat T_1}\hat He^{\hat T_1}$. The transformed operators are

$$
\tilde a^\dagger_{p\sigma} = a^\dagger_{p\sigma} - \sum_{ai}\delta_{pi}t_i^a a^\dagger_{a\sigma},\qquad
\tilde a_{p\sigma} = a_{p\sigma} + \sum_{ai}\delta_{pa}t_i^a a_{i\sigma} .
$$

Only occupied creators and virtual annihilators change.

**Integrals.** $\tilde H$ has the usual form, with integrals transformed by two *different* coefficient matrices:

$$
\mathbf X = \mathbf C(\mathbf 1 - \mathbf t_1^{\mathsf T}),\qquad \mathbf Y = \mathbf C(\mathbf 1 + \mathbf t_1),\qquad
\tilde h_{pq} = \sum_{\mu\nu}X_{\mu p}Y_{\nu q}h_{\mu\nu},\qquad \tilde g_{pqrs} = \sum X_{\mu p}Y_{\nu q}X_{\rho r}Y_{\sigma s}g_{\mu\nu\rho\sigma} .
$$

Here $(\mathbf t_1)_{ai} = t_i^a$ is the only nonzero block.

- **Symmetry.** The integrals lose their index symmetries except $\tilde g_{pqrs} = \tilde g_{rspq}$. Every commutator formula that uses only that symmetry (HJO Boxes 13.1-13.2) still holds.
- **Simplification.** In effect, CCSD becomes CCD with modified integrals. The transformation costs as much as an ordinary AO→MO transformation, done directly from the AO integrals with $\mathbf X$ and $\mathbf Y$.

!!! example "Two routes to the CCSD energy, water/cc-pVDZ (computed for this note)"
    | | $R_{\text{ref}}$ | $2R_{\text{ref}}$ |
    |---|---:|---:|
    | PySCF RCCSD | −76.2381164518 | −75.9296329214 |
    | Eq. (13.7.18), $E_{\text{HF}} + \sum\tau L$ | −76.2381164516 | −75.9296329235 |
    | $\langle\text{HF}|\tilde H|\text{HF}\rangle + \sum t_{ij}^{ab}\tilde L_{iajb}$, integrals from $\mathbf X,\mathbf Y$ | −76.2381164518 | −75.9296329214 |
    | $\langle\text{HF}|\tilde H|\text{HF}\rangle$ alone | −76.024022 | −75.586980 |
    | $E_{\text{HF}}$ | −76.024039 | −75.587711 |

    - **Agreement.** The T1-transformed energy reproduces PySCF exactly: the singles disappear into the integrals and only $\hat T_2$ is left. Eq. (13.7.18) agrees to $2\times10^{-9}$, at the level of the amplitude convergence.
    - **Size of the singles.** $\langle\text{HF}|\tilde H|\text{HF}\rangle - E_{\text{HF}}$ is +0.02 m$E_h$ at $R_{\text{ref}}$ but +0.73 m$E_h$ at $2R_{\text{ref}}$, where the singles are larger (max $|t_i^a|$ = 0.008 and 0.106). Note the sign: the singles raise $\langle\tilde H\rangle$ and lower the energy through $\tilde L$.

## Projection basis and the norm

**Biorthogonal bras (HJO Sec. 13.7.5).**

- **Kets.** $|{}^a_i\rangle = \hat E_{ai}|\text{HF}\rangle$ and $|{}^{ab}_{ij}\rangle = \hat E_{ai}\hat E_{bj}|\text{HF}\rangle$.
- **Why not their adjoints.** These overlap awkwardly with the kets, e.g. $\langle{}^a_i|{}^c_k\rangle = 2\delta_{ai,ck}$.
- **Biorthogonal choice.** Use instead

$$
\langle\overline{{}^a_i}| = \tfrac12\langle{}^a_i|,\qquad
\langle\overline{{}^{ab}_{ij}}| = \tfrac13\langle{}^{ab}_{ij}| + \tfrac16\langle{}^{ba}_{ij}|,
$$

  which are biorthogonal to the kets up to the permutation $P^{ab}_{ij}$. Only their existence matters for projection.

**Norm of the CCSD state (HJO Sec. 13.7.6).** Projected onto the singles and doubles,

$$
\|\text{CCSD}\|^2_{\text{HF+S+D}} = 1 + 2\sum_{ai}(t_i^a)^2 + \sum_{aibj}\big(2\tau_{ij}^{ab} - \tau_{ij}^{ba}\big)\tau_{ij}^{ab} .
$$

The exact norm would need every FCI configuration (compare [[coupled-cluster-hierarchy-and-size-extensivity]], where I computed the higher levels by brute force).

!!! example "Norm check, water CCSD/cc-pVDZ (computed for this note)"
    The singles and doubles terms of Eq. (13.7.68) are 0.0005971 and 0.057335 at $R_{\text{ref}}$, and 0.0382966 and 0.441714 at $2R_{\text{ref}}$. My spin-orbital enumeration of $\|\hat C_1|\text{HF}\rangle\|^2$ and $\|\hat C_2|\text{HF}\rangle\|^2$ gives the same numbers to all digits.

## The projections and their cost

**Singles and doubles projections (HJO Secs. 13.7.7-13.7.8).** Written with T1-transformed integrals, the singles projection $\Omega_{ai}$ has four terms (A1-D1) and the doubles projection $\Omega_{aibj}$ five (A2-E2). Each is a contraction of $\tilde g$ or $\tilde F$ with $\mathbf t_2$ or with products of two $\mathbf t_2$.

**Operation counts (HJO Sec. 13.7.9).** With $O$ occupied and $V$ virtual orbitals:

- **Dominant term.** The "particle-particle ladder" A2, $\sum_{cd}\tilde g_{acbd}t_{ij}^{cd}$, costs $O^2V^4$.
- **Other sixth-order terms.** B2 costs $O^4V^2$, and C2 and D2 cost $O^3V^3$.
- **Overall.** One CCSD iteration scales as $O^2V^4$, against roughly $n^4$ for small-molecule HF.

**Storage is often the real limit.** HJO's example (circa 2000): 400 basis functions and 40 electrons without symmetry need 26 GB of MO integrals but only 230 MB of amplitudes. One iteration then took 4-5 h at 500 Mflop/s.

**AO-direct alternative.** Form $\mathbf T^{\mu\nu}_{ij} = \sum_{cd}t_{ij}^{cd}Y_{\mu c}Y_{\nu d}$ (plus a singles term), contract it with the AO integrals in an $n^4O^2$ step, and back-transform. This needs no stored MO integrals at slightly higher operation count.

## Source

Helgaker, Jørgensen and Olsen, *Molecular Electronic-Structure Theory* (Wiley, Chichester, 2000), Sec. 13.7, pp. 685-698, Eqs. (13.7.1)-(13.7.109), Boxes 13.1-13.2. Recomputed for this note with PySCF 2.14 and my own T1-transformed integrals via `ao2mo.general` with $(\mathbf X, \mathbf Y, \mathbf X, \mathbf Y)$ (`hjo/c13/t1trans.py`).
