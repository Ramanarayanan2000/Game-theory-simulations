

import numpy as np
import random as r
import matplotlib.pyplot as plt

N = 500# Total no. of individuals in the population

A = int(N/2)# No. of A or 0 type initially in the population
B = int(N/2)# No. of B or 1 type initially in the population

xA = [(A/N)]#list for storing frequency of type A in each generation
xB = [(B/N)]#list for storing frequency of type B in each generation

iteratn = 0
while A != 0 and B != 0:
    
    #probability weights
    p1 = (A/N)*(A/N) # A dies and A reproduce
    p2 = (B/N)*(B/N) # B dies and B reproduce
    p3 = (A/N)*(B/N) # A dies and B reproduce
    p4 = (B/N)*(A/N) # B dies and A reproduce
    
    #defining points that would split [0,1] into intervals of length 
    #corresponding to the probability weights
    a = p1
    b = p1 + p2
    c = p1 + p2 + p3
    
    #updating A and B
    r1 = r.random()
    
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
    iteratn += 1
    
    
genertn = [i for i in range(iteratn+1)]

plt.plot(genertn,xA,label = 'type 0')
plt.plot(genertn,xB,label = 'type 1')
plt.xlabel('generation')
plt.ylabel('frequency')
plt.grid(True)
plt.legend()
plt.title('Evolution by Moran process, Population size ='+str(N))  
plt.savefig('moran process.png') 
plt.show()
     
        
        
        
        
        
        
        
        
        
        
        
        
        
    
