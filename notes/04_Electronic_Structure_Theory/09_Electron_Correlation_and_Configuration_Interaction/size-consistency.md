---
id: size-consistency
title: Size consistency and the failure of truncated CI
summary: A method is size consistent if the energy of noninteracting fragments is the sum of fragment energies. Hartree-Fock and full CI are; truncated CI is not. Szabo's N noninteracting minimal-basis H2 model gives DCI correlation ∝ √N instead of N, with numbers, the full CI dimer (quadruple coefficient = product of doubles), the exponential decay of ⟨Ψ0|Φ0⟩, and a computed water dimer.
status: in-progress
kind: derivation
level: intermediate
tags: [size-consistency, size-extensivity, truncated-ci, cisd, davidson-correction, separability]
prerequisites: [cisd, full-ci]
related: [exact-wave-function-properties-and-symmetry, perturbation-theory-second-quantization, electron-correlation, minimal-basis-h2-model, coupled-pair-approximations, coupled-cluster-doubles, linked-cluster-theorem, heh-plus-minimal-basis-model, ci-in-practice]
order: 60
date: 2026-11-03
---

## Definition

Comparing molecules of different size (reaction energies, interaction energies) needs methods that are equally good for systems with different numbers of electrons.

**Size consistency.** For two noninteracting identical monomers, a method is **size consistent** if $E(\text{dimer}) = 2E(\text{monomer})$.

**General form.** For an interacting many-particle system, the energy should become proportional to the number of particles as $N\to\infty$. This is often called size extensivity.

**Examples.**

- **Hartree-Fock is size consistent.** For noninteracting closed shells the orbitals localize on each monomer and all cross integrals vanish.
- **Full CI is size consistent**, as any exact theory is.
- **Truncated CI is not.**

## Why DCI fails

Monomer DCI allows doubles on each monomer. In the dimer, having **both** monomers doubly excited at once is a quadruple excitation of the supermolecule, which DCI excludes. The dimer DCI wave function cannot be the product of the monomer DCI wave functions.

## The N-monomer model

**Setup.** Take $N$ minimal-basis H$_2$ molecules ([[minimal-basis-h2-model]]) infinitely far apart. Monomer $i$ has orbitals $1_i$ (occupied) and $2_i$ (virtual). Every integral linking different monomers vanishes.

**Matrix elements.**

- Each local double $|\Psi_{1_i\bar1_i}^{2_i\bar2_i}\rangle$ couples to $|\Psi_0\rangle$ with $K_{12}$ and has excitation energy $2\Delta$, as in [[full-ci]].
- Local doubles on different monomers differ by four spin orbitals and do not couple to each other.
- Doubles that mix monomers have zero matrix elements (Szabo Ex. 4.10).

**DCI equations.** The eigenvalue problem is

$$
\begin{pmatrix}
0 & K_{12} & K_{12} & \cdots & K_{12}\\
K_{12} & 2\Delta & 0 & \cdots & 0\\
K_{12} & 0 & 2\Delta & & 0\\
\vdots & & & \ddots & \\
K_{12} & 0 & 0 & & 2\Delta
\end{pmatrix}
\begin{pmatrix}1\\ c_1\\ c_2\\ \vdots\\ c_N\end{pmatrix}
= {}^NE_{\text{corr}}(\text{DCI})
\begin{pmatrix}1\\ c_1\\ c_2\\ \vdots\\ c_N\end{pmatrix}.
$$

By symmetry all $c_i$ are equal, $c_i = K_{12}/({}^NE_{\text{corr}} - 2\Delta)$, and ${}^NE_{\text{corr}} = NK_{12}c_i$. Hence

$$
{}^NE_{\text{corr}}(\text{DCI}) = \Delta - \sqrt{\Delta^2 + NK_{12}^2},
\qquad\text{whereas}\qquad
{}^NE_{\text{corr}}(\text{exact}) = N\Big(\Delta - \sqrt{\Delta^2 + K_{12}^2}\Big).
$$

**Large-$N$ behaviour.** For large $N$, ${}^NE_{\text{corr}}(\text{DCI})\to-\sqrt N\,K_{12}$, so the correlation energy **per monomer goes to zero**. DCI is useless for an extended system.

Adding quadruples (DQCI) is exact only for $N = 2$. For larger $N$ the per-monomer correlation still vanishes, only more slowly. No truncated CI is size consistent.

!!! example "Numbers for STO-3G H₂ at R = 1.4 bohr (Szabo Ex. 4.11, 4.14e)"
    $\Delta = 0.788645$ and $K_{12} = 0.181258$ hartree. "+Q" is the Davidson-corrected DCI of [[cisd]].

    | $N$ | ${}^NE_{\text{corr}}(\text{DCI})/N$ | DCI / exact | DCI+Q / exact |
    |---:|---:|---:|---:|
    | 1 | −0.020562 | 1.000 | 1.013 |
    | 2 | −0.020307 | 0.988 | 1.012 |
    | 3 | −0.020064 | 0.976 | 1.010 |
    | 10 | −0.018629 | 0.906 | 0.993 |
    | 11 | −0.018455 | 0.898 | 0.989 |
    | 20 | −0.017115 | 0.832 | 0.958 |
    | 100 | −0.011881 | 0.578 | 0.752 |

    **Dimer.** For $N = 2$, ${}^2E_{\text{corr}}(\text{DCI}) = -0.0406$ against the exact $-0.0411$ hartree, as in Szabo.

    **Errors match the book.** DCI errs by 2.4% at $N=3$, 10% at $N=11$ and 42% at $N=100$. The Davidson correction errs by 25% at $N=100$, and by about 1% for $3\le N\le11$; Szabo states "within 1%", and with these integrals it is 1.0-1.1% at the ends of that range. Computed for this note.

## Full CI is size consistent (Szabo Ex. 4.12)

For the dimer, full CI adds the simultaneous double excitation (a quadruple) $|\Psi_Q\rangle$ with coefficient $c_3$, which couples to each local double by $K_{12}$ and has excitation energy $4\Delta$. Solving the $4\times4$ problem gives

$$
{}^2E_{\text{corr}} = 2\big(\Delta - \sqrt{\Delta^2 + K_{12}^2}\big),
\qquad
c_3 = c_1c_2 = c_1^2 .
$$

The correlation energy is exactly twice the monomer value. The coefficient of the quadruple is the **product** of the coefficients of the doubles that compose it. This is general for independent fragments, and it motivates approximating quadruples as products of doubles. That idea is the starting point of coupled-pair and cluster theories (Szabo Ch. 5).

## Perturbation theory is size consistent (Szabo Ex. 4.13)

Expanding for $NK_{12}^2\ll\Delta^2$:

$$
{}^NE_{\text{corr}}(\text{DCI}) = -\frac{NK_{12}^2}{2\Delta} + \frac{N^2K_{12}^4}{8\Delta^3} - \cdots
$$

The leading term is exactly $N$ times the monomer second-order energy $-K_{12}^2/(2\Delta)$. The $N^2$ term is spurious, and it is what the Davidson correction cancels at leading order ([[cisd]]). Low-order perturbation estimates are linear in $N$: size consistent.

**Only the Rayleigh-Schrödinger choice.** Brillouin-Wigner theory puts the exact total energy in every denominator. Truncated at second order, its per-fragment correlation for $n$ separated HeH⁺ ions drops to 0.3% of the RS value at $n = 1000$ ([[perturbation-theory-second-quantization]]).

## The Hartree-Fock overlap vanishes for large systems (Szabo Ex. 4.15)

The normalized monomer full CI wave function is $(1+c^2)^{-1/2}\big(|\Psi_0\rangle + c|\Psi_{1\bar1}^{2\bar2}\rangle\big)$ with $c = -0.11344$. Ignoring antisymmetry between infinitely separated monomers, the $N$-monomer wave function is a product, and

$$
\langle\Psi_0|\Phi_0\rangle = (1 + c^2)^{-N/2} = 0.9936\ (N=1),\quad 0.9381\ (N=10),\quad 0.5277\ (N=100).
$$

The overlap decays exponentially with $N$. The Hartree-Fock energy is size consistent, yet the Hartree-Fock wave function becomes a vanishing component of the exact one. Intermediate normalization ($c_0 = 1$) therefore remains well defined, while the normalized $c_0$ is not a good measure of quality for large systems.

!!! example "Two noninteracting water molecules (6-31G, PySCF 2.14)"
    Two H$_2$O at the geometry of Szabo Table 3.10, 100 bohr apart, all electrons correlated. Energies in hartree:

    | Quantity | Dimer | 2 × monomer |
    |---|---:|---:|
    | $E_{\text{HF}}$ | −151.967995 | −151.967993 |
    | $E_{\text{corr}}$(CISD) | −0.250687 | −0.260135 |
    | $E_{\text{corr}}$(CISD+Q) | −0.268167 | −0.270370 |
    | $E_{\text{corr}}$(FCI) | | −0.273696 |

    **Hartree-Fock** is additive (the $2\,\mu$Ha difference is SCF convergence).

    **CISD** loses 9.4 mHa (3.6% of its monomer correlation) just from doubling the system. This is far larger than typical intermolecular interaction energies.

    **The Davidson correction** reduces the error to 2.2 mHa.

## The same failure seen from Jørgensen and Simons

**Be₂.** If Be needs $2s^2$ and $2p^2$, a balanced Be₂ calculation needs the products $2s_A^22s_B^2$, $2s_A^22p_B^2$, $2p_A^22s_B^2$ and $2p_A^22p_B^2$. The last is a quadruple excitation, and Be$_n$ needs $2n$-fold excitations. A doubles CI or MCSCF can give a smooth curve that is nevertheless biased towards the molecule near equilibrium ([[ci-in-practice]]).

**n separated HeH⁺ ions (J-S Problem 2.7).** The DCI matrix has the same arrow shape as for H₂, and $E_{\text{corr}} = \tfrac12[C - (C^2 + 4nB^2)^{1/2}]$, which grows as $\sqrt n$. With J-S's integrals, DCI recovers 97.4%, 80.3% and 42.9% of $n$ times the monomer correlation energy for $n = 10$, 100 and 1000 ([[heh-plus-minimal-basis-model]]).

**Literature (Bartlett and Purvis, quoted by J-S).** DCI size-consistency errors for $n$ H₂ molecules are 1.5, 4.8, 12.3, 48.0 and 79.1% for $n = 2$, 4, 10, 100 and 1000; for He atoms 0.8, 2.4, 6.5, 34.8 and 70.8%. The two-function HeH⁺ model shows smaller errors because its correlation energy is small and its excitation gap large.

## Helgaker, Jørgensen and Olsen: size-extensivity in second quantization

HJO use **size-extensive** for the requirement that a method give the same energy for noninteracting fragments whether it is applied to each fragment separately or to the compound system. The wave function should then be **multiplicatively separable** and the energy **additively separable**.

**Fragment operators commute.** Orbitals on noninteracting fragments $A$ and $B$ are orthogonal, so their elementary operators anticommute. Two strings $\hat O_A$ and $\hat O_B$ therefore anticommute if both have half-integral rank (an odd number of elementary operators) and commute otherwise. Hamiltonians are rank 1 or 2, so each commutes with every operator of the other fragment.

**Exact separability.** With wave operators $\hat\psi_A$, $\hat\psi_B$ (strings of creators generating the fragment states from the vacuum),

$$
\hat H(\hat\psi_A\hat\psi_B)|\text{vac}\rangle = (E_A + E_B)\,\hat\psi_A\hat\psi_B|\text{vac}\rangle .
$$

No antisymmetrizer is needed: the operator algebra supplies the permutational symmetry. This holds for the exact state in any finite Fock space.

**Linear models: product spaces.** A linear variational wave function is size-extensive only if the compound space is the **direct product** of the fragment spaces.

- **Matrix form.** $\mathbf H = \mathbf H_A\otimes\mathbf 1 + \mathbf 1\otimes\mathbf H_B$ (a Kronecker sum), with eigenvalues $E_A + E_B$ and eigenvectors $\mathbf C_A\otimes\mathbf C_B$.
- **Cost.** The dimension is $m_Am_B$, exponential in the number of fragments, and the coefficients $\mathbf C_A\otimes\mathbf C_B$ are spurious "interaction" parameters for systems that do not interact.
- **Any other space** gives a different (higher) energy. Truncated CI of the compound system is such a space.

**Exponential models: manifest separability.** With $\hat\psi_A = \exp(\hat X_A)\hat A^\dagger$ and similarly for $B$, the compound wave operator is

$$
\hat\psi_A\hat\psi_B = \exp(\hat X_A + \hat X_B)\,\hat A^\dagger\hat B^\dagger,
$$

so the parameters simply add, their number grows linearly, and parameters optimal for the fragments remain optimal for the compound system. HJO call a model **manifestly separable** if its compound wave function becomes a product when the interaction parameters $\mathbf P_{AB}$ are zero. The exponential (coupled-cluster) ansatz has this property; the linear (CI) ansatz does not ([[coupled-cluster-second-quantization]]).

**Size-extensive is not "equally accurate".** Most size-extensive methods describe the four atoms of $\text{H}_4\to4\text{H}$ exactly in a given basis but the molecule only approximately. Size-extensivity guarantees only that the dissociated system comes out the same whether computed in one piece or in fragments.

!!! example "Checks (computed for this note)"
    - **Kronecker sum** of random symmetric $4\times4$ and $5\times5$ matrices: all 20 eigenvalues equal the sums $E_A + E_B$ to $3\times10^{-15}$, and the ground eigenvector is $\mathbf C_A\otimes\mathbf C_B$ to $4\times10^{-16}$. Removing a single product basis vector raises the lowest eigenvalue by 0.0162.
    - **$n$ H₂ molecules (STO-3G, 1.4 bohr, 50 bohr apart).** CCSD correlation per molecule is −0.020562 for $n = 1, 2, 4, 8$. CISD gives −0.020562, −0.020307, −0.019832, −0.018999.

## Source

Szabo and Ostlund, *Modern Quantum Chemistry* (Dover, 1996; reprint of the revised first edition, McGraw-Hill, 1989), Sec. 4.6, pp. 261-269, Eqs. (4.53)-(4.70), Ex. 4.10-4.15. Jørgensen and Simons, *Second Quantization-Based Methods in Quantum Chemistry* (Academic Press, New York, 1981), Ch. 2, Sec. D.5, p. 47, and Problem 2.7 with Solution, pp. 54-66. All numbers computed for this note except the Bartlett-Purvis percentages. Helgaker, Jørgensen and Olsen, *Molecular Electronic-Structure Theory* (Wiley, Chichester, 2000), Sec. 4.3, pp. 126-135.
