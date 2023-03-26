
import numpy as np
import random as r
import matplotlib.pyplot as plt

Nt = 100
a_fixd = 0# counts the no. of times A gets fixed



for t in range(1,Nt+1):
    N = 500# Total no. of individuals in the population

    A = int(N/2)# No. of A or 0 type initially in the population
    B = int(N/2)# No. of B or 1 type initially in the population

    xA = [(A/N)]
    xB = [(B/N)]
    iteratn = 0
    while A != 0 and B != 0:
        
        #probability weights
        p1 = (A/N)*(A/N) # A dies and A reproduce
        p2 = (B/N)*(B/N) # B dies and B reproduce
        p3 = (A/N)*(B/N) # A dies and B reproduce
        p4 = (B/N)*(A/N) # B dies and A reproduce
        
        
        a = p1
        b = p1 + p2
        c = p1 + p2 + p3
        
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
         
        #print(A)
        x0 = A/N
        x1 = B/N
        xA.append(x0)
        xB.append(x1)    
        iteratn += 1
        #print(iteratn)
    if A == N:
        a_fixd += 1
    print('trial_num =',t)

fixatn_fracA = a_fixd/Nt
fixatn_fracB = (Nt - a_fixd)/Nt
    
print('fraction of times type 0 was fixed = ',fixatn_fracA)
print('fraction of times type 1 was fixed = ',fixatn_fracB)
        
