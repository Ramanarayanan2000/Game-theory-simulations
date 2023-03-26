

import numpy as np
import random as rand
import matplotlib.pyplot as plt


Nt = 1000#number of trials
N = 100# Total no. of individuals in the population
r = 0.99# The fitness of type 0 or type A

#function which takes in population size, fitness and number of individuals of type 0
#as input and returns the fixation probability of type 0
def fixn(popsize,fit,i):
    x_i = (1 - (1/fit**i))/(1 - (1/fit**popsize))
    return round(x_i,3)
    
theo_invsn_prob = round((1 - (1/r))/(1 - (1/(r**N))),3)#theoretical value of invasion probability of type 0 rounded to 3 decimal places

a_fixd = 0# counts the no. of times A gets fixed
for t in range(1,Nt + 1):
    
    A = int(N/2)# No. of A or 0 type initially in the population
    B = int(N/2)# No. of B or 1 type initially in the population
    
    xA = [(A/N)]#list for storing frequency of type A in each generation
    xB = [(B/N)]#list for storing frequency of type B in each generation
    
    iteratn = 0
    while A != 0 and B != 0:
        
        
        
        mean_fit_A = r*A/(r*A + B) # mean fitness of A in the population
        mean_fit_B = B/(r*A + B)   # mean fitness of B in the population
        
        
        #probability weights
        p1 = (A/N)*mean_fit_A # A dies and A reproduce
        p2 = (B/N)*mean_fit_B # B dies and B reproduce
        p3 = (A/N)*mean_fit_B # A dies and B reproduce
        p4 = (B/N)*mean_fit_A # B dies and A reproduce
        
        #defining points that would split [0,1] into intervals of length 
        #corresponding to the probability weights
        a = p1
        b = p1 + p2
        c = p1 + p2 + p3
        
        #updating A and B
        r1 = rand.random()
        
        if 0 < r1 <= a:
            A = A + 0
        if a < r1 <= b:
            B = B + 0
        if b < r1 <= c:
            A = A - 1
            B = B + 1
        if c < r1 <=1:
            A = A + 1
            B = B - 1
         
    
        x0 = A/N
        x1 = B/N
        xA.append(x0)
        xB.append(x1)
        
        if t == 1:# for counting the no.of generation before fixation in trial 1
            iteratn += 1

    if A == N:
        a_fixd += 1
    
    # Plotting the evolution of frequencies just for trial 1
    if t == 1:
        genertn = [i for i in range(iteratn+1)]
        plt.figure(figsize=(11, 8.5))
        plt.plot(genertn,xA,label = 'type 0')
        plt.plot(genertn,xB,label = 'type 1')
        plt.xlabel('Generation',fontsize = 15)
        plt.ylabel('Frequency',fontsize = 15)
        plt.grid(True)
        plt.legend()
        plt.title('Moran process, Population size ='+str(N)+', r ='+str(r),fontsize = 20)  
        name = 'moran_r_'+str(r)+'.png'
        plt.savefig(name) 
        plt.show()

    #print('trial_num =',t)# can uncommend this to see the progress of the simulation while the code is running if required
        
frac_0 = a_fixd/Nt
frac_1 = 1 - frac_0
fix_0 = fixn(N, r, N/2)
print('Fraction of times type O was fixed = ',frac_0)
print('Fraction of times type 1 was fixed = ',frac_1)
print('Theoretical fixation probability of type 0 = ',fix_0)    