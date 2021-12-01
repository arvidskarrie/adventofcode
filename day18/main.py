
from itertools import combinations 
import re
from collections import Counter
import string
from copy import deepcopy

inner_parenthesis_regex = r'\(([1234567890 +*]+)\)'
NOT_SET = 'not set'
PLUS = '+'
TIMES = '*'

def evaluate_line(line):
    inner_parentheses = re.findall(inner_parenthesis_regex, line)

    if inner_parentheses != []:
        for inner_line in inner_parentheses:
            outer_string = "(" + inner_line + ")"
            inner_sum = evaluate_line(inner_line)
            line = line.replace(outer_string, str(inner_sum))
        return evaluate_line(line)
    
    line = re.split(' ', line)
    total_value = 0

    value_list = []
    operator_list = [PLUS]

    for i in range(len(line)):
        if i % 2 == 0: # number
            value_list.append(int(line[i]))
        else: # operator
            operator_list.append(line[i])
            
    for op, num in zip(operator_list, value_list):
        if op == PLUS: 
            total_value += num
        else:
            total_value *= num

    return total_value

def part_1():
    total_sum = 0
    
    #with open("input.txt") as file:
    with open("input_test.txt") as file:
        for line in file:
            total_sum += evaluate_line(line)

    return total_sum

def part_2():
    total_sum = 0
    
    with open("input.txt") as file:
    #with open("input_test.txt") as file:
        for line in file:
            line = "(" + line.rstrip().replace(' * ', ') * (') + ")"
            total_sum += eval(line)

    return total_sum




print(part_1()) # 25190263477788
print(part_2()) # 297139939002972