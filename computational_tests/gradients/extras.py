import sys; sys.path.insert(0,'.')
from common import *
from pyscf import scf
# (a) RHF gradient decomposition, STO-3G and 6-31G, O_z and H1_y
for basis in ('sto-3g','6-31g'):
    mol=water(basis); mf=rhf(mol); C,eps=mf.mo_coeff,mf.mo_energy; nocc=5; o=slice(0,nocc)
    dS,dh,dg=skeleton_ao(mol,mf)
    P=2*C[:,o]@C[:,o].T; W=2*C[:,o]@np.diag(eps[o])@C[:,o].T
    nuc=nuc_grad(mol)
    for x,lab in ((2,'O_z'),(4,'H1_y')):
        one=np.sum(P*dh[x]); two=0.5*np.einsum('mn,ls,mnls',P,P,dg[x])-0.25*np.einsum('ml,ns,mnls',P,P,dg[x]); ws=-np.sum(W*dS[x])
        print(basis,lab,f'one {one:.6f} two {two:.6f} -WS {ws:.6f} nuc {nuc[x]:.6f} total {one+two+ws+nuc[x]:.6f}')
# (b) static polarizability alpha_zz by CPHF vs finite field, 6-31G
mol=water('6-31g'); mf=rhf(mol); C,eps=mf.mo_coeff,mf.mo_energy; nocc=5; n=C.shape[1]
eri=eri_mo(C,mol.intor('int2e')); M=cphf_matrix(eps,eri,nocc)
mol.set_common_orig((0,0,0)); r=mol.intor('int1e_r')
alpha=np.zeros((3,3)); U=[]
for k in range(3):
    hf_=mo_transform(C,r[k]); B=-hf_[nocc:,:nocc]          # perturbation h -> h + F r_k, S^F = 0, skeleton F^F = r
    U.append(np.linalg.solve(M,B.ravel()))
for k in range(3):
    for l in range(3):
        alpha[k,l]=-4*U[k]@mo_transform(C,r[l])[nocc:,:nocc].ravel()   # alpha = -d2E/dF dF
f=1e-3; E={}
for s in (1,0,-1):
    m=scf.RHF(mol); hc=m.get_hcore()+s*f*r[2]; m.get_hcore=lambda *a,hc=hc:hc; m.conv_tol=1e-13; m.kernel(); E[s]=m.e_tot
print('alpha (CPHF):',np.diag(alpha),' finite-field alpha_zz:',-(E[1]-2*E[0]+E[-1])/f**2)
# (c) iterations of a plain Jacobi-preconditioned solve vs direct, sizes
print('6-31G CPHF dim',M.shape, 'min eigenvalue of M',np.linalg.eigvalsh(M).min())
