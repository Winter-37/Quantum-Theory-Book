---
id: minimal-coupling-and-aharonov-bohm
title: Electromagnetic interactions; minimal coupling, gauge invariance and the Aharonov–Bohm effect
summary: A charged particle in electromagnetic fields enters quantum mechanics through the potentials, H = (p − qA)²/2m + qφ. Covers Ehrenfest's theorem giving the Lorentz force, Landau levels, gauge transformations compensated by a local phase e^{iqΛ/ħ}, and the Aharonov–Bohm effect, in which a bead on a ring around a solenoid has energies (ħ²/2mb²)(n − qΦ/2πħ)² although B = 0 on the ring. Interfering beams acquire a phase difference qΦ/ħ. Checked with a lattice ring carrying a Peierls phase.
status: in-progress
kind: theory
level: intermediate
tags: [minimal-coupling, vector-potential, gauge-invariance, aharonov-bohm, landau-levels, lorentz-force, peierls-phase, berry-phase, griffiths]
prerequisites: [schrodinger-equation-in-three-dimensions, energy-time-uncertainty-principle]
related: [spin-one-half, orbital-angular-momentum, hilbert-space-and-hermitian-operators]
order: 70
date: 2026-11-04
---

## Minimal coupling

**Why potentials are needed.** The Lorentz force $\mathbf F = q(\mathbf E+\mathbf v\times\mathbf B)$ is velocity dependent and is not the gradient of a potential energy. The Schrödinger equation $i\hbar\,\partial_t\Psi = \hat H\Psi$ therefore needs the Hamiltonian form, with the scalar potential $\varphi$ and the vector potential $\mathbf A$, where $\mathbf E = -\nabla\varphi-\partial_t\mathbf A$ and $\mathbf B = \nabla\times\mathbf A$:

$$
H = \frac{1}{2m}(\mathbf p-q\mathbf A)^2+q\varphi
\quad\longrightarrow\quad
i\hbar\frac{\partial\Psi}{\partial t} = \left[\frac{1}{2m}(-i\hbar\nabla-q\mathbf A)^2+q\varphi\right]\Psi .
$$

This is the **minimal coupling** rule, $\mathbf p\to\mathbf p-q\mathbf A$.

**Two momenta.** The canonical momentum $\hat{\mathbf p} = -i\hbar\nabla$ and the kinetic momentum $m\mathbf v = \mathbf p-q\mathbf A$ now differ.

**Ehrenfest** (Problem 4.42):

$$
\frac{d\langle\mathbf r\rangle}{dt} = \frac1m\langle\mathbf p-q\mathbf A\rangle .
$$

For fields that are uniform over the packet,

$$
m\frac{d\langle\mathbf v\rangle}{dt} = q\left(\mathbf E+\langle\mathbf v\rangle\times\mathbf B\right),
$$

the Lorentz force law on average.

**Landau levels** (Problem 4.43). Take $\mathbf A = \tfrac{B_0}{2}(x\hat\jmath - y\hat\imath)$, giving a uniform $\mathbf B = B_0\hat k$, and $\varphi = Kz^2$:

$$
E = \left(n_1+\tfrac12\right)\hbar\omega_1+\left(n_2+\tfrac12\right)\hbar\omega_2,\qquad
\omega_1 = \frac{qB_0}{m},\quad \omega_2 = \sqrt{\frac{2qK}{m}} .
$$

With $K = 0$, motion in the $xy$ plane is quantized into equally spaced **Landau levels** at the cyclotron frequency.

**Spin.** A particle with spin adds the Zeeman term $-\gamma\mathbf B\cdot\mathbf S$ ([[spin-one-half]]).

## Gauge invariance

**Classical gauge freedom.** The potentials are not unique. For any real $\Lambda(\mathbf r,t)$,

$$
\varphi' = \varphi-\frac{\partial\Lambda}{\partial t},\qquad \mathbf A' = \mathbf A+\nabla\Lambda
$$

give the same $\mathbf E$ and $\mathbf B$.

**Quantum compensation.** If $\Psi$ solves the Schrödinger equation with $(\varphi,\mathbf A)$, then

$$
\Psi' = e^{iq\Lambda/\hbar}\,\Psi
$$

solves it with $(\varphi',\mathbf A')$ (Problem 4.44). A position-dependent phase is not a global phase, but here it is exactly compensated by the change of potentials. All densities, currents and expectation values of gauge-invariant operators are unchanged, so the theory is gauge invariant.

## The Aharonov–Bohm effect

The potentials enter the Schrödinger equation directly, so they can matter even where $\mathbf E = \mathbf B = 0$.

**Bead on a ring around a solenoid** (Example 4.6).

- **Geometry.** A charge $q$ moves on a ring of radius $b$. A long solenoid of radius $a<b$ on the axis carries flux $\Phi = \pi a^2B$.
- **Potentials on the ring.** $\mathbf B = 0$, but in Coulomb gauge $\mathbf A = \frac{\Phi}{2\pi r}\hat\phi$.

**Energies.** With $\nabla\to(\hat\phi/b)\,d/d\phi$, the solutions are $\psi\propto e^{in\phi}$, and single-valuedness forces integer $n$:

$$
E_n = \frac{\hbar^2}{2mb^2}\left(n-\frac{q\Phi}{2\pi\hbar}\right)^2,\qquad n = 0,\pm1,\pm2,\ldots
$$

**What changes.** The flux lifts the $\pm n$ degeneracy of the free ring: motion parallel to the solenoid current lies lower for $q>0$. The spectrum depends on a field that the particle never touches. It is periodic in $\Phi$ with period $h/q$: only $\Phi$ modulo the flux quantum is observable.

**General statement.** In a region where $\nabla\times\mathbf A = 0$, write $\Psi = e^{ig}\Psi'$ with $g(\mathbf r) = \frac{q}{\hbar}\int_{\mathcal O}^{\mathbf r}\mathbf A\cdot d\mathbf r'$. This $g$ is well defined only where the line integral is path independent, i.e. in a simply connected field-free region. Then $\Psi'$ obeys the field-free equation.

**Interference.** Two beams passing on opposite sides of the solenoid pick up phases $\pm q\Phi/2\hbar$, so

$$
\text{phase difference} = \frac{q\Phi}{\hbar}.
$$

This shift of the interference fringes has been observed experimentally, first by Chambers and then in later experiments (Griffiths footnote 68). It does not make $\mathbf A$ itself measurable: only the gauge-invariant enclosed flux, $\oint\mathbf A\cdot d\mathbf r = \Phi$, enters.

!!! example "Lattice check with a Peierls phase ($\hbar = m = b = q = 1$)"
    **Model.** Discretize the ring into $N = 400$ sites. The vector potential enters as a phase $e^{i\theta}$ on each hopping term, with $\theta = 2\pi\beta/N$ and $\beta \equiv q\Phi/2\pi\hbar$. This is the lattice form of $\exp[\frac{iq}{\hbar}\int\mathbf A\cdot d\mathbf r]$, the **Peierls substitution**.

    **Results.** The lowest five eigenvalues compared with $(n-\beta)^2/2$:

    | $\beta$ | Lattice | Exact |
    |---|---|---|
    | 0 | 0, 0.49999, 0.49999, 1.99984, 1.99984 | 0, 0.5, 0.5, 2, 2 |
    | 0.2 | 0.02, 0.32, 0.71998, 1.61989, 2.41976 | 0.02, 0.32, 0.72, 1.62, 2.42 |
    | 0.5 | 0.125, 0.125, 1.12495, 1.12495, 3.1246 | 0.125, 0.125, 1.125, 1.125, 3.125 |

    At $\beta = 0.2$ the degeneracy is lifted. At half a flux quantum it reappears between $n$ and $1-n$, confirming the $h/q$ periodicity.

## Connection forward

The Aharonov–Bohm phase is the prototype of a **geometric (Berry) phase**: a phase acquired by transport around a loop, fixed by the flux of a "field" through the loop rather than by the time taken. Griffiths treats the adiabatic theorem in Ch. 11 of the 3rd edition. In molecules, the analogous phase around a conical intersection is the molecular Aharonov–Bohm effect, a planned topic for the nonadiabatic notes.

## Source

Griffiths and Schroeter, *Introduction to Quantum Mechanics* (3rd ed., Cambridge University Press, 2018), Sec. 4.5, Eqs. (4.186)-(4.214), Example 4.6, Figs. 4.16-4.17 (described); Problems 4.42-4.45. Page numbers are not given because the PDF used is an e-book rendering without print pagination. The flux-periodicity remark, the Peierls lattice check and the Berry-phase connection are additions. The experiment is cited as Griffiths cites it ("Chambers and others", his footnote 68); the original reference was not checked here and should be verified before quoting. Numbers from `griffiths/ch04_3d.py` (section G).
