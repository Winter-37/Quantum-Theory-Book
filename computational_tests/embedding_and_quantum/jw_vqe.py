"""Jordan-Wigner Hamiltonian of H2/STO-3G built from scratch, Pauli decomposition, and a one-parameter UCCD VQE."""
import numpy as np, itertools
from scipy.optimize import minimize_scalar
from pyscf import gto, scf, fci, ao2mo
I2=np.eye(2); X=np.array([[0,1],[1,0]]); Y=np.array([[0,-1j],[1j,0]]); Z=np.diag([1,-1]); P={'I':I2,'X':X,'Y':Y,'Z':Z}
def kron(*m):
    out=np.array([[1.]]);
    for a in m: out=np.kron(out,a)
    return out
def annihilator(j,n):            # qubit j = spin orbital j; |1> occupied; JW string of Z on qubits < j
    lower=np.array([[0,1],[0,0]])  # |0><1| : removes an electron
    return kron(*([Z]*j+[lower]+[I2]*(n-j-1)))
mol=gto.M(atom='H 0 0 0; H 0 0 0.735',basis='sto-3g',verbose=0); mf=scf.RHF(mol).run()
C=mf.mo_coeff; h=C.T@mf.get_hcore()@C; g=ao2mo.restore(1,ao2mo.kernel(mol,C),2)
n=4  # spin orbitals: 0=1a,1=1b,2=2a,3=2b  (orbital = so//2, spin = so%2)
a=[annihilator(j,n) for j in range(n)]; ad=[x.conj().T for x in a]
H=mol.energy_nuc()*np.eye(16)
for p,q in itertools.product(range(n),repeat=2):
    if p%2==q%2: H+=h[p//2,q//2]*ad[p]@a[q]
for p,q,r,s in itertools.product(range(n),repeat=4):
    if p%2==q%2 and r%2==s%2: H+=0.5*g[p//2,q//2,r//2,s//2]*ad[p]@ad[r]@a[s]@a[q]
Nop=sum(ad[j]@a[j] for j in range(n))
# check anticommutation
print('max |{a_i,a_j^+}-delta|', max(np.abs(a[i]@ad[j]+ad[j]@a[i]-(i==j)*np.eye(16)).max() for i in range(n) for j in range(n)))
w,v=np.linalg.eigh(H); efci=fci.FCI(mf).kernel()[0]
Nv=np.real(np.einsum('ik,ij,jk->k',v.conj(),Nop,v)); i2=np.argmin(np.where(np.abs(Nv-2)<1e-8,w,np.inf))
print('E_FCI pyscf',efci,'  lowest eigenvalue of JW H in N=2:',w[i2],' overall lowest',w[0],'N of overall lowest',Nv[0])
# Pauli decomposition
terms={}
for lab in itertools.product('IXYZ',repeat=n):
    c=np.trace(kron(*[P[l] for l in lab])@H)/16
    if abs(c)>1e-10: terms[''.join(lab)]=c
print('number of Pauli strings (incl. identity):',len(terms)); 
for k,c in sorted(terms.items(),key=lambda t:-abs(t[1]))[:6]: print('  ',k,np.round(c.real,6))
# basis state index: qubit 0 is the most significant bit in kron order
def ket(bits): e=np.zeros(16); e[int(''.join(map(str,bits)),2)]=1; return e
hf=ket([1,1,0,0]); print('<HF|H|HF> =',hf@H@hf,' E_RHF =',mf.e_tot)
# UCCD: T = t a2a+ a2b+ a1b a1a ; U = exp(t(T - T^+))
T=ad[2]@ad[3]@a[1]@a[0]; A=T-T.conj().T
from scipy.linalg import expm
E=lambda t: np.real((expm(t*A)@hf).conj()@H@(expm(t*A)@hf))
r=minimize_scalar(E,bounds=(-1,1),method='bounded',options={'xatol':1e-12})
print('VQE-UCCD theta=%.8f  E=%.12f  E-E_FCI=%.2e'%(r.x,r.fun,r.fun-efci))
# shot cost: variance of H in the optimal state, shots for 1.6 mEh (chemical accuracy) with a single-measurement estimator bound
psi=expm(r.x*A)@hf; var=np.real(psi.conj()@H@H@psi-(psi.conj()@H@psi)**2)
print('Var(H) in exact ground state', var, '(zero for an eigenstate)')
# per-term sampling: sum |c_i| bound
lam=sum(abs(c) for k,c in terms.items() if k!='IIII'); print('sum|c_i| (non-identity) =',lam,'  shots for eps=1.6e-3 with naive term-by-term sampling <= (sum|c|/eps)^2 =', (lam/1.6e-3)**2)
