import random
import math

def f_range(start, stop, step):
    while start < stop:
        yield start
        start += step

run = True

r = 0.1
x = []
y = []

energy = 0
energy_prime = 0
deltaE = 0

kT = 3.25

#Initialize Balls
for i in f_range(-3,3.1,0.25):
    x.append(i)
for j in f_range(-3,3.1,0.25):
    y.append(j)

'''print("F")
for i in range(len(x)):
    for j in range(len(y)):
        print("c3", x[i], y[j], "0", r)
        print("C 0 0 1")
print("F")'''

n = len(x)
spin_list = []

for i in range(n*n):
    spin_list.append(1)

#Initial energy of configuration with all up-spins
for i in range(n):
    for j in range(n):
        if i > 0:
            energy = energy - spin_list[i + j*n]*spin_list[(i-1) + j*n]
        if j > 0:
            energy = energy - spin_list[i + j*n]*spin_list[i + (j-1)*n]

#Metropolis Algorithm
#a = 0
#while run == True:
#a += 1
for a in range(10000000):
    
    up = 0
    down = 0
    
    i_chosen = random.randrange(n)
    j_chosen = random.randrange(n)

    spin_list[i_chosen + j_chosen*n] = -spin_list[i_chosen + j_chosen*n]
    
    #Energy_prime calculation
    if i_chosen + 1 < n:
        deltaE += spin_list[i_chosen + j_chosen*n]*spin_list[(i_chosen+1) + j_chosen*n]
    if i_chosen - 1 >= 0:
        deltaE += spin_list[i_chosen + j_chosen*n]*spin_list[(i_chosen-1) + j_chosen*n]
    if j_chosen + 1 < n:
        deltaE += spin_list[i_chosen + j_chosen*n]*spin_list[(i_chosen) + (j_chosen+1)*n]
    if j_chosen - 1 >= 0:
        deltaE += spin_list[i_chosen + j_chosen*n]*spin_list[(i_chosen) + (j_chosen-1)*n]

    deltaE = 2*deltaE
    energy_prime = energy - deltaE

    #Conditionals to test energy_prime vs. energy
    if energy_prime < energy:
        spin_list[i_chosen + j_chosen*n] = spin_list[i_chosen + j_chosen*n]
        energy = energy_prime
    elif energy_prime > energy:
        u = random.random()
        P = math.exp(-(energy_prime - energy)/kT)
        if u < P:
            spin_list[i_chosen + j_chosen*n] = spin_list[i_chosen + j_chosen*n]
            energy = energy_prime
        elif u > P:
            spin_list[i_chosen + j_chosen*n] = -spin_list[i_chosen + j_chosen*n]

    energy_prime = 0
    deltaE = 0
    
    if a % 1000 == 0:
        for i in range(len(x)):
            for j in range(len(y)):
                if spin_list[i + j*n] == 1:
                    up += 1
                    #print("C 0 0 1")
                    #print("c3", x[i], y[j], "0", r)
                elif spin_list[i + j*n] == -1:
                    down += 1
                    #print("C 1 0 0")
                    #print("c3", x[i], y[j], "0", r)
        abs_mag = abs((up-down)/len(spin_list))
        '''print("C 1 1 1")
        print("T -1 -1")
        print("suggestions: ", a)
        print("C 1 1 1")
        print("T 0.1 -1")
        print("abs_mag =", abs_mag)
        print("F")'''

        abs_mag = abs((up-down)/len(spin_list))
        print(abs_mag)