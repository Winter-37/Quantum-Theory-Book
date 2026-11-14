---
id: geometry-error-of-an-approximate-surface
title: Geometry error of an approximate surface - the force at the reference minimum, not the energy offset, sets it
summary: Write an approximate energy as the reference energy plus an error ΔE(x). At the reference minimum the approximate gradient equals ∇ΔE, a Newton step gives the geometry error −H⁻¹∇ΔE to first order, and the energy gained by relaxing is ½gᵀH⁻¹g, second order in the force. A constant offset drops out entirely. Soft modes amplify small forces. Applies to any approximate method, variational or not. Verified for MP2 against FCI on an H6 ring: a 24 mEh offset, a 15 mÅ shift predicted to 4%, and a 0.49 mEh relaxation energy predicted to 2%.
status: in-progress
kind: derivation
level: intermediate
tags: [geometry-optimization, error-analysis, potential-energy-surface, non-variational, force, hessian]
prerequisites: [geometry-optimization, analytic-gradients-and-force-constants]
related: [mp2, size-consistency]
order: 20
date: 2026-11-08
---

Notation: $x$ nuclear coordinates; $E_{\rm ref}(x)$ a reference surface (FCI, else CCSD(T)) with minimum $x_{\rm ref}$; $E(x)$ the approximate surface, with gradient $g(x)$ and Hessian $\mathbf H$.

## The argument

1. **Split the error.**

    $$
    E(x) = E_{\rm ref}(x) + \Delta E(x),
    $$

    with $\Delta E$ of either sign when $E$ is not variational.
2. **Force at the reference minimum.** Since $\nabla E_{\rm ref}(x_{\rm ref}) = 0$,

    $$
    g(x_{\rm ref}) = \nabla\Delta E(x_{\rm ref}).
    $$

    The approximate surface pushes on the reference structure only through the slope of its error.
3. **Geometry error.** One Newton step on $E$ from $x_{\rm ref}$ reaches the minimum of $E$ to first order:

    $$
    x_{\min} - x_{\rm ref} \approx -\mathbf H^{-1}\,\nabla\Delta E(x_{\rm ref}).
    $$

    A constant $\Delta E$ has no gradient and does not move the minimum.
4. **Relaxation energy.** Inserting this into the quadratic model,

    $$
    E(x_{\rm ref}) - E(x_{\min}) \approx \tfrac12\,g^{\mathsf T}\mathbf H^{-1}g ,
    $$

    second order in the force. A force of a few m$E_h$/bohr and bond-like curvature give micro-hartrees, so an energy offset of milli-hartrees is unrelated to the relaxation energy.

## Consequences

- **The diagnostic.** Evaluate $g$ at $x_{\rm ref}$. It predicts the geometry error, which the energy offset cannot.
- **Soft modes.** Along a mode of curvature $k$ the shift is $F/k$. A small force along a torsion can move the structure far, so a good surface can still give a poor dihedral angle.
- **Symmetric references.** If $x_{\rm ref}$ is stationary by symmetry, any method that keeps the symmetry has $g=0$ there. A symmetry-breaking force is then purely an artefact of the method, for example of a partition of the molecule that has lower symmetry than the molecule itself.
- **Relative energies.** A barrier compares two stationary points on surfaces with similar offsets, so it is more accurate than either total energy.

## Worked example

!!! example "H$_6$ ring, STO-3G, symmetric stretch: MP2 against FCI"
    One coordinate, the nearest-neighbour distance $r$ of the regular hexagon. Derivatives by central differences, $h = 2\times10^{-3}$ Å. Script: `geom_err_mp2.py`.

    - **Minima.** FCI $r_{\rm ref} = 0.988155$ Å; MP2 $0.973284$ Å; shift $-14.87$ mÅ.
    - **Offset.** $E_{\rm MP2}-E_{\rm FCI} = +23.85$ m$E_h$ at $r_{\rm ref}$: MP2 lies above FCI here.
    - **Force and curvature of the MP2 surface at $r_{\rm ref}$.** $g = +65.08$ m$E_h$/Å, $k = 4.215\ E_h$/Å$^2$ (FCI: 4.026).
    - **Prediction.** $-g/k = -15.44$ mÅ against $-14.87$ found (4% high: the shift is large enough for cubic terms to show).
    - **Relaxation energy.** $490.1\ \mu E_h$ found, $g^2/2k = 502.4\ \mu E_h$ predicted.
    - **Reading it.** The MP2 error grows by about 65 m$E_h$ per Å of stretch, and that slope, not the 24 m$E_h$ offset, is what moves the bond. A method with a larger but flatter error would give a better geometry.

## Source

- The argument is a second-order Taylor expansion, written out here with the force at the reference minimum as the diagnostic.
- Numbers computed here.
