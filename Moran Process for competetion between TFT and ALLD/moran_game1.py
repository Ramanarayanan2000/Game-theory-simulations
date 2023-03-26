

import numpy as np
import matplotlib.pyplot as plt


#function that takes in pay-off matrix, initensity of selection, number of 
#individuals in the population and no. of A individuals and returns the frequency of A and
#generations as arrays
def moran_process(M,w,N,A_init):
    
    A = A_init
    B = N - A_init
        
    xA = [(A/N)]#list for storing frequency of type A in each generation
    generation = 0
    
    
    
    while A != 0 and B != 0:
        
        #expected payoffs
        F_A = (M[0,0]*(A-1) + M[0,1]*(N-A))/(N-1)
        F_B = (M[1,0]*A + M[1,1]*(B-1))/(N-1)
        
        #fitness
        fA = 1 - w + w*F_A
        fB = 1 - w + w*F_B
        
        mean_fit_A = (fA*A)/(fA*A + fB*B) # mean fitness of A in the population
        mean_fit_B = (fB*B)/(fA*A + fB*B)   # mean fitness of B in the population
        
        
        #probability weights of the 4 possible events
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
        r1 = np.random.rand()
        
        if 0 < r1 <= a:# A dies and A reproduce
            A = A + 0
        if a < r1 <= b:# B dies and B reproduce
            B = B + 0
        if b < r1 <= c:# A dies and B reproduce
            A = A - 1
            B = B + 1
        if c < r1 <=1:# B dies and A reproduce
            A = A + 1
            B = B - 1
            
        generation += 1
        x0 = A/N
        xA.append(x0)
            

            
    return [np.array(xA),np.array(generation)]
            
    
#The prisoner's dilemma matrix elemnts
a = 3
b = 0
c = 5
d = 1

pd = np.array([[a,b],[c,d]])

# expected no. of rounds
m = 10

#pay-off matrix

M = np.array([[m*a,(b + (m-1)*d)],
               [(c + (m-1)*d),m*d]])

#array of population sizes
N = np.array([100,150,200,250, 300, 350, 400,450,500,550,600,650,700,800,900,1000])
#N = np.array([500])
#N =  np.array([100,150,200])
              
#no of trials
Nt = 5000

#intensity of selection
W = [0.01,0.1,1]
evol_rate = np.zeros([len(W),len(N)])
#no of TFT players initially
tft_init = 1

for j in range(len(W)):
    
    w = W[j]
    #stores the simulated invasion probability 
    rho_tft = []
    for k in N:
        #storing the no.of times tft_gets fixed
        tft_fixd = 0
        
        
        for trial in range(1,Nt+1):
            print('N,trial no =',k,trial) 
            simulation = moran_process(M,w,k,tft_init)
            tft_freq = simulation[0]
            if tft_freq[-1] == 1:
                tft_fixd += 1
        
        
        rho_tft.append(tft_fixd/Nt)
         
    evol_rate[j,:] = N*rho_tft   
#print(rho_tft)


plt.figure(figsize=(11, 8.5))
plt.plot(N,evol_rate[0,:],label = 'w = '+str(W[0]),lw = 3)
plt.plot(N,evol_rate[1,:],label = 'w = '+str(W[1]),lw=3)
plt.plot(N,evol_rate[2,:],label = 'w = '+str(W[2]),lw=3)
plt.xlabel('Population Size, N',fontsize = 25)
plt.xticks(fontsize = 20)
plt.ylabel( 'Rate of Evolution, N'+r'$\rho_{TFT}$',fontsize = 25)
plt.yticks(fontsize = 20)
plt.grid(True)
plt.title('Rate of Evolution vs Population size',fontsize = 25) 
plt.legend(prop = {'size':20}) 
plt.savefig('evolrate_vs_popsize') 
plt.show()


    
    
    
    
    
    
    
    
    
    
    
    
    
    