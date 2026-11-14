"""Check H = E_HF + F_N + V_N (normal ordering relative to the HF Fermi vacuum) and Wick's theorem, LiH/STO-3G."""
import numpy as np, scipy.sparse as sp, itertools
from pyscf import gto
from fermi import jw_ops, basis_index, spin_orbital_integrals, hamiltonian_matrix
mol = gto.M(atom='Li 0 0 0; H 0 0 1.6', basis='sto-3g', verbose=0)
h, g, no, enuc, mf = spin_orbital_integrals(mol)
n = h.shape[0]; ops = jw_ops(n); ad = [o.T.tocsr() for o in ops]
occ = np.arange(n) < no
H = hamiltonian_matrix(h, g, ops)
ref = basis_index(range(no), n)
E_HF = H[ref, ref]
f = h + np.einsum('piqi->pq', g[:, occ][:, :, :, occ])
print("E_HF (matrix) + Vnn =", E_HF + enuc, "  PySCF:", mf.e_tot)
print("E_HF = sum h_ii + 1/2 sum <ij||ij> :", np.trace(h[np.ix_(occ, occ)]) + 0.5*np.einsum('ijij', g[np.ix_(occ, occ, occ, occ)]) - E_HF)

def normal_order(string):
    """string: list of (p, dagger). Returns (sign, reordered string) with quasi-creators first, relative to HF."""
    qc = [(k, op) for k, op in enumerate(string) if (op[1] and not occ[op[0]]) or ((not op[1]) and occ[op[0]])]
    qa = [(k, op) for k, op in enumerate(string) if (k, op) not in qc]
    perm = [k for k, _ in qc] + [k for k, _ in qa]
    sign = 1
    p = list(perm)
    for i in range(len(p)):            # parity by bubble sort
        for j in range(len(p)-1-i):
            if p[j] > p[j+1]: p[j], p[j+1] = p[j+1], p[j]; sign = -sign
    return sign, [op for _, op in qc] + [op for _, op in qa]

def mat(string):
    M = sp.identity(2**n, format='csr')
    for p, dag in string: M = M @ (ad[p] if dag else ops[p])
    return M

def nmat(string):
    s, st = normal_order(string); return s * mat(st)

# F_N and V_N built from explicit normal-ordered strings
FN = sp.csr_matrix((2**n, 2**n)); VN = sp.csr_matrix((2**n, 2**n))
for p, q in itertools.product(range(n), repeat=2):
    if abs(f[p, q]) > 1e-14: FN = FN + f[p, q]*nmat([(p, 1), (q, 0)])
for p, q, r, s in itertools.product(range(n), repeat=4):
    if p < q and r < s and abs(g[p, q, r, s]) > 1e-14:
        VN = VN + g[p, q, r, s]*nmat([(p, 1), (q, 1), (s, 0), (r, 0)])
D = H - E_HF*sp.identity(2**n) - FN - VN
print("max |H - E_HF - F_N - V_N| over the whole Fock space:", abs(D).max())
print("<HF|F_N|HF>, <HF|V_N|HF> =", FN[ref, ref], VN[ref, ref])
# Wick: a_p^+ a_q^+ a_s a_r = {pqsr} + sum single contractions {..} + full contractions, checked for random index sets
rng = np.random.default_rng(1); worst = 0
def contr(x, y):   # contraction of x (left) with y (right) relative to HF vacuum
    (p, dp), (q, dq) = x, y
    if dp and not dq and p == q and occ[p]: return 1.0       # i^+ j  -> delta_ij (occupied)
    if (not dp) and dq and p == q and not occ[p]: return 1.0  # a b^+ -> delta_ab (virtual)
    return 0.0
for trial in range(40):
    idx = rng.integers(0, n, 4); st = [(idx[0], 1), (idx[1], 1), (idx[2], 0), (idx[3], 0)]
    W = nmat(st)
    for i, j in itertools.combinations(range(4), 2):
        c = contr(st[i], st[j])
        if c:
            rest = [st[k] for k in range(4) if k not in (i, j)]
            sgn = (-1)**(j - i - 1)           # bring the pair together
            W = W + sgn*c*nmat(rest)
    # double contractions
    for (i, j), (k, l) in [((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2))]:
        c = contr(st[i], st[j])*contr(st[k], st[l])
        sgn = {((0,1),(2,3)): 1, ((0,2),(1,3)): -1, ((0,3),(1,2)): 1}[((i,j),(k,l))]
        if c: W = W + sgn*c*sp.identity(2**n)
    worst = max(worst, abs(mat(st) - W).max() if (mat(st)-W).nnz else 0)
print("Wick's theorem, 40 random a+a+aa strings: max deviation =", worst)
# control: strings with at least one nonzero contraction; compare with and without the contraction terms
cnt = 0; worst_full = 0; worst_naive = 0
for trial in range(400):
    idx = rng.integers(0, n, 4); st = [(idx[0], 1), (idx[1], 1), (idx[2], 0), (idx[3], 0)]
    if not any(contr(st[i], st[j]) for i, j in itertools.combinations(range(4), 2)): continue
    cnt += 1
    W = nmat(st); W0 = nmat(st)
    for i, j in itertools.combinations(range(4), 2):
        c = contr(st[i], st[j])
        if c:
            rest = [st[k] for k in range(4) if k not in (i, j)]
            W = W + (-1)**(j-i-1)*c*nmat(rest)
    for (i, j), (k, l), sg in [((0,1),(2,3),1), ((0,2),(1,3),-1), ((0,3),(1,2),1)]:
        c = contr(st[i], st[j])*contr(st[k], st[l])
        if c: W = W + sg*c*sp.identity(2**n)
    worst_full = max(worst_full, abs((mat(st) - W).toarray()).max())
    worst_naive = max(worst_naive, abs((mat(st) - W0).toarray()).max())
print(f"{cnt} strings with contractions: Wick max dev = {worst_full:.1e}; normal-ordered part alone dev = {worst_naive:.1e}")
# corollary: variance of a one-body operator in a determinant = sum_{i occ, a virt} |A_ai|^2
X = rng.normal(size=(n, n)); A1 = X + X.T
Am = sp.csr_matrix((2**n, 2**n))
for p, q in itertools.product(range(n), repeat=2): Am = Am + A1[p, q]*(ad[p] @ ops[q])
v = np.zeros(2**n); v[ref] = 1
var_exact = v @ (Am @ (Am @ v)) - (v @ (Am @ v))**2
var_wick = np.sum(A1[np.ix_(~occ, occ)]**2)
print(f"variance of a random one-body operator: exact {var_exact:.12f}, Wick formula {var_wick:.12f}")
