---
id: variational-and-unitary-coupled-cluster
title: Variational and unitary coupled cluster (VCC, UCC, XCC) - why the energy functionals do not truncate, upper bounds, and projective CCSD falling below FCI for stretched H₄
summary: Standard CC is projective. The energy ⟨Φ₀|e^{−T}He^{T}|Φ₀⟩ is not an expectation value, but e^{−T}He^{T} terminates after four commutators. Making CC variational replaces this by an expectation value. VCC uses ⟨e^{T}Φ₀|H|e^{T}Φ₀⟩/⟨e^{T}Φ₀|e^{T}Φ₀⟩ and UCC uses ⟨Φ₀|e^{−σ}He^{σ}|Φ₀⟩ with σ = T − T†. Because [T†, T] ≠ 0, neither functional terminates, and practical schemes (truncated UCC, expectation-value CC = XCC) cut the series at a chosen order. With exact exponentials both are upper bounds to FCI, and both are size-extensive. Computed with exact matrix exponentials for linear H₄/STO-3G. As the chain is stretched, projective CCSD falls below FCI (−18.3 mE_h at R = 2.0 Å), while VCCSD (+4.49) and UCCSD (+4.57) stay above. The UCCSD energy from its truncated BCH series oscillates by hundreds of mE_h and has converged to 0.03 mE_h only after eight commutators. The projective CC series vanishes identically beyond four.
status: in-progress
kind: theory
level: advanced
tags: [coupled-cluster, variational-cc, unitary-cc, ucc, xcc, upper-bound, bch, h4, vqe]
prerequisites: [coupled-cluster-second-quantization, baker-campbell-hausdorff, variational-principle]
related: [coupled-cluster-hierarchy-and-size-extensivity, coupled-cluster-variants-brueckner-qcisd-open-shell, coupled-cluster-optimization-and-lagrangian, full-ci, size-consistency]
also: []
date: 2026-11-07
---

## Projective versus variational

**Notation.** $\hat T = \hat T_1+\hat T_2+\cdots$ is the usual excitation operator. The amplitudes are real throughout.

**Projective CC** ([[coupled-cluster-second-quantization]]). The Schrödinger equation $\hat H e^{\hat T}|\Phi_0\rangle = Ee^{\hat T}|\Phi_0\rangle$ is multiplied by $e^{-\hat T}$ and projected:

$$
E_{\text{CC}} = \langle\Phi_0|e^{-\hat T}\hat He^{\hat T}|\Phi_0\rangle,\qquad
0 = \langle\Phi_\mu|e^{-\hat T}\hat He^{\hat T}|\Phi_0\rangle .
$$

- **Why it is practical.** $\hat T$ contains only quasi-creators, so all $\hat T$ components commute. In the BCH expansion each $\hat T$ must contract with $\hat H$, and $\hat H$ has at most four lines, so $e^{-\hat T}\hat He^{\hat T}$ ends after the fourfold commutator. This is exact, not an approximation.
- **The price.** The energy is not the expectation value of any normalized state. A truncated CC energy is not bounded from below by $E_{\text{FCI}}$ and can fall below it.

**Variational CC (VCC).**

$$
E_{\text{VCC}}[\hat T] = \frac{\langle\Phi_0|e^{\hat T^\dagger}\hat He^{\hat T}|\Phi_0\rangle}{\langle\Phi_0|e^{\hat T^\dagger}e^{\hat T}|\Phi_0\rangle},\qquad \partial E_{\text{VCC}}/\partial t_\mu = 0 .
$$

**Unitary CC (UCC).** With the anti-Hermitian generator $\hat\sigma = \hat T - \hat T^\dagger$, the state $e^{\hat\sigma}|\Phi_0\rangle$ is automatically normalized, and

$$
E_{\text{UCC}}[\hat T] = \langle\Phi_0|e^{-\hat\sigma}\hat He^{\hat\sigma}|\Phi_0\rangle = \sum_{k=0}^\infty\frac1{k!}\langle\Phi_0|[\cdots[[\hat H,\hat\sigma],\hat\sigma],\cdots,\hat\sigma]_k|\Phi_0\rangle .
$$

**Why neither terminates.**

- $\hat T^\dagger$ contains quasi-annihilators, so $[\hat T^\dagger,\hat T]\ne0$.
- $\hat T^\dagger$ and $\hat T$ can contract with *each other*, not only with $\hat H$.
- Both functionals therefore generate arbitrarily long strings. VCC must be truncated in the numerator and denominator, UCC in the commutator series.
- Expectation-value CC (XCC) is one such systematic truncation, by order in a perturbation-theory counting.

## Properties

| | projective CC | exact VCC | exact UCC |
|---|---|---|---|
| Energy is an expectation value | no | yes | yes |
| Upper bound to $E_{\text{FCI}}$ | no | yes | yes |
| Hellmann-Feynman (no $\Lambda$ equations) | no | yes | yes |
| Size-extensive | yes | yes | yes |
| Similarity transform terminates | after 4 commutators | no | no |
| Exact for separated 2-electron fragments at the SD level | yes | yes | yes |

**Size-extensivity of the exact functionals.** For non-interacting $A+B$, $\hat T = \hat T_A + \hat T_B$ with $[\hat T_A,\hat T_B]=0$ and similarly for $\hat T^\dagger$. The exponentials factor, $e^{\hat T}|\Phi_0\rangle = e^{\hat T_A}|\Phi_0^A\rangle\,e^{\hat T_B}|\Phi_0^B\rangle$, so the expectation values separate.

**Size-extensivity of truncated functionals.** They remain size-extensive when the truncation keeps only commutators (connected terms). This is why truncated UCC is written in commutator form.

**Lagrangian.** Projective CC needs one for properties ([[coupled-cluster-optimization-and-lagrangian]]). VCC and UCC are stationary in the amplitudes, so the Hellmann-Feynman theorem applies directly.

**Why UCC matters for quantum computing.** $e^{\hat\sigma}$ is unitary, so it can be implemented as a quantum circuit (after Trotterization and a fermion-to-qubit mapping). The energy is then measured as an expectation value, and the non-terminating BCH series is never evaluated classically. That is why the UCCSD ansatz is the standard chemistry-motivated VQE ansatz. Circuits, Trotter ordering and measurement are not covered here.

!!! example "Linear H₄/STO-3G: projective, variational and unitary CCSD with exact exponentials (computed for this note)"
    **Setup.** Four H atoms, equally spaced by $R$ on a line, with an RHF reference: 8 spin orbitals, 4 electrons, and 26 spin-conserving singles and doubles amplitudes.

    - **Fock-space operators.** $\hat H$ and every excitation operator are $256\times256$ matrices built with Jordan-Wigner. Exponentials are exact matrix exponentials.
    - **Projective CCSD.** It solves $\langle\Phi_\mu|e^{-\hat T}\hat He^{\hat T}|\Phi_0\rangle=0$ by root finding, and agrees with PySCF `GCCSD` to all printed digits.
    - **VCCSD and UCCSD.** Both are minimized with BFGS, starting from the CCSD amplitudes.

    $E - E_{\text{FCI}}$ in m$E_h$:

    | $R$ (Å) | $E_{\text{HF}}$ ($E_h$) | $E_{\text{FCI}}$ ($E_h$) | CCSD | VCCSD | UCCSD |
    |---:|---:|---:|---:|---:|---:|
    | 0.8 | −2.121387 | −2.167561 | +0.005 | +0.014 | +0.015 |
    | 1.2 | −2.003867 | −2.102608 | −0.063 | +0.314 | +0.321 |
    | 1.6 | −1.772203 | −1.967560 | −3.012 | +1.940 | +1.988 |
    | 2.0 | −1.575616 | −1.897781 | −18.305 | +4.492 | +4.570 |

    **Results.**

    - **Non-variational collapse.** Projective CCSD is excellent near equilibrium. On stretching it drops below FCI, by $-18.3$ m$E_h$ at 2.0 Å, where the RHF reference is strongly multiconfigurational.
    - **Upper bounds.** Both variational forms stay above FCI, as they must. UCCSD lies a little above VCCSD at every $R$; I have not shown that this ordering holds in general.
    - **Error growth.** The variational energies are bounded, but their error still grows to about 4.5 m$E_h$. Bounding the energy does not fix the missing triples and quadruples.

    **The BCH series, $R=2.0$ Å.** $E_k$ is the UCCSD energy truncated after $k$ nested commutators, at the optimal UCCSD amplitudes. $E_k - E_{\text{UCC}}$ in m$E_h$:

    | $k$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
    |---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
    | | 317.59 | −211.96 | −119.89 | −0.26 | 12.07 | 3.51 | −0.71 | −0.40 | 0.03 |

    **What the series shows.**

    - It oscillates and is still off by 0.4 m$E_h$ after seven commutators.
    - A truncated-UCC energy at low order is not variational. $E_1$ and $E_2$ lie far *below* the exact functional.
    - For the projective CCSD amplitudes at the same geometry, the norms of $\tfrac1{k!}[\cdots[\hat H,\hat T],\cdots,\hat T]_k|\Phi_0\rangle$ are 2.75, 0.43, 0.24, $2.4\times10^{-3}$ and $4.5\times10^{-5}$ for $k=0$ to 4, and **exactly zero** for $k=5$ and 6. That is the termination of the traditional similarity transform, seen numerically.

    **Separated pairs.** For two H₂ molecules 50 Å apart (STO-3G, 0.74 Å bond), VCCSD, UCCSD and FCI all give $-2.2745676690\,E_h$. That is twice the monomer energy, to $2\times10^{-11}$, a residue that FCI shows as well. At the singles-and-doubles level all three methods are exact for non-interacting two-electron fragments.

## Source

T. D. Crawford, *Coupled Cluster Theory*, ESQC 2026 lecture slides, part 1 ("Variational coupled cluster theory", "Size consistency"). The references cited there are:

- M. R. Hoffmann and J. Simons, *J. Chem. Phys.* **88**, 993 (1988) (UCC).
- R. J. Bartlett, S. A. Kucharski and J. Noga, *Chem. Phys. Lett.* **155**, 133 (1989) (UCC).
- R. J. Bartlett and J. Noga, *Chem. Phys. Lett.* **150**, 29 (1988) (XCC).

Part 3 of the ESQC 2026 multiconfigurational-methods lectures ("UCCSD ansatz", in the VQE section) motivates the quantum-computing use.

Statements of the properties are standard and written in my own words. Numbers: `esqc/cc/ucc_vcc.py`, `esqc/cc/ucc_extensivity.py`, `esqc/cc/fermi.py` (PySCF 2.15, SciPy `expm`).
