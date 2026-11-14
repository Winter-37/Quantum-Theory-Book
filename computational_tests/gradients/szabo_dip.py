import sys; sys.path.insert(0,'.')
from common import *
from ci_grad import CISDState, gradients, relaxed_density_gradient
mol=water('sto-3g',R=1.809,theta=104.52)
st=CISDState(mol); st.response_setup()
gU,gz,X,L,z,_=gradients(st); _,Dp=relaxed_density_gradient(st,z,X,L)
for orig in ((0,0,0), tuple(mol.atom_coords().T@mol.atom_mass_list()/mol.atom_mass_list().sum())):
    mol.set_common_orig(orig); r=mol.intor('int1e_r')
    print(orig, 'unrelaxed',np.sum(st.D*mo_transform(st.C,r[2])),'relaxed',np.sum(Dp*mo_transform(st.C,r[2])))
