---
id: rotational-selection-rules-and-wigner-eckart
title: Rotational selection rules for scalar and vector operators (Wigner–Eckart theorem)
summary: Sandwiching the commutators of a scalar with L̂ between |nℓm⟩ states gives Δℓ = Δm = 0 and m-independent matrix elements, ⟨n'ℓ'm'|f|nℓm⟩ = δ δ ⟨n'ℓ‖f‖nℓ⟩. The vector-operator commutators give Δℓ = 0, ±1 and Δm = 0, ±1, with all components fixed by Clebsch–Gordan coefficients and one reduced matrix element. Hydrogen checks: ⟨r²⟩ = 42a² (2s) and 30a² (2p), ⟨r⟩ = 5a for the 2p superposition, and all 45 elements ⟨32m'|r_i|21m⟩ from the single integral ⟨320|z|210⟩ = 2¹²3³√3 a/5⁷.
status: in-progress
kind: derivation
level: intermediate
tags: [wigner-eckart-theorem, selection-rules, reduced-matrix-element, scalar-operator, vector-operator, spherical-tensor-operators, clebsch-gordan, dipole-transitions, hydrogen, griffiths]
prerequisites: [rotation-operator-and-rotational-symmetry, addition-of-angular-momenta]
related: [parity-and-parity-selection-rules, hydrogen-atom, orbital-angular-momentum, spin-tensor-operators, symmetry-conservation-and-degeneracy]
order: 50
date: 2026-11-05
---

## Setting

**States.** $|n\ell m\rangle$ is any state with $\hat L^2|n\ell m\rangle = \ell(\ell+1)\hbar^2|n\ell m\rangle$ and $\hat L_z|n\ell m\rangle = m\hbar|n\ell m\rangle$. The label $n$ stands for everything else; the states need not be eigenstates of any Hamiltonian. The ladder coefficients are

$$
\hat L_\pm|n\ell m\rangle = A^{m}_{\ell,\pm}|n\ell,m\pm1\rangle,\qquad
A^m_\ell = \hbar\sqrt{\ell(\ell+1)-m(m+1)},\quad B^m_\ell = \hbar\sqrt{\ell(\ell+1)-m(m-1)},
$$

with $A$ for raising and $B$ for lowering, and $\langle\psi|\hat L_\pm\phi\rangle = \langle\hat L_\mp\psi|\phi\rangle$.

**Scope.** Only rotation properties are used, so the results hold for true scalars and pseudoscalars alike, and for true vectors and pseudovectors alike. Parity adds further restrictions ([[parity-and-parity-selection-rules]]).

## Scalar operators

**Commutators.** A scalar satisfies $[\hat L_z,\hat f] = [\hat L_\pm,\hat f] = [\hat L^2,\hat f] = 0$ ([[rotation-operator-and-rotational-symmetry]]).

**Selection rules.** Sandwich between $\langle n'\ell'm'|$ and $|n\ell m\rangle$ and let $\hat L_z$, $\hat L^2$ act on whichever side they face:

$$
(m'-m)\langle n'\ell'm'|\hat f|n\ell m\rangle = 0,\qquad
[\ell'(\ell'+1)-\ell(\ell+1)]\langle n'\ell'm'|\hat f|n\ell m\rangle = 0 .
$$

Since $\ell,\ell'\ge0$, the second bracket vanishes only for $\ell' = \ell$. So $\Delta\ell = \Delta m = 0$.

**$m$-independence.** From $[\hat L_+,\hat f] = 0$:

$$
B^{m'}_{\ell'}\langle n'\ell'(m'-1)|\hat f|n\ell m\rangle - A^m_\ell\langle n'\ell'm'|\hat f|n\ell(m+1)\rangle = 0 .
$$

Both terms are zero unless $m' = m+1$ and $\ell' = \ell$, and then $B^{m+1}_\ell = A^m_\ell\neq0$. Hence $\langle n'\ell m|\hat f|n\ell m\rangle = \langle n'\ell(m+1)|\hat f|n\ell(m+1)\rangle$. The $\hat L_-$ commutator gives the same rule (Problem 6.20). Summary:

$$
\langle n'\ell'm'|\hat f|n\ell m\rangle = \delta_{\ell\ell'}\,\delta_{mm'}\,\langle n'\ell\|f\|n\ell\rangle .
$$

The double-bar **reduced matrix element** depends on $n$, $n'$, $\ell$ but not on $m$.

!!! example "Expectation values of r² and r in hydrogen n = 2 (Example 6.4, Problem 6.21)"
    **Units.** Exact SymPy integrals, $a$ = Bohr radius.

    **$\langle r^2\rangle$.** One integral per $\ell$ suffices:

    $$
    \langle20\|r^2\|20\rangle = \int_0^\infty r^4R_{20}^2\,dr = 42a^2,\qquad
    \langle21\|r^2\|21\rangle = \int_0^\infty r^4R_{21}^2\,dr = 30a^2 .
    $$

    Computing all three $m$ values of $\ell = 1$ directly gives $30a^2$ each.

    **Superposition.** For $\psi = (|200\rangle - i|211\rangle)/\sqrt2$, the cross terms vanish because $\Delta\ell\neq0$ (verified: $\langle200|r^2|211\rangle = 0$), so

    $$
    \langle r^2\rangle = \tfrac12(42+30)a^2 = 36a^2 .
    $$

    **Problem 6.21.** For $\psi = (\psi_{211}+\psi_{21-1})/\sqrt2$, $\hat r$ is a scalar. The cross terms have $\Delta m = 2$ and vanish (checked), so

    $$
    \langle r\rangle = \langle21\|r\|21\rangle = 5a .
    $$

## Vector operators

**Commutators.** With $\hat V_\pm = \hat V_x\pm i\hat V_y$ (all signs verified in [[rotation-operator-and-rotational-symmetry]]):

$$
[\hat L_z,\hat V_z] = 0,\quad [\hat L_z,\hat V_\pm] = \pm\hbar\hat V_\pm,\quad [\hat L_\pm,\hat V_\pm] = 0,\quad [\hat L_\pm,\hat V_z] = \mp\hbar\hat V_\pm,\quad [\hat L_\pm,\hat V_\mp] = \pm2\hbar\hat V_z .
$$

**$m$ rules.** Sandwiching $[\hat L_z,\hat V_\pm] = \pm\hbar\hat V_\pm$ gives $[m'-(m\pm1)]\langle n'\ell'm'|\hat V_\pm|n\ell m\rangle = 0$. Hence:

- $\hat V_+$ requires $m' = m+1$;
- $\hat V_z$ requires $m' = m$;
- $\hat V_-$ requires $m' = m-1$.

$\hat V_x$ and $\hat V_y$ are half-sums and half-differences of $\hat V_\pm$, so they connect $m'=m\pm1$ only.

**Full result (Wigner–Eckart for rank 1).** The remaining commutators fix the relative sizes of all nonzero elements (Problem 6.24). They are proportional to Clebsch–Gordan coefficients $C^{j_1j_2J}_{m_1m_2M} = \langle j_1m_1;j_2m_2|JM\rangle$ ([[addition-of-angular-momenta]]):

$$
\langle n'\ell'm'|\hat V_+|n\ell m\rangle = -\sqrt2\,C^{\ell1\ell'}_{m\,1\,m'}\langle n'\ell'\|V\|n\ell\rangle,
$$

$$
\langle n'\ell'm'|\hat V_-|n\ell m\rangle = \sqrt2\,C^{\ell1\ell'}_{m\,-1\,m'}\langle n'\ell'\|V\|n\ell\rangle,
$$

$$
\langle n'\ell'm'|\hat V_z|n\ell m\rangle = C^{\ell1\ell'}_{m\,0\,m'}\langle n'\ell'\|V\|n\ell\rangle .
$$

Clebsch–Gordan coefficients vanish unless $M = m_1+m_2$ and $|j_1-j_2|\le J\le j_1+j_2$, so

$$
\Delta\ell = 0,\pm1,\qquad \Delta m = 0,\pm1 .
$$

Combined with Laporte's rule for a true vector such as $\hat{\mathbf r}$, $\Delta\ell = 0$ is excluded and electric-dipole transitions obey $\Delta\ell = \pm1$.

**Why Clebsch–Gordan coefficients appear.** A vector operator carries angular momentum 1: its three spherical components $\hat V_{+1} = -\hat V_+/\sqrt2$, $\hat V_0 = \hat V_z$ and $\hat V_{-1} = \hat V_-/\sqrt2$ rotate into each other like $|1\,q\rangle$. Acting with $\hat V_q$ on $|\ell m\rangle$ couples $\ell\otimes1$. In this language the three formulas collapse to one:

$$
\langle n'\ell'm'|\hat V_q|n\ell m\rangle = C^{\ell1\ell'}_{m\,q\,m'}\langle n'\ell'\|V\|n\ell\rangle .
$$

A scalar is the rank-0 case, and the hierarchy continues to rank-2 tensors (quadrupoles).

**Conventions.** Griffiths' reduced matrix element absorbs all normalization. Other texts (Sakurai, for instance) divide by $\sqrt{2\ell'+1}$ or $\sqrt{2\ell+1}$ and use $\langle\ell m;1q|\ell'm'\rangle$ in the same role. The selection rules are identical, but the numerical values of reduced elements differ between books; check the convention before mixing tables. Note also that the scalar $\hat r$ and the vector $\hat{\mathbf r}$ have different reduced elements despite the shared symbol.

!!! example "All 45 elements ⟨32m'|r_i|21m⟩ in hydrogen (Example 6.5)"
    **One integral.** The angular part reduces to $\int Y_2^{0*}\cos\theta\,Y_1^0\,d\Omega$:

    $$
    \langle320|z|210\rangle = \int_0^\infty R_{32}\,r\,R_{21}\,r^2dr\int Y_2^{0*}\cos\theta\,Y_1^0\,d\Omega
    $$

    $$
    = \frac{2^{12}\,3^3\sqrt3}{5^7}\,a = 2.45185\,a .
    $$

    **Reduced element.** With $C^{112}_{000} = \sqrt{2/3}$,

    $$
    \langle32\|V\|21\rangle = \frac{2^{12}3^4}{5^7\sqrt2}\,a = 3.00289\,a .
    $$

    **The nine nonzero elements** (abbreviating the reduced element as $R$):

    | Element | Value | | Element | Value |
    |---|---|---|---|---|
    | $\langle322\lvert V_+\rvert211\rangle$ | $-\sqrt2R$ | | $\langle32,-1\lvert V_-\rvert210\rangle$ | $R$ |
    | $\langle321\lvert V_+\rvert210\rangle$ | $-R$ | | $\langle32,-2\lvert V_-\rvert21,-1\rangle$ | $\sqrt2R$ |
    | $\langle320\lvert V_+\rvert21,-1\rangle$ | $-R/\sqrt3$ | | $\langle321\lvert V_z\rvert211\rangle$ | $R/\sqrt2$ |
    | $\langle320\lvert V_-\rvert211\rangle$ | $R/\sqrt3$ | | $\langle320\lvert V_z\rvert210\rangle$ | $\sqrt{2/3}\,R$ |
    | | | | $\langle32,-1\lvert V_z\rvert21,-1\rangle$ | $R/\sqrt2$ |

    **Check.** All $3\times5\times3 = 45$ matrix elements of $V_+$, $V_-$, $V_z$ (with $\hat{\mathbf V} = \hat{\mathbf r}$) were integrated exactly with SymPy and compared with the formulas above, using `sympy.physics.quantum.cg`. There are exactly 9 nonzero elements and 0 mismatches. The value of $\langle320|z|210\rangle$ and the reduced element both agree with Griffiths in closed form.

## Source

Griffiths and Schroeter, *Introduction to Quantum Mechanics* (3rd ed., Cambridge University Press, 2018), Sec. 6.7 (6.7.1–6.7.2), Eqs. (6.40)–(6.66), Examples 6.4–6.5, Fig. 6.8 (the $1\otimes1$ Clebsch–Gordan table, used via SymPy); Problems 6.20–6.24. Page numbers are not given because the PDF used is an e-book rendering without print pagination. All integrals and the 45-element comparison are computed in `griffiths/ch06_symmetry.py` (section F). The spherical-component form is from Griffiths' footnotes. The remark on other books' normalizations of the reduced element is from memory of the standard convention and should be checked against Sakurai before use (to verify).
