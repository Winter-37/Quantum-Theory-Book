"""SQD at a fixed subspace size: which sampler supplies the determinants matters, not only how many.
Water 6-31G, frozen O 1s, (8e,12o), FCI dimension 245025. For each sampler, take the k most frequent alpha and
beta strings among shots with the right electron counts (symmetrized over spin), diagonalize in their product space."""
import numpy as np, ffsim
from collections import Counter
from pyscf import scf, mcscf, cc, fci, ao2mo
from pyscf.fci import selected_ci, cistring
from sqd_demo import water

def strings_from_bits(bits, norb, nelec, k):
    a = bits[:, norb:]; b = bits[:, :norb]                 # ffsim: alpha bits on the right half, little-endian
    ok = (a.sum(1) == nelec[0]) & (b.sum(1) == nelec[1])
    w = 2**np.arange(norb)[::-1]
    ints = lambda m: (m.astype(int) @ w)
    cnt = Counter(ints(a[ok])) + Counter(ints(b[ok]))
    top = sorted(cnt, key=lambda s: -cnt[s])[:k]
    return np.array(sorted(top)), ok.mean()

def energy(h1, h2, norb, nelec, strs, ecore):
    return selected_ci.kernel_fixed_space(selected_ci.SCI(), h1, h2, norb, nelec, ci_strs=(strs, strs), tol=1e-12)[0] + ecore

def main(r_oh, ks=(30, 60, 120), shots=200_000, seed=3):
    mol = water(r_oh); mf = scf.RHF(mol).run(conv_tol=1e-12)
    norb, nelec = mol.nao-1, (4, 4)
    cas = mcscf.CASCI(mf, norb, nelec); h1, ecore = cas.get_h1eff(); h2 = ao2mo.restore(1, cas.get_h2eff(), norb)
    efci, cfci = fci.direct_spin1.kernel(h1, h2, norb, nelec, ecore=ecore, conv_tol=1e-12)
    ccsd = cc.CCSD(mf, frozen=1).run(conv_tol=1e-10)
    op = ffsim.UCJOpSpinBalanced.from_t_amplitudes(ccsd.t2, t1=ccsd.t1, n_reps=2,
            interaction_pairs=([(p, p+1) for p in range(norb-1)], [(p, p) for p in range(0, norb, 4)]))
    lucj = ffsim.apply_unitary(ffsim.hartree_fock_state(norb, nelec), op, norb=norb, nelec=nelec)
    rng = np.random.default_rng(seed)
    samp = lambda v: ffsim.sample_state_vector(v, norb=norb, nelec=nelec, shots=shots, bitstring_type=ffsim.BitstringType.BIT_ARRAY, seed=rng)
    fcivec = np.asarray(cfci).reshape(-1)
    nstr = cistring.num_strings(norb, 4)
    # uniform null model: random strings with the right counts
    allstr = cistring.make_strings(range(norb), 4)
    print(f"r_OH={r_oh}  E_FCI={efci:.6f}  E_CCSD-E_FCI={1e3*(ccsd.e_tot-efci):.3f} mEh  strings/spin={nstr}")
    src = {'FCI |c|^2': samp(fcivec), 'LUCJ (CCSD, L=2)': samp(lucj)}
    for k in ks:
        line = [f"  k={k:4d} (dim {k*k:6d}, {100*k*k/nstr**2:5.2f}% of FCI):"]
        for name, bits in src.items():
            strs, _ = strings_from_bits(bits, norb, nelec, k)
            if len(strs) < k: line.append(f"{name}: only {len(strs)} distinct");
            line.append(f"{name} {1e3*(energy(h1,h2,norb,nelec,strs,ecore)-efci):8.3f}")
        u = np.sort(rng.choice(allstr, size=k, replace=False))
        # always include HF string so the null model is not handicapped by missing the reference
        hf = cistring.make_strings(range(4), 4)[0] if False else int('0'*(norb-4)+'1111', 2)
        if hf not in u: u[0] = hf; u = np.sort(u)
        line.append(f"uniform+HF {1e3*(energy(h1,h2,norb,nelec,u,ecore)-efci):8.3f}  (mEh)")
        print('  '.join(line))

if __name__ == '__main__':
    for r in (0.96, 1.92): main(r)
