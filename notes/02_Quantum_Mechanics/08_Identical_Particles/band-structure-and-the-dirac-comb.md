---
id: band-structure-and-the-dirac-comb
title: Bloch's theorem and band structure from the Dirac comb
summary: For a periodic potential, Bloch's theorem gives ψ(x+a) = e^{iqa}ψ(x), with q = 2πn/Na on a ring of N cells. For a comb of delta spikes, matching one cell gives cos(qa) = cos(ka) + β sin(ka)/(ka). Energies where the right side leaves [−1, 1] are forbidden, so the spectrum consists of bands of N states separated by gaps. Filling the bands explains metals, insulators and semiconductors. Band edges for β = 10 are confirmed by direct diagonalization of a 30-cell comb, along with the wells case and the degeneracy count.
status: in-progress
kind: derivation
level: intermediate
tags: [bloch-theorem, band-structure, dirac-comb, kronig-penney, band-gap, crystal-momentum, metals-insulators-semiconductors, periodic-boundary-conditions, griffiths]
prerequisites: [delta-function-potential, free-electron-gas]
related: [one-dimensional-scattering-and-transfer-matrix, finite-square-well, exchange-symmetry-spin-and-symmetrization-principle]
also: []
date: 2026-11-05
---

## Bloch's theorem

**Statement.** For a periodic potential $V(x+a) = V(x)$, the solutions of the Schrödinger equation can be chosen to satisfy

$$
\psi(x+a) = e^{iqa}\,\psi(x)
$$

for a constant $q$. Reason: the translation by $a$ commutes with $\hat H$, so $\hat H$ and the translation operator have simultaneous eigenstates, and the eigenvalue has modulus 1. The proof is in Griffiths Ch. 6.

**Consequence.** $|\psi|^2$ is periodic even though $\psi$ is not. Only one cell needs to be solved: the Bloch condition generates the solution everywhere.

**Edges.** A real crystal ends, which breaks periodicity. For about $10^{23}$ cells, edge effects are negligible deep inside. Wrap the line into a ring of $N$ cells, $\psi(x+Na) = \psi(x)$. Then $e^{iNqa} = 1$, so

$$
q = \frac{2\pi n}{Na},\qquad n = 0,\pm1,\pm2,\ldots
$$

In particular $q$ is real. The Bloch phase $e^{iqa}$ repeats after $N$ values of $n$, so each band holds $N$ states.

## The Dirac comb

**Potential.** $V(x) = \alpha\sum_{j=0}^{N-1}\delta(x-ja)$ with $\alpha>0$ (spikes). Inside a cell, $\psi = A\sin kx + B\cos kx$ with $k = \sqrt{2mE}/\hbar$.

**Matching at $x = 0$.** Use the Bloch form for the cell to the left. Continuity of $\psi$ and the derivative jump $\Delta\psi' = (2m\alpha/\hbar^2)\psi(0)$ ([[delta-function-potential]], with the sign of $\alpha$ reversed) give

$$
\cos(qa) = \cos(ka) + \frac{m\alpha}{\hbar^2k}\sin(ka).
$$

**Dimensionless form.** With $z = ka$ and $\beta = m\alpha a/\hbar^2$:

$$
\cos(qa) = f(z) \equiv \cos z + \beta\,\frac{\sin z}{z}.
$$

**Bands and gaps.** Where $|f(z)|>1$, no real $q$ exists: the energy is forbidden, a **gap**. Where $|f(z)|\le1$, each of the $N$ values $\cos(2\pi n/N)$ crosses $f(z)$ once. These $N$ closely spaced levels form a **band**. Bands always end at $z = j\pi$, where $f = \cos z = \pm1$. Gaps open just above each $j\pi$.

## Worked examples

!!! example "β = 10: band edges (units $\hbar = m = a = 1$)"
    **Allowed ranges of $z = ka$** up to $4\pi$, from $|f(z)|\le1$:

    | Band | $z$ from | $z$ to |
    |---|---|---|
    | 1 | 2.62769 | 3.14159 ($\pi$) |
    | 2 | 5.30734 | 6.28319 ($2\pi$) |
    | 3 | 8.06714 | 9.42478 ($3\pi$) |
    | 4 | 10.90871 | $4\pi$ |

    **Bottom of the first band** (Problem 5.25). $f(z)=1$ at $z = 2.627675$. With $\alpha/a = 1$ eV and $\beta = 10$, $\hbar^2/ma^2 = 0.1$ eV, so

    $$
    E = \frac{z^2}{2}\cdot0.1\ \text{eV} = 0.345\ \text{eV}.
    $$

    **Independent check: direct diagonalization.** A ring of $N = 30$ cells, 200 grid points per cell, each spike represented as $\alpha/\Delta x$ on one site:

    | Band | States | $z$ range |
    |---|---|---|
    | 1 | 30 | [2.6277, 3.1416] |
    | 2 | 30 | [5.3073, 6.2829] |
    | 3 | 30 | [8.0668, 9.4239] |

    Exactly $N$ states per band, with edges matching the analytic ones to grid accuracy.

!!! example "Degeneracy (Problem 5.27) and wells (Problem 5.26)"
    **Degeneracy.** $q$ and $-q$ give the same $\cos(qa)$, so most levels are doubly degenerate. The exceptions are $\cos(qa) = \pm1$: $n=0$ always, and $n=N/2$ when $N$ is even. For $N = 1, 2, 3, 4$ the distinct values of $\cos(qa)$ are $\{1\}$, $\{\pm1\}$, $\{1, -\tfrac12\}$ and $\{1, 0, -1\}$.

    **Wells** ($\beta = -1.5$). For $E<0$ write $\kappa a = z$, giving $\cos(qa) = \cosh z - 1.5\,\sinh z/z$. The first band starts in negative energy: it covers $E\in[-1.961, 0)$ (units $\hbar^2/ma^2$) and continues into $E>0$ up to $z=\pi$.

    **Tight-binding picture.** The single-well bound state, broadened by tunnelling between neighbouring wells, becomes the lowest band. Each band still holds $N$ states.

## Conductors, insulators, semiconductors

**Filling.** Each band holds $N$ spatial states, so $2N$ electrons with spin. With $d$ free electrons per atom, $Nd$ electrons fill $d/2$ bands:

- $d = 1$: half-filled band, so excitations cost almost nothing: a **conductor** (metal);
- $d = 2$: the band is exactly full, and the next excitation must cross the gap: an **insulator**.

**Semiconductors.** If the gap is small, thermal energy promotes some electrons across it (Si, Ge). Real 3D band structures can overlap and complicate this counting, but the gap mechanism is the same.

**Comparison with the free gas.** The free-electron gas ([[free-electron-gas]]) has no gaps and so predicts that every solid conducts. The periodic potential, through Bloch's theorem and Pauli filling, explains the enormous range of real conductivities. The Kronig–Penney model (square barriers in place of spikes) gives the same qualitative picture.

The transfer-matrix language of [[one-dimensional-scattering-and-transfer-matrix]] gives the same condition. Let $\mathsf T$ be the $2\times2$ matrix that carries $(\psi,\psi')$ across one period; it has $\det\mathsf T = 1$. Bloch's theorem then reads $\cos(qa) = \tfrac12\mathrm{Tr}\,\mathsf T$.

For the comb, $\mathsf T$ is free propagation over length $a$, $\begin{pmatrix}\cos ka & \sin ka/k\\ -k\sin ka & \cos ka\end{pmatrix}$, followed by the spike jump $\begin{pmatrix}1&0\\ 2m\alpha/\hbar^2&1\end{pmatrix}$. The half-trace reproduces $\cos ka + (m\alpha/\hbar^2k)\sin ka$. This identity is standard and added here; it is not in Griffiths.

## Source

Griffiths and Schroeter, *Introduction to Quantum Mechanics* (3rd ed., Cambridge University Press, 2018), Sec. 5.3.2, Eqs. (5.58)-(5.73), Figs. 5.4-5.6 (described); Problems 5.24-5.28. Page numbers are not given because the PDF used is an e-book rendering without print pagination. Band edges, the finite-comb diagonalization and the wells analysis are computed in `griffiths/ch05_identical.py` (section G). The tight-binding and transfer-matrix remarks are additions.
