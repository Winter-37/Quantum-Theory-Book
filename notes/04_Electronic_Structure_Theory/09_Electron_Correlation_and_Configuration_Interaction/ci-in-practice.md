---
id: ci-in-practice
title: The CI method in practice - CI as frozen-orbital MCSCF, choice of orbitals, configuration selection and direct iterative solution
summary: Jørgensen and Simons' view of configuration interaction. CI is the frozen-orbital limit of MCSCF; linear coefficients make the energy quadratic, so one eigenvalue problem gives every stationary point. Without orbital relaxation many singles are needed, and in full CI all orbital rotations are redundant. Choices of orbitals (canonical HF, MCSCF, iterative natural orbitals), perturbative and energy-based configuration selection, the power method and the perturbative (Jacobi-type) direct-CI iteration with an integral-driven σ = Hc, and the size-consistency problem (Be₂). Computed comparison of solvers for water.
status: in-progress
kind: algorithm
level: intermediate
tags: [configuration-interaction, direct-ci, power-method, iterative-diagonalization, natural-orbitals, configuration-selection, size-consistency]
prerequisites: [full-ci, cisd, mcscf-second-order-optimization]
related: [natural-orbitals, size-consistency, heh-plus-minimal-basis-model, iepa, matrix-eigenvalue-problem]
order: 110
date: 2026-11-03
---

## CI as the frozen-orbital limit of MCSCF

**Two parametrizations.** With fixed orbitals, the state $|0\rangle = \sum_g|\Phi_g\rangle C_{g0}$ can be optimized either through the linear coefficients or through the state-rotation parameters $P_{n0}$ of $e^{i\hat S}$ ([[mcscf-second-order-optimization]]).

**Linear coefficients.** $E(\mathbf C) = \mathbf C^T\mathbf H\mathbf C/\mathbf C^T\mathbf C$ contains no more than quadratic terms in $\mathbf C$. Making it stationary gives the CI eigenvalue problem

$$
\mathbf H\mathbf C_0 = E_0\mathbf C_0,\qquad H_{gg'} = \langle\Phi_g|\hat H|\Phi_{g'}\rangle .
$$

The same equation gives **every** stationary point (all roots) at once.

**Rotation parameters.** $E(\mathbf P)$ contains all powers of $\mathbf P$. It can be solved with the Newton scheme of MCSCF restricted to $\mathbf P$: $\mathbf V = \mathbf A_{22}\mathbf P$, with $V_n = \langle n|\hat H|0\rangle$ and $(\mathbf A_{22})_{mn} = \langle m|\hat H|n\rangle - \delta_{mn}E_0$. It converges to the same eigenvector.

**What freezing the orbitals costs.** A CI of MCSCF quality needs many extra configurations to mimic orbital relaxation:

- many singles, which act as first-order orbital rotations ([[orbital-rotations]]);
- some doubles, triples and so on, to complete the relaxation.

In **full CI** every orbital rotation is redundant ([[mcscf-second-order-optimization]]), so the orbitals do not matter. HeH⁺ illustrates this: the two-configuration MCSCF equals the three-configuration full CI ([[heh-plus-minimal-basis-model]]).

**Practical consequence.** Full CI is too large, and CI energies converge slowly with expansion length while cost grows steeply. So two choices decide a CI calculation: which orbitals, and which configurations.

## Choice of orbitals

- **Canonical RHF orbitals.** These are the usual choice, and singles do not mix with the HF determinant (Brillouin). They are poor for short expansions, though: the virtual orbitals feel the potential of all $N$ electrons, whereas an electron excited into them should feel $N-1$. Virtuals are therefore diffuse, and many are needed.
- **MCSCF orbitals.** Optimize the orbitals for a short MCSCF containing the dominant configurations, then run a much larger CI in these orbitals. Most of the orbital relaxation is then already built in.
- **Iterative natural orbitals (INO; Bender and Davidson).** Run a CI in a fixed configuration list, diagonalize its one-particle density matrix $\langle0|a_r^\dagger a_s|0\rangle$, use the natural orbitals for a new CI, and repeat until self-consistent ([[natural-orbitals]]). Löwdin showed that natural orbitals give the most compact expansion, the fewest configurations for a given overlap with the exact function.
  - **INO is not MCSCF.** INOs diagonalize the density; MCSCF orbitals minimize the energy.
  - **The configuration list must contain configurations singly excited with respect to each other.** If it contains only mutually doubly excited configurations, the density matrix is already diagonal in any orbital set, and every set is "natural". For Be, with MCSCF configurations $1s^22s^2$ and $1s^22p^2$, the INO list must also include $1s^22sns$ and $1s^22pnp$ ($n = 3,4,\ldots$). These play the role of the MCSCF orbital rotations $\kappa_{ns,2s}$ and $\kappa_{np,2p}$.

## Selecting configurations

- **Perturbative estimates.** Rayleigh-Schrödinger perturbation theory tells which classes enter at which order. With HF orbitals of a closed shell, only doubles appear in the first-order wave function ([[mp2]]). Keep configurations whose estimated coefficient or energy contribution exceeds a threshold.
- **Reference spaces.** When several configurations are important, they form a reference space, and its coupling to other configurations is estimated perturbatively.
- **Energy-lowering tests (Buenker and Peyerimhoff).** Solve a series of $(n+1)$-dimensional CIs: the $n$ reference functions plus one candidate configuration. Reject candidates whose energy lowering of the reference roots falls below a threshold.

## Large CI matrices: direct methods

**The constraint.** With 10⁴-10⁶ configurations (or many more today), the matrix cannot be stored or diagonalized by methods such as Householder that modify it. Methods are needed that find a few roots using only products $\boldsymbol\sigma = \mathbf H\mathbf c$.

**Power method.** Apply $\mathbf H$ repeatedly to a guess, $\{\mathbf C^0, \mathbf H\mathbf C^0, \mathbf H^2\mathbf C^0, \ldots\}$. Expanding $\mathbf C^0 = \sum_k a_k\mathbf C_k$ in the unknown eigenvectors,

$$
\mathbf H^n\mathbf C^0 = E_0^n\Big[a_0\mathbf C_0 + \sum_{k\ge1}a_k\Big(\frac{E_k}{E_0}\Big)^n\mathbf C_k\Big]\to a_0E_0^n\mathbf C_0 ,
$$

where $E_0$ is the eigenvalue of largest modulus. Shifting the diagonal by a constant makes the wanted (lowest) root the largest in modulus. Convergence is governed by $|E_1/E_0|$ and fails if $a_0 = 0$. The next root follows by deflation with $\mathbf H + |E_0|\,\mathbf C_0\mathbf C_0^T$.

**Perturbative iteration.** Split $\mathbf H = \mathbf H^0 + \mathbf V$, with $\mathbf H^0$ the diagonal (or a small block of dominant configurations plus the diagonal, as in Davidson's scheme). Then

$$
(\mathbf H^0 - E)\mathbf C = -\mathbf V\mathbf C
\quad\Longrightarrow\quad
\mathbf C^{(n)} = (E - \mathbf H^0)^{-1}\mathbf V\mathbf C^{(n-1)},
\qquad
E = E^0 + (\mathbf C^0)^T\mathbf V\mathbf C ,
$$

in intermediate normalization (component along the reference fixed to 1). Each iteration adds higher-order corrections. The first iteration from the HF vector, with $\mathbf H^0$ the full diagonal, is the Epstein-Nesbet second-order energy ([[iepa]]). Damping may be needed when the first steps oscillate (J-S Problem 2.5).

**Integral-driven direct CI.** For a reference plus pair excitations, J-S write the elements of $\mathbf V\mathbf C$ as sums of two-electron integrals times coefficients (Eqs. 2.111-2.117). The iteration can then be organized by reading each integral once per iteration and adding its contributions to all affected coefficients, without ever building $\mathbf H$. This is the idea of direct CI; graphical unitary-group (GUGA) programs are organized the same way. Modern codes use the Davidson subspace method on the same $\boldsymbol\sigma = \mathbf H\mathbf c$ products (general knowledge).

!!! example "Water full CI, STO-3G, 441 determinants (computed for this note)"
    $\boldsymbol\sigma = \mathbf H\mathbf c$ from PySCF's string-driven contraction; $\mathbf H$ is never stored. Errors in the electronic energy relative to full CI:

    | Method | Iterations | Error (hartree) |
    |---|---:|---:|
    | Perturbative, $\mathbf H^0$ = diagonal | 1 | −4.3e−3 (= Epstein-Nesbet) |
    | | 3 | −7.5e−4 |
    | | 10 | 8.7e−6 |
    | | 20 | 2.4e−8 |
    | | 30 | 6.4e−11 |
    | Power method, shifted | 10 | 2.3e−2 |
    | | 100 | 1.2e−4 |
    | | 500 | 5.0e−9 |
    | | 1000 | 1e−12 |
    | Davidson (PySCF) | 7 | converged (1e−10) |

    - **Perturbative.** Converges linearly and oscillates in sign, with the error shrinking by a factor of about 0.55 per iteration here.
    - **Power method.** Needs hundreds of iterations, because $|E_1 - \text{shift}|/|E_0 - \text{shift}|$ is close to 1.
    - **Davidson.** Builds an optimal subspace from the same diagonal-preconditioned residuals.

    **HeH⁺ (J-S Problem 2.5).** The 3×3 version of the perturbative iteration converges to the full CI root in about 4 iterations ([[heh-plus-minimal-basis-model]]).

## Size consistency

**Be₂ (J-S's example).** Suppose $2s^2$ and $2p^2$ ($^1S$) are needed for Be. A balanced Be₂ calculation that dissociates to two such atoms must then contain $2s_A^22s_B^2$, $2s_A^22p_B^2$, $2p_A^22s_B^2$ and $2p_A^22p_B^2$. The last is a **quadruple** excitation relative to $2s_A^22s_B^2$, and Be$_n$ would need $2n$-fold excitations.

**Consequence.** A doubles CI or MCSCF can give a smooth curve that is still unbalanced: it correlates the molecule near equilibrium better than the fragments at dissociation. Reaction and bond energies need a method that is size consistent ([[size-consistency]]). MCSCF with orbital optimization keeps expansions short enough to choose configurations physically, but does not remove the problem. J-S's numerical illustration is $n$ separated HeH⁺ ions ([[heh-plus-minimal-basis-model]]).

**Data handling.** J-S close by noting that the integral-transformation, storage and eigenvalue technology developed for large CI is the same machinery that makes efficient MCSCF, HF, coupled-cluster and Green's-function programs possible.

## Code

```python
from pyscf.fci import direct_spin1
h2e = direct_spin1.absorb_h1e(h1, g2, norb, nelec, .5)
sigma = lambda c: direct_spin1.contract_2e(h2e, c, norb, nelec).ravel()    # sigma = H c, direct
Hd = direct_spin1.make_hdiag(h1, g2, norb, nelec); ref = Hd.argmin()
c = np.zeros(Hd.size); c[ref] = 1.0; E = Hd[ref]
for it in range(30):                         # J-S Eqs. (2.109)-(2.110), H0 = diagonal
    d = E - Hd; d[ref] = np.inf
    c = (sigma(c) - Hd * c) / d; c[ref] = 1.0
    E = Hd[ref] + (sigma(c) - Hd * c)[ref]
```

## Source

Jørgensen and Simons, *Second Quantization-Based Methods in Quantum Chemistry* (Academic Press, New York, 1981), Ch. 2, Sec. D "Configuration Interaction Method", pp. 39-48, Eqs. (2.93)-(2.117); Problem 2.5, p. 52, and Solution pp. 60-62. The Davidson remark is general knowledge. Water numbers computed for this note with PySCF 2.14.
