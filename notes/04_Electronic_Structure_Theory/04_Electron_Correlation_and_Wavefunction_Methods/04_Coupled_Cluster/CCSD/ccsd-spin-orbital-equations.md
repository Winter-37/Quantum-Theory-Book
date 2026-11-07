---
id: ccsd-spin-orbital-equations
title: Spin-orbital CCSD working equations - the energy, the T1 and T2 residuals with Stanton-Gauss intermediates, factorization of the quadratic terms, and the o²v⁴ cost
summary: Projecting e^{−T}Ĥ_N e^{T}|Φ₀⟩ onto ⟨Φ₀|, ⟨Φ_i^a| and ⟨Φ_ij^ab| gives the CCSD energy E = Σf_ia t_i^a + ¼Σ⟨ij||ab⟩t_ij^ab + ½Σ⟨ij||ab⟩t_i^a t_j^b and two residual equations. The equations are written with the effective doubles τ and τ̃ and the Stanton-Gauss intermediates F_ae, F_mi, F_me, W_mnij, W_abef and W_mbej, in a general (possibly non-canonical) spin-orbital basis. Intermediates turn every quartic or o⁴v⁴-looking product into a sequence of contractions of cost at most o²v⁴, the particle-particle ladder. One detail is that the quadratic t·t·⟨mn||ef⟩ ladder term is split between W_mnij and W_abef, a factor ¼ in each. Implemented in 40 lines of NumPy, with DIIS, and checked against PySCF: water/6-31G correlation energy −0.1353794996 E_h, difference 2 × 10⁻¹¹, 15 iterations.
status: in-progress
kind: implementation
level: advanced
tags: [coupled-cluster, ccsd, spin-orbital, intermediates, stanton-gauss, implementation, diis, cost]
prerequisites: [coupled-cluster-second-quantization, normal-ordering-and-wicks-theorem]
related: [coupled-cluster-doubles, closed-shell-ccsd-t1-transformation, coupled-cluster-diagrams, coupled-cluster-hierarchy-and-size-extensivity, coupled-cluster-optimization-and-lagrangian, perturbative-triples-cc2-cc3]
also: []
date: 2026-11-07
---

## The equations to be solved

**Setup.** Notation as in [[normal-ordering-and-wicks-theorem]]: spin orbitals, $\langle pq||rs\rangle$ antisymmetrized physicists' integrals, Fock matrix $f_{pq}$ of the reference.

**Cluster operators.** $\hat T = \hat T_1 + \hat T_2$, with

$$
\hat T_1 = \sum_{ia}t_i^a\{a_a^\dagger a_i\},\qquad
\hat T_2 = \tfrac14\sum_{ijab}t_{ij}^{ab}\{a_a^\dagger a_b^\dagger a_j a_i\},\qquad t_{ij}^{ab}=-t_{ji}^{ab}=-t_{ij}^{ba}.
$$

**Projected equations.** With $\bar H = e^{-\hat T}\hat H_N e^{\hat T}$, which terminates after four commutators ([[coupled-cluster-second-quantization]]):

$$
E_{\text{CC}} = \langle\Phi_0|\bar H|\Phi_0\rangle,\qquad 0 = \langle\Phi_i^a|\bar H|\Phi_0\rangle,\qquad 0 = \langle\Phi_{ij}^{ab}|\bar H|\Phi_0\rangle .
$$

**Evaluation.** Each matrix element is evaluated with the generalized Wick theorem. Only fully contracted terms survive, and every $\hat T$ must be connected to $\hat H_N$.

**Energy.** Only $\hat F_N$ and $\hat V_N$ pieces with two or four quasi-annihilators can close against $\hat T_1$, $\hat T_2$ or $\tfrac12\hat T_1^2$:

$$
\boxed{E_{\text{CC}} = \sum_{ia}f_{ia}t_i^a + \tfrac14\sum_{ijab}\langle ij||ab\rangle t_{ij}^{ab} + \tfrac12\sum_{ijab}\langle ij||ab\rangle t_i^at_j^b .}
$$

The first term vanishes for canonical HF orbitals. The energy is exact once the singles and doubles amplitudes are, at any truncation level.

## Effective doubles and intermediates

**Notation.** $P(pq)X_{pq} = X_{pq} - X_{qp}$, $\delta$ is the Kronecker delta, and the energy denominators are

$$
D_i^a = f_{ii} - f_{aa},\qquad D_{ij}^{ab} = f_{ii}+f_{jj}-f_{aa}-f_{bb}.
$$

**Effective doubles.**

$$
\tau_{ij}^{ab} = t_{ij}^{ab} + t_i^at_j^b - t_i^bt_j^a,\qquad
\tilde\tau_{ij}^{ab} = t_{ij}^{ab} + \tfrac12\big(t_i^at_j^b - t_i^bt_j^a\big).
$$

$\tau$ is the full $\hat C_2 = \hat T_2 + \tfrac12\hat T_1^2$ amplitude. $\tilde\tau$ carries half the disconnected part, because the other half is supplied elsewhere in the same intermediate.

**One-particle intermediates.** Off-diagonal parts of $f$ only, because the diagonal is moved into $D$:

$$
\begin{aligned}
F_{ae} &= (1-\delta_{ae})f_{ae} - \tfrac12\sum_m f_{me}t_m^a + \sum_{mf}t_m^f\langle ma||fe\rangle - \tfrac12\sum_{mnf}\tilde\tau_{mn}^{af}\langle mn||ef\rangle,\\
F_{mi} &= (1-\delta_{mi})f_{mi} + \tfrac12\sum_e t_i^ef_{me} + \sum_{ne}t_n^e\langle mn||ie\rangle + \tfrac12\sum_{nef}\tilde\tau_{in}^{ef}\langle mn||ef\rangle,\\
F_{me} &= f_{me} + \sum_{nf}t_n^f\langle mn||ef\rangle .
\end{aligned}
$$

**Two-particle intermediates.**

$$
\begin{aligned}
W_{mnij} &= \langle mn||ij\rangle + P(ij)\sum_e t_j^e\langle mn||ie\rangle + \tfrac14\sum_{ef}\tau_{ij}^{ef}\langle mn||ef\rangle,\\
W_{abef} &= \langle ab||ef\rangle - P(ab)\sum_m t_m^b\langle am||ef\rangle + \tfrac14\sum_{mn}\tau_{mn}^{ab}\langle mn||ef\rangle,\\
W_{mbej} &= \langle mb||ej\rangle + \sum_f t_j^f\langle mb||ef\rangle - \sum_n t_n^b\langle mn||ej\rangle - \sum_{nf}\big(\tfrac12t_{jn}^{fb} + t_j^ft_n^b\big)\langle mn||ef\rangle .
\end{aligned}
$$

## The residual equations

**Singles.**

$$
\begin{aligned}
t_i^aD_i^a ={}& f_{ia} + \sum_e t_i^eF_{ae} - \sum_m t_m^aF_{mi} + \sum_{me}t_{im}^{ae}F_{me} - \sum_{nf}t_n^f\langle na||if\rangle\\
&- \tfrac12\sum_{mef}t_{im}^{ef}\langle ma||ef\rangle - \tfrac12\sum_{men}t_{mn}^{ae}\langle nm||ei\rangle .
\end{aligned}
$$

**Doubles.**

$$
\begin{aligned}
t_{ij}^{ab}D_{ij}^{ab} ={}& \langle ij||ab\rangle
+ P(ab)\sum_e t_{ij}^{ae}\Big(F_{be} - \tfrac12\sum_m t_m^bF_{me}\Big)
- P(ij)\sum_m t_{im}^{ab}\Big(F_{mj} + \tfrac12\sum_e t_j^eF_{me}\Big)\\
&+ \tfrac12\sum_{mn}\tau_{mn}^{ab}W_{mnij} + \tfrac12\sum_{ef}\tau_{ij}^{ef}W_{abef}
+ P(ij)P(ab)\sum_{me}\Big(t_{im}^{ae}W_{mbej} - t_i^et_m^a\langle mb||ej\rangle\Big)\\
&+ P(ij)\sum_e t_i^e\langle ab||ej\rangle - P(ab)\sum_m t_m^a\langle mb||ij\rangle .
\end{aligned}
$$

**Solving.** Divide by $D$, update, extrapolate with DIIS, and repeat ([[coupled-cluster-optimization-and-lagrangian]]). Setting $t_i^a=0$ everywhere reduces the doubles equation to the CCD equation of [[coupled-cluster-doubles]].

!!! note "Where the ¼ factors come from"
    **The term.** The doubles residual must contain the quadratic ladder term

    $$
    \tfrac14\sum_{mnef}\langle mn||ef\rangle\,\tau_{ij}^{ef}\tau_{mn}^{ab}.
    $$

    **How the intermediates share it.**

    - **$W_{mnij}$ route.** $\tfrac12\sum_{mn}\tau_{mn}^{ab}W_{mnij}$ with the $\tfrac14\tau\langle\,||\,\rangle$ part of $W_{mnij}$ supplies $\tfrac18$ of it.
    - **$W_{abef}$ route.** $\tfrac12\sum_{ef}\tau_{ij}^{ef}W_{abef}$ supplies the other $\tfrac18$.

    **Same pattern for the $F$ intermediates.**

    - Using $\tilde\tau$ (half the $\hat T_1^2$ part) inside $F_{ae}$ and $F_{mi}$, plus the explicit $-\tfrac12 t_m^bF_{me}$ and $+\tfrac12 t_j^eF_{me}$ corrections, gives each disconnected product with the right weight.
    - Getting one of these factors wrong double-counts terms. For water/6-31G (computed for this note), using $\tfrac12$ instead of $\tfrac14$ in $W_{abef}$ shifts the CCSD correlation energy by $-0.32$ m$E_h$.
    - Using $\tau$ instead of $\tilde\tau$ in the $F$ intermediates shifts it by only $-5\times10^{-7}\,E_h$, because $|t_1|$ is small here. That error would grow for systems with large singles.

## Cost

**Notation.** $o$ occupied and $v$ virtual spin orbitals.

| Step | Contraction | Scaling |
|---|---|---|
| $W_{abef}$, particle-particle ladder | $\tfrac12\sum_{ef}\tau_{ij}^{ef}W_{abef}$ | $o^2v^4$ |
| $W_{mbej}$ ring terms | $\sum_{me}t_{im}^{ae}W_{mbej}$ | $o^3v^3$ |
| $W_{mnij}$, hole-hole ladder | $\tfrac12\sum_{mn}\tau_{mn}^{ab}W_{mnij}$ | $o^4v^2$ |
| $F$ intermediates | $\sum\tilde\tau\langle\,||\,\rangle$ | $o^3v^2$, $o^2v^3$ |

**Why intermediates matter.** Written out without intermediates, the doubles equation has terms such as $\tfrac14\sum_{mnef}t_{ij}^{ef}t_{mn}^{ab}\langle mn||ef\rangle$. Evaluated naively, at fixed $ijab$, these cost $o^4v^4$. Factorized as $\sum_{mn}t_{mn}^{ab}\big(\sum_{ef}\langle mn||ef\rangle t_{ij}^{ef}\big)$, they cost two $o^4v^2$ steps. Intermediates do this factorization systematically.

**Overall scaling.** CCSD costs $O(N^6)$ per iteration, dominated by the $o^2v^4$ ladder when $v\gg o$. Storage is dominated by $\langle ab||cd\rangle$ ($v^4$), which production codes avoid storing in the MO basis by building the ladder term from AO integrals.

## Implementation and check

```python
import numpy as np
def ccsd_residuals(f, g, o, v, t1, t2):
    """spin-orbital CCSD residuals D*t_new (Stanton-Gauss intermediates); g = <pq||rs>"""
    fo, fv = np.diag(f)[o], np.diag(f)[v]
    fov = f[o, v]; foo = f[o, o] - np.diag(fo); fvv = f[v, v] - np.diag(fv)
    tt = np.einsum('ia,jb->ijab', t1, t1); tt = tt - tt.transpose(0, 1, 3, 2)
    tau, tau_t = t2 + tt, t2 + 0.5*tt
    Fae = fvv - 0.5*np.einsum('me,ma->ae', fov, t1) + np.einsum('mf,mafe->ae', t1, g[o,v,v,v]) \
          - 0.5*np.einsum('mnaf,mnef->ae', tau_t, g[o,o,v,v])
    Fmi = foo + 0.5*np.einsum('ie,me->mi', t1, fov) + np.einsum('ne,mnie->mi', t1, g[o,o,o,v]) \
          + 0.5*np.einsum('inef,mnef->mi', tau_t, g[o,o,v,v])
    Fme = fov + np.einsum('nf,mnef->me', t1, g[o,o,v,v])
    Wmnij = g[o,o,o,o] + np.einsum('je,mnie->mnij', t1, g[o,o,o,v]) - np.einsum('ie,mnje->mnij', t1, g[o,o,o,v]) \
            + 0.25*np.einsum('ijef,mnef->mnij', tau, g[o,o,v,v])
    Wabef = g[v,v,v,v] - np.einsum('mb,amef->abef', t1, g[v,o,v,v]) + np.einsum('ma,bmef->abef', t1, g[v,o,v,v]) \
            + 0.25*np.einsum('mnab,mnef->abef', tau, g[o,o,v,v])
    Wmbej = g[o,v,v,o] + np.einsum('jf,mbef->mbej', t1, g[o,v,v,v]) - np.einsum('nb,mnej->mbej', t1, g[o,o,v,o]) \
            - np.einsum('jnfb,mnef->mbej', 0.5*t2 + np.einsum('jf,nb->jnfb', t1, t1), g[o,o,v,v])
    r1 = fov + np.einsum('ie,ae->ia', t1, Fae) - np.einsum('ma,mi->ia', t1, Fmi) + np.einsum('imae,me->ia', t2, Fme) \
         - np.einsum('nf,naif->ia', t1, g[o,v,o,v]) - 0.5*np.einsum('imef,maef->ia', t2, g[o,v,v,v]) \
         - 0.5*np.einsum('mnae,nmei->ia', t2, g[o,o,v,o])
    x = np.einsum('ijae,be->ijab', t2, Fae - 0.5*np.einsum('mb,me->be', t1, Fme)); r2 = g[o,o,v,v] + x - x.transpose(0,1,3,2)
    x = np.einsum('imab,mj->ijab', t2, Fmi + 0.5*np.einsum('je,me->mj', t1, Fme)); r2 -= x - x.transpose(1,0,2,3)
    r2 += 0.5*np.einsum('mnab,mnij->ijab', tau, Wmnij) + 0.5*np.einsum('ijef,abef->ijab', tau, Wabef)
    x = np.einsum('imae,mbej->ijab', t2, Wmbej) - np.einsum('ie,ma,mbej->ijab', t1, t1, g[o,v,v,o])
    r2 += x - x.transpose(1,0,2,3) - x.transpose(0,1,3,2) + x.transpose(1,0,3,2)
    x = np.einsum('ie,abej->ijab', t1, g[v,v,v,o]); r2 += x - x.transpose(1,0,2,3)
    x = np.einsum('ma,mbij->ijab', t1, g[o,v,o,o]); r2 -= x - x.transpose(0,1,3,2)
    return r1, r2
```

!!! example "Water/6-31G, all electrons (computed for this note)"
    **Setup.** RHF orbitals were converted to 26 interleaved spin orbitals, with $\langle pq||rs\rangle$ built from the MO $(pq|rs)$. The amplitudes start from MP2, $t_{ij}^{ab}=\langle ij||ab\rangle/D_{ij}^{ab}$ and $t_i^a = f_{ia}/D_i^a = 0$, and are accelerated by DIIS on the joint $(t_1,t_2)$ vector (8 vectors).

    | Quantity | This code | PySCF `RCCSD` |
    |---|---:|---:|
    | $E_{\text{HF}}$ ($E_h$) | −75.9839744727 | −75.9839744727 |
    | $E_{\text{corr}}^{\text{CCSD}}$ ($E_h$) | −0.1353794996 | −0.1353794996 |
    | Difference | $2.4\times10^{-11}$ | |
    | Iterations to $10^{-11}$ | 15 | |

    The same converged amplitudes give $E_{(T)}$ equal to PySCF's to $2\times10^{-13}$ ([[perturbative-triples-cc2-cc3]]).

## Source

T. D. Crawford, *Coupled Cluster Theory*, ESQC 2026 lecture slides, part 1 ("The CCSD energy equation", "The CCSD amplitude equations", "A few observations") and part 2 ("Computational cost").

J. F. Stanton, J. Gauss, J. D. Watts and R. J. Bartlett, *J. Chem. Phys.* **94**, 4334 (1991), doi:10.1063/1.460620. These are the intermediates in the form used here.

T. D. Crawford and H. F. Schaefer, *Rev. Comput. Chem.* **14**, 33-136 (2000), doi:10.1002/9780470125915.ch2.

G. D. Purvis and R. J. Bartlett, *J. Chem. Phys.* **76**, 1910 (1982). This is the first CCSD implementation.

Equations written out from these sources in my notation and verified by implementation (`esqc/cc/ccsd_so.py`, `esqc/cc/run_ccsd.py`, PySCF 2.15). The code block above was itself re-run from this note's text and gives −0.1353794996 $E_h$.
