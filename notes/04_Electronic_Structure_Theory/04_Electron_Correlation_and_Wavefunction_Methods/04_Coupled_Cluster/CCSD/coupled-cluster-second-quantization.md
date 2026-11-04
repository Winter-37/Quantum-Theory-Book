---
id: coupled-cluster-second-quantization
title: Coupled-cluster theory in second quantization - exp(T), the terminating similarity transform, perturbative and Newton solutions
summary: The cluster operator T = T1 + T2 + ... acting as exp(T) on a determinant produces every excitation level as connected clusters plus disjoint products (C2 = T2 + T1²/2, C4 = T4 + T2²/2 + T1T3 + T1²T2/2 + T1⁴/24). Projecting exp(−T)H exp(T)|0⟩ = E|0⟩ gives an energy and amplitude equations that terminate after four nested commutators (verified numerically). With HF orbitals and T = T2, iterating the equations reproduces MP2, then MP2+MP3, then the fourth-order quadruples; T4 enters only at fifth order. Newton-Raphson converges quadratically, its first step from zero being linear CCD. Computed for water.
status: in-progress
kind: theory
level: advanced
tags: [coupled-cluster, ccsd, ccd, cluster-operator, similarity-transformation, bch, newton-raphson, mbpt, size-consistency]
prerequisites: [coupled-cluster-doubles, creation-and-annihilation-operators, mp3]
related: [coupled-pair-approximations, linked-cluster-theorem, orbital-rotations, one-particle-hamiltonian-models, spin-tensor-operators, baker-campbell-hausdorff]
also: []
date: 2026-11-03
---

## Why an exponential

**The problem with CI.** A truncated CI or MCSCF function contains a fixed, finite number of electron-pair interactions. For a large system it becomes a vanishing part of the exact wave function ([[size-consistency]]). Perturbation theory helps but assumes the fluctuation potential is small.

**The physical picture.** Electron-pair correlations dominate, and quadruple excitations arise mainly as products of two independent pair excitations (Sinanoğlu). Coupled cluster builds this in by writing

$$
|0\rangle = e^{\hat T}|0^\circ\rangle,
\qquad
\hat T = \hat T_1 + \hat T_2 + \cdots + \hat T_N,
$$

$$
\hat T_1 = \sum_{\alpha r}t_\alpha^r\,a_r^\dagger a_\alpha,
\qquad
\hat T_2 = \sum_{\alpha>\beta}\sum_{r>s}t_{\alpha\beta}^{rs}\,a_r^\dagger a_s^\dagger a_\beta a_\alpha,\ \ldots
$$

where Greek letters are spin orbitals occupied in the reference determinant $|0^\circ\rangle$ and $r,s,\ldots$ are unoccupied. Almost all applications use a single-determinant reference.

**Disjoint clusters.** All the excitation operators commute (they contain only particle creators and hole annihilators). A product such as $\hat T_2\hat T_2$ vanishes whenever the two clusters share a hole or a particle index, so it describes **disjoint** pairs only. Even with $\hat T$ truncated at $\hat T_2$, the wave function contains $\tfrac1{2!}\hat T_2^2$, $\tfrac1{3!}\hat T_2^3,\ldots$ up to $N/2$ disjoint pairs, which is what size consistency needs.

## Excitation-level content

Expanding $e^{\hat T}$ and grouping by excitation level, $e^{\hat T}|0^\circ\rangle = (1 + \hat C_1 + \hat C_2 + \hat C_3 + \hat C_4 + \cdots)|0^\circ\rangle$ with

$$
\hat C_1 = \hat T_1,\qquad
\hat C_2 = \hat T_2 + \tfrac12\hat T_1^2,\qquad
\hat C_3 = \hat T_3 + \hat T_1\hat T_2 + \tfrac16\hat T_1^3,
$$

$$
\hat C_4 = \hat T_4 + \tfrac12\hat T_2^2 + \hat T_1\hat T_3 + \tfrac12\hat T_1^2\hat T_2 + \tfrac1{24}\hat T_1^4 .
$$

The CI quadruples thus have five cluster parts. $\tfrac12\hat T_2^2$ (two independent pairs) is expected to dominate; $\hat T_4$, a genuine four-electron correlation, should be small; and the terms with $\hat T_1$ can be made small by good orbitals, since $e^{\hat T_1}$ is essentially an orbital rotation ([[orbital-rotations]], [[one-particle-hamiltonian-models]]).

## The equations

**Similarity transform.** Insert into $\hat He^{\hat T}|0^\circ\rangle = Ee^{\hat T}|0^\circ\rangle$ and multiply by $e^{-\hat T}$:

$$
e^{-\hat T}\hat He^{\hat T}|0^\circ\rangle = \Big(\hat H + [\hat H, \hat T] + \tfrac1{2!}[[\hat H, \hat T], \hat T] + \tfrac1{3!}[[[\hat H, \hat T], \hat T], \hat T] + \tfrac1{4!}[[[[\hat H, \hat T], \hat T], \hat T], \hat T]\Big)|0^\circ\rangle = E|0^\circ\rangle .
$$

**Termination.** $\hat H$ has at most four general creation/annihilation operators. Each commutator with $\hat T$ contracts away at least one of them (the rank reduction of [[baker-campbell-hausdorff]]). After four commutators only operators of the form $a^\dagger\cdots a_{\text{hole}}\cdots$ (pure excitations) remain, and these commute with $\hat T$, so the fifth commutator is zero. This holds however $\hat T$ is truncated: the equations are at most quartic in the amplitudes.

**Projection.** The energy is the projection on $\langle0^\circ|$; the amplitudes are fixed by requiring the projections on all excited determinants included in $\hat T$ (e.g. singles and doubles for CCSD) to vanish. The number of equations equals the number of amplitudes.

**Not variational.** The energy is not an expectation value. The variational expression $\langle0^\circ|e^{\hat T^\dagger}\hat He^{\hat T}|0^\circ\rangle/\langle0^\circ|e^{\hat T^\dagger}e^{\hat T}|0^\circ\rangle$ would not terminate, because $\hat T^\dagger$ does not commute with $\hat T$. It is the $e^{-\hat T}$ on the left that closes the equations. The commutator structure also means the energy contains only linked terms, so CC is size consistent ([[linked-cluster-theorem]]).

!!! example "The commutator series terminates (computed for this note)"
    Linear H$_4$ (STO-3G, 1.5 bohr spacing), 8 spin orbitals, Hamiltonian and a random $\hat T_1 + \hat T_2$ (amplitudes ~0.1) built as $256\times256$ Fock-space matrices with the Jordan-Wigner construction. Frobenius norms of the $k$-fold nested commutators $[\ldots[\hat H, \hat T], \ldots, \hat T]$:

    | $k$ | 1 | 2 | 3 | 4 | 5 | 6 |
    |---|---:|---:|---:|---:|---:|---:|
    | norm | 5.44 | 3.25e−1 | 7.48e−2 | 2.16e−2 | 1.2e−19 | 5.8e−21 |

    The fifth commutator is zero to machine precision, for the full operator, not just its projection.

## Doubles only, Hartree-Fock orbitals

**Why $\hat T\approx\hat T_2$.** With Hartree-Fock orbitals, Brillouin's theorem suggests that $\hat T_1$, which mainly relaxes orbitals, is less important than $\hat T_2$. J-S add that a balanced treatment includes both (CCSD).

**Energy.** Partition $\hat H = \hat H^\circ + \hat U$ with $\hat H^\circ = \sum\varepsilon_r a_r^\dagger a_r$. Projecting on $\langle0^\circ|$ and using $\langle0^\circ|\hat T_2 = 0$ and that $\hat T_2^2|0^\circ\rangle$ (quadruples) cannot reach $\langle0^\circ|$ through $\hat H$:

$$
E = \langle0^\circ|\hat H(1 + \hat T_2)|0^\circ\rangle = E_{\text{HF}} + \sum_{\alpha>\beta}\sum_{m>n}\langle\alpha\beta||mn\rangle\,t_{\alpha\beta}^{mn}.
$$

**Amplitude equation.** Projecting on doubles, only $\langle{}^{mn}_{\alpha\beta}|\hat H(1 + \hat T_2 + \tfrac12\hat T_2^2)|0^\circ\rangle - \langle{}^{mn}_{\alpha\beta}|\hat T_2\hat H(1 + \hat T_2)|0^\circ\rangle$ survives, a **quadratic** equation:

$$
(\varepsilon_\alpha + \varepsilon_\beta - \varepsilon_m - \varepsilon_n)\,t_{\alpha\beta}^{mn} = \langle mn||\alpha\beta\rangle + (\text{terms linear in } t) + (\text{terms quadratic in } t),
$$

J-S Eq. (4.19), equivalent to the CCD equations of [[coupled-cluster-doubles]] and Szabo's CCA ([[coupled-pair-approximations]]).

## Perturbative solution: iterations generate MPn

**Scheme.** Start with $t = 0$ on the right, solve for the $t$ on the left, reinsert, repeat. Assigning orders to the terms shows the link to many-body perturbation theory:

1. **First iteration:** $t_{\alpha\beta}^{mn} = \langle mn||\alpha\beta\rangle/(\varepsilon_\alpha + \varepsilon_\beta - \varepsilon_m - \varepsilon_n)$. The energy is exactly MP2 ([[mp2]]).
2. **Second iteration, linear terms only:** the energy is exactly MP2 + MP3 ([[mp3]]).
3. **Next iteration including the quadratic terms:** the energy contains all fourth-order quadruples contributions, which come only from $\tfrac12\hat T_2^2$ (two simultaneous pair interactions).
4. **Converged:** all diagrams built from doubles and products of doubles, summed to infinite order.

**Missing pieces at fourth order.** Singles and triples also contribute at fourth order, so a complete fourth order needs $\hat T_1$ and $\hat T_3$. The connected quadruples $\hat T_4$ first enter at **fifth** order: true four-body correlation is much less important than pair correlation.

!!! example "Water, STO-3G, Szabo geometry (computed for this note)"
    | Step | Correlation energy (hartree) |
    |---|---:|
    | Iteration 1 | −0.0354993056 (= MP2) |
    | Iteration 2, linear terms | −0.0450914856 (= MP2 + MP3 = −0.0354993056 − 0.0095921800) |
    | Iteration 3, with quadratic terms | −0.0477034 |
    | Converged CCD | −0.0491220 |
    | Full CI | −0.0494860 |

    Iterating the full CCD residual from $t = 0$ (quadratic terms always included) gives errors relative to converged CCD of 1.4e−2, 4.3e−3, 1.5e−3 after 1-3 iterations, 2.1e−4 after 5, 1.4e−5 after 8 and 4.2e−7 after 12: linear convergence by a factor of roughly 2.5-3 per iteration.

## Newton-Raphson

**Form.** Collecting terms, the doubles equations read $\mathbf 0 = \mathbf a + \mathbf b\,\mathbf t + \mathbf c\,\mathbf t\mathbf t$ with $a_{rs,\alpha\beta} = \langle rs||\alpha\beta\rangle$. Newton-Raphson linearizes $\mathbf f(\mathbf t) = \mathbf a + \mathbf b\mathbf t + \mathbf c\mathbf t\mathbf t$ about the current $\mathbf t_0$ and solves

$$
\mathbf f(\mathbf t_0) + \frac{\partial\mathbf f}{\partial\mathbf t}\Big|_{\mathbf t_0}\Delta\mathbf t = \mathbf 0,
\qquad \mathbf t_0\to\mathbf t_0 + \Delta\mathbf t .
$$

The first molecular CC calculations used it; J-S note that the large linear systems led later work to prefer the perturbative iteration with convergence acceleration (reduced linear equations, as in Davidson's method).

**First step from zero is linear CCD.** At $\mathbf t_0 = 0$ the Jacobian is $\mathbf b$, so the first Newton step solves $\mathbf a + \mathbf b\mathbf t = 0$: L-CCD (D-MBPT(∞)).

!!! example "Newton-Raphson CCD for water, STO-3G (computed for this note)"
    270 unique amplitudes $t_{ij}^{ab}$ ($i<j$, $a<b$), Jacobian by central differences:

    | Newton step | Energy | Residual norm | Error vs converged CCD |
    |---:|---:|---:|---:|
    | 1 | −0.0498106 | 4.4e−3 | −6.9e−4 |
    | 2 | −0.0491222 | 1.1e−6 | −1.4e−7 |
    | 3 | −0.0491220 | 7.8e−14 | −4e−13 |

    - **Step 1** gives −0.0498106, the L-CCD energy (−0.049811), as predicted.
    - **Quadratic convergence**: the residual goes 4.4e−3 → 1.1e−6 → 7.8e−14.
    - The cost is the Jacobian: here 270 × 270, in general (number of amplitudes)², which is why iterative perturbative solvers with acceleration are used in practice.

## Minimal-basis HeH⁺ (J-S Problem 4.1)

**One amplitude.** In J-S's two-orbital HeH⁺ ([[heh-plus-minimal-basis-model]]) the only double excitation is $1\sigma^2\to2\sigma^2$, with amplitude $t$. With $K = \langle11|22\rangle$ and $\Delta = \langle2\sigma^2|H|2\sigma^2\rangle - \langle1\sigma^2|H|1\sigma^2\rangle = 2(\varepsilon_2 - \varepsilon_1) + J_{11} + J_{22} - 4J_{12} + 2K_{12}$, the CCD equations are

$$
E_{\text{corr}} = Kt,\qquad 0 = K + \Delta\,t - K\,t^2 .
$$

The quadratic term comes from $-t\langle D|H|0\rangle t$ (the $-\hat T_2\hat H\hat T_2$ part of the similarity transform); $\tfrac12\hat T_2^2|0^\circ\rangle$ vanishes for two electrons.

**Equivalence with CI for two electrons.** Projecting $(1 - \hat T_2)H(1 + \hat T_2)|0^\circ\rangle = E|0^\circ\rangle$ on $\langle0^\circ|$ and $\langle D|$ and eliminating $E$ gives exactly the 2×2 CI eigenvalue problem in intermediate normalization $(1, t)$. Both roots of the quadratic are therefore CI eigenvalues: the physical root is the ground state, and the other is the doubly excited state.

!!! example "HeH⁺ coupled cluster (computed for this note; J-S in parentheses; electronic energies)"
    $K = 0.1262$, $\Delta = 2.2573$, $E_{\text{HF}} = -4.272099$.

    | Method | $t$ | $E_{\text{corr}}$ | $E$ |
    |---|---:|---:|---:|
    | MP2 + MP3 (perturbative CC, Problem 3.2) | | −0.006743 (−0.0066/−0.0067) | |
    | Linear CCD, $t = -K/\Delta$ | −0.0559 (0.0559) | −0.007052 (−0.0070) | |
    | CCD, physical root | −0.0557 (0.0560) | −0.007030 (−0.0071) | −4.279130 (−4.2791) |
    | CCD, second root | 17.9466 (−17.8432) | 2.264329 (2.2500) | −2.007770 (−2.0220) |
    | 2×2 CI eigenvalues | | | −4.279130, −2.007770 (−4.2790, −2.0079) |

    - **Sign of $t$.** J-S's amplitudes have the opposite sign: they write the energy with $\langle\beta\alpha||mn\rangle = -\langle11|22\rangle$. The energies are unaffected.
    - **CC = CI exactly.** Both CCD roots equal the CI eigenvalues to all printed digits. J-S's second root (−2.0220) differs from their CI value (−2.0079) by 0.014, which they attribute to four-digit integrals. Since CCD and CI are the same equations here, rounding cannot separate them; the difference must be arithmetic.
    - **Linear CC is not third-order MBPT.** Both use the linear equation, but MBPT inserts perturbative amplitudes while L-CCD solves the equation exactly. The energies differ: −0.006743 against −0.007052.
    - **n separated ions.** Integrals between ions vanish, so iterating the equations never creates amplitudes coupling different ions. Every iteration, and therefore the converged CCD energy, is $n$ times the monomer value. Doubles CI gives the $\sqrt n$ failure of [[size-consistency]].

## Where this fits

- **From Szabo's side** ([[coupled-pair-approximations]], [[coupled-cluster-doubles]]): CCD arises by approximating quadruple CI coefficients as products of doubles; the exponential is a compact way to say the same thing.
- **From J-S's side:** the exponential is the starting point, the similarity transform gives terminating equations, and the hierarchy L-CCD → CCD → CCSD → … and the MPn connection follow from the commutator structure.
- **J-S's 1981 outlook (Sec. G).** The nonlinear equations, of very large dimension and with multiple solutions (two even in the HeH⁺ example), were then the main obstacle. J-S point to the analysis of how CC solutions relate to CI eigenproblems (Monkhorst and Živković, 1978, as cited) and to the need for open-shell and multiconfigurational references.
- **Orbitals and singles:** $e^{\hat T_1}$ plays the role of an orbital rotation, so CCSD is relatively insensitive to the choice of reference orbitals.

## Code

```python
# Jordan-Wigner check of the commutator termination
X = H.copy()
for k in range(1, 7):
    X = X @ T - T @ X                       # k-fold nested commutator [..[H,T],T..]
    print(k, np.linalg.norm(X))

# CC iterations as MPn generator (spin-orbital, see pair.py in coupled-cluster-doubles)
t = d.oovv / d.D                            # iteration 1: MP2 amplitudes
t2 = d.R_lin(t) / d.D                       # iteration 2, linear terms: energy = MP2 + MP3
t3 = d.R_ccd(t2) / d.D                      # iteration 3 with quadratic terms
```

## Source

Jørgensen and Simons, *Second Quantization-Based Methods in Quantum Chemistry* (Academic Press, New York, 1981), Ch. 4, pp. 90-98: form of the wave function (4.1)-(4.10), amplitude equations and termination (4.11)-(4.13), Hartree-Fock orbitals and $T\approx T_2$ (4.14)-(4.19), perturbative solution (4.20)-(4.21), Newton-Raphson (4.22)-(4.24), summary (Sec. G); Problem 4.1 with Solution, pp. 98-102. Numerical demonstrations computed for this note with PySCF 2.14 integrals.
