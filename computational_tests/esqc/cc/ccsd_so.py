"""Spin-orbital CCSD with the Stanton-Gauss intermediates (Stanton, Gauss, Watts, Bartlett, JCP 94, 4334 (1991)),
plus (T) and [T]. Checked against PySCF (RCCSD / GCCSD / CCSD(T))."""
import numpy as np
from fermi import spin_orbital_integrals

def setup(mol, mf=None):
    h, g, no, enuc, mf = spin_orbital_integrals(mol, mf)
    occ = np.arange(h.shape[0]) < no
    f = h + np.einsum('piqi->pq', g[:, occ][:, :, :, occ])
    o, v = slice(0, no), slice(no, h.shape[0])
    return f, g, o, v, mf

def ccsd(f, g, o, v, maxiter=200, tol=1e-11, diis=8, verbose=False):
    fo, fv = np.diag(f)[o], np.diag(f)[v]
    D1 = fo[:, None] - fv[None, :]
    D2 = fo[:, None, None, None] + fo[None, :, None, None] - fv[None, None, :, None] - fv[None, None, None, :]
    t1 = f[o, v]/D1; t2 = g[o, o, v, v]/D2
    fov = f[o, v]; foo = f[o, o] - np.diag(fo); fvv = f[v, v] - np.diag(fv)
    E = lambda t1, t2: np.einsum('ia,ia', fov, t1) + 0.25*np.einsum('ijab,ijab', g[o,o,v,v], t2) + 0.5*np.einsum('ijab,ia,jb', g[o,o,v,v], t1, t1)
    hist = []; Eold = E(t1, t2)
    for it in range(maxiter):
        tau_t = t2 + 0.5*(np.einsum('ia,jb->ijab', t1, t1) - np.einsum('ib,ja->ijab', t1, t1))
        tau = t2 + np.einsum('ia,jb->ijab', t1, t1) - np.einsum('ib,ja->ijab', t1, t1)
        Fae = fvv - 0.5*np.einsum('me,ma->ae', fov, t1) + np.einsum('mf,mafe->ae', t1, g[o,v,v,v]) - 0.5*np.einsum('mnaf,mnef->ae', tau_t, g[o,o,v,v])
        Fmi = foo + 0.5*np.einsum('ie,me->mi', t1, fov) + np.einsum('ne,mnie->mi', t1, g[o,o,o,v]) + 0.5*np.einsum('inef,mnef->mi', tau_t, g[o,o,v,v])
        Fme = fov + np.einsum('nf,mnef->me', t1, g[o,o,v,v])
        Wmnij = g[o,o,o,o] + np.einsum('je,mnie->mnij', t1, g[o,o,o,v]) - np.einsum('ie,mnje->mnij', t1, g[o,o,o,v]) + 0.25*np.einsum('ijef,mnef->mnij', tau, g[o,o,v,v])
        Wabef = g[v,v,v,v] - np.einsum('mb,amef->abef', t1, g[v,o,v,v]) + np.einsum('ma,bmef->abef', t1, g[v,o,v,v]) + 0.25*np.einsum('mnab,mnef->abef', tau, g[o,o,v,v])
        Wmbej = g[o,v,v,o] + np.einsum('jf,mbef->mbej', t1, g[o,v,v,v]) - np.einsum('nb,mnej->mbej', t1, g[o,o,v,o]) \
                - np.einsum('jnfb,mnef->mbej', 0.5*t2 + np.einsum('jf,nb->jnfb', t1, t1), g[o,o,v,v])
        # T1
        r1 = fov + np.einsum('ie,ae->ia', t1, Fae) - np.einsum('ma,mi->ia', t1, Fmi) + np.einsum('imae,me->ia', t2, Fme) \
             - np.einsum('nf,naif->ia', t1, g[o,v,o,v]) - 0.5*np.einsum('imef,maef->ia', t2, g[o,v,v,v]) - 0.5*np.einsum('mnae,nmei->ia', t2, g[o,o,v,o])
        # T2
        tmp = Fae - 0.5*np.einsum('mb,me->be', t1, Fme)
        P1 = np.einsum('ijae,be->ijab', t2, tmp); r2 = g[o,o,v,v] + P1 - P1.transpose(0,1,3,2)
        tmp = Fmi + 0.5*np.einsum('je,me->mj', t1, Fme)
        P2 = np.einsum('imab,mj->ijab', t2, tmp); r2 -= P2 - P2.transpose(1,0,2,3)
        r2 += 0.5*np.einsum('mnab,mnij->ijab', tau, Wmnij) + 0.5*np.einsum('ijef,abef->ijab', tau, Wabef)
        P3 = np.einsum('imae,mbej->ijab', t2, Wmbej) - np.einsum('ie,ma,mbej->ijab', t1, t1, g[o,v,v,o])
        r2 += P3 - P3.transpose(1,0,2,3) - P3.transpose(0,1,3,2) + P3.transpose(1,0,3,2)
        P4 = np.einsum('ie,abej->ijab', t1, g[v,v,v,o]); r2 += P4 - P4.transpose(1,0,2,3)
        P5 = np.einsum('ma,mbij->ijab', t1, g[o,v,o,o]); r2 -= P5 - P5.transpose(0,1,3,2)
        t1n, t2n = r1/D1, r2/D2
        # DIIS on the full amplitude vector
        vec = np.concatenate([t1n.ravel(), t2n.ravel()]); err = vec - np.concatenate([t1.ravel(), t2.ravel()])
        hist.append((vec, err)); hist = hist[-diis:]
        if len(hist) > 2:
            m = len(hist); B = -np.ones((m+1, m+1)); B[m, m] = 0
            for i in range(m):
                for j in range(m): B[i, j] = hist[i][1] @ hist[j][1]
            c = np.linalg.solve(B, np.r_[np.zeros(m), -1])[:m]
            vec = sum(ci*hv[0] for ci, hv in zip(c, hist))
        t1 = vec[:t1.size].reshape(t1.shape); t2 = vec[t1.size:].reshape(t2.shape)
        Enew = E(t1, t2)
        if verbose: print(it, Enew)
        if abs(Enew - Eold) < tol and np.linalg.norm(err) < 1e-8: break
        Eold = Enew
    return Enew, t1, t2, it+1

def triples(f, g, o, v, t1, t2):
    """CCSD(T) and CCSD[T] in spin orbitals (Crawford & Schaefer form). Returns E[T], E_ST, E(T)=E[T]+E_ST."""
    fo, fv = np.diag(f)[o], np.diag(f)[v]
    D3 = (fo[:,None,None,None,None,None] + fo[None,:,None,None,None,None] + fo[None,None,:,None,None,None]
          - fv[None,None,None,:,None,None] - fv[None,None,None,None,:,None] - fv[None,None,None,None,None,:])
    def P_ij_k(x):   # P(i/jk) acting on index positions 0,1,2 : x - x(j i k) - x(k j i)
        return x - x.transpose(1,0,2,3,4,5) - x.transpose(2,1,0,3,4,5)
    def P_a_bc(x):
        return x - x.transpose(0,1,2,4,3,5) - x.transpose(0,1,2,5,4,3)
    # disconnected: P(i/jk)P(a/bc) t_i^a <jk||bc>
    tdisc = P_ij_k(P_a_bc(np.einsum('ia,jkbc->ijkabc', t1, g[o,o,v,v])))
    # connected: P(i/jk)P(c/ab)[ sum_e t_jk^ae <ei||bc>... ] ; written as in Crawford project #6:
    c1 = np.einsum('jkae,eibc->ijkabc', t2, g[v,o,v,v])      # t_jk^ae <ei||bc>
    c2 = np.einsum('imbc,majk->ijkabc', t2, g[o,v,o,o])      # t_im^bc <ma||jk>
    tcon = P_ij_k(P_a_bc(c1 - c2))
    ET_bracket = (1/36)*np.einsum('ijkabc,ijkabc', tcon/D3, tcon)
    E_ST = (1/36)*np.einsum('ijkabc,ijkabc', tcon/D3, tdisc)
    return ET_bracket, E_ST, ET_bracket + E_ST
