import numpy as np, time
from pyscf import gto, scf, cc
from ccsd_so import setup, ccsd, triples
mol = gto.M(atom='O 0 0 0.1173; H 0 0.7572 -0.4692; H 0 -0.7572 -0.4692', basis='6-31g', verbose=0)
f, g, o, v, mf = setup(mol)
t0 = time.time(); E, t1, t2, nit = ccsd(f, g, o, v); t = time.time()-t0
mcc = cc.CCSD(mf); mcc.conv_tol = 1e-11; mcc.kernel()
print(f"water/6-31G  E_HF={mf.e_tot:.10f}")
print(f"spin-orbital Stanton-Gauss CCSD corr = {E:.10f} ({nit} it, {t:.1f}s);  PySCF RCCSD = {mcc.e_corr:.10f}; diff {E-mcc.e_corr:.1e}")
ETb, EST, ET = triples(f, g, o, v, t1, t2)
from pyscf.cc import ccsd_t
et = mcc.ccsd_t()
print(f"E[T] = {ETb:.10f}  E_ST = {EST:.10f}  E(T) = {ET:.10f};  PySCF (T) = {et:.10f}; diff {ET-et:.1e}")
