---
id: coupled-cluster-doubles
title: Coupled-cluster doubles (CCD) from the full CI hierarchy
summary: CCD (Szabo's CCA) closes the full CI hierarchy by writing quadruple coefficients as antisymmetrized products of doubles. It is exact for any number of noninteracting two-electron fragments, its wave function is exp(T2)|Ψ0⟩, and its amplitude equations are quadratic. Derivation for N separated H2 molecules, the cluster form, the spin-orbital working equations with intermediates, and computed checks.
status: in-progress
kind: derivation
level: intermediate
tags: [ccd, coupled-cluster, cluster-expansion, exponential-ansatz, cpmet, size-consistency]
prerequisites: [coupled-pair-approximations, creation-and-annihilation-operators, size-consistency]
related: [coupled-cluster-second-quantization, iepa, one-particle-hamiltonian-models, mp3]
order: 30
date: 2026-11-03
---

## The idea in one line

Approximate every coefficient of a quadruple excitation by the antisymmetrized sum of products of doubles coefficients, $c_{abcd}^{rstu}\approx c_{ab}^{rs}*c_{cd}^{tu}$. The full derivation of the resulting equation, and its place among DCI, L-CCD and CEPA, is in [[coupled-pair-approximations]]. This note works out what the approximation means and shows that it is the same as an exponential wave function.

## Exact for N separated H₂ molecules

**Setup.** $N$ minimal-basis H$_2$ molecules, all integrals between different molecules zero ([[size-consistency]]). Each local double $|\Psi_{1_i\bar1_i}^{2_i\bar2_i}\rangle$ has coefficient $c$ (all equal by symmetry) and couples to $|\Psi_0\rangle$ with $K_{12}$.

**Energy equation.** ${}^NE_{\text{corr}} = NcK_{12}$.

**Doubles equation.** A given local double mixes with $|\Psi_0\rangle$ (element $K_{12}$), with itself (diagonal $2\Delta$), and with the $N-1$ quadruples in which another molecule is also excited (element $K_{12}$ each, coefficient $c^2$ in CCA):

$$
K_{12} + 2\Delta c + (N-1)K_{12}c^2 = {}^NE_{\text{corr}}\,c = NK_{12}c^2 .
$$

The $N$-dependent terms cancel, leaving the monomer equation

$$
K_{12} + 2\Delta c - K_{12}c^2 = 0
\quad\Longrightarrow\quad
c = \frac{\Delta - (\Delta^2 + K_{12}^2)^{1/2}}{K_{12}},
\qquad
{}^NE_{\text{corr}}(\text{CCA}) = N\Big(\Delta - (\Delta^2 + K_{12}^2)^{1/2}\Big).
$$

CCA is exact for every $N$. DCI gives $\sqrt N$ behaviour and DQCI is exact only for $N = 2$.

**Why it works.** By approximating quadruples as products of doubles, the hextuple coefficients are implicitly cubes, the octuples fourth powers, and so on. In this model all higher coefficients are exactly such products, so nothing is lost. The cancellation of the $N^2$-type term between the two sides is the algebraic origin of size consistency; it is the same cancellation as in perturbation theory ([[linked-cluster-theorem]]).

## The cluster form of the wave function

**Doubles operator.** With $|\Psi_{ab}^{rs}\rangle = a_r^\dagger a_s^\dagger a_b a_a|\Psi_0\rangle$ ([[creation-and-annihilation-operators]]),

$$
\hat T_2 = \frac14\sum_{abrs} c_{ab}^{rs}\,a_r^\dagger a_s^\dagger a_b a_a,
\qquad
|\Phi_{\text{CCA}}\rangle = e^{\hat T_2}|\Psi_0\rangle = \Big(1 + \hat T_2 + \tfrac12\hat T_2^2 + \cdots\Big)|\Psi_0\rangle .
$$

**Expansion.** All the excitation operators commute. $\tfrac12\hat T_2^2$ produces every quadruple in many ways; collecting the terms, with the anticommutation signs, gives

$$
e^{\hat T_2}|\Psi_0\rangle = |\Psi_0\rangle + \sum_{a<b,\,r<s} c_{ab}^{rs}|\Psi_{ab}^{rs}\rangle + \sum_{\substack{a<b<c<d\\ r<s<t<u}} c_{ab}^{rs}*c_{cd}^{tu}\,|\Psi_{abcd}^{rstu}\rangle + \cdots ,
$$

with exactly the 18-term product of Szabo Eq. (5.53). The exponential is the compact way of writing "every higher excitation is a sum of products of doubles".

**Equivalent derivation.** Insert $e^{\hat T_2}|\Psi_0\rangle$ into $(H - E_0)|\Phi\rangle = E_{\text{corr}}|\Phi\rangle$ and project on $\langle\Psi_0|$ and $\langle\Psi_{ab}^{rs}|$. Because a double cannot couple to a hextuple, only the doubles and quadruples terms survive and the CCA equations are recovered.

**Extensions.** Replacing $\hat T_2$ by $\hat T_1 + \hat T_2$ with $\hat T_1 = \sum_{ar}c_a^r a_r^\dagger a_a$ gives CCSD. The second-quantized treatment of the general $e^{\hat T}$ ansatz, including why the similarity-transformed Hamiltonian terminates, is in [[coupled-cluster-second-quantization]].

!!! example "Two separated H₂ molecules as an exponential (Szabo Ex. 5.11)"
    With $c$ the monomer doubles coefficient, the exact dimer wave function is

    $$
    |\Phi_0\rangle = \exp\Big(c\,a_{2_1}^\dagger a_{\bar2_1}^\dagger a_{\bar1_1}a_{1_1} + c\,a_{2_2}^\dagger a_{\bar2_2}^\dagger a_{\bar1_2}a_{1_2}\Big)|1_1\bar1_1 1_2\bar1_2\rangle .
    $$

    The two operators commute and each squares to zero (an orbital cannot be emptied twice), so the exponential factorizes into $(1 + c\,\hat\tau_1)(1 + c\,\hat\tau_2)$. That produces $|\Psi_0\rangle$, both local doubles with coefficient $c$, and the quadruple with coefficient $c^2$: the full CI result.

    **Numbers (STO-3G, R = 1.4 bohr).** $c = -0.11344$. The CCD code below gives −0.041123 hartree for the dimer in both localized and delocalized orbitals, twice the monomer full CI −0.020562. Computed for this note.

## Working equations

**Spin-orbital CCD residual.** With $t_{ij}^{ab}\equiv c_{ij}^{ab}$, occupied $i,j,k,l$, virtual $a,b,c,d$ and canonical Hartree-Fock orbitals, the amplitude equation is (general knowledge; the standard form of Stanton and Gauss with $\hat T_1 = 0$, consistent with J-S Eq. 4.19)

$$
D_{ij}^{ab}t_{ij}^{ab} = \langle ij||ab\rangle + P(ab)\sum_e t_{ij}^{ae}F_{be} - P(ij)\sum_m t_{im}^{ab}F_{mj} + \tfrac12\sum_{mn}t_{mn}^{ab}W_{mnij} + \tfrac12\sum_{ef}t_{ij}^{ef}W_{abef} + P(ij)P(ab)\sum_{me}t_{im}^{ae}W_{mbej},
$$

with $D_{ij}^{ab} = \varepsilon_i + \varepsilon_j - \varepsilon_a - \varepsilon_b$, $P(ij)f(i,j) = f(i,j) - f(j,i)$, and intermediates

$$
F_{ae} = -\tfrac12\sum_{mnf}t_{mn}^{af}\langle mn||ef\rangle, \quad
F_{mi} = \tfrac12\sum_{nef}t_{in}^{ef}\langle mn||ef\rangle,
$$

$$
W_{mnij} = \langle mn||ij\rangle + \tfrac14\sum_{ef}t_{ij}^{ef}\langle mn||ef\rangle,\quad
W_{abef} = \langle ab||ef\rangle + \tfrac14\sum_{mn}t_{mn}^{ab}\langle mn||ef\rangle,\quad
W_{mbej} = \langle mb||ej\rangle - \tfrac12\sum_{nf}t_{jn}^{fb}\langle mn||ef\rangle .
$$

The energy is $E_{\text{corr}} = \tfrac14\sum_{ijab}\langle ij||ab\rangle t_{ij}^{ab}$. Dropping every term with two amplitudes gives L-CCD; the remaining linear terms are those of [[coupled-pair-approximations]].

**Cost.** The $\tfrac12\sum_{ef}t_{ij}^{ef}W_{abef}$ term scales as $o^2v^4$ and dominates for large basis sets.

```python
def R_ccd(d, t):                       # returns D*t_new; t_new = R_ccd(t) / D
    oovv = d.oovv
    Fae = -0.5 * np.einsum("mnaf,mnef->ae", t, oovv)
    Fmi =  0.5 * np.einsum("inef,mnef->mi", t, oovv)
    Wmnij = d.oooo + 0.25 * np.einsum("ijef,mnef->mnij", t, oovv)
    Wabef = d.vvvv + 0.25 * np.einsum("mnab,mnef->abef", t, oovv)
    Wmbej = d.ovvo - 0.5 * np.einsum("jnfb,mnef->mbej", t, oovv)
    r = oovv.copy()
    x = np.einsum("ijae,be->ijab", t, Fae);  r += x - x.transpose(0, 1, 3, 2)
    x = -np.einsum("imab,mj->ijab", t, Fmi); r += x - x.transpose(1, 0, 2, 3)
    r += 0.5 * np.einsum("mnab,mnij->ijab", t, Wmnij) + 0.5 * np.einsum("ijef,abef->ijab", t, Wabef)
    r += P_ijab(np.einsum("imae,mbej->ijab", t, Wmbej))
    return r
```

!!! example "Checks (computed for this note)"
    - **Water, STO-3G**, Szabo geometry: CCD −0.049122 hartree, identical to PySCF's independent CCD code. Full CI is −0.049486.
    - **Water, 6-31G:** CCD −0.134648 against full CI −0.136848.
    - **A first version** of the quadratic terms written directly from the 18-term product disagreed with PySCF (−0.04699); rewriting with the intermediates above fixed it. Sign bookkeeping in the product term is the usual source of error.

## What CCD does not include

- **Singles.** With Hartree-Fock orbitals $\hat T_1$ enters the energy only indirectly; CCSD adds it (−0.049369 versus CCD −0.049122 for STO-3G water).
- **Connected triples and quadruples.** $\hat T_3$ first contributes at fourth order and $\hat T_4$ at fifth order of perturbation theory ([[coupled-cluster-second-quantization]]).
- **Variationality.** The CCD energy is a projected energy, not an expectation value. It can lie below full CI, though it did not in the cases above.

## Source

Szabo and Ostlund, *Modern Quantum Chemistry* (Dover, 1996; reprint of the revised first edition, McGraw-Hill, 1989), Sec. 5.2.1-5.2.2, pp. 287-291, Eqs. (5.49)-(5.62), Ex. 5.11. Spin-orbital working equations: general knowledge in the Stanton-Gauss intermediate form (not from Szabo); their T2-only content corresponds to Jørgensen and Simons, *Second Quantization-Based Methods in Quantum Chemistry* (Academic Press, New York, 1981), Ch. 4, Eq. (4.19), p. 95. Numbers computed for this note with PySCF 2.14.
