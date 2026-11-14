import numpy as np
from scipy.optimize import minimize
exec(open('jw_vqe.py').read().split("# Pauli decomposition")[0])
def ry(t): c,s=np.cos(t/2),np.sin(t/2); return np.array([[c,-s],[s,c]])
def cnot(c,t,n=4):
    P0=np.diag([1,0]);P1=np.diag([0,1]); op0=[I2]*n; op1=[I2]*n; op0[c]=P0; op1[c]=P1; op1[t]=X
    return kron(*op0)+kron(*op1)
ent=cnot(2,3)@cnot(1,2)@cnot(0,1)
def state(th,L):
    psi=np.zeros(16); psi[int('1100',2)]=1
    for l in range(L):
        psi=ent@kron(*[ry(t) for t in th[4*l:4*l+4]])@psi
    return psi
for L in (1,2,3):
    best=None
    for s in range(20):
        r=minimize(lambda t: state(t,L)@H@state(t,L), np.random.default_rng(s).normal(0,0.3,4*L), method='BFGS',options={'gtol':1e-10})
        if best is None or r.fun<best.fun: best=r
    psi=state(best.x,L); print(f"HEA L={L} ({4*L} params): E-E_FCI={best.fun-efci:.2e}  <N>={psi@Nop@psi:.6f}  Var(N)={psi@Nop@Nop@psi-(psi@Nop@psi)**2:.2e}")
