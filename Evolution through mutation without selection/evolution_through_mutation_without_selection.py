


import matplotlib.pyplot as plt
import random as r

T = 2000
gen = [n for n in range(2001)]

#part a
#u1 = 0.003
#u2 = 0.001
#N = [50,1000,10000]#list of various population sizes

#part b
u1 = 0.07
u2 = 0.001
N = [1000]#list of various population sizes

#theoretical values of equilibrium frequencies
theo_xA = u2/(u1+u2)
theo_xB = 1 - theo_xA
for k in N:
    populn = [0]*int(k/2) + [1]*int(k/2)#initial population 
    #lists for storing frequencies of A and B
    x_A = []
    x_B = []
    for i in range(T+1):
        for j in range(k):
            
            if populn[j] == 0:
                r1 = r.random()
                if r1 < u1:
                    populn[j] = 1

            if populn[j] == 1:
                r2 = r.random()
                if r2 < u2:
                    populn[j] = 0
         
        xA = 1 - sum(populn)/k            
        xB = sum(populn)/k
        
        x_A.append(xA)
        x_B.append(xB)
    plt.figure(k) 
    plt.grid(True)
    plt.title('N ='+str(k))
    plt.plot(gen,[theo_xA]*2001,label = 'theoretical equilibrium xA = ' + str(theo_xA),linestyle = 'dashed')
    plt.plot(gen,[theo_xB]*2001,label = 'theoretical equilibrium xB = ' + str(theo_xB),linestyle = 'dashed')
    plt.plot(gen,x_A,label = 'xA')
    plt.plot(gen,x_B,label = 'xB')
    plt.legend()
    #plt.savefig('popsize_'+str(k)+'.png',format = 'png')
    plt.show()
    
    print('Freq of A=',xA,'Freq of B=',xB)
