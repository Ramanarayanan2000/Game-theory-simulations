

import matplotlib.pyplot as plt
import random as r
import numpy as np

T = 2000
N = np.array([50,100,200,300,400,600, 800,1000, 5000])#array of various population sizes
inverse_N = 1/N
gen = np.array([n for n in range(T+1)])

N_T = 100

u1 = 0.003
u2 = 0.001

#theoretical values of equilibrium frequencies
theo_xA = u2/(u1+u2)
theo_xB = 1 - theo_xA

variance = []

for k in N:
    equilbr_freq = np.zeros(N_T)
    for nt in range(N_T):

        
        populn = np.array([0]*int(k/2) + [1]*int(k/2))#initial population 
       
        
        for i in range(1,T+1):
            for j in range(k):
                
                if populn[j] == 0:
                    r1 = r.random()
                    if r1 < u1:
                        populn[j] = 1

                if populn[j] == 1:
                    r2 = r.random()
                    if r2 < u2:
                        populn[j] = 0
             
           
        
        equilbr_freq[nt] = sum(populn)/k# Assuming the equilibriated timestep to be 2000
        print('trial_num for N ='+str(k)+', =',nt)
    
    
    mean = np.mean(equilbr_freq)#returns the mean equilibrum frequency averaged over N_T trials
    var = np.var(equilbr_freq)#returns the variance of equilibrum frequency averaged over N_T trials
    
    variance.append(var)
    
#Plotting and fitting to a straight line
    
coef = np.polyfit(inverse_N,variance,1)#stores the value of the fitted value of coefficients in the linear fit
poly1d_fn = np.poly1d(coef) 
# poly1d_fn is now a function which takes in coef and returns an estimate for y

print('linear fit parameter, Slope = ',coef[0])
print('linear fit parameter, Intercept = ',coef[1])

plt.plot(inverse_N,variance, 'yo')
plt.plot( inverse_N, poly1d_fn(inverse_N), '--k',label = 'Linear fit')
plt.xlabel('$N^{-1}$')
plt.ylabel('variance')
plt.grid(True)
plt.title('Plot of variance of Equilibrium frequency of type 1 vs $N^{-1}$')
plt.legend()
plt.savefig('var_vs_pop.png')
plt.show()
    

