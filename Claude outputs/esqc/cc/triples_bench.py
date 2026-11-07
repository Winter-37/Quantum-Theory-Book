"""CCSD+T(4), CCSD[T], CCSD(T), CCSDT vs FCI for water/6-31G (all electrons), R_e and 2R_e."""
import numpy as np
from pyscf import gto, scf, cc, fci
from pyscf.cc import rccsdt
from ccsd_so import setup, ccsd, triples
def water(scale):
    R = 0.9572*scale; th = np.radians(104.52)/2
    return gto.M(atom=f'O 0 0 0; H 0 {R*np.sin(th)} {R*np.cos(th)}; H 0 {-R*np.sin(th)} {R*np.cos(th)}', basis='6-31g', verbose=0)
for scale in (1.0, 2.0):
    mol = water(scale)
    mf = scf.RHF(mol); mf.conv_tol = 1e-12; mf.kernel()
    if scale == 2.0:
        mo, _, st, _ = mf.stability(return_status=True)
    f, g, o, v, _ = setup(mol, mf)
    Ec, t1, t2, _ = ccsd(f, g, o, v)
    # first-order amplitudes (MP1) for CCSD+T(4)
    fo, fv = np.diag(f)[o], np.diag(f)[v]
    D2 = fo[:,None,None,None]+fo[None,:,None,None]-fv[None,None,:,None]-fv[None,None,None,:]
    ET4, _, _ = triples(f, g, o, v, np.zeros_like(t1), g[o,o,v,v]/D2)
    ETb, EST, ET = triples(f, g, o, v, t1, t2)
    mt = rccsdt.RCCSDT(mf); mt.conv_tol = 1e-10; mt.kernel()
    cis = fci.FCI(mf); efci = cis.kernel()[0]
    Eccsd = mf.e_tot + Ec
    rows = [("CCSD", Eccsd), ("CCSD+T(4)", Eccsd+ET4), ("CCSD[T]", Eccsd+ETb), ("CCSD(T)", Eccsd+ET), ("CCSDT", mt.e_tot)]
    print(f"\nscale {scale}: E_HF={mf.e_tot:.8f}  E_FCI={efci:.8f}  E_T(4)={ET4:.6f} E[T]={ETb:.6f} E_ST={EST:.6f}  max|t1|={abs(t1).max():.3f}")
    for name, e in rows: print(f"  {name:10s} {e:.8f}   E-E_FCI = {1e3*(e-efci):8.3f} mEh")
