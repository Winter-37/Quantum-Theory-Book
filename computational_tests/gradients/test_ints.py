import numpy as np, sys
sys.path.insert(0,'.')
from common import *
mol=water('6-31g')
dS,dh,dg=skeleton_ao(mol)
h=1e-4; err=[0,0,0]
for A in range(3):
  for k in range(3):
    mp=displaced(mol,A,k,h); mm=displaced(mol,A,k,-h)
    i=3*A+k
    fS=(mp.intor('int1e_ovlp')-mm.intor('int1e_ovlp'))/(2*h)
    fh=(scf.hf.get_hcore(mp)-scf.hf.get_hcore(mm))/(2*h)
    fg=(mp.intor('int2e')-mm.intor('int2e'))/(2*h)
    err=[max(err[0],abs(fS-dS[i]).max()),max(err[1],abs(fh-dh[i]).max()),max(err[2],abs(fg-dg[i]).max())]
print('max |analytic - FD| skeleton S,h,eri:',err)
