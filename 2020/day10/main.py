
from itertools import combinations 
import re
from collections import Counter
import string
from copy import deepcopy

def find_neighbour_difference(data, val):
    matches = 0
    for i in range(len(data)-1):
        if data[i+1] - data[i] == val:
            matches += 1

    return matches

def find_suites(unnecessary_list):
    suite_list = []
    suite_length = 1
    for i in range(1, len(unnecessary_list)):
        if unnecessary_list[i] - unnecessary_list[i-1] == 1:
            suite_length += 1
        else:
            print(suite_length, unnecessary_list[i-1])
            suite_list.append(suite_length)
            suite_length = 1
            
    suite_list.append(suite_length)

    suite_list.sort()
    return suite_list

def find_unnecessary_values(data):
    unnecessary_list = []
    for i in range(1, len(data)-1):
        if data[i+1] - data[i-1] <= 3:
            unnecessary_list.append(data[i])

    return find_suites(unnecessary_list)

def part_1():
    data = []

    #with open("input.txt") as file:
    with open("input_test.txt") as file:
        for line in file:
            data.append(int(line.rstrip()))
    
    data.append(0)
    data.sort()
    data.append(data[-1] + 3)

    print(data)

    return find_neighbour_difference(data, 1) * find_neighbour_difference(data, 3)

def part_2():
    data = []

    with open("input.txt") as file:
    #with open("input_test.txt") as file:
        for line in file:
            data.append(int(line.rstrip()))
    
    data.append(0)
    data.sort()
    data.append(data[-1] + 3)

    print(data)

    return find_unnecessary_values(data)


#print(part_1()) # 2277
print(part_2()) # 892