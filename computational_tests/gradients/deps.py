import sys; sys.path.insert(0,'.')
exec(open('rhf_grad_hess.py').read().split("for basis in")[0])
mol, mf, C, eps, nocc, eri, dS, dh, dg, Us, Fsk, Sxs, M = analysis('6-31g')
o=slice(0,nocc); v=slice(nocc,None); worst=0
for A in range(3):
  for k in range(3):
    x=3*A+k; U=Us[x]; S=Sxs[x]; F=Fsk[x]
    de=np.array([F[i,i]-S[i,i]*eps[i]-np.sum(S[o,o]*(2*eri[i,i,o,o]-eri[i,o,i,o]))
        +np.sum(U[v,o]*(4*eri[i,i,v,o]-eri[i,v,i,o]-eri[i,o,i,v].T)) for i in range(nocc)])
    h=1e-4; e=[rhf(displaced(mol,A,k,s*h),mf.make_rdm1()).mo_energy[:nocc] for s in (1,-1)]
    worst=max(worst,abs(de-(e[0]-e[1])/(2*h)).max())
print('d eps_i/dx (Eq. 10.25) vs FD, max', worst)
print('M eigen range', np.linalg.eigvalsh(M)[[0,-1]])
