

import numpy as np
import matplotlib.pyplot as plt
import random as r

#All the 3 parts can be simulated using this scrip by appropriately commenting
#uncommenting the necessary variables for that part

#part1
#N = 10000
#f0 = 1.001
#f1 = 1
#u01 = 0.01
#u10 = 0
#init_pop = np.zeros(N) #initial pop

#part2
N = 10000
f0 = 1.1
f1 = 1
u01 = 0.01
u10 = 0
init_pop = np.array([0]*int(N/2)+[1]*int(N/2)) #initial pop

#part3
#N = 100
#f0 = 1.1
#f1 = 1
#u01 = 0.01
#u10 = 0
#init_pop = np.array([0]*int(N/2)+[1]*int(N/2)) #initial pop

norm_fit0 = f0/(f1+f0) 
norm_fit1 = f1/(f1+f0)

#a = np.zeros(N)#trial
#rn = np.random.rand(1,4)#trial


def mutation_of_individual(individual,u01,u10):
    
    if individual == 0:
        r1 = np.random.rand()
        if r1 < u01:
            individual = 1
            
    else :
        r2 = np.random.rand()
        if r2 < u10:
            individual = 0
            
    return individual

mutated_pop = np.vectorize(mutation_of_individual)



def single_reproduction_event_generator(parent_pop,norm_fit0,norm_fit1):
    
    birth_happened = False
    
    while not birth_happened:
        indx = np.random.randint(0,N)
        prospective_parent = parent_pop[indx]
        
        if prospective_parent == 0:
            r3 = np.random.rand()
            if r3 < norm_fit0:
                birth_happened = True
                
        else :
            r4 = np.random.rand()
            if r4 < norm_fit1:
                birth_happened = True

    child = prospective_parent
    
    return  child

#Evolving the population


epsilon = 1/N * 0.1

parent_popln = init_pop
equilibrium = False
generation = 0
freq_1 = [sum(parent_popln)/N]
while not equilibrium:
    
    #mutation of the parents
    parent_popln = mutated_pop(parent_popln,u01,u10)
    
    #selection to offspring
    offspring_pop = np.zeros(N)# a dummy array which will be updated to final offsprings.
    for i in range(N):
        offspring_pop[i] = single_reproduction_event_generator(parent_popln,norm_fit0,norm_fit1)
    
    x1 = sum(offspring_pop)/N
    freq_1.append(x1)
    
    if generation > 50:
        if np.std(freq_1[-5:]) < epsilon:
            equilibrium = True
    
    if generation > 2000:
        equilibrium = True
    
    print(generation)
    generation += 1
    parent_popln = offspring_pop
    
freq_0 = 1 - np.array(freq_1)

q = 1 - u01
theo_freq0 = round((f0*q - 1)/(f0 - 1),4)
theo_freq1 = round(1 - theo_freq0,4)

if f0*q > 1:
    print('f0q > 1, Coexistence is possible')
    print('The theoretical equilibrium frequency of type 0 = ',theo_freq0)
    print('The theoretical equilibrium frequency of type 0 = ',theo_freq1)
else :
    print('f0q < 1, coexistence not possible')

theo_freq0 = (f0*q - 1)/(f0 - 1)
theo_freq1 = 1 - (f0*q - 1)/(f0 - 1)

array0 = theo_freq0*np.ones(generation+1)
array1 = theo_freq1*np.ones(generation+1)

gen = np.array([g for g in range(generation+1)]) 
plt.figure(figsize=(11, 8.5))
plt.plot(gen,freq_0,label = 'type 0')
plt.plot(gen,freq_1,label = 'type 1')
if f0*q > 1:
    plt.plot(gen,array0,label ='equilbrm freq of 0')
    plt.plot(gen,array1,label ='equilbrm freq of 1')
plt.xlabel('Generations',fontsize = 20)
plt.xticks(fontsize = 15)
plt.ylabel('Frequency',fontsize = 20)
plt.yticks(fontsize = 15)
plt.grid(True)
plt.legend(prop = {'size':20})
plt.title('Error Threshold simulation, N ='+str(N)+', u ='+str(u01)+', f0 = '+str(f0),fontsize = 20)  
name = 'errorthresh_'+str(u01)+'_'+str(f0)+'_'+str(N)+'.png'
plt.savefig(name) 
plt.show()
    












