# Game theory simulation

import numpy as np
import matplotlib.pyplot as plt

#The prisoner's dilemma matrix elemnts
a = 3
b = 0
c = 5
d = 1

pd = np.array([[a,b],[c,d]])

# expected no. of rounds
m = 6


#payoff matrix
M = np.array([[m*a,m*a,(b+(m-1)*d)],
              [m*a,m*a,m*b],
              [(c+(m-1)*d),m*c,m*d]])

def replicator_eqn(x,M):
    
    
    x = np.transpose(x)
    fit = np.matmul(M,x)#returns column vector whose elements are fitness of each phenotype
    phi = np.dot(x,fit)#returns sum of xi*fitness(xi) = avg. payoff/population payoff
    
    dx = np.multiply(x,fit) - x*phi #the replicator eqn vector
    
    return dx



#solving the replicator eqns using euler method

dt = 0.01
time = 10
t = int(time/dt)

#initial 
x1 = 1/3
x2 = 1/3
x3 = 1/3
x_init = np.array([x1,x2,x3])
freq = np.zeros([t+1,3])
x = x_init
freq[0,:] = x_init

for i in range(t):
    
    freq[i+1,:] = freq[i,:] + dt*replicator_eqn(freq[i,:],M)
 
plt.figure(figsize=(11, 8.5))
plt.plot(freq[:,0],label = 'TFT',lw =3)
plt.plot(freq[:,1],label = 'ALLC',lw = 3)
plt.plot(freq[:,2],label = 'ALLD',lw =3) 
plt.xlabel('Generations',fontsize = 25)
plt.xticks(fontsize = 20)
plt.ylabel('Frequencies',fontsize = 25)
plt.yticks(fontsize = 20)
plt.title('TFT vs ALLC vs ALLD, m = 6',fontsize = 25) 
plt.legend(prop = {'size':20})
plt.savefig('Replicator solution m = 6')


    
    
    
    
    
    
    