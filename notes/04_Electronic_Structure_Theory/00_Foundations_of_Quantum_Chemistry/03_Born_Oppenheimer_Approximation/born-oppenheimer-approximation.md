---
id: born-oppenheimer-approximation
title: The Born-Oppenheimer approximation
summary: Because nuclei are much heavier than electrons, solve the electronic problem at clamped nuclei; its energy plus nuclear repulsion is the potential energy surface on which the nuclei then move. Product form of the wave function and what is neglected.
status: in-progress
kind: theory
level: introductory
tags: [basics, born-oppenheimer, potential-energy-surface, adiabatic]
prerequisites: [molecular-hamiltonian]
related: [atomic-units, nonadiabatic-couplings, geometry-optimization]
also: []
date: 2026-11-03
---

## Idea

A proton is about 1836 electron masses, so nuclei move far more slowly than electrons. To a good approximation the electrons adjust instantly to the current nuclear positions. Szabo treats this qualitatively, and this note does the same. The neglected terms are named at the end.

## Step 1: the electronic problem

Fix the nuclei at $\{\mathbf R_A\}$. In the [[molecular-hamiltonian]] the nuclear kinetic energy is dropped and the nuclear repulsion becomes a constant. The electronic Schrödinger equation is

$$
\hat H_{\text{elec}}\,\Phi_{\text{elec}} = \mathcal E_{\text{elec}}\,\Phi_{\text{elec}},
\qquad
\Phi_{\text{elec}} = \Phi_{\text{elec}}\big(\{\mathbf r_i\};\{\mathbf R_A\}\big),
\qquad
\mathcal E_{\text{elec}} = \mathcal E_{\text{elec}}\big(\{\mathbf R_A\}\big).
$$

The semicolon marks a **parametric** dependence: for each nuclear arrangement the wave function is a different function of the electron coordinates, but the nuclear coordinates are not variables of it. Adding the nuclear repulsion gives the total energy at fixed nuclei,

$$
\mathcal E_{\text{tot}}(\{\mathbf R_A\}) = \mathcal E_{\text{elec}}(\{\mathbf R_A\}) + \sum_{A}\sum_{B>A}\frac{Z_AZ_B}{R_{AB}} .
$$

## Step 2: nuclear motion on a surface

Return to the full Hamiltonian and replace the electronic operators by their average over $\Phi_{\text{elec}}$. The electronic terms plus the nuclear repulsion average to $\mathcal E_{\text{tot}}$, which gives a nuclear Hamiltonian

$$
\hat H_{\text{nucl}} = -\sum_{A=1}^{M}\frac{1}{2M_A}\nabla_A^2 + \mathcal E_{\text{tot}}(\{\mathbf R_A\}),
\qquad
\hat H_{\text{nucl}}\Phi_{\text{nucl}} = \mathcal E\,\Phi_{\text{nucl}} .
$$

$\mathcal E_{\text{tot}}(\{\mathbf R_A\})$ is the **potential energy surface** (PES). Its eigenstates $\Phi_{\text{nucl}}(\{\mathbf R_A\})$ describe vibration, rotation and translation, and $\mathcal E$ is the Born-Oppenheimer estimate of the full energy (electronic + vibrational + rotational + translational). The total wave function is approximated as a product,

$$
\Phi\big(\{\mathbf r_i\},\{\mathbf R_A\}\big) \approx \Phi_{\text{elec}}\big(\{\mathbf r_i\};\{\mathbf R_A\}\big)\,\Phi_{\text{nucl}}\big(\{\mathbf R_A\}\big).
$$

Equilibrium geometries are minima of the PES, transition states are first-order saddle points, and harmonic frequencies come from its Hessian. All of these are properties of $\mathcal E_{\text{tot}}$ alone, which is why electronic-structure codes optimize geometries on it.

## What is neglected

When $\nabla_A^2$ acts on the product, it also differentiates $\Phi_{\text{elec}}$ through its parametric $\mathbf R_A$ dependence. The product form keeps only

$$
\nabla_A^2(\Phi_{\text{elec}}\Phi_{\text{nucl}}) \approx \Phi_{\text{elec}}\nabla_A^2\Phi_{\text{nucl}} .
$$

It drops two terms:

- $2\,\nabla_A\Phi_{\text{elec}}\cdot\nabla_A\Phi_{\text{nucl}}$, whose projections onto other electronic states are the first-derivative **nonadiabatic couplings**.
- $\Phi_{\text{nucl}}\nabla_A^2\Phi_{\text{elec}}$, whose diagonal part is the **diagonal Born-Oppenheimer correction**.

Both are suppressed by $1/M_A$. They become large when two electronic states come close in energy, since the couplings carry an energy-gap denominator. Near avoided crossings and conical intersections the single-surface picture fails (see [[nonadiabatic-couplings]]).

## Source

Szabo and Ostlund, *Modern Quantum Chemistry* (Dover, 1996; reprint of the revised first edition, McGraw-Hill, 1989), Sec. 2.1.2, pp. 43-45, Eqs. (2.10)-(2.18). Szabo refers to B. T. Sutcliffe for the quantitative treatment. The "What is neglected" section is standard material written from general knowledge, not from Szabo.
