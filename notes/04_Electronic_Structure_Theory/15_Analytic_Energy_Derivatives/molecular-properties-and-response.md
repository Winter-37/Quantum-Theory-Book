---
id: molecular-properties-and-response
title: Molecular properties as energy derivatives - expectation values, transition moments, finite fields, coupled Hartree-Fock and MCSCF response, CI and coupled-cluster response
summary: Jørgensen and Simons' classification of properties into expectation values, transition properties and response properties. Response properties are derivatives of E(α) for H + αH₁. They can be obtained numerically (finite field, with error-cancelling difference formulas) or analytically. For MCSCF the generalized Brillouin theorem gives E(α) = ⟨H⟩ + α⟨H₁⟩ + α²⟨H₂⟩ − α²(F G)(A − B)⁻¹(F G)ᵀ; one configuration gives coupled Hartree-Fock. CI without orbital response is a sum over states with frozen orbitals, and Hellmann-Feynman holds only for parameters that are fully optimized. Coupled cluster needs both T⁽¹⁾ and T⁽²⁾. HeH⁺ problems 5.1-5.3 and water calculations recomputed.
status: in-progress
kind: theory
level: advanced
tags: [response-properties, dipole-moment, polarizability, finite-field, coupled-hartree-fock, cphf, cmchf, hellmann-feynman, orbital-relaxation, ci-response]
prerequisites: [mcscf-second-order-optimization, scf-second-order-and-stability, brillouin-theorem, cisd]
related: [lagrangian-for-nonvariational-energies, polarization-propagator-rpa, propagators-and-superoperators, analytic-gradients-and-force-constants, heh-plus-minimal-basis-model, coupled-cluster-second-quantization, rayleigh-schrodinger-perturbation-theory, orbital-rotations]
order: 10
date: 2026-11-03
---

## Three classes of properties

**Expectation values.** Dipole and quadrupole moments, spin densities: $\langle0|\mathbf r|0\rangle$ with $\mathbf r = \sum_{rs}\langle\phi_r|\mathbf r|\phi_s\rangle r^\dagger s$ (electronic part; the electron charge sign is applied separately).

- **Which configurations matter.** A one-electron operator has no matrix element between $|0^{(0)}\rangle$ and a double excitation. The first-order RS wave function (doubles only) therefore changes $\langle\mathbf r\rangle$ only in second order, where singles also contribute. Singles and doubles are equally important for one-electron properties, while doubles dominate the energy.
- **Energy differences are different.** Excitation and ionization energies as differences of two state energies are small differences of large numbers, and they carry no upper-bound property. Green's-function methods compute them directly ([[propagators-and-superoperators]]).

**Transition properties.** Moments $\langle0|\mathbf r|n\rangle$ between stationary states. If $|0\rangle$ and $|n\rangle$ are built from different orbital sets (separate MCSCF or natural-orbital CI calculations, the usual case), their determinants are not orthogonal. Evaluating $\langle0|r^\dagger s|n\rangle$ then needs nonorthogonal-orbital machinery. Propagators avoid this by delivering moments and energies directly from one reference ([[polarization-propagator-rpa]]).

**Response properties.** For $H\to H + \alpha H_1$,

$$
E(\alpha) = E_0 - \alpha E_1 - \tfrac12\alpha^2E_2 - \tfrac16\alpha^3E_3 - \cdots
$$

For a static field $\alpha H_1 = \mathscr E\cdot\mathbf r$ (electron charge −1), $E_1$ is the dipole moment, $E_2$ the polarizability and $E_3$, $E_4$ the hyperpolarizabilities. Terms beyond the first exist because the state responds to the perturbation.

## Finite field

**Method.** Compute $E(\alpha)$ with the perturbation in the Hamiltonian for several small $\alpha$ and fit. Combinations of $E_\pm(\alpha) = E(\alpha)\pm E(-\alpha)$ at $\alpha$ and $2\alpha$ cancel the next-higher power. With $E(\alpha) = E_0 + c_1\alpha + c_2\alpha^2 + c_3\alpha^3 + c_4\alpha^4 + \cdots$:

$$
c_1\alpha = \tfrac23E_-(\alpha) - \tfrac1{12}E_-(2\alpha) + O(\alpha^5),\qquad
c_2\alpha^2 = \tfrac23E_+(\alpha) - \tfrac1{24}E_+(2\alpha) - \tfrac54E_0 + O(\alpha^6).
$$

These follow from $E_-(\alpha) = 2c_1\alpha + 2c_3\alpha^3$ and $E_+(\alpha) = 2E_0 + 2c_2\alpha^2 + 2c_4\alpha^4$ (derived here; J-S Eq. 5.4 is this type of formula, partly illegible in the scan).

**Limitations.**

- **Numerical.** The field must be large enough to beat convergence noise and small enough to stay in the Taylor regime.
- **Accuracy.** The result is only as good as $|\tilde0\rangle$ in the field. The basis must be able to polarize, and the configuration list must describe all field strengths equally well.

## Analytic response: MCSCF

**Energy in the field.** Parametrize the MCSCF state by orbital and state rotations, $|\tilde0\rangle = e^{i\lambda}e^{iS}|0\rangle$ ([[mcscf-second-order-optimization]]), and expand the parameters as $\lambda = \alpha\lambda^{(1)} + \alpha^2\lambda^{(2)} + \cdots$ (no zeroth-order term, since $|0\rangle$ is optimal without the field). For $H + \alpha H_1 + \alpha^2H_2$, the generalized Brillouin theorem removes the linear terms, and through $\alpha^2$

$$
E(\alpha;\boldsymbol\kappa,\mathbf P) = E_0 + \alpha\langle0|H_1|0\rangle + \alpha^2\langle0|H_2|0\rangle - 2\alpha(\mathbf F\ \mathbf G)\begin{pmatrix}\boldsymbol\kappa\\ \mathbf P\end{pmatrix} + (\boldsymbol\kappa\ \mathbf P)(\mathbf A - \mathbf B)\begin{pmatrix}\boldsymbol\kappa\\ \mathbf P\end{pmatrix},
$$

with gradients of the perturbation $\mathbf F = \langle0|[\mathbf Q, H_1]|0\rangle$ (orbital) and $\mathbf G = \langle0|[\mathbf R, H_1]|0\rangle$ (state). Here $\mathbf A - \mathbf B$ is the field-free MCSCF Hessian in J-S's convention.

**Solving for the response.** Stationarity gives $(\boldsymbol\kappa, \mathbf P)^{\mathsf T} = \alpha(\mathbf A - \mathbf B)^{-1}(\mathbf F, \mathbf G)^{\mathsf T}$. Substituting:

$$
E(\alpha) = E_0 + \alpha\langle0|H_1|0\rangle + \alpha^2\langle0|H_2|0\rangle - \alpha^2(\mathbf F\ \mathbf G)(\mathbf A - \mathbf B)^{-1}\begin{pmatrix}\mathbf F\\ \mathbf G\end{pmatrix} + O(\alpha^3).
$$

This is the coupled multiconfiguration Hartree-Fock (CMCHF) result (Dalgaard and Jørgensen, 1978, as cited by J-S).

- **The linear coefficient** is the expectation value $\langle0|H_1|0\rangle$.
- **The response** costs one linear solve with the Hessian already needed for second-order MCSCF optimization.

**One configuration: coupled Hartree-Fock.** Dropping the state part,

$$
E(\alpha) = E_0 + \alpha\langle0|H_1|0\rangle + \alpha^2\langle0|H_2|0\rangle - \alpha^2\,\mathbf F(\mathbf A_{11} - \mathbf B_{11})^{-1}\mathbf F + O(\alpha^3),
$$

with the RHF orbital Hessian of [[scf-second-order-and-stability]]. For a closed shell in spatial orbitals (modern sign convention, general knowledge), this is

$$
\alpha_{zz} = 4\,\mathbf z_{ov}^{\mathsf T}(\mathbf A + \mathbf B)^{-1}\mathbf z_{ov}.
$$

Replacing $\mathbf A + \mathbf B$ by its diagonal of orbital-energy differences gives the **uncoupled** value. The full matrix is what "coupled" refers to: the orbitals relax self-consistently in the field.

## Hellmann-Feynman

**Statement.** Differentiating the MCSCF result at $\alpha = 0$ gives $dE/d\alpha = \langle0|H_1|0\rangle$. This holds for SCF and MCSCF because $|0\rangle$ is optimized with respect to **all** its parameters, so the zeroth-order $\lambda^{(0)}$ and $S^{(0)}$ vanish.

**When it fails.** If some parameters are not optimized, extra first-order terms appear and $dE/d\alpha\ne\langle0|H_1|0\rangle$. Truncated CI is the standard example: CI coefficients are variational but the orbitals (from HF) are not. In full CI the orbital parameters are redundant and the theorem holds again.

## CI response

**Frozen orbitals.** If orbital variations are not considered, only the state block remains:

$$
E(\alpha) = E_0 + \alpha\langle0|H_1|0\rangle + \alpha^2\langle0|H_2|0\rangle - \alpha^2\,\mathbf G^\dagger\mathbf A_{22}^{-1}\mathbf G,
$$

with $G_n = \langle n|H_1|0\rangle$ and $(\mathbf A_{22})_{mn} = \langle m|H|n\rangle - \delta_{mn}E_0$ in the space orthogonal to $|0\rangle$. Diagonalizing $\mathbf A_{22}$ gives the familiar sum over states,

$$
\mathbf G^\dagger\mathbf A_{22}^{-1}\mathbf G = \sum_{n\ne0}\frac{|\langle0|H_1|n\rangle|^2}{E_n - E_0}.
$$

The diagonalization is not needed; one linear solve gives the same number.

**What it simulates.** This corresponds to a finite-field CI with the **same orbitals** at every field strength. A finite-field CI that re-optimizes the SCF orbitals in the field also includes orbital relaxation, but at the SCF level rather than the MCSCF level, so it has no simple analytic counterpart in this framework.

!!! example "Water 6-31G** at Szabo's geometry (computed for this note)"
    Electronic $\mu_z$ (dipole along the $C_2$ axis; field step 0.001 a.u., five-point formulas):

    | Quantity | Value (a.u.) |
    |---|---|
    | HF, expectation value $-\langle0|z|0\rangle$ | −1.356212 |
    | HF, finite field $-dE/dF$ | −1.356212 |
    | CISD, expectation value (unrelaxed) | −1.387811 |
    | CISD, finite field, orbitals frozen | −1.387812 |
    | CISD, finite field, HF orbitals re-optimized in the field | −1.388596 |

    - **Hellmann-Feynman.** HF obeys it. CISD obeys it only when the orbitals are frozen, because the CI coefficients are variational. Orbital relaxation shifts the CISD dipole by $8\times10^{-4}$ a.u.; this "relaxed" value is the true derivative of the CISD energy.
    - **Polarizability.** HF $\alpha_{zz}$ = 5.0713 from CPHF, 5.0713 from finite field, and 5.0713 from the TDHF sum over all 95 states ([[polarization-propagator-rpa]]). The uncoupled value is 4.3102, 15% low.

## Coupled-cluster response

**Equations.** With $H(\alpha) = H + \alpha H_1$ and frozen orbitals, expand $T(\alpha) = T^{(0)} + \alpha T^{(1)} + \alpha^2T^{(2)} + \cdots$ in the CC equations $\langle0|e^{-T}H(\alpha)e^T|0\rangle = E(\alpha)$, $\langle\mu|e^{-T}H(\alpha)e^T|0\rangle = 0$ ([[coupled-cluster-second-quantization]]). In first order,

$$
E^{(1)} = \langle0|e^{-T^{(0)}}\big\{H_1 + [H, T^{(1)}]\big\}e^{T^{(0)}}|0\rangle,\qquad \mathbf D\,\mathbf t^{(1)} = -\mathbf H_1,
$$

linear equations with $D_{\mu\nu} = \langle\mu|e^{-T^{(0)}}[H, \tau_\nu]e^{T^{(0)}}|0\rangle$ (the CC Jacobian; $\tau_\nu$ an excitation operator) and $(\mathbf H_1)_\mu = \langle\mu|e^{-T^{(0)}}H_1e^{T^{(0)}}|0\rangle$. J-S Eq. (5.32) writes this as $\mathbf D\mathbf t^{(1)} = \mathbf H_1$, with the sign absorbed into their definitions. $T^{(2)}$ solves equations with the same $\mathbf D$ and a right-hand side built from $T^{(1)}$.

**Contrast with MCSCF.**

- **$E^{(2)}$ needs $T^{(2)}$.** The CC energy is not stationary with respect to the amplitudes, i.e. there is no generalized Brillouin theorem. MCSCF needs only first-order parameters.
- **$E^{(1)}$ is not $\langle H_1\rangle$.** The extra term with $[H, T^{(1)}]$ would vanish only if the CC energy were stationary.

(Later work removed these drawbacks with a Lagrangian; general knowledge, not in J-S.)

## Perturbative response

Partition $H(\alpha) = H^0 + \alpha H_1 + (H - H^0)$ with $H^0$ the Fock operator. Label energy terms $E^{(n,m)}$ by order $n$ in $\alpha H_1$ and $m$ in the fluctuation potential, and sum over $m$:

$$
E^{(1)} = \sum_mE^{(1,m)},\qquad E^{(2)} = \sum_mE^{(2,m)}.
$$

Each term is evaluated algebraically ([[rayleigh-schrodinger-perturbation-theory]]) or by diagrams with $H_1$ as an extra one-body vertex. The properties are size consistent because the energies are. J-S Fig. 5.1 shows all zeroth- and first-order diagrams for a second-order property.

## HeH⁺ (J-S Problems 5.1-5.3)

!!! example "Minimal-basis HeH⁺ properties (computed for this note; J-S in parentheses)"
    Dipole integrals, He at the origin: $\langle1s_{\mathrm H}|z|1s_{\mathrm{He}}\rangle = 0.2854$, $\langle1s_{\mathrm H}|z|1s_{\mathrm H}\rangle = 1.4$. Integrals and orbitals from [[heh-plus-minimal-basis-model]].

    - **5.1, MO integrals.** $(1|z|1) = 0.1165$, $(2|z|2) = 1.4912$ (1.4911), $(1|z|2) = 0.5442$.
    - **5.1, full CI.** Excitation energies 1.0227 (1.0225) and 2.3297 (2.3295). Transition moments 0.7575 (0.7578) and 0.0143 (0.0144). Polarizability $\alpha_{zz}(0) = 1.1223$ and $\alpha_{zz}(0.1) = 1.1331$ (1.1342).
    - **5.2, CHF.** $\langle0|[z, Q^\dagger + Q]|0\rangle = 2(1|z|2)$. $A_{11} = 2.1467$ (2.1464), $B_{11} = -0.2523$ (−0.2522). Hence $\alpha_{zz} = 2\cdot4\cdot0.5442^2/(A_{11} - B_{11}) = 0.9876$ (0.9878).
    - **5.3, CMCHF.** Two-configuration MCSCF reference. J-S's gradient (1.1076, −0.1551) and their $\mathbf A$, $\mathbf B$ give $(\mathbf A - \mathbf B)^{-1}$ = [[0.4264, −0.0800], [−0.0800, 0.4566]] and $\alpha_{zz} = 1.1230$ (printed 1.1232). In this model the two-configuration MCSCF is the full CI, so CMCHF and full CI agree. The 0.001 difference from my 1.1223 comes from the four-decimal integrals.

    CHF misses 12% of the correlated polarizability here.

## Source

Jørgensen and Simons, *Second Quantization-Based Methods in Quantum Chemistry* (Academic Press, New York, 1981), Ch. 5, Secs. A-F, pp. 103-113, Eqs. (5.1)-(5.37); Problems 5.1-5.3 with Solutions, pp. 117-121. The finite-difference formulas were derived here. The modern sign convention for $\mathbf A$, $\mathbf B$ and the remark on Lagrangian CC response are general knowledge. Water numbers computed with PySCF 2.14.
