"""Sum-rule test for the oo/vv response at a geometry with no symmetry (water, STO-3G, fixed list)."""
import numpy as np, sys
sys.path.insert(0, '.')
from sci_grad import *
geom = [['O', (0.0, 0.0, 0.0)], ['H', (0.25, 1.55, 1.25)], ['H', (-0.15, -1.80, 1.05)]]
mol = gto.M(atom=geom, basis='sto-3g', unit='Bohr', verbose=0)
mf = rhf(mol); nocc = mol.nelectron // 2; n = mf.mo_coeff.shape[1]
h = mo_transform(mf.mo_coeff, mf.get_hcore()); g = eri_mo(mf.mo_coeff, mol.intor('int2e'))
efci, cfci = fci.direct_spin1.kernel(h, g, n, (nocc, nocc), tol=1e-13)
for tau in (0.05, 0.02):
    sel = np.flatnonzero(np.abs(cfci.ravel()) > tau)
    st = State(mol, sel); st.setup()
    G, *_ = gradients(st); gfd = fd(mol, st, sel)
    dF = st.X - st.X.T; o, v = slice(0, nocc), slice(nocc, None)
    print(f'tau {tau}: {len(sel)} dets; max|dF| oo {abs(dF[o,o]).max():.1e} vv {abs(dF[v,v]).max():.1e}; min gap oo/vv '
          f'{min(abs(st.eps[p]-st.eps[q]) for p in range(n) for q in range(p) if (p<nocc)==(q<nocc)):.3f}')
    for nm, gg in (('FD', gfd), ('full', G['full']), ('zvec', G['zvec']), ('vo only', G['vo_only'])):
        print(f'   {nm:8s} max|.-FD| {abs(gg-gfd).max():.1e}  net force {abs(gg.reshape(-1,3).sum(0)).max():.1e}  '
              f'net torque {torque(mol, gg):.1e}')
