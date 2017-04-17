import numpy as np
import matplotlib.pyplot as plt


size=150# Size of lattice along x direction

alpharr=np.zeros(101)

for i in range(1,101):
		alpharr[i]=i/100.0
		
print alpharr

nu_arr=np.linspace(0,2*np.pi,50)
print nu_arr


def pbc(i):
	if i==(size):
		return(0)
	elif i==-1:
		return(size-1)
	else:
		return(i)



def Hamiltonian(alpha,nu):
	H=np.zeros((size,size))
	for i in range(0,size):
		H[i,i]=2*np.cos((2*np.pi*(i+1)*alpha)-nu)+2.0*np.cos(2*np.pi*(i+1)/np.sqrt(7))
		H[i,pbc(i+1)]=1.0
		H[i,pbc(i-1)]=1.0
	
	return(H)


y_vals=np.zeros(size)
x_vals=np.zeros(size)

for alpha in alpharr:
	y_vals[:]=alpha
	for nu in nu_arr:  #Diagonalze Hamiltonain. Plot energies for each alpha ..(\eps,\alpha)
		x_vals=np.linalg.eigvalsh(Hamiltonian(alpha,nu))
		plt.plot(x_vals,y_vals,'ko',markersize=0.2)

plt.show()
	


	
