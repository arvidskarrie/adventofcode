
from itertools import combinations 
import re
from collections import Counter
import string
from copy import deepcopy
from math import gcd

def part_1():
    numbers = [] 
    
    #with open("input_test.txt") as file:
    with open("input.txt") as file:
        line = file.readline().rstrip()
        line = re.split(',', line)
        for num in line:
            numbers.append(int(num))
    
    start_value = len(numbers)
    for idx in range(start_value, 2020):
        last_number = numbers[idx-1]
        if not last_number in numbers[:-1]:
            # New number
            numbers.append(0)
        else:
            # Find age of this number
            for rev_idx in range(idx-2, -1, -1):
                #print(rev_idx, numbers[rev_idx], (idx-1) - rev_idx)
                if numbers[rev_idx] == last_number:
                    numbers.append((idx-1) - rev_idx)
                    break
    return numbers[2019]

def part_2():
    numbers = {5: 0, 2: 1, 8: 2, 16: 3, 18: 4, 0: 5}
    last_number = 1 # Not in dict
    
    #with open("input_test.txt") as file:
    #with open("input.txt") as file:
    #    line = file.readline().rstrip()
    #    line = re.split(',', line)
    #    for num in line:
    #        numbers.append(int(num))
    #start_value = len(numbers)
    
    start_value = 6
        
    for idx in range(start_value, 30000000-1):
    #for idx in range(start_value, 2019):
        if idx % 100000 == 0: print(idx)
        if not last_number in numbers:
            numbers[last_number] = idx
            last_number = 0
        else:
            age_diff = idx - numbers[last_number]
            numbers[last_number] = idx
            last_number = age_diff

    return last_number



print(part_1()) # 517
print(part_2()) # 29839 