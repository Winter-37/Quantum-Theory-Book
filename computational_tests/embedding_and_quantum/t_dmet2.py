import numpy as np
from pyscf import gto, fci
from dmet_mini import *
from t_dmet import hring
def veff_s(eri, Ds): return jk(eri, Ds/2)          # J[Ds] - 1/2 K[Ds] for spin-summed Ds
def dmet_both(mol, frags, mu, solver='fci', data=None):
    mf,h,eri,gam = data or setup(mol)
    Es, G, Emf, N, own, two = [], np.zeros_like(h), mol.energy_nuc(), 0., 0., 0.
    for imp in frags:
        E = embed(h,eri,gam,imp); r1,r2 = solve(E,mu,solver)
        Emf += frag_energy(E,r1,r2); N += np.trace(r1[:E['nimp'],:E['nimp']])
        w1,w2 = weights(r1.shape[0],E['nimp'])
        G += E['C']@(w1*r1)@E['C'].T
        own += 0.5*np.sum((w1*r1)*veff_s(E['eri'],r1)); two += 0.5*np.sum(w2*E['eri']*r2)
    Ecorr = mol.energy_nuc() + np.sum(G*h) + 0.5*np.sum(G*veff_s(eri,G)) - own + two
    return Emf, Ecorr, N
mol = hring(6,1.0); mf,h,eri,gam = d = setup(mol)
fr=[[0,1],[2,3],[4,5]]
print('HF solver  (mf, corr, N):', dmet_both(mol,fr,0.0,'hf',d), ' E_RHF', mf.e_tot)
print('FCI solver mu=0 (mf, corr, N):', dmet_both(mol,fr,0.0,'fci',d))
