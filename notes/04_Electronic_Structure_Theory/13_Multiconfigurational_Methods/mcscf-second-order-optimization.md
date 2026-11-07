---
id: mcscf-second-order-optimization
title: Second-order MCSCF optimization - exponential parametrization, generalized Brillouin theorem and Newton methods
summary: Jørgensen and Simons parametrize an MCSCF state as exp(iλ)exp(iS)|0⟩, with orbital rotations λ and state rotations S between the reference and its orthogonal complement. Expanding the energy to second order gives the gradient (generalized Brillouin theorem) and the Hessian as double commutators. One-step and two-step Newton-Raphson schemes, mode damping, redundant parameters and the linearly convergent super-CI method. A computed CAS(2,2) example for H2 shows why plain Newton fails from a Hartree-Fock start and how a level-shifted step converges quadratically.
status: in-progress
kind: algorithm
level: advanced
tags: [mcscf, casscf, newton-raphson, generalized-brillouin-theorem, orbital-hessian, augmented-hessian, super-ci, redundancy]
prerequisites: [orbital-rotations, mcscf-and-gvb, second-quantized-operators]
related: [scf-second-order-and-stability, spin-tensor-operators, natural-orbitals, brillouin-theorem, heh-plus-minimal-basis-model, baker-campbell-hausdorff, ci-in-practice]
order: 20
date: 2026-11-03
---

## Stationary points and excited states (J-S Sec. 2A)

**The problem.** An approximate energy $E(C_1,\ldots,C_j)$ depends on variational parameters: linear CI coefficients, orbital parameters, or both. We look for **stationary points**, $\partial E/\partial C_i = 0$. The second derivatives classify each one as a local minimum, a saddle point or a maximum.

**Excited states.** An excited state is a stationary point, not a minimum. A procedure that simply goes downhill can collapse to the lowest state of the same symmetry. This is prevented by constraining the parameters (for example orthogonality to the ground state) or by following the dominant coefficients from iteration to iteration. A Newton method on an exactly unitary parametrization converges quadratically to a stationary point of either kind, and the number of negative Hessian eigenvalues identifies which one.

**Why second order.** If the energy were exactly quadratic in the parameters, one Newton step would land on the stationary point. Iterations are needed only because of the cubic and higher terms that a second-order model drops.

## Parameters

**Wave function.** $|0\rangle = \sum_g|\Phi_g\rangle C_{g0}$ is a linear combination of configurations $|\Phi_g\rangle$ (each a product of creation operators acting on the vacuum). MCSCF varies both the orbitals and the coefficients $C_{g0}$ ([[mcscf-and-gvb]]).

**State rotations instead of coefficients.** Complete $|0\rangle$ by orthonormal complement states $|n\rangle = \sum_g|\Phi_g\rangle C_{gn}$ within the same configuration space. A change of the CI vector is a unitary rotation among $\{|0\rangle, |n\rangle\}$. For real wave functions, and since only $|0\rangle$ is optimized, the generator needs only rotations between $|0\rangle$ and each $|n\rangle$:

$$
\hat S = i\sum_{n\ne0}P_{n0}\big(|n\rangle\langle0| - |0\rangle\langle n|\big).
$$

There is one fewer parameter $P_{n0}$ than coefficients, and normalization is automatic.

**Closed form.** Because the generator matrix is so sparse, the exponential sums analytically:

$$
e^{i\hat S}|0\rangle = \cos x\,|0\rangle - \frac{\sin x}{x}\sum_n P_{n0}|n\rangle,
\qquad x^2 = \sum_n P_{n0}^2 .
$$

(The sign in front of the sum depends on the sign convention for $P$.)

**Full parametrization.** $|\tilde0\rangle = e^{i\hat\lambda}e^{i\hat S}|0\rangle$, with $e^{i\hat\lambda}$ the orbital rotation of [[orbital-rotations]]. In this order the orbital rotation simply transforms all creation operators in $|0\rangle$ and in $\hat S$; the opposite order would require overlaps between states in different orbital sets, so J-S use this one.

## Energy to second order

**Expansion.** Using the Baker-Campbell-Hausdorff expansion,

$$
E(\lambda, S) = \langle0|e^{-i\hat S}e^{-i\hat\lambda}\hat He^{i\hat\lambda}e^{i\hat S}|0\rangle
= E_0 - 2(\boldsymbol\kappa\ \mathbf P)\begin{pmatrix}\mathbf W\\ \mathbf V\end{pmatrix} + (\boldsymbol\kappa\ \mathbf P)(\mathbf A - \mathbf B)\begin{pmatrix}\boldsymbol\kappa\\ \mathbf P\end{pmatrix} + \cdots
$$

with excitation operators $\hat Q^\dagger = \{a_r^\dagger a_s\}_{r>s}$ (orbital) and $\hat R^\dagger = \{|n\rangle\langle0|\}$ (state), and

$$
\mathbf W = \langle0|[\hat Q, \hat H]|0\rangle,\qquad \mathbf V = \langle0|[\hat R, \hat H]|0\rangle,
$$

$$
\mathbf A = \begin{pmatrix}\langle0|[\hat Q, \hat H, \hat Q^\dagger]|0\rangle & \langle0|[\hat Q, \hat H, \hat R^\dagger]|0\rangle\\ \langle0|[\hat R, \hat H, \hat Q^\dagger]|0\rangle & \langle0|[\hat R, \hat H, \hat R^\dagger]|0\rangle\end{pmatrix},
\qquad
\mathbf B = \begin{pmatrix}\langle0|[\hat Q, \hat H, \hat Q]|0\rangle & \langle0|[\hat Q, \hat H, \hat R]|0\rangle\\ \langle0|[\hat R, \hat H, \hat Q]|0\rangle & \langle0|[\hat R, \hat H, \hat R]|0\rangle\end{pmatrix},
$$

where the symmetrized double commutator is $[\hat X, \hat H, \hat Y] = \tfrac12\big([\hat X,[\hat H, \hat Y]] + [[\hat X, \hat H], \hat Y]\big)$. It appears naturally because $\langle0|[\hat\lambda,[\hat H,\hat\lambda]]|0\rangle = \langle0|[[\hat\lambda,\hat H],\hat\lambda]|0\rangle$.

**Generalized Brillouin theorem (GBT).** At a stationary point $\mathbf W = \mathbf 0$ and $\mathbf V = \mathbf 0$. $\mathbf V = 0$ says $\langle n|\hat H|0\rangle = 0$: $|0\rangle$ is an eigenvector of $\hat H$ in the configuration space. $\mathbf W = 0$ says $\langle0|[a_r^\dagger a_s, \hat H]|0\rangle = 0$ for every nonredundant rotation: the orbital analogue, which for a single determinant is Brillouin's theorem ([[brillouin-theorem]]).

**Hessian.** $\mathbf A - \mathbf B$ is the electronic Hessian. Its eigenvalues classify the stationary point: all positive for a minimum, one negative for the first excited state of the symmetry, and so on.

**What is needed.** $\mathbf W$, $\mathbf A_{11}$ and $\mathbf B_{11}$ require only one- and two-electron integrals and the one- and two-particle density matrices of $|0\rangle$; the mixed blocks need transition density matrices $\langle n|\ldots|0\rangle$. For example, $(\mathbf A_{22})_{mn} = \langle m|\hat H|n\rangle - \delta_{mn}\langle0|\hat H|0\rangle$ and $V_n = \langle n|\hat H|0\rangle$ (J-S Eqs. 2.38-2.44). The excitation operators are taken as singlet tensor operators so that spin symmetry is preserved ([[spin-tensor-operators]]).

## Newton-Raphson schemes

**One-step (quadratically convergent).** Truncating at second order and setting the derivative to zero:

$$
\begin{pmatrix}\mathbf W\\ \mathbf V\end{pmatrix} = (\mathbf A - \mathbf B)\begin{pmatrix}\boldsymbol\kappa\\ \mathbf P\end{pmatrix}.
$$

Solve, rotate orbitals and states, rebuild, repeat until $\mathbf W$ and $\mathbf V$ vanish. Orbitals and CI are updated together, including the orbital-CI coupling block $\mathbf A_{12} - \mathbf B_{12}$.

**Two-step.** Diagonalize the CI matrix first in each iteration. Then $\mathbf V = 0$, $\mathbf A_{22}$ is diagonal ($E_n - E_0$) and $\mathbf B_{22} = 0$. Eliminating $\mathbf P$ by partitioning gives an orbital-only equation with an effective Hessian:

$$
\boldsymbol\kappa = \Big[\mathbf A_{11} - \mathbf B_{11} - (\mathbf A_{12} - \mathbf B_{12})\mathbf A_{22}^{-1}(\mathbf A_{21} - \mathbf B_{21})\Big]^{-1}\mathbf W .
$$

New orbitals, new CI, repeat. Many programs drop the coupling term; convergence often barely suffers, but it is then no longer quadratic.

**GBT view.** Requiring that the GBT error at iteration $n+1$ be the square of that at iteration $n$ gives the same linear equations: the Newton scheme is also "the one that makes the GBT hold to second order".

**Mode damping.** Far from convergence the Hessian may have the wrong number of negative eigenvalues, and a Newton step then heads for a saddle point or overshoots. J-S transform to the Hessian eigenvectors (normal modes) and restrict or reverse the step along each mode so that the walk goes downhill in all modes for a ground state (and uphill along exactly one mode for the first excited state). In the two-step scheme damping is only possible in the orbital-dominated space. (The augmented-Hessian or level-shifted Newton step used below is a common modern realization of the same idea; general knowledge, not from J-S.)

## Redundant parameters

**Test.** An orbital excitation $a_r^\dagger a_s$ is redundant if its effect can be reproduced by state rotations, that is, if $a_r^\dagger a_s|l\rangle$ lies in the configuration space for every state $|l\rangle$. J-S's criterion: $\sum_m|\langle m|a_r^\dagger a_s|l\rangle|^2 = \langle l|a_s^\dagger a_r a_r^\dagger a_s|l\rangle$.

**Factorization.** The redundant generators form a subgroup, so $e^{i\hat\lambda} = e^{i\hat\lambda'}e^{i\hat\lambda''}$ with $\hat\lambda''$ redundant. The $e^{i\hat\lambda''}$ factor only rotates within the configuration space, which $e^{i\hat S}$ already covers. Redundant rotations can be dropped.

**Common cases (general knowledge).** In a CASSCF wave function the inactive-inactive, active-active and virtual-virtual rotations are redundant; only inactive-active, inactive-virtual and active-virtual rotations remain. Keeping a redundant parameter makes the Hessian singular.

## Super-CI and other first-order methods

**Super-CI (Banerjee-Grein).** Insist only on the orbital GBT at each step. Take the linear trial function $X_0|0\rangle + \sum_{r>s}X_{rs}(a_r^\dagger a_s - a_s^\dagger a_r)|0\rangle$, solve the "super-CI" secular problem $\mathbf{HX} = E\mathbf{SX}$, and read off new orbitals $\tilde\phi_s = X_0\phi_s + \sum_r X_{rs}\phi_r - \ldots$ correct to first order, which must then be re-orthonormalized. A new CI calculation follows.

**Convergence.** The super-CI wave function agrees with $e^{i\hat\lambda}|0\rangle$ only to first order in the parameters; the second-order terms such as $\langle0|\hat H(i\hat\lambda)^2|0\rangle$ are missing, and orbital-CI coupling is usually ignored. Super-CI is therefore linearly, not quadratically, convergent, although each super-CI energy is an upper bound.

**Cost consideration.** Every MCSCF iteration needs a (partial) two-electron integral transformation, often the dominant cost, so methods that converge in few iterations pay off.

## A computed example: H₂ CAS(2,2)

**Setup.** H$_2$, 6-31G**, R = 1.4 bohr, active space $\{\sigma_g, \sigma_u\}$ with two electrons, 10 molecular orbitals. Parameters: 16 active-virtual orbital rotations ($\boldsymbol\kappa$) and 3 state rotations ($\mathbf P$) in the four-determinant active space; active-active rotations are omitted as redundant. Energy gradient and Hessian by finite differences of the exactly parametrized energy $E(\boldsymbol\kappa, \mathbf P)$.

!!! example "Newton iterations from the Hartree-Fock orbitals and the HF determinant (computed for this note)"
    **Plain Newton** ($\mathbf x = -\mathbf H^{-1}\mathbf g$): the starting Hessian has a negative eigenvalue (−0.040): at the HF point the energy curves downward along the direction that mixes in $\sigma_u^2$, so the HF point is a saddle of $E(\boldsymbol\kappa, \mathbf P)$. The steps wander: after 8 iterations the energy is still −1.131285 hartree, the HF value, and the gradient norm stays at 0.03-0.08.

    **Level-shifted (augmented-Hessian) Newton with a step limit of 0.3:**

    | Iteration | Energy (hartree) | Gradient norm | Lowest Hessian eigenvalue |
    |---:|---:|---:|---:|
    | 0 | −1.1312843 | 1.5e−1 | −0.0401 |
    | 1 | −1.1406179 | 1.4e−1 | −0.0109 |
    | 2 | −1.1491465 | 4.0e−2 | +0.0255 |
    | 3 | −1.1495311 | 4.3e−3 | +0.0301 |
    | 4 | −1.14953626 | 5.4e−5 | +0.0298 |
    | 5 | −1.14953626 | 6.8e−9 | +0.0298 |

    - **Converged energy** −1.1495363, identical to PySCF's CASSCF(2,2) (−1.1495363).
    - **Quadratic convergence.** Once the Hessian is positive definite, the gradient goes 4.3e−3 → 5.4e−5 → 6.8e−9, roughly squaring each step.
    - **Lesson.** The second-order model is only trustworthy near the minimum; far away, the step must be controlled (mode damping, level shift, trust radius).

```python
def energy(x, C, cbasis):              # x = (kappa for active-virtual pairs, P for state rotations)
    k, P = x[:len(pairs)], x[len(pairs):]
    K = np.zeros((nmo, nmo))
    for val, (p, q) in zip(k, pairs): K[p, q], K[q, p] = val, -val
    Cn = C @ expm(K)                                         # orbital rotation exp(kappa)
    x2 = np.linalg.norm(P)
    c = np.cos(x2) * cbasis[:, 0] + (np.sin(x2) / x2 if x2 > 1e-14 else 1.0) * (cbasis[:, 1:] @ P)  # exp(S)|0>
    ca = Cn[:, :nact]
    h1 = ca.T @ hcore @ ca; g2 = ao2mo.restore(1, ao2mo.kernel(mol, ca), nact)
    return direct_spin1.energy(h1, g2, c.reshape(2, 2), nact, (1, 1)) + mol.energy_nuc()
# step: augmented Hessian [[0, g^T], [g, H]] -> lowest eigenvector (1, x); cap |x|; then
# C <- C expm(K(x)) ;  cbasis <- cbasis expm(S(x))   (rotate reference and complement together)
```

!!! example "HeH⁺ two-configuration MCSCF: J-S Problem 2.6 recomputed"
    Configurations $1\sigma^2$ and $2\sigma^2$, with one orbital parameter and one state parameter, start from the SCF orbitals and the CI states.

    - **First iteration.** Gradient $\partial E/\partial\kappa = 0.0447$ (J-S $2|W| = 0.0448$). Hessian $(\mathbf A - \mathbf B)$: 2.4009 (orbital), 0.4215 in magnitude (coupling), 2.2714 (state); J-S give 2.4006, 0.4218 and 2.2711.
    - **Step.** $|\kappa| = 0.0096$, $|P| = 0.0018$.
    - **Convergence.** The energy goes from −2.85055810 to −2.85077291 in one step and stays there.
    - **Result.** This equals the three-configuration full CI: the $1\sigma2\sigma$ configuration is generated by the orbital rotation.

    Details are in [[heh-plus-minimal-basis-model]].

## Source

Jørgensen and Simons, *Second Quantization-Based Methods in Quantum Chemistry* (Academic Press, New York, 1981), Ch. 2, Secs. A-B, pp. 18-35, Eqs. (2.1)-(2.79): unitary parametrization (2.6)-(2.23), energy expansion and GBT (2.24)-(2.32), one-step (2.33)-(2.34) and two-step (2.35)-(2.37) procedures, matrix elements (2.38)-(2.44), mode damping (2.45)-(2.52), redundancy (2.53)-(2.62), GBT-based and super-CI procedures (2.63)-(2.79); Problem 2.6, p. 53, and Solution pp. 62-64. The CASSCF redundancy list and the augmented-Hessian remark are general knowledge. Example computed for this note with PySCF 2.14 integrals and CI routines.
