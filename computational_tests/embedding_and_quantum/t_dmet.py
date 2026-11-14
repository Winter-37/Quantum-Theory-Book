import numpy as np, sys
from pyscf import gto, scf, fci
from dmet_mini import *
def hring(n, r):
    R = r/(2*np.sin(np.pi/n))
    return gto.M(atom=[['H',(R*np.cos(2*np.pi*k/n),R*np.sin(2*np.pi*k/n),0)] for k in range(n)], basis='sto-3g', unit='A', verbose=0)
def main():
  mol = hring(6, 1.0)
  mf, h, eri, gam = setup(mol)
  print('E_RHF', mf.e_tot, 'idempotency', np.abs(gam@gam-gam).max(), 'tr', np.trace(gam))
  imp=[0,1]
  E = embed(h, eri, gam, imp)
  gII = gam[np.ix_(imp,imp)]; n = np.linalg.eigvalsh(gII)
  print('n_k (impurity NOs)', n, ' sigma', E['s'], ' sqrt(n(1-n))', np.sqrt(n*(1-n))[::-1])
  print('N_emb', E['nel'], '2*tr gemb', 2*np.trace(E['gemb']), ' gemb idempotent', np.abs(E['gemb']@E['gemb']-E['gemb']).max())
  # Form B vs core form
  C=E['C']; Dcore = gam - C@E['gemb']@C.T
  hcoreform = C.T@(h + jk(eri, Dcore))@C
  print('Form B vs h_emb+v_core', np.abs(hcoreform - E['hB']).max(), ' C^T Dcore', np.abs(C.T@Dcore).max())
  # HF limit
  frags=[[0,1],[2,3],[4,5]]
  Ehf, Nhf = dmet(mol, frags, 0.0, 'hf')
  print('DMET-HF', Ehf, 'RHF', mf.e_tot, 'diff', Ehf-mf.e_tot, 'N', Nhf)
  efci = fci.FCI(mf).kernel()[0]
  for fr,lab in [([[0,1],[2,3],[4,5]],'2-atom'),([[0,1,2],[3,4,5]],'3-atom'),([[k] for k in range(6)],'1-atom')]:
      E0,N0 = dmet(mol, fr, 0.0)
      mu,(E1,N1) = fit_mu(mol, fr)
      print(lab, 'mu=0: E',E0,'N',N0,' | mu*',mu,'E',E1,'N',N1,' E-EFCI', E1-efci)
  print('E_FCI', efci, 'Ecorr', efci-mf.e_tot)

if __name__ == "__main__":
  main()
