"""Small exact fermion toolkit: Jordan-Wigner sparse matrices in Fock space, spin-orbital integrals from PySCF."""
import numpy as np, scipy.sparse as sp, itertools
from pyscf import gto, scf, ao2mo

def jw_ops(n):
    I = sp.identity(2, format='csr'); Z = sp.csr_matrix(np.diag([1., -1.]))
    a1 = sp.csr_matrix(np.array([[0., 1.], [0., 0.]]))   # |0><1| : annihilates occupied (basis |0>,|1>)
    ops = []
    for p in range(n):
        m = sp.identity(1, format='csr')
        for q in range(n):
            m = sp.kron(m, Z if q < p else (a1 if q == p else I), format='csr')
        ops.append(m)
    return ops   # a_p ; a_p^dagger = a_p.T

def basis_index(occ, n):
    """index of determinant |occ> in the 2^n Fock basis (orbital 0 = most significant qubit)"""
    return sum(1 << (n-1-p) for p in occ)

def spin_orbital_integrals(mol, mf=None):
    """spin-orbital MO h_pq and antisymmetrized <pq||rs> (physicists'), orbitals ordered occ-first,
    spin blocks interleaved (alpha,beta) by energy. Returns h, g (antisym), nocc, E_nuc, mf."""
    if mf is None:
        mf = scf.RHF(mol); mf.conv_tol = 1e-12; mf.kernel()
    C = mf.mo_coeff; nmo = C.shape[1]; nso = 2*nmo
    h_mo = C.T @ mf.get_hcore() @ C
    eri = ao2mo.restore(1, ao2mo.full(mol, C), nmo)          # (pq|rs) chemists'
    spin = np.array([0, 1]*nmo); orb = np.repeat(np.arange(nmo), 2)
    h = np.zeros((nso, nso)); same = spin[:, None] == spin[None, :]
    h = h_mo[np.ix_(orb, orb)] * same
    # <pq|rs> = (pr|qs) delta(sp,sr) delta(sq,ss)
    g = eri[np.ix_(orb, orb, orb, orb)].transpose(0, 2, 1, 3)
    g = g * (spin[:, None, None, None] == spin[None, None, :, None]) * (spin[None, :, None, None] == spin[None, None, None, :])
    gA = g - g.transpose(0, 1, 3, 2)
    nocc = mol.nelectron
    return h, gA, nocc, mol.energy_nuc(), mf

def hamiltonian_matrix(h, gA, ops):
    n = len(ops); H = sp.csr_matrix(ops[0].shape)
    ad = [o.T.tocsr() for o in ops]
    for p, q in itertools.product(range(n), repeat=2):
        if abs(h[p, q]) > 1e-14: H = H + h[p, q] * (ad[p] @ ops[q])
    for p, q, r, s in itertools.product(range(n), repeat=4):
        if abs(gA[p, q, r, s]) > 1e-14 and p < q and r < s:
            H = H + gA[p, q, r, s] * (ad[p] @ ad[q] @ ops[s] @ ops[r])
    return H.tocsr()
