import math
import sys

def average(list):
    average = sum(list)/len(list)
    return average

def mean_of_squares(list):
    list_squared = [i*i for i in list]
    list_squared_average = sum(list_squared)/len(list_squared)
    return list_squared_average

def f_range(start, stop, step):
    while start < stop:
        yield start
        start += step

#kT = float(sys.argv[1])
for kT in f_range(0.01, 0.3, 0.01):
    data = open('n_200_en_vs_kT_at_%f' % kT)

    data_list = []
    mag_list = []
    blocked_mag_list = []

    thermalization = 10
    block = 30
#blocklist = [1,2,5,10,25,30,40,45]
    total = 0
    i = 0

#Append values from data to a list called data_list
    for values in data:
        data_list.extend(values.split())
    data_list = [float(i) for i in data_list]
#print(data_list)

#Take important pts from data_list (post-thermalization) and place them into a new list, mag_list
    for elements in range(thermalization,len(data_list)):
        mag_list.append(data_list[elements])

#Blocking Code
    for i in range(0, len(mag_list), block):
        if i + (block - 1) < len(mag_list):
            for j in range(block):
                total += mag_list[i + j]
            blocked_mag_list.append(total/block)
            total = 0

    sigma = math.sqrt((mean_of_squares(blocked_mag_list) - average(blocked_mag_list)*average(blocked_mag_list))/(len(blocked_mag_list) - 1))
#print(block, sigma)
#print(block, sigma, average(blocked_mag_list), len(mag_list), len(blocked_mag_list))
    print(kT, average(blocked_mag_list))
    blocked_mag_list = []
    data_list = []
    mag_list = []

    data.close()

