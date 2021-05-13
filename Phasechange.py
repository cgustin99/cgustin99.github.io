import random
import math

x_list = []
y_list = []

n = 100 #number of particles
d = 0.025 #radius of particles
k = 1.0
r_0 = 0.05
kT = 0.2

a = 0 #Counter

energy = 0 #Initial Potential
energy_prime = 0
e = 0
e_prime = 0
deltaE = 0
energy_from_scratch = 0


for elements in range(1, n + 1):
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    x_list.append(x)
    y_list.append(y)

for particles in range(n):
    for i in range(particles + 1, n):
        radius_x = abs(x_list[particles] - x_list[i])
        radius_y = abs(y_list[particles] - y_list[i])
        radius = math.sqrt(radius_x * radius_x + radius_y * radius_y)
        energy = k*(math.pow((r_0/radius), 12) - math.pow((r_0/radius), 6)) + energy
#print("energy original =", energy)

#Initialize
'''for i in range(1, n):
    print("c3", x_list[i], y_list[i], "0", d)
print("F")'''

#while True:
for a in range(100000):
    j = random.randint(0, n - 1)
    #print("j:", j)
    
    for m in range(n):
        if m != j:
            r_x = abs(x_list[j] - x_list[m])
            r_y = abs(y_list[j] - y_list[m])
            r = math.sqrt(r_x * r_x + r_y * r_y)
            e = k*(math.pow((r_0/r), 12) - math.pow((r_0/r), 6)) + e
#print("e:", e)

    random_x = x_list[j]
    random_y = y_list[j]

    rsuggest_x = random.uniform(-1e-2,1e-2)
    rsuggest_y = random.uniform(-1e-2,1e-2)
    new_x_position = random_x + rsuggest_x
    new_y_position = random_y + rsuggest_y
    

    if -1 <= new_x_position <= 1 and -1 <= new_y_position <= 1:
        x_list[j] = new_x_position
        y_list[j] = new_y_position
        
        for h in range(n):
            if h!= j:
                r_new_x = abs(x_list[j] - x_list[h])
                r_new_y = abs(y_list[j] - y_list[h])
                r_new = math.sqrt(r_new_x * r_new_x + r_new_y * r_new_y)
                e_prime = k*(math.pow((r_0/r_new), 12) - math.pow((r_0/r_new), 6)) + e_prime
#print("e_prime:", e_prime)

        deltaE = e_prime - e
#print("deltaE:", deltaE)
        energy_prime = energy + deltaE
#print("energy =", energy, "energy_prime =", energy_prime)
        #print("POS DIFFERENCE:",(energy_prime - energy)/kT)
#print("NEG DIFFERENCE:", -(energy_prime - energy)/kT)
        
        if energy_prime < energy:
            energy = energy_prime
#print("accept 1")
        elif energy_prime > energy:
            u = random.random()
            P = math.exp(-(energy_prime - energy)/kT)
            #print("u:", u, "P:", P)
            if u < P:
                energy = energy_prime
            #print("accept 2")
            elif u > P:
                x_list[j] = random_x
                y_list[j] = random_y
#print("reject")

        energy_prime = deltaE = e = e_prime = 0
        

        #Animate
        
    


    else:
        e = 0

    if a % 1000 == 0:
        '''for i in range(n):
            print("c3", x_list[i], y_list[i], "0", d)
            print("T -1 -1")
            print("Energy: ", energy)
        print("F")'''
        print(energy)

