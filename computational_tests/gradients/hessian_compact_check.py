import sys; sys.path.insert(0,'.')
t=open('rhf_grad_hess.py').read()
src=t.split("for basis in")[0]+"\n"+t.split("# ---------------- RHF Hessian, Yamaguchi Eq. (4.54) ----------------")[1].split("for b in")[0]
exec(src)
for basis in ('sto-3g','6-31g'):
  mol, mf, C, eps, nocc, eri, dS, dh, dg, Us, Fsk, Sxs, M = analysis(basis)
  Htot,Href,Hsk,Hr=hessian(basis)
  o=slice(0,nocc);v=slice(nocc,None);n3=9
  A4=4*eri-eri.transpose(0,2,1,3)-eri.transpose(0,3,2,1)
  rows=[];rhs=[]
  for x in range(n3):
    for y in range(n3):
      Ux=Us[x][v,o].ravel();Uy=Us[y][v,o].ravel()
      R=Hr[x,y]+4*Ux@M@Uy
      Sx,Sy=Sxs[x],Sxs[y]
      T1=np.einsum('ij,ij,i->',Sx[o,o],Sy[o,o],eps[o])*2
      T2=np.einsum('ij,kl,ijkl',Sx[o,o],Sy[o,o],A4[o,o,o,o])
      T4=np.sum(Sx[o,o]*Fsk[y][o,o])+np.sum(Sy[o,o]*Fsk[x][o,o])
      T3=np.einsum('pi,pi,i',Sx[:,o],Sy[:,o],eps[o])
      rows.append([T1,T2,T3,T4]);rhs.append(R)
  c,res,_,_=np.linalg.lstsq(np.array(rows),np.array(rhs),rcond=None)
  print(basis,c, 'max resid',abs(np.array(rows)@c-np.array(rhs)).max())
