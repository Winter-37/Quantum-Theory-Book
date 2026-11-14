import numpy as np, ffsim
from pyscf import scf, mcscf, cc, fci, ao2mo
from sqd_demo import water
from sqd_fixed_dim import strings_from_bits, energy
for r in (0.96,1.92):
    mol=water(r); mf=scf.RHF(mol).run(conv_tol=1e-12); norb,nelec=mol.nao-1,(4,4)
    cas=mcscf.CASCI(mf,norb,nelec); h1,ec=cas.get_h1eff(); h2=ao2mo.restore(1,cas.get_h2eff(),norb)
    efci=fci.direct_spin1.kernel(h1,h2,norb,nelec,ecore=ec,conv_tol=1e-12)[0]
    ccsd=cc.CCSD(mf,frozen=1).run(conv_tol=1e-10); ham=ffsim.linear_operator(ffsim.MolecularHamiltonian(h1,h2,constant=ec),norb=norb,nelec=nelec)
    hf=ffsim.hartree_fock_state(norb,nelec)
    for lab,pairs,L in [('local L=2',([(p,p+1) for p in range(norb-1)],[(p,p) for p in range(0,norb,4)]),2),('all pairs L=2',None,2),('all pairs L=4',None,4)]:
        op=ffsim.UCJOpSpinBalanced.from_t_amplitudes(ccsd.t2,t1=ccsd.t1,n_reps=L,interaction_pairs=pairs)
        v=ffsim.apply_unitary(hf,op,norb=norb,nelec=nelec); e=np.real(np.vdot(v,ham@v))
        bits=ffsim.sample_state_vector(v,norb=norb,nelec=nelec,shots=200000,bitstring_type=ffsim.BitstringType.BIT_ARRAY,seed=1)
        s,_=strings_from_bits(bits,norb,nelec,10**6)
        print(f"r={r} {lab:14s} <H>-E_FCI={1e3*(e-efci):8.2f} mEh  |<HF|psi>|^2={abs(v.reshape(-1)[0])**2:.4f}  distinct strings/spin={len(s)}  E_SQD(all of them)-E_FCI={1e3*(energy(h1,h2,norb,nelec,s,ec)-efci):.3f}")
    print(f"r={r} |<HF|FCI>|^2 = {abs(fci.direct_spin1.kernel(h1,h2,norb,nelec,ecore=ec)[1].reshape(-1)[0])**2:.4f}")
