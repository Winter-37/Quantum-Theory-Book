import numpy as np
from scipy.optimize import brentq
from pyscf import gto, scf, fci, mp
def hring(n, r):
    R = r/(2*np.sin(np.pi/n))
    return gto.M(atom=[['H',(R*np.cos(2*np.pi*k/n),R*np.sin(2*np.pi*k/n),0)] for k in range(n)], basis='sto-3g', unit='A', verbose=0)
def run(r):
    mf=scf.RHF(hring(6,r)).run(conv_tol=1e-12); c=fci.FCI(mf); c.conv_tol=1e-13
    return c.kernel()[0], mp.MP2(mf).run().e_tot
efci=lambda r: run(r)[0]; emp2=lambda r: run(r)[1]
h=2e-3; d1=lambda f,r:(f(r+h)-f(r-h))/(2*h); d2=lambda f,r:(f(r+h)-2*f(r)+f(r-h))/h**2
rref=brentq(lambda r:d1(efci,r),0.85,1.05,xtol=1e-7); rm=brentq(lambda r:d1(emp2,r),0.85,1.05,xtol=1e-7)
g=d1(emp2,rref); k=d2(emp2,rref); kr=d2(efci,rref)
print(f"FCI {rref:.6f}  MP2 {rm:.6f}  shift {1e3*(rm-rref):.3f} mA | offset {1e3*(emp2(rref)-efci(rref)):.3f} mEh | g {1e3*g:.4f} mEh/A k {k:.4f} (FCI k {kr:.4f}) | -g/k {1e3*(-g/k):.3f} mA | relax {1e6*(emp2(rref)-emp2(rm)):.3f} uEh  g2/2k {1e6*g*g/(2*k):.3f}")
