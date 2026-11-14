"""Minimal closed-shell one-shot DMET (Löwdin LOs, SVD bath, Form B, FCI or HF solver, global mu).
Used to produce the worked numbers in the notebook's DMET notes."""
import numpy as np
from pyscf import gto, scf, ao2mo, fci
from functools import reduce

def lowdin(S):
    w, v = np.linalg.eigh(S)
    return v @ np.diag(w**-0.5) @ v.T, v @ np.diag(w**0.5) @ v.T

def setup(mol):
    mf = scf.RHF(mol); mf.conv_tol = 1e-13; mf.kernel()
    S = mol.intor('int1e_ovlp'); X, Sh = lowdin(S)
    h = X @ mf.get_hcore() @ X
    eri = ao2mo.restore(1, ao2mo.kernel(mol, X, compact=False), mol.nao)
    gam = Sh @ (mf.make_rdm1() / 2) @ Sh          # per-spin density in LO basis, idempotent
    return mf, h, eri, gam

def jk(eri, D):                                    # closed-shell veff from a per-spin density D
    return 2*np.einsum('ijkl,kl->ij', eri, D) - np.einsum('ikjl,kl->ij', eri, D)

def bath(gam, imp, thr=1e-8):
    n = gam.shape[0]; env = [k for k in range(n) if k not in imp]
    U, s, Vt = np.linalg.svd(gam[np.ix_(env, imp)], full_matrices=False)
    keep = s > thr
    C = np.zeros((n, len(imp) + keep.sum()))
    C[imp, :len(imp)] = np.eye(len(imp)); C[np.ix_(env, range(len(imp), C.shape[1]))] = U[:, keep]
    return C, s, env

def embed(h, eri, gam, imp):
    C, s, env = bath(gam, imp)
    gemb = C.T @ gam @ C
    F = h + jk(eri, gam)
    eri_e = ao2mo.restore(1, ao2mo.incore.full(ao2mo.restore(8, eri, h.shape[0]), C), C.shape[1])
    hB = C.T @ F @ C - jk(eri_e, gemb)             # Form B
    nel = int(round(2*np.trace(gemb)))
    return dict(C=C, s=s, env=env, gemb=gemb, hB=hB, eri=eri_e, hemb=C.T @ h @ C, nel=nel, nimp=len(imp))

def solve(E, mu, solver='fci'):
    n, ni = E['hB'].shape[0], E['nimp']
    hs = E['hB'].copy(); hs[range(ni), range(ni)] -= mu
    if solver == 'fci':
        cis = fci.direct_spin1.FCI(); cis.conv_tol = 1e-13
        e, c = cis.kernel(hs, E['eri'], n, E['nel'])
        r1, r2 = cis.make_rdm12(c, n, E['nel'])     # spin-summed, r2[p,q,r,s] = <p+ r+ s q>
    else:                                           # HF in the embedding space
        m = gto.M(); m.nelectron = E['nel']; m.incore_anyway = True
        mf = scf.RHF(m); mf.get_hcore = lambda *a: hs; mf.get_ovlp = lambda *a: np.eye(n)
        mf._eri = ao2mo.restore(8, E['eri'], n); mf.conv_tol = 1e-13
        mf.kernel(dm0=2*E['gemb']); d = mf.make_rdm1()
        r1 = d; r2 = np.einsum('pq,rs->pqrs', d, d) - 0.5*np.einsum('ps,rq->pqrs', d, d)
    return r1, r2

def weights(n, ni):
    imp = np.zeros(n); imp[:ni] = 1
    w1 = 0.5*(imp[:, None] + imp[None, :])
    w2 = 0.25*(imp[:, None, None, None] + imp[None, :, None, None] + imp[None, None, :, None] + imp[None, None, None, :])
    return w1, w2

def frag_energy(E, r1, r2):
    """Mean-field (democratic) functional: h' = (h_emb + h_B)/2, weights w1, w2."""
    w1, w2 = weights(E['hB'].shape[0], E['nimp'])
    hp = 0.5*(E['hemb'] + E['hB'])
    return np.sum(w1*hp*r1) + 0.5*np.sum(w2*E['eri']*r2)

def dmet(mol, frags, mu, solver='fci', data=None):
    mf, h, eri, gam = data or setup(mol)
    Etot, N = mol.energy_nuc(), 0.0
    for imp in frags:
        E = embed(h, eri, gam, imp)
        r1, r2 = solve(E, mu, solver)
        Etot += frag_energy(E, r1, r2); N += np.trace(r1[:E['nimp'], :E['nimp']])
    return Etot, N

def fit_mu(mol, frags, solver='fci', mu0=0.0, tol=1e-11):
    data = setup(mol); Nt = mol.nelectron
    f = lambda m: dmet(mol, frags, m, solver, data)[1] - Nt
    m0, m1 = mu0, mu0 - 1e-3*np.sign(f(mu0) or 1)
    f0, f1 = f(m0), f(m1)
    for _ in range(60):
        if abs(f1) < tol: break
        m0, m1, f0 = m1, m1 - f1*(m1 - m0)/(f1 - f0), f1
        f1 = f(m1)
    return m1, dmet(mol, frags, m1, solver, data)
