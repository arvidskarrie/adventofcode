
from itertools import combinations 
import re
from collections import Counter
import string
from copy import deepcopy
from math import gcd

def lcm(a, b):
    return abs(a*b) // gcd(a, b)

def part_1():    
    #with open("input_test.txt") as file:
    with open("input.txt") as file:
        start_time = int(file.readline().rstrip())
        bus_list_unfiltered = file.readline().rstrip()
                 
        bus_list_unfiltered = re.split(',|x', bus_list_unfiltered.rstrip()) 

    bus_list = []
    for bus in bus_list_unfiltered:
        if bus:
            bus_list.append(int(bus))

    # Find if any bus leaves at requested time
    time = start_time
    while True:
        for bus in bus_list:
            if time % bus == 0:
                return bus, time - start_time, bus * (time - start_time)
        time += 1

def part_2():    
    #with open("input_test.txt") as file:
    with open("input.txt") as file:
        _old_start_time = file.readline().rstrip()
        bus_list_unfiltered = file.readline().rstrip()
                 
        bus_list_unfiltered = re.split(',', bus_list_unfiltered.rstrip()) 

    bus_list = []
    for bus in bus_list_unfiltered:
        if bus:
            if bus == 'x':
                bus_list.append(1)
            else:
                bus_list.append(int(bus))

    minimum_base_number = 1
    lowest_common_multiple = 1
    for bus_index in range(len(bus_list)):
        while(True):
            if (minimum_base_number + bus_index) % bus_list[bus_index] == 0:
                lowest_common_multiple = lcm(lowest_common_multiple, bus_list[bus_index])
                break
            else:
                minimum_base_number += lowest_common_multiple

    return minimum_base_number





            
            


#print(part_1()) # 153
print(part_2()) # 29839 