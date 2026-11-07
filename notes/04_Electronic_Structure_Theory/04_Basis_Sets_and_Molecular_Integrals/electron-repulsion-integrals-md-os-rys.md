---
id: electron-repulsion-integrals-md-os-rys
title: Coulomb and electron-repulsion integrals over Gaussians - the Boys function, McMurchie-Davidson Hermite integrals, Obara-Saika recurrences and Rys quadrature
summary: All Coulomb integrals over Gaussians reduce to the Boys function F_n(T). Evaluating it needs a Taylor expansion about tabulated points, downward recursion and the asymptotic formula; I implemented this to 3×10⁻¹⁵. Three schemes turn F_n into integrals over Cartesian Gaussians: McMurchie-Davidson (Hermite integrals R_tuv by recursion, then an E-coefficient transformation), Obara-Saika (vertical, electron-transfer and horizontal recurrences) and Rys quadrature (Gauss-Rys roots and weights from the Boys moments). I implemented all three; they agree with libcint to 1.1×10⁻¹⁴ over 153 random quartets with l ≤ 2. The note also covers the electrostatics of spherical Gaussians and HJO's cost comparison.
status: in-progress
kind: algorithm
level: advanced
tags: [electron-repulsion-integrals, boys-function, mcmurchie-davidson, obara-saika, rys-quadrature, hermite-coulomb-integrals, horizontal-recurrence, electron-transfer-recurrence, nuclear-attraction, incomplete-gamma-function]
prerequisites: [gaussian-overlap-distributions-and-one-electron-integrals, integral-notation]
related: [multipole-methods-and-integral-screening, solid-harmonics-angular-basis, scf-procedure]
order: 80
date: 2026-11-04
---

## Coulomb interactions of spherical Gaussians

**The basic charge distribution (HJO Sec. 9.7).** It is the normalized spherical Gaussian $\rho_p(\mathbf r) = (p/\pi)^{3/2}e^{-pr_P^2}$, the $s$-type overlap distribution of [[gaussian-overlap-distributions-and-one-electron-integrals]].

**Its potential and the repulsion of two such charges.**

$$
V_p(\mathbf r) = \frac{\operatorname{erf}(\sqrt p\,r_P)}{r_P},\qquad
\iint\frac{\rho_p(\mathbf r_1)\rho_q(\mathbf r_2)}{r_{12}}\,\mathrm d\mathbf r_1\mathrm d\mathbf r_2 = \frac{\operatorname{erf}\big(\sqrt\alpha\,R_{PQ}\big)}{R_{PQ}},\qquad \alpha = \frac{pq}{p+q}.
$$

**Interpretation.** At large distance both become point-charge interactions $1/R$. The nonclassical part decays as $\operatorname{erfc}$ ([[multipole-methods-and-integral-screening]]).

**Checks.**

- **Potential.** I compared it with radial quadrature at $r$ = 0.3, 1.0 and 2.5; it agrees to $10^{-10}$.
- **Repulsion.** For $p = 1.2$, $q = 0.5$ and $R = 1.7$ my MD code gives 0.498111972812, identical to the erf formula.

## The Boys function

**Definition and properties (HJO Eqs. 9.8.1-9.8.14).**

$$
F_n(x) = \int_0^1e^{-xt^2}t^{2n}\,\mathrm dt,\qquad
F_n(0) = \frac1{2n+1},\qquad \frac{\mathrm dF_n}{\mathrm dx} = -F_{n+1},\qquad
F_0(x) = \frac12\sqrt{\frac\pi x}\operatorname{erf}\sqrt x .
$$

**Large $x$.** $F_n(x)\approx\dfrac{(2n-1)!!}{2^{n+1}}\sqrt{\dfrac\pi{x^{2n+1}}}$ (9.8.9).

**Recursions.**

$$
F_{n+1}(x) = \frac{(2n+1)F_n(x) - e^{-x}}{2x},\qquad
F_n(x) = \frac{2xF_{n+1}(x) + e^{-x}}{2n+1}\quad(9.8.13,\ 9.8.14).
$$

Upward recursion subtracts nearly equal numbers at small $x$, so downward recursion is the stable choice. In terms of the incomplete gamma function, $F_n(x) = \gamma(n+\tfrac12, x)/(2x^{n+1/2})$.

**HJO's evaluation recipe (Sec. 9.8.2).**

- **Simple approximations fall short.** The asymptotic formula and a Taylor series about 0 each reach $10^{-10}$ only for $x>19.35$ and $x<0.18$ respectively.
- **What to use instead.**
  1. Tabulate $F_n$ at spacing 0.1.
  2. Expand about the nearest grid point, $F_n(x_t - \Delta x) = \sum_k F_{n+k}(x_t)\Delta x^k/k!$ (9.8.12). Six terms give errors below $10^{-14}$.
  3. Get the lower orders by downward recursion.
  4. For large $x$, use the asymptotic formula.

!!! example "Boys-function checks (computed for this note)"
    - **Thresholds.** The asymptotic $F_0$ has an error of $10^{-10}$ exactly at $x = 19.35$. The Taylor series about 0 through $k = 6$ reaches $10^{-10}$ at $x = 0.186$. Both are HJO's numbers.
    - **Asymptotics depend on $n$.** The relative error of the asymptotic $F_8$ is 0.38 at $x = 10$, $10^{-3}$ at 20 and $10^{-6}$ at 30. A switch-over point must depend on $n$ or be large. I used $x\ge30$ with upward recursion from the asymptotic $F_0$, where the neglected $e^{-x}$ terms are $<10^{-13}$.
    - **Accuracy of my implementation** (`boys_hjo`: grid 0-30, six Taylor terms, downward recursion): maximum absolute deviation from the incomplete-gamma value $3.2\times10^{-15}$ for $0\le x\le45$, $n\le12$.
    - **Identities.** The downward recursion, $F_0$ = erf form and $\mathrm dF_n/\mathrm dx = -F_{n+1}$ hold to $10^{-16}$, $2\times10^{-16}$ and $10^{-10}$ (finite differences).

## McMurchie-Davidson: Hermite Coulomb integrals

**Hermite Coulomb integrals (HJO Eqs. 9.9.9-9.9.20).**

$$
R_{tuv}(p,\mathbf R_{PC}) = \Big(\frac\partial{\partial P_x}\Big)^t\Big(\frac\partial{\partial P_y}\Big)^u\Big(\frac\partial{\partial P_z}\Big)^vF_0(pR_{PC}^2).
$$

They are generated from auxiliary integrals $R^n_{000} = (-2p)^nF_n(pR_{PC}^2)$ by

$$
R^n_{t+1,u,v} = tR^{n+1}_{t-1,u,v} + X_{PC}R^{n+1}_{tuv},
$$

and likewise for $u$ and $v$ with $Y_{PC}$, $Z_{PC}$. The targets are $R_{tuv} = R^0_{tuv}$.

**Integrals over Cartesian Gaussians.**

- **Nuclear attraction** (per nucleus, before multiplying by $-Z_C$): $V_{ab} = \dfrac{2\pi}p\sum_{tuv}E^{ab}_{tuv}R_{tuv}(p,\mathbf R_{PC})$.
- **Electron repulsion** (9.9.33), in chemists' notation ([[integral-notation]]):

$$
g_{abcd} = (ab|cd) = \frac{2\pi^{5/2}}{pq\sqrt{p+q}}\sum_{tuv}E^{ab}_{tuv}\sum_{\tau\nu\phi}(-1)^{\tau+\nu+\phi}E^{cd}_{\tau\nu\phi}\,R_{t+\tau,u+\nu,v+\phi}(\alpha,\mathbf R_{PQ}),
$$

with $E_{tuv} = E_tE_uE_v$ the products of the 1D Hermite coefficients.

**Where the time goes.** The Hermite-to-Cartesian transformation is the expensive step. HJO split it into two half-transformations (9.9.44-9.9.47) and do the second after contraction.

## Obara-Saika: vertical, electron-transfer and horizontal recurrences

**Vertical recurrence (HJO 9.10.24-9.10.25).** Write $\Theta^N_{ijkl}$ for the $x$-dependent part of the auxiliary integrals, with $W = (p\mathbf P + q\mathbf Q)/(p+q)$, so that $W_x - P_x = -(\alpha/p)X_{PQ}$:

$$
\Theta^N_{i+1,j,k,l} = X_{PA}\Theta^N_{ijkl} - \frac\alpha pX_{PQ}\Theta^{N+1}_{ijkl}
+ \frac i{2p}\Big(\Theta^N_{i-1,j,k,l} - \frac\alpha p\Theta^{N+1}_{i-1,j,k,l}\Big)
+ \frac j{2p}\Big(\Theta^N_{i,j-1,k,l} - \frac\alpha p\Theta^{N+1}_{i,j-1,k,l}\Big)
+ \frac k{2(p+q)}\Theta^{N+1}_{i,j,k-1,l} + \frac l{2(p+q)}\Theta^{N+1}_{i,j,k,l-1},
$$

starting from $\Theta^N_{0000} = \frac{2\pi^{5/2}}{pq\sqrt{p+q}}K^{ab}K^{cd}F_N(\alpha R_{PQ}^2)$.

**Cheaper three-step path (Sec. 9.10.3).**

1. **Build $(e0|00)$** with the four-term special case of the vertical recurrence.
2. **Electron transfer** (9.10.27), from translational invariance:

$$
e_{i,0,k+1,0} = -\frac{bX_{AB} + dX_{CD}}q\,e_{i0k0} + \frac i{2q}e_{i-1,0,k,0} + \frac k{2q}e_{i,0,k-1,0} - \frac pq\,e_{i+1,0,k,0}.
$$

3. **Horizontal recurrences** (9.10.28-9.10.29):

$$
e_{i,j+1,k,l} = e_{i+1,j,k,l} + X_{AB}e_{ijkl},\qquad e_{i,j,k,l+1} = e_{i,j,k+1,l} + X_{CD}e_{ijkl} .
$$

The horizontal step contains no exponents, so it is done **after contraction**. This is the main reason the OS1/OS2 variants are fast.

## Rys quadrature

**Idea (HJO Sec. 9.11).** Substitute the Boys integral into $R_{tuv}$:

$$
R_{tuv} = \int_0^1\bar H_t(s^2)\bar H_u(s^2)\bar H_v(s^2)\,e^{-pR_{PC}^2s^2}\,\mathrm ds .
$$

- **Why quadrature is exact.** The $\bar H_t$ are polynomials of degree $t$ in $s^2$. Gaussian quadrature with weight $e^{-Ts^2}$ on $[0,1]$ (Gauss-Rys) is therefore exact with $\gamma = \lfloor(t+u+v)/2\rfloor + 1$ points (9.11.32-9.11.33), where $T = pR_{PC}^2$.
- **The polynomials** follow from $\bar H_0 = 1$ and (9.11.36):

$$
\bar H_{t+1}(s^2) = -2ps^2\big[X_{PC}\bar H_t(s^2) + t\bar H_{t-1}(s^2)\big].
$$

- **Two electrons.** The same holds with $p\to\alpha$ and $C\to Q$ (9.11.38-9.11.39).

**Roots and weights from the Boys function.** The moments of the weight in $x = s^2$ are exactly the Boys functions:

$$
\int_0^1x^ke^{-Tx}\,\mathrm ds = F_k(T).
$$

I built the three-term recurrence of the orthogonal polynomials from a Cholesky factorization of the Hankel moment matrix (Golub-Welsch), then diagonalized the Jacobi matrix. This is numerically fine for the few roots needed here. Production codes use fitted polynomials instead.

## Checks of my implementation

!!! example "Own ERI code versus libcint (computed for this note)"
    **Test set.** The 13 Cartesian functions of the one-electron test ($s$, $p$, $d$, $p$ on four non-symmetric centres), with 153 quartets ($ab|cd$) (150 random plus three chosen ones), compared with PySCF `int2e_cart` after per-function rescaling:

    | Scheme | Max deviation |
    |---|---:|
    | McMurchie-Davidson ($E$ coefficients + $R_{tuv}$ recursion) | $1.1\times10^{-14}$ |
    | Obara-Saika (vertical + horizontal, memoized) | $1.1\times10^{-14}$ |
    | Rys quadrature for $R_{tuv}$ inside MD | $1.1\times10^{-14}$ |

    - **Recurrence checks.** I verified the electron-transfer relation (9.10.27) to $2\times10^{-16}$ on $(i0|k0)$ $x$-integrals with $i, k\le2$. Both horizontal relations (9.10.28-9.10.29) are exact (zero difference).
    - **Rys roots at $T = 2.5$, three points.** $s_k^2$ = 0.040626, 0.347820, 0.815246 with weights 0.362303, 0.153765, 0.030224. They reproduce $F_0,\dots,F_5$ exactly, as a three-point rule must.

```python
def R_herm(tmax, p, PC):            # Hermite Coulomb integrals R^0_tuv, HJO (9.9.18)-(9.9.20)
    T = p*np.dot(PC, PC); Fn = [boys_exact(n, T) for n in range(3*tmax + 1)]; R = {}
    def r(t, u, v, n):
        if t < 0 or u < 0 or v < 0: return 0.0
        if (t, u, v, n) in R: return R[t, u, v, n]
        if t == u == v == 0: val = (-2*p)**n*Fn[n]
        elif t > 0: val = (t-1)*r(t-2, u, v, n+1) + PC[0]*r(t-1, u, v, n+1)
        elif u > 0: val = (u-1)*r(t, u-2, v, n+1) + PC[1]*r(t, u-1, v, n+1)
        else:       val = (v-1)*r(t, u, v-2, n+1) + PC[2]*r(t, u, v-1, n+1)
        R[t, u, v, n] = val; return val
    return r
```

## Which scheme? (HJO Secs. 9.9.6, 9.10.4 and 9.11.7, quoted)

**Notation.** HJO tabulate costs in terms of $L$ (angular momentum) and $p$ (primitives per contracted function).

- **Variants with electron transfer.** MD1, OS1 and R1 scale alike: dominated by the transfer step ($L^6p^4$) and the horizontal step ($L^9$). They are preferred for high angular momentum, OS in particular because it has fewer steps.
- **Vertical-horizontal variants.** MD2, OS2 and R2 perform similarly.
- **Variants without either.** These cost about $L^{10}p^4$ or $L^8p^4$ (MD4), $L^9p^4$ (R4) and $L^{13}p^4$ (OS4, the least favourable).
- **Practical rule.** Put exponent-dependent work before contraction and exponent-free work after it. MD's Hermite form also gives field and field-gradient integrals almost free.

## Source

Helgaker, Jørgensen and Olsen, *Molecular Electronic-Structure Theory* (Wiley, Chichester, 2000), Secs. 9.7-9.11, pp. 361-398, Eqs. (9.7.1)-(9.11.65), Tables 9.2-9.6. Equations read from the text extraction and page images. Implementation (`ints.py`: `boys_hjo`, `R_herm`, `eri_md`, `eri_os`, `rys_roots`, `R_rys`) and all checks against PySCF 2.14/libcint done for this note. The cost scalings are quoted from HJO.
