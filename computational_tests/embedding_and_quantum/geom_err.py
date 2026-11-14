import numpy as np
from scipy.optimize import brentq
from pyscf import gto, scf, fci
from dmet_mini import *
B=0.529177210903
def hring(n, r):
    R = r/(2*np.sin(np.pi/n))
    return gto.M(atom=[['H',(R*np.cos(2*np.pi*k/n),R*np.sin(2*np.pi*k/n),0)] for k in range(n)], basis='sto-3g', unit='A', verbose=0)
fr=[[0,1],[2,3],[4,5]]
def efci(r):
    m=hring(6,r); mf=scf.RHF(m).run(conv_tol=1e-12); c=fci.FCI(mf); c.conv_tol=1e-13; return c.kernel()[0]
mu_cache={'mu':0.0}
def edmet(r):
    mu,(e,n)=fit_mu(hring(6,r),fr,mu0=mu_cache['mu']); mu_cache['mu']=mu; return e
h=2e-3   # Angstrom
d1=lambda f,r:(f(r+h)-f(r-h))/(2*h)
d2=lambda f,r:(f(r+h)-2*f(r)+f(r-h))/h**2
rref=brentq(lambda r:d1(efci,r),0.85,1.05,xtol=1e-7)
rdm=brentq(lambda r:d1(edmet,r),0.85,1.05,xtol=1e-7)
g=d1(edmet,rref); k=d2(edmet,rref)
print(f"FCI min r_nn={rref:.6f} A   DMET(3xH2) min r_nn={rdm:.6f} A   actual shift {1e3*(rdm-rref):.3f} mA")
print(f"offset E_DMET-E_FCI at r_ref = {1e3*(edmet(rref)-efci(rref)):.3f} mEh;  force dE/dr at r_ref = {1e3*g:.4f} mEh/A;  curvature {k:.4f} Eh/A^2")
print(f"predicted shift -g/k = {1e3*(-g/k):.3f} mA;  relaxation energy E(rref)-E(rdm) = {1e6*(edmet(rref)-edmet(rdm)):.3f} uEh;  g^2/2k = {1e6*g*g/(2*k):.3f} uEh")
