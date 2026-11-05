---
id: one-dimensional-scattering-and-transfer-matrix
title: "One-dimensional scattering: steps, barriers, the S-matrix and the transfer matrix"
summary: General 1D scattering from a localized potential. The S-matrix (outgoing in terms of incoming amplitudes) and transfer matrix M (right in terms of left), their relations, R and T for either direction, the flux factor when the asymptotic speeds differ, and M = M₂M₁ for composite potentials. Worked cases: potential step and cliff, rectangular barrier (tunnelling), the reflectionless sech² well. Includes the piecewise-constant transfer-matrix algorithm used to check every scattering number in these notes.
status: in-progress
kind: algorithm
level: intermediate
tags: [scattering, s-matrix, transfer-matrix, tunnelling, potential-step, rectangular-barrier, reflectionless-potential, probability-current, griffiths]
prerequisites: [delta-function-potential, finite-square-well, normalization-and-probability-current]
related: [free-particle-and-wave-packets, stationary-states]
also: []
date: 2026-11-04
---

## Setup and the S-matrix

**Geometry.** $V$ is nonzero only in a finite region II. On either side ($k = \sqrt{2mE}/\hbar$):

$$
\text{I (left):}\ \psi = Ae^{ikx}+Be^{-ikx},\qquad
\text{III (right):}\ \psi = Fe^{ikx}+Ge^{-ikx}.
$$

In region II, $\psi = Cf(x)+Dg(x)$ for two independent solutions $f$ and $g$. Matching $\psi$ and $\psi'$ at the two edges gives four linear conditions. Eliminating $C$ and $D$ leaves outgoing amplitudes ($B$, $F$) as linear functions of incoming ones ($A$, $G$). This linear map is the **scattering matrix**:

$$
\begin{pmatrix}B\\F\end{pmatrix} = \begin{pmatrix}S_{11}&S_{12}\\S_{21}&S_{22}\end{pmatrix}\begin{pmatrix}A\\G\end{pmatrix}.
$$

**Reflection and transmission.**

- From the left ($G=0$): $R_l = |S_{11}|^2$ and $T_l = |S_{21}|^2$.
- From the right ($A=0$): $R_r = |S_{22}|^2$ and $T_r = |S_{12}|^2$.

**Unitarity.** Conservation of probability current with a real $V$ ([[normalization-and-probability-current]]) makes $\mathsf S$ unitary, so $R+T=1$ in each direction.

**Example: delta well** ([[delta-function-potential]]), with $\beta = m\alpha/\hbar^2k$:

$$
\mathsf S = \frac{1}{1-i\beta}\begin{pmatrix}i\beta & 1\\ 1 & i\beta\end{pmatrix}.
$$

Numerically, $\mathsf S^\dagger\mathsf S = \mathsf 1$ at $E = 0.2$ and $1.0$.

## The transfer matrix

**Definition.** $\mathsf M$ propagates amplitudes from left to right:

$$
\begin{pmatrix}F\\G\end{pmatrix} = \mathsf M\begin{pmatrix}A\\B\end{pmatrix}.
$$

**Relation to $\mathsf S$** (by rearranging the $\mathsf S$ equations):

$$
\mathsf M = \frac{1}{S_{12}}\begin{pmatrix}-\det\mathsf S & S_{22}\\ -S_{11} & 1\end{pmatrix},
\qquad
\det\mathsf M = \frac{S_{21}}{S_{12}}.
$$

**Coefficients in terms of $\mathsf M$.** For a beam from the left ($G=0$): $B = -(M_{21}/M_{22})A$ and $F = (\det\mathsf M/M_{22})A$. Hence

$$
R_l = \left|\frac{M_{21}}{M_{22}}\right|^2,\quad
T_l = \left|\frac{\det\mathsf M}{M_{22}}\right|^2,\quad
R_r = \left|\frac{M_{12}}{M_{22}}\right|^2,\quad
T_r = \frac{1}{|M_{22}|^2}.
$$

For the real potentials in these notes $S_{12}=S_{21}$, so $\det\mathsf M = 1$ and $T_l = T_r = 1/|M_{22}|^2$.

**Why $\mathsf M$ is useful: composition.** If $V$ consists of two separated pieces with $V=0$ between them, the right-hand amplitudes of piece 1 are the left-hand amplitudes of piece 2. Therefore

$$
\mathsf M = \mathsf M_2\mathsf M_1 .
$$

This generalizes to any number of pieces.

**Delta well at $x=a$** ($V=-\alpha\delta(x-a)$). From continuity and the derivative jump:

$$
\mathsf M_a = \begin{pmatrix}1+i\beta & i\beta e^{-2ika}\\ -i\beta e^{2ika} & 1-i\beta\end{pmatrix},\qquad\det\mathsf M_a = 1 .
$$

The double-delta transmission in [[delta-function-potential]] is $1/|(\mathsf M_{+a}\mathsf M_{-a})_{22}|^2$.

## Flux factor: when the two sides differ

If $V\to V_0\neq0$ on the right, the transmitted wave travels at a different speed. $T$ must be the ratio of probability *currents*, $J = (\hbar k/m)|{\rm amplitude}|^2$, not of squared amplitudes:

$$
T = \frac{k_{\rm right}}{k_{\rm left}}\,\frac{|F|^2}{|A|^2} = \sqrt{\frac{E-V_0}{E}}\,\frac{|F|^2}{|A|^2}.
$$

## Worked examples

!!! example "Potential step $V = V_0\,\theta(x)$ (Griffiths Problem 2.34)"
    **Below the step** ($E<V_0$). The right-hand solution decays and carries no current, so $R=1$ (numerically 1.0000000000 at $E=V_0/2$). There is still a nonzero density under the step.

    **Above the step** ($E>V_0$), with $l = \sqrt{2m(E-V_0)}/\hbar$:

    $$
    R = \left(\frac{k-l}{k+l}\right)^2,\qquad T = \frac{4kl}{(k+l)^2}.
    $$

    | $E/V_0$ | $R$ | $T$ (flux) | $|F|^2/|A|^2$ (naive) |
    |---|---|---|---|
    | 2 | 0.029437 | 0.970563 | 1.372583 |
    | 4 | 0.005155 | 0.994845 | 1.148748 |

    The naive ratio exceeds 1. The flux factor is essential.

!!! example "Cliff: a sudden drop $-V_0$ (Griffiths Problem 2.35)"
    **Reflection.** The same formula holds with $l = \sqrt{2m(E+V_0)}/\hbar$. At $E = V_0/3$, $l = 2k$ and $R = (1/3)^2 = 1/9$.

    **Neutron entering a nucleus** ($E = 4$ MeV, drop $12$ MeV). Again $l = 2k$, so $R = 1/9$ and the probability of entering (and possibly inducing fission) is $T = 8/9 = 0.889$.

    **Why a falling car does not reflect.** A falling car sees a gradual drop over many wavelengths. Reflection from a step is a sudden-change effect, so the step model does not describe a cliff.

!!! example "Rectangular barrier: tunnelling (Griffiths Problem 2.33)"
    **Potential.** $V = +V_0$ for $|x|<a$.

    **Transmission in the three regimes.**

    $$
    T^{-1} = \begin{cases}
    1 + \dfrac{V_0^2}{4E(V_0-E)}\sinh^2\!\left(\dfrac{2a}{\hbar}\sqrt{2m(V_0-E)}\right), & E<V_0\\[2ex]
    1 + \dfrac{2mV_0a^2}{\hbar^2}, & E=V_0\\[2ex]
    1 + \dfrac{V_0^2}{4E(E-V_0)}\sin^2\!\left(\dfrac{2a}{\hbar}\sqrt{2m(E-V_0)}\right), & E>V_0.
    \end{cases}
    $$

    Griffiths gives the first line as a partial answer. The second and third are derived here, and all three are checked numerically.

    **Check** ($\hbar=m=V_0=a=1$):

    | $E$ | 0.25 | 0.5 | 1.0 | 1.5 |
    |---|---|---|---|---|
    | Closed form $T$ | 0.022196 | 0.070651 | 0.333333 | 0.783940 |
    | Transfer matrix $T$ | 0.022196 | 0.070651 | 0.333333 | 0.783940 |

    **Opaque limit.** For a thick barrier, $\sinh^2\approx\tfrac14e^{2\kappa(2a)}$, so $T\propto e^{-2\kappa\cdot\text{width}}$ with $\kappa = \sqrt{2m(V_0-E)}/\hbar$. This is the exponential sensitivity behind tunnelling microscopy, and the WKB tunnelling formula generalizes it.

!!! example "Reflectionless potential $V = -(\hbar^2a^2/m)\,\mathrm{sech}^2(ax)$ (Griffiths Problem 2.52)"
    **Bound state.** $\psi_0 = \sqrt{a/2}\,\mathrm{sech}(ax)$ is the single bound state, with $E_0 = -\hbar^2a^2/2m$ (checked symbolically: $\hat H\psi_0/\psi_0 = -\tfrac12$ for $\hbar=m=a=1$).

    **Scattering states.** For every $E>0$,

    $$
    \psi_k(x) = A\,\frac{ik - a\tanh(ax)}{ik+a}\,e^{ikx}
    $$

    is a solution. As $x\to-\infty$, $\tanh\to-1$ and $\psi_k\to Ae^{ikx}$: a pure incident wave with no reflected part. As $x\to+\infty$, $\psi_k\to A\frac{ik-a}{ik+a}e^{ikx}$, a transmitted wave with a pure phase. So

    $$
    R = 0,\qquad T = 1\quad\text{at every energy.}
    $$

    **Numerical check.** Slicing $V$ into 30000 constant steps on $[-15,15]$ gives $T = 1.00000000$ with $R \le 2\times10^{-14}$ at $E = 0.05$, $0.5$ and $2$.

## Algorithm: piecewise-constant transfer matrix

Used for every scattering check in this folder (`transmission()` in `ch02_tise.py`).

1. **Partition.** Split the line at $x_1<x_2<\cdots<x_N$ with constant $V_j$ in each region. In region $j$ take $\psi = A_je^{iq_jx}+B_je^{-iq_jx}$ with $q_j = \sqrt{2m(E-V_j)}/\hbar$, which is imaginary in forbidden regions. Complex arithmetic handles evanescent waves automatically.
2. **Match at each boundary.** Continuity of $\psi$ and $\psi'$ at $x_b$ reads $\mathsf D(q_{j+1},x_b)\,\mathbf c_{j+1} = \mathsf D(q_j,x_b)\,\mathbf c_j$, with

    $$
    \mathsf D(q,x) = \begin{pmatrix}e^{iqx} & e^{-iqx}\\ iq\,e^{iqx} & -iq\,e^{-iqx}\end{pmatrix}.
    $$

3. **Multiply.** $\mathsf M = \prod_b \mathsf D(q_{j+1},x_b)^{-1}\mathsf D(q_j,x_b)$, ordered right to left.
4. **Read off.** Set $(A,B)=(1,B)$ and $(F,G)=(F,0)$. Solve $B = -M_{21}/M_{22}$, then $T = (q_N/q_0)|F|^2$ and $R = |B|^2$.

**Cost.** $O(N)$ products of $2\times2$ matrices per energy.

**Numerical caution.** For thick opaque barriers the growing exponentials can overflow. The usual remedy is to compose scattering matrices instead, since their entries stay bounded.

Smooth potentials are handled by fine slicing; the sech² check above used this. A delta function is a single slice of height $h$ and width $1/h$ with $h\to\infty$; $h = 10^5$ reproduces the analytic delta-well $T$ to $2\times10^{-6}$.

## Source

Griffiths and Schroeter, *Introduction to Quantum Mechanics* (3rd ed., Cambridge University Press, 2018), Further Problems on Ch. 2: Problems 2.33-2.35 (Eq. 2.175), 2.52, 2.53 (Eqs. 2.178-2.182), 2.54 (Eqs. 2.183-2.184), Figs. 2.19, 2.21, 2.22 (described). Page numbers are not given because the PDF used is an e-book rendering without print pagination. The $\mathsf M$–$\mathsf S$ relations, the $E\ge V_0$ barrier formulas, the delta $\mathsf M$-matrix and the algorithm section are worked solutions or standard methods written for this note, not quoted, and are all checked numerically. Recomputed with `griffiths/ch02_tise.py` (sections F and H).
