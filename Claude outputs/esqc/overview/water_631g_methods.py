"""Water/6-31G (all electrons, r=0.9572 A, 104.52 deg): total energies of the standard methods vs FCI."""
import numpy as np
from pyscf import gto, scf, dft, mp, ci, cc, mcscf, fci, mrpt
th = np.radians(104.52)/2; R = 0.9572
mol = gto.M(atom=f'O 0 0 0; H 0 {R*np.sin(th)} {R*np.cos(th)}; H 0 {-R*np.sin(th)} {R*np.cos(th)}', basis='6-31g', verbose=0)
mf = scf.RHF(mol); mf.conv_tol = 1e-12; mf.kernel()
ks = dft.RKS(mol); ks.xc = 'b3lyp'; ks.kernel()
emp2 = mp.MP2(mf).kernel()[0]
mci = ci.CISD(mf); mci.kernel()
mcc = cc.CCSD(mf); mcc.conv_tol = 1e-10; mcc.kernel(); et = mcc.ccsd_t()
cas = mcscf.CASSCF(mf, 6, 8); cas.kernel()            # CAS(8e,6o): valence minus O 2s? see note
nev = mrpt.NEVPT(cas).kernel()
cf = fci.FCI(mf); efci, _ = cf.kernel()
# excited singlet: EOM-EE-CCSD vs FCI
eee, _ = mcc.eomee_ccsd_singlet(nroots=1)
cf2 = fci.addons.fix_spin_(fci.FCI(mf), ss=0); cf2.nroots = 2; e2, _ = cf2.kernel()
rows = [("RHF", mf.e_tot), ("KS-DFT B3LYP", ks.e_tot), ("MP2", mf.e_tot+emp2), ("CISD", mci.e_tot),
        ("CCSD", mcc.e_tot), ("CCSD(T)", mcc.e_tot+et), ("CASSCF(8,6)", cas.e_tot), ("NEVPT2 (SC)", cas.e_tot+nev), ("FCI", efci)]
for n, e in rows: print(f"{n:14s} {e:14.8f}  {1e3*(e-efci):9.3f} mEh")
print("lowest singlet excitation: EOM-CCSD %.5f Eh, FCI %.5f Eh" % (eee if np.isscalar(eee) else eee[0], e2[1]-e2[0]))
print("CASSCF natural occupations:", np.round(cas.mo_occ[mol.nelectron//2-4: mol.nelectron//2+2], 4))
