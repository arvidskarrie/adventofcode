
from itertools import combinations 
import re
from collections import Counter
import string
from copy import deepcopy

def get_all_preamble_sums(preamble_list):
    sums = []
    preamble_combinations = combinations(preamble_list, 2)

    for combo in preamble_combinations:
        sums.append(sum(combo))
    return sums

def part_1():
    data = []
    preamble_length = 25

    with open("input.txt") as file:
    #with open("input_test.txt") as file:
        for line in file:
            data.append(int(line))
    
    preamble = data[0:preamble_length]

    for i in range(preamble_length, len(data)):
        if not data[i] in get_all_preamble_sums(preamble):
            return data[i]
        else:
            preamble[i%preamble_length] = data[i]

    return preamble

def part_2(part_1_val):
    data = []

    with open("input.txt") as file:
    #with open("input_test.txt") as file:
        for line in file:
            data.append(int(line))

    for i in range(len(data)):
        for j in range (i+1, len(data)):
            cont_sum = sum(data[i:j])
            if cont_sum == part_1_val:
                return min(data[i:j]) + max(data[i:j])
            elif cont_sum > part_1_val:
                break


PART_1_SOLUTION = part_1() # 41682220
print(part_2(PART_1_SOLUTION)) # 892