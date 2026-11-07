---
id: electronic-structure-methods-at-a-glance
title: Electronic-structure methods at a glance - wave-function ansatz, energy expression, working equations, formal properties and key references, with one water/6-31G benchmark
summary: A one-page reference for the standard methods, in one notation (spin orbitals, ⟨pq||rs⟩, occupied i, j, virtual a, b). It covers HF (RHF/UHF/GHF), Kohn-Sham DFT, MP2, CI, CC with (T) and EOM-CC, unitary/variational CC, MCSCF/CASSCF, MRCI, CASPT2/NEVPT2, DMRG, VQE and SQD. For each it gives the wave-function form, the energy expression, the equations that fix the parameters, whether the method is variational and size-extensive, its cost, the original paper and a textbook chapter. A water/6-31G benchmark against all-electron FCI is included. CCSD(T) is 0.52 mE_h above FCI and CCSD 1.52. CISD (+6.8) and MP2 (+8.0) are an order of magnitude worse. Valence CASSCF(8,6) captures only static correlation (81.6 mE_h above FCI), and NEVPT2 on top of it brings this to 11.3. The B3LYP total energy (−264 mE_h relative to FCI) is not comparable with the wave-function numbers.
status: in-progress
kind: reference
level: intermediate
tags: [overview, cheat-sheet, wave-function-methods, dft, hartree-fock, coupled-cluster, ci, mcscf, perturbation-theory, references]
prerequisites: []
related: [reading-order-electronic-structure, standard-models-h2-and-water, size-consistency, electron-correlation, ghf, rhf, mp2, cisd, full-ci, ccsd-spin-orbital-equations, perturbative-triples-cc2-cc3, eom-ccsd-and-size-extensivity, variational-and-unitary-coupled-cluster, mcscf-and-gvb, caspt2-and-caspt-series]
also: [04_Electronic_Structure_Theory/04_Electron_Correlation_and_Wavefunction_Methods/05_Comparison_of_Correlation_Methods]
date: 2026-11-07
---

## Notation

**Hamiltonian.** Clamped nuclei, atomic units, spin orbitals $\chi_p$, and

$$
\hat H = \sum_{pq}h_{pq}a_p^\dagger a_q + \tfrac14\sum_{pqrs}\langle pq||rs\rangle a_p^\dagger a_q^\dagger a_s a_r + V_{nn}.
$$

**Index conventions.** $i,j,k$ occupied and $a,b,c$ virtual in the reference $\Phi_0$; $|\Phi_i^a\rangle$, $|\Phi_{ij}^{ab}\rangle$ are excited determinants.

**Reference-dependent quantities.** $f_{pq} = h_{pq}+\sum_i\langle pi||qi\rangle$ is the Fock matrix and $\varepsilon_p$ the canonical orbital energies. $D_{ij}^{ab}=\varepsilon_i+\varepsilon_j-\varepsilon_a-\varepsilon_b$. $N$ is a generic measure of system size.

**Property definitions.**

- *Variational*: the energy is an expectation value of a normalized trial state, hence an upper bound.
- *Size-extensive*: the energy scales correctly with the number of non-interacting units ([[size-consistency]]).

## Summary table

| Method | Wave function | Variational | Size-extensive | Cost |
|---|---|---|---|---|
| HF | one determinant | yes | yes¹ | $N^4$ (formal) |
| KS-DFT | determinant of a non-interacting reference | no² | yes | $N^3$-$N^4$ |
| MP2 | $\Phi_0$ + first-order doubles | no | yes | $N^5$ |
| CISD | linear S+D expansion | yes | no | $N^6$ / iteration |
| FCI | all determinants | yes (exact in basis) | yes | factorial |
| CCSD | $e^{\hat T_1+\hat T_2}\Phi_0$ | no | yes | $N^6$ / iteration |
| CCSD(T) | CCSD + perturbative connected triples | no | yes | $N^7$ (once) |
| EOM-CCSD | $\hat R_k e^{\hat T}\Phi_0$ | no | for ground state and local excitations | $N^6$ / root |
| UCCSD / VCCSD | $e^{\hat T-\hat T^\dagger}\Phi_0$ / normalized $e^{\hat T}\Phi_0$ | yes (if not truncated) | yes | non-terminating |
| CASSCF | FCI in active space, orbitals optimized | yes | yes³ | factorial in active size |
| MRCI(SD) | reference + S, D out of it | yes | no (+Q helps) | high |
| CASPT2 / NEVPT2 | CASSCF + first-order correction | no | approx. / yes⁴ | $\sim N^5$ + active-space RDMs |
| DMRG | matrix product state | yes | yes | polynomial in active size $L$ and bond dimension $m$ |
| VQE | parametrized circuit $U(\boldsymbol\theta)\Phi_0$ | yes (ideal device) | ansatz-dependent | quantum resource count |
| SQD | diagonalize $\hat H$ in sampled determinants | yes (subspace) | no in general | classical diagonalization of the subspace |

**Footnotes.**

1. RHF is size-extensive but not size-consistent for dissociation into open-shell fragments ([[h2-dissociation-rhf-uhf]]).
2. The KS energy is variational in the density for the *exact* functional; approximate functionals give no bound.
3. Given a consistent choice of active space for the fragments.
4. CASPT2 is not exactly size-extensive because of its projected $\hat H_0$ ([[caspt2-and-caspt-series]]); strongly contracted NEVPT2 with the Dyall Hamiltonian is size-consistent (Angeli et al. 2001).

## Mean-field methods

**Hartree-Fock** ([[rhf]], [[uhf]], [[ghf]]).

$$
\Phi_0 = |\chi_1\cdots\chi_N|,\qquad
E_{\text{HF}} = \sum_i h_{ii} + \tfrac12\sum_{ij}\langle ij||ij\rangle,\qquad
\hat f\chi_p = \varepsilon_p\chi_p\ \Rightarrow\ \mathbf F\mathbf C = \mathbf S\mathbf C\boldsymbol\varepsilon .
$$

- **RHF, UHF, GHF.** These restrict $\chi$ to closed-shell, collinear or general spinors.
- **Stationarity.** Equivalent to $f_{ia}=0$ (Brillouin).
- **References.** Hartree, *Proc. Camb. Phil. Soc.* **24**, 89 (1928); Fock, *Z. Phys.* **61**, 126 (1930); Roothaan, *Rev. Mod. Phys.* **23**, 69 (1951); Hall, *Proc. R. Soc. A* **205**, 541 (1951); Pople and Nesbet, *J. Chem. Phys.* **22**, 571 (1954).
- **Textbooks.** Szabo-Ostlund Ch. 3; HJO Ch. 10.

**Kohn-Sham DFT** ([[kohn-sham-dft]]).

$$
E[\rho] = T_s[\rho] + \int v(\mathbf r)\rho(\mathbf r)\,\mathrm d\mathbf r + J[\rho] + E_{xc}[\rho],\qquad
\Big[-\tfrac12\nabla^2 + v + v_J + v_{xc}\Big]\phi_i = \varepsilon_i\phi_i,\qquad \rho = \sum_i|\phi_i|^2 .
$$

- **What the determinant is.** It is the non-interacting reference, not an approximation to the interacting wave function. All many-body effects sit in $E_{xc}$.
- **Hybrids.** They mix in a fraction of exact exchange, e.g. B3LYP.
- **References.** Hohenberg and Kohn, *Phys. Rev.* **136**, B864 (1964); Kohn and Sham, *Phys. Rev.* **140**, A1133 (1965); Becke, *J. Chem. Phys.* **98**, 5648 (1993).

## Single-reference correlation

**MP2** ([[mp2]]). $\hat H_0 = \sum_p\varepsilon_p a_p^\dagger a_p$ and $\hat V = \hat H-\hat H_0$.

$$
|\Psi^{(1)}\rangle = \tfrac14\sum_{ijab}\frac{\langle ab||ij\rangle}{D_{ij}^{ab}}|\Phi_{ij}^{ab}\rangle,\qquad
E^{(2)} = \tfrac14\sum_{ijab}\frac{|\langle ij||ab\rangle|^2}{D_{ij}^{ab}} .
$$

- **References.** Møller and Plesset, *Phys. Rev.* **46**, 618 (1934).
- **Textbooks.** Szabo-Ostlund Ch. 6; HJO Ch. 14.

**Configuration interaction** ([[cisd]], [[full-ci]]).

$$
\Psi = c_0\Phi_0 + \sum_{ia}c_i^a\Phi_i^a + \tfrac14\sum_{ijab}c_{ij}^{ab}\Phi_{ij}^{ab}+\cdots,\qquad
\mathbf H\mathbf c = E\mathbf c .
$$

- **Truncation.** It gives an upper bound, but the energy appearing in the amplitude equations makes truncated CI non-extensive ([[coupled-cluster-diagrams]]).
- **Textbooks.** Szabo-Ostlund Ch. 4; HJO Ch. 11.

**Coupled cluster** ([[coupled-cluster-second-quantization]], [[ccsd-spin-orbital-equations]]).

$$
\Psi = e^{\hat T}\Phi_0,\quad
E = \langle\Phi_0|e^{-\hat T}\hat He^{\hat T}|\Phi_0\rangle = E_{\text{HF}} + \sum f_{ia}t_i^a + \tfrac14\sum\langle ij||ab\rangle t_{ij}^{ab} + \tfrac12\sum\langle ij||ab\rangle t_i^at_j^b,
$$

$$
0 = \langle\Phi_\mu|e^{-\hat T}\hat He^{\hat T}|\Phi_0\rangle\quad(\mu = \text{singles, doubles}).
$$

**Triples correction.** CCSD(T) adds $E_{[T]}+E_{ST}$ from converged amplitudes ([[perturbative-triples-cc2-cc3]]).

**References.**

- Čížek, *J. Chem. Phys.* **45**, 4256 (1966).
- Purvis and Bartlett, *J. Chem. Phys.* **76**, 1910 (1982).
- Raghavachari, Trucks, Pople and Head-Gordon, *Chem. Phys. Lett.* **157**, 479 (1989).
- Textbooks: HJO Ch. 13; Shavitt-Bartlett; Crawford-Schaefer, *Rev. Comput. Chem.* **14**, 33 (2000).

**EOM-CC** ([[eom-ccsd-and-size-extensivity]]).

$$
\Psi_k = \hat R_k e^{\hat T}\Phi_0,\qquad \bar H\hat R_k|\Phi_0\rangle = E_k\hat R_k|\Phi_0\rangle,\qquad \bar H = e^{-\hat T}\hat He^{\hat T},
$$

a non-Hermitian eigenproblem in the S+D space. Reference: Stanton and Bartlett, *J. Chem. Phys.* **98**, 7029 (1993).

**Unitary and variational CC** ([[variational-and-unitary-coupled-cluster]]).

$$
E_{\text{UCC}} = \langle\Phi_0|e^{-\hat\sigma}\hat He^{\hat\sigma}|\Phi_0\rangle,\qquad \hat\sigma = \hat T - \hat T^\dagger,
$$

minimized over $\hat T$. The BCH series does not terminate. References: Hoffmann and Simons, *J. Chem. Phys.* **88**, 993 (1988); Bartlett, Kucharski and Noga, *Chem. Phys. Lett.* **155**, 133 (1989).

## Multireference methods

**MCSCF / CASSCF** ([[mcscf-and-gvb]], [[mcscf-parametrization-gradient-and-hessian]]).

$$
\Psi = e^{-\hat\kappa}\sum_{I\in\text{CAS}}c_I\Phi_I,\qquad
E = \sum_{pq}h_{pq}D_{pq} + \tfrac12\sum_{pqrs}g_{pqrs}d_{pqrs},\qquad
\frac{\partial E}{\partial\kappa_{pq}} = 0,\ \ \mathbf H_{\text{CAS}}\mathbf c = E\mathbf c .
$$

- **Densities.** $D$ and $d$ are the one- and two-body densities. Here $g_{pqrs}=(pq|rs)$ in spatial orbitals, as in HJO.
- **Variants.** A state average minimizes $\sum_k w_kE_k$ ([[state-averaged-mcscf-and-configuration-rotations]]).
- **References.** Roos, Taylor and Siegbahn, *Chem. Phys.* **48**, 157 (1980); HJO Ch. 12.

**MRCI** ([[mrci]]).

$$
\Psi = \sum_I c_I\Phi_I + \sum_{\text{S,D out of the reference}}c_\mu\Phi_\mu,
$$

with the excitations often internally contracted, $\hat E_{pq}\hat E_{rs}\Psi_0$. It is solved as a linear eigenproblem and is not size-extensive (Davidson +Q). Reference: Werner and Knowles, *J. Chem. Phys.* **89**, 5803 (1988).

**CASPT2 / NEVPT2** ([[caspt2-and-caspt-series]], [[nevpt2]]).

$$
(\hat H_0 - E_0)|\Psi^{(1)}\rangle = -\hat Q\hat V|\Psi_0\rangle,\qquad E^{(2)} = \langle\Psi_0|\hat V|\Psi^{(1)}\rangle .
$$

- **CASPT2** uses a projected generalized-Fock $\hat H_0$. Reference: Andersson, Malmqvist, Roos, Sadlej and Wolinski, *J. Phys. Chem.* **94**, 5483 (1990).
- **NEVPT2** uses Dyall's $\hat H_0$, which keeps two-electron terms in the active space. Reference: Angeli, Cimiraglia, Evangelisti, Leininger and Malrieu, *J. Chem. Phys.* **114**, 10252 (2001).

**DMRG** ([[dmrg]]).

$$
\Psi = \sum_{k_1\cdots k_L}\mathbf A^{k_1}\mathbf A^{k_2}\cdots\mathbf A^{k_L}\,|k_1k_2\cdots k_L\rangle,\qquad k_l\in\{0,\uparrow,\downarrow,\uparrow\downarrow\},
$$

- **Ansatz.** The matrices have bond dimension at most $m$, and are optimized site by site (sweeps) by small eigenproblems.
- **Exactness.** It is variational and becomes FCI-in-the-active-space as $m\to\infty$.
- **References.** White, *Phys. Rev. Lett.* **69**, 2863 (1992); White and Martin, *J. Chem. Phys.* **110**, 4127 (1999).

## Quantum-computing methods

**VQE** ([[vqe]]).

$$
E(\boldsymbol\theta) = \langle\Phi_0|\hat U^\dagger(\boldsymbol\theta)\hat H\hat U(\boldsymbol\theta)|\Phi_0\rangle = \sum_k c_k\langle\hat P_k\rangle_{\boldsymbol\theta},
$$

where $\hat H$ is mapped to Pauli strings $\hat P_k$ and $\boldsymbol\theta$ is minimized classically. UCCSD and ADAPT are chemistry-motivated choices of $\hat U$. Reference: Peruzzo et al., *Nat. Commun.* **5**, 4213 (2014).

**SQD / quantum-selected CI** ([[sqd]]).

- **Method.** Sample bitstrings (determinants) from a quantum state and recover their particle number and spin. Then project and diagonalize, $\mathbf H_S\mathbf c = E\mathbf c$ on the sampled set $S$.
- **Character.** It is variational within $S$. Its quality depends on how much important weight the samples reveal.
- **References.** J. Robledo-Moreno et al., *Sci. Adv.* **11**, eadu9991 (2025), doi:10.1126/sciadv.adu9991. Quantum-selected CI: K. Kanno et al., arXiv:2302.11320 (to verify).

!!! example "Water/6-31G, all electrons, r = 0.9572 Å, 104.52°: total energies against FCI (computed for this note)"
    | Method | $E$ ($E_h$) | $E-E_{\text{FCI}}$ (m$E_h$) |
    |---|---:|---:|
    | RHF | −75.983997 | +136.840 |
    | MP2 | −76.112793 | +8.044 |
    | CISD | −76.114058 | +6.779 |
    | CCSD | −76.119320 | +1.518 |
    | CCSD(T) | −76.120314 | +0.524 |
    | CASSCF(8e,6o), full valence | −76.039200 | +81.637 |
    | SC-NEVPT2 on that CASSCF | −76.109530 | +11.307 |
    | FCI | −76.120837 | 0 |
    | KS-DFT, B3LYP | −76.384916 | (−264.078) |

    **Reading the numbers.**

    - **Correlation energy.** $E_{\text{FCI}}-E_{\text{RHF}} = -136.8$ m$E_h$. CCSD recovers 98.9% of it and CCSD(T) 99.6%.
    - **CASSCF.** It recovers only 40%. Its natural occupations (1.999, 1.999, 1.978, 1.976, 0.025, 0.023) show that water at equilibrium has almost no static correlation, so CASSCF alone misses the dynamic part.
    - **NEVPT2.** It adds most of the missing dynamic correlation but is limited by the small basis and by second order.
    - **DFT.** The B3LYP total energy lies *below* FCI. A DFT total energy is not an approximation to the FCI energy in a finite basis, so only energy differences should be compared.
    - **Excited state.** The lowest singlet excitation is 0.30849 $E_h$ with EOM-EE-CCSD and 0.31220 $E_h$ with FCI (second singlet root).

## Source

The equations are standard; each is given here in my notation, with the original paper listed beside it. Textbook pointers:

- A. Szabo and N. S. Ostlund, *Modern Quantum Chemistry* (Dover, 1996), Chs. 3, 4 and 6.
- T. Helgaker, P. Jørgensen and J. Olsen, *Molecular Electronic-Structure Theory* (Wiley, 2000), Chs. 10-14.
- I. Shavitt and R. J. Bartlett, *Many-Body Methods in Chemistry and Physics* (Cambridge University Press, 2009).

The ESQC 2026 lectures by Loos (HF), Crawford (CC) and the multiconfigurational-methods series (CASSCF, DMRG, VQE, SQD) were used for the method list and classifications.

References not checked against the original article in this session: everything except Stanton-Bartlett 1993, Purvis-Bartlett 1982, Raghavachari et al. 1989 and Robledo-Moreno et al. 2025, which were checked online. The others are standard citations but should be spot-checked; Kanno et al. is marked "to verify".

Numbers: `esqc/overview/water_631g_methods.py` (PySCF 2.15: RHF, B3LYP, MP2, CISD, CCSD, CCSD(T), CASSCF, `mrpt.NEVPT`, FCI, EOM-EE-CCSD).
