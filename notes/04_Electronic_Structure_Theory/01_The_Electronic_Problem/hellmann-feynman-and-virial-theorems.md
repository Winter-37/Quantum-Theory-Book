---
id: hellmann-feynman-and-virial-theorems
title: The Hellmann-Feynman and molecular virial theorems for exact and approximate wave functions
summary: Both theorems follow from the stationarity of the energy. Hellmann-Feynman (dE/dα = ⟨V⟩) holds for approximate wave functions only if they are variational with respect to every change the perturbation induces, which atom-centred basis sets violate (in first quantization). The molecular electronic virial theorem 2⟨T⟩ + ⟨V⟩ = −R·dE/dR follows from stationarity under uniform scaling, giving E = −⟨T⟩ and V = 2E at equilibrium. Checked for H₂ and He with a scale-optimized STO-3G basis (exact to 10⁻⁸) and shown to fail for the unscaled basis.
status: in-progress
kind: derivation
level: intermediate
tags: [hellmann-feynman, virial-theorem, variational-principle, coordinate-scaling, kinetic-energy, basis-set-quality]
prerequisites: [variational-principle, molecular-hamiltonian]
related: [molecular-properties-and-response, analytic-gradients-and-force-constants, upper-bounds-and-interlacing, lagrangian-for-nonvariational-energies, minimal-basis-h2-model]
order: 40
date: 2026-11-04
---

## Hellmann-Feynman

**Exact states.** For $\hat H(\alpha) = \hat H + \alpha\hat V$ with normalized eigenstates $|\Psi_\alpha\rangle$,

$$
\frac{\mathrm dE}{\mathrm d\alpha}\Big|_0 = \langle\Psi|\hat V|\Psi\rangle ,
$$

because the terms from $\mathrm d\Psi/\mathrm d\alpha$ vanish by stationarity. For nuclear displacements this gives forces as expectation values of $\partial\hat H/\partial\mathbf R$.

**Approximate states.** The theorem holds whenever the approximate wave function is optimized with respect to all changes induced by the perturbation.

**The basis-set catch.** Atom-centred basis functions move with the nuclei. A wave function optimized at one geometry cannot be expanded in the basis of a displaced geometry, so it is **not** variational with respect to the displacement, even when it is fully optimized within its basis at every geometry. Hellmann-Feynman forces then miss the basis-function (Pulay) terms ([[analytic-gradients-and-force-constants]]).

**Second-quantization view (HJO).** The basis enters only through the integrals in the Hamiltonian, not through the state. A geometry change can therefore be regarded as a change of the operator alone, and Hellmann-Feynman holds formally. This saves no work, since the Hamiltonian derivative now contains the integral derivatives, but it lets fixed and moving bases be treated on the same footing. (This is the operator-level analogue of the HJO remark that second-quantized operators carry the basis; [[second-quantization-in-a-finite-basis]].)

## The molecular electronic virial theorem

**Scaling.** Scale the electron coordinates uniformly, $\Psi_a(\mathbf r_i) = a^{3N/2}\Psi(a\mathbf r_i)$ (normalization is preserved), with the nuclei fixed. Then

$$
\langle\Psi_a|\hat T|\Psi_a\rangle = a^2\langle\Psi|\hat T|\Psi\rangle,\qquad \langle\Psi_a|\hat V(\mathbf R)|\Psi_a\rangle = a\langle\Psi|\hat V(a\mathbf R)|\Psi\rangle ,
$$

since a Coulomb potential scales as $1/r$ only when the nuclear positions are scaled along with the electrons.

**Stationarity in $a$ at $a = 1$ (HJO Eq. 4.2.64).**

$$
2\langle\Psi|\hat T|\Psi\rangle + \langle\Psi|\hat V(\mathbf R)|\Psi\rangle = -\Big\langle\Psi\Big|\frac{\mathrm d\hat V(a\mathbf R)}{\mathrm da}\Big|_{a=1}\Big|\Psi\Big\rangle .
$$

**With Hellmann-Feynman (Eqs. 4.2.66 and 4.2.73).** For a wave function that is also variational under scaling of the nuclear framework,

$$
2\langle\hat T\rangle + \langle\hat V\rangle = -\frac{\mathrm dE(a\mathbf R)}{\mathrm da}\Big|_{a=1} = \sum_I\mathbf R_I\cdot\mathbf F_I ,
$$

with $\hat V$ including nuclear repulsion and $\mathbf F_I = -\mathrm dE/\mathrm d\mathbf R_I$. For a diatomic the right side is $-R\,\mathrm dE/\mathrm dR$.

**At equilibrium and for atoms** the scaling force vanishes:

$$
\langle\hat T\rangle = -\tfrac12\langle\hat V\rangle,\qquad \langle\hat T\rangle = -E,\qquad \langle\hat V\rangle = 2E .
$$

Hence no stationary point can have positive energy relative to separated particles, since $\langle\hat T\rangle\ge0$.

**Further results.**

- **Diatomic forces.** Translation and rotation invariance give five conditions on the forces; the virial theorem gives the sixth. The whole diatomic force follows from $\langle\hat T\rangle$ and $\langle\hat V\rangle$, if the wave function is scale-optimal.
- **All particles scaled.** When nuclei are treated as quantum particles too, $2\langle\hat T_{\text{mol}}\rangle + \langle\hat V_{\text{mol}}\rangle = 0$ exactly. The scaling-force term appears only because the clamped-nucleus attraction does not scale with the electrons alone.

**Diagnostic.** Finite basis sets are not variational under scaling unless a scale factor is optimized, so $-\langle\hat V\rangle/\langle\hat T\rangle\ne2$ even for atoms. The deviation is a cheap indicator of basis quality.

!!! example "Scale-optimized STO-3G (computed for this note)"
    All exponents are multiplied by $s^2$, with $s$ optimized at each geometry. For a basis centred on the nuclei this is exactly a uniform scaling of electrons and nuclei together, so the virial theorem must hold.

    **H₂, RHF:**

    | R (bohr) | $s_{\text{opt}}$ | $E$ | $\langle\hat T\rangle$ | $-\langle\hat V\rangle/\langle\hat T\rangle$ | $2T + V + R\,\mathrm dE/\mathrm dR$ | Same, unscaled STO-3G |
    |---:|---:|---:|---:|---:|---:|---:|
    | 1.000 | 1.0513 | −1.070044 | 1.393732 | 1.76775 | $3\times10^{-8}$ | −0.158 |
    | 1.400 | 0.9598 | −1.119218 | 1.113477 | 2.00516 | $3\times10^{-8}$ | +0.124 |
    | 2.000 | 0.8653 | −1.078044 | 0.876334 | 2.23018 | $-8\times10^{-10}$ | +0.431 |
    | 3.000 | 0.7719 | −0.976457 | 0.700072 | 2.39479 | $9\times10^{-9}$ | +0.812 |

    - **Exactness.** The virial relation holds to finite-difference precision at every $R$ for the scaled basis and fails badly without scaling.
    - **Equilibrium of the scaled model.** At $R_e = 1.3895$ bohr ($s = 0.9619$), $-\langle\hat V\rangle/\langle\hat T\rangle = 2.000000$ and $E/\langle\hat T\rangle = -1.000000$, with $E = -1.119240$.
    - **Away from equilibrium.** The ratio drifts from 2 in the direction set by the force: below 2 when compressed (repulsive force), above 2 when stretched.

    **He atom.**

    - **Unscaled STO-3G.** $-\langle\hat V\rangle/\langle\hat T\rangle = 1.99442$, $E = -2.807784$.
    - **Optimal scale 0.99721.** The ratio becomes 2.0000000 and $E = -2.807806 = -\langle\hat T\rangle$.

## Source

Helgaker, Jørgensen and Olsen, *Molecular Electronic-Structure Theory* (Wiley, Chichester, 2000), Secs. 4.2.6-4.2.7, pp. 119-123, Eqs. (4.2.52)-(4.2.74); Exercise 4.3. Equations read from the page images. The scale-factor demonstration is my own construction, computed with PySCF 2.14.
