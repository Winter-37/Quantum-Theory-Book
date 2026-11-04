---
id: variation-method
title: The variation method - ranking and improving trial wave functions by their energy
summary: Any normalized trial wavefunction has an energy at or above the ground-state energy, so approximate wavefunctions can be ranked and improved by lowering the energy.
status: complete
kind: derivation
level: introductory
tags: [basics, variational]
prerequisites: []
related: [rhf, electron-correlation]
date: 2026-10-31
---

## Overview

Exact solutions of the time-independent Schrödinger equation are available only for the simplest systems, so we need approximate solutions. The variational principle says that any approximate wavefunction gives an energy that is never below the true ground-state energy. Lowering the energy therefore always moves the approximation closer to the answer.

## Notation and definitions

The time-independent Schrödinger equation is an eigenvalue problem,

$$
\hat H\,|\Phi\rangle = E\,|\Phi\rangle ,
$$

where $\hat H$ is the Hamiltonian, a Hermitian operator, $|\Phi\rangle$ is the wavefunction, and $E$ is the energy. Energies are in hartree (atomic units).

Assume the spectrum is discrete. Then there is an infinite set of exact solutions, labelled by $\alpha = 0, 1, 2, \dots$:

$$
\hat H\,|\Phi_\alpha\rangle = E_\alpha\,|\Phi_\alpha\rangle ,
\qquad
E_0 \le E_1 \le E_2 \le \cdots
$$

Because $\hat H$ is Hermitian, every $E_\alpha$ is real, and the eigenfunctions can be chosen orthonormal:

$$
\langle \Phi_\alpha|\Phi_\beta\rangle = \delta_{\alpha\beta} .
$$

We assume the $|\Phi_\alpha\rangle$ are complete. Then any trial function $|\tilde\Phi\rangle$ that satisfies the same boundary conditions can be written as

$$
|\tilde\Phi\rangle = \sum_\alpha c_\alpha\,|\Phi_\alpha\rangle ,
\qquad
c_\alpha = \langle \Phi_\alpha|\tilde\Phi\rangle ,
$$

and its bra is $\langle\tilde\Phi| = \sum_\alpha c_\alpha^*\,\langle\Phi_\alpha|$. The trial function is normalized, so $\langle\tilde\Phi|\tilde\Phi\rangle = \sum_\alpha |c_\alpha|^2 = 1$.

## Key results

For a normalized trial function, the variational energy satisfies

$$
E[\tilde\Phi] = \langle\tilde\Phi|\hat H|\tilde\Phi\rangle \;\ge\; E_0 .
$$

Equality holds only when $|\tilde\Phi\rangle$ is the exact ground state, up to a phase.

## Derivation

Insert the expansion of $|\tilde\Phi\rangle$ and its bra into the energy. Using $\hat H|\Phi_\alpha\rangle = E_\alpha|\Phi_\alpha\rangle$ and orthonormality,

$$
\langle\tilde\Phi|\hat H|\tilde\Phi\rangle
= \sum_{\alpha\beta} c_\beta^*\,c_\alpha\,\langle\Phi_\beta|\hat H|\Phi_\alpha\rangle
= \sum_\alpha |c_\alpha|^2\,E_\alpha .
$$

Each $E_\alpha \ge E_0$, and $\sum_\alpha |c_\alpha|^2 = 1$, so

$$
E[\tilde\Phi] = \sum_\alpha |c_\alpha|^2\,E_\alpha \;\ge\; E_0\sum_\alpha |c_\alpha|^2 = E_0 .
$$

Equality requires $c_\alpha = 0$ for every $\alpha$ with $E_\alpha > E_0$. If the ground state is non-degenerate, the trial function must then be the ground state itself.

The same argument gives a bound for excited states. If $|\tilde\Phi\rangle$ is orthogonal to the ground state ($c_0 = 0$), the sum starts at $\alpha = 1$, so $E[\tilde\Phi] \ge E_1$.

Two consequences follow:

- For a family of trial functions depending on parameters $\boldsymbol\theta$, minimizing $E(\boldsymbol\theta)$ gives the best approximation within that family.
- If the trial function differs from the exact ground state by an error $\epsilon$, the energy error is of order $\epsilon^2$. Energies converge faster than wavefunctions.

## Physical interpretation

The variational energy is a weighted average of the exact eigenvalues, with weights $|c_\alpha|^2$. It can never fall below the lowest eigenvalue, so a lower energy always means a better wavefunction within the family being searched. This lets us rank approximations without knowing the exact answer.

## Worked example

!!! example "Hydrogen atom with a Gaussian trial function"
    Atomic units. Take $\tilde\psi(\mathbf r)=(2\alpha/\pi)^{3/4}e^{-\alpha r^2}$, which is normalized for any $\alpha>0$. Its expectation values are

    $$\langle T\rangle=\frac{3\alpha}{2},\qquad \langle V\rangle=-\Big\langle\frac1r\Big\rangle=-2\sqrt{\frac{2\alpha}{\pi}}$$

    so $E(\alpha)=\tfrac32\alpha-2\sqrt{2\alpha/\pi}$. Setting $dE/d\alpha=0$ gives $\alpha=8/(9\pi)\approx0.2829$, and

    $$E_{\min}=-\frac{4}{3\pi}\approx-0.4244\ \text{Eh}.$$

    The exact ground-state energy is $-0.5000$ Eh. This trial function recovers 84.9% of it, leaving an error of $0.0756$ Eh, or $2.06$ eV.

## Limitations

The argument needs a ground state with a lowest energy $E_0$, which holds for the Hamiltonians of atoms and molecules. It also assumes a discrete spectrum. A single Gaussian has no cusp at the nucleus and decays too quickly at long range, so it can never reach the exact energy. This is why basis sets use contracted Gaussians (STO-$n$G).

## References

1. Source: section 1.3, "The variation method", Modern Quantum Chemistry, Szabo and Ostlund
