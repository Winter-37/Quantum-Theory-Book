"""SQD on water (6-31G, frozen O 1s): LUCJ from CCSD (ffsim), state-vector sampling, configuration recovery,
subspace diagonalization (qiskit-addon-sqd), against FCI. Also a depolarized-sampling test."""
import numpy as np, sys, ffsim
from pyscf import gto, scf, mcscf, cc, fci
from pyscf.fci import selected_ci
from qiskit_addon_sqd.fermion import diagonalize_fermionic_hamiltonian

def water(r_oh, ang=104.5):
    t = np.deg2rad(ang/2)
    return gto.M(atom=[['O', (0, 0, 0)], ['H', (r_oh*np.sin(t), 0, r_oh*np.cos(t))], ['H', (-r_oh*np.sin(t), 0, r_oh*np.cos(t))]],
                 basis='6-31g', unit='A', verbose=0)

def run(r_oh, shots=10_000, n_reps=2, alpha_list=(1.0,), seed=7, samples_per_batch=300, num_batches=5):
    mol = water(r_oh); mf = scf.RHF(mol).run(conv_tol=1e-12)
    ncore = 1; norb = mol.nao - ncore; nelec = ((mol.nelectron - 2*ncore)//2,)*2
    cas = mcscf.CASCI(mf, norb, nelec); h1, ecore = cas.get_h1eff()
    from pyscf import ao2mo
    h2 = ao2mo.restore(1, cas.get_h2eff(), norb)
    efci = fci.direct_spin1.kernel(h1, h2, norb, nelec, ecore=ecore, conv_tol=1e-12)[0]
    ccsd = cc.CCSD(mf, frozen=ncore).run(conv_tol=1e-10)
    pairs_aa = [(p, p+1) for p in range(norb-1)]; pairs_ab = [(p, p) for p in range(0, norb, 4)]
    op = ffsim.UCJOpSpinBalanced.from_t_amplitudes(ccsd.t2, t1=ccsd.t1, n_reps=n_reps, interaction_pairs=(pairs_aa, pairs_ab))
    vec = ffsim.apply_unitary(ffsim.hartree_fock_state(norb, nelec), op, norb=norb, nelec=nelec)
    ham = ffsim.MolecularHamiltonian(h1, h2, constant=ecore)
    e_lucj = np.real(np.vdot(vec, ffsim.linear_operator(ham, norb=norb, nelec=nelec) @ vec))
    dim_fci = fci.cistring.num_strings(norb, nelec[0])**2
    out = dict(r=r_oh, E_HF=mf.e_tot, E_CCSD=ccsd.e_tot, E_FCI=efci, E_LUCJ=e_lucj, dim_fci=dim_fci, runs=[])
    rng = np.random.default_rng(seed)
    clean = ffsim.sample_state_vector(vec, norb=norb, nelec=nelec, shots=shots, bitstring_type=ffsim.BitstringType.BIT_ARRAY, seed=rng)
    for a in alpha_list:
        bits = clean.copy()
        nnoise = int(round((1-a)*shots))
        if nnoise: bits[:nnoise] = rng.random((nnoise, 2*norb)) < 0.5          # uniform bits: depolarized fraction
        good = (bits[:, :norb].sum(1) == nelec[1]) & (bits[:, norb:].sum(1) == nelec[0])
        res = diagonalize_fermionic_hamiltonian(h1, h2, bits, samples_per_batch=samples_per_batch, norb=norb, nelec=nelec,
                                                num_batches=num_batches, max_iterations=5, seed=seed, symmetrize_spin=True)
        e_sqd = res.energy + ecore
        sa, sb = res.sci_state.ci_strs_a, res.sci_state.ci_strs_b
        # independent check: diagonalize H in the same product space with PySCF
        e_chk = selected_ci.kernel_fixed_space(selected_ci.SCI(), h1, h2, norb, nelec, ci_strs=(sa, sb), tol=1e-12)[0] + ecore
        out['runs'].append(dict(alpha=a, frac_right_N=good.mean(), dim=len(sa)*len(sb), E_SQD=e_sqd, E_check=e_chk))
    return out

if __name__ == '__main__':
    for r in (0.96, 1.92):
        o = run(r, alpha_list=(1.0, 0.1, 0.02))
        print(f"\nr_OH={o['r']} A  E_HF={o['E_HF']:.6f} E_CCSD={o['E_CCSD']:.6f} E_LUCJ={o['E_LUCJ']:.6f} E_FCI={o['E_FCI']:.6f}  FCI dim={o['dim_fci']}")
        for q in o['runs']:
            print(f"  signal {q['alpha']:.2f}: right-N {q['frac_right_N']:.3f}  dim {q['dim']:7d}  E_SQD={q['E_SQD']:.6f} "
                  f"(check {q['E_check']:.6f})  E-E_FCI = {1e3*(q['E_SQD']-o['E_FCI']):.3f} mEh")
