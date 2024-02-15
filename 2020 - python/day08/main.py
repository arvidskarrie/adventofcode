
from itertools import combinations 
import re
from collections import Counter
import string
from copy import deepcopy

DONE = 0
NOP = 1
ACC = 2
JMP = 3

operator_dict = {'nop': NOP, 'acc': ACC, 'jmp': JMP}

def part_1():
    boot_code = []
    accumulator_total = 0

    with open("input.txt") as file:
    #with open("input_test.txt") as file:
        for line in file:
            split_line = re.split(' ', line.rstrip())
            split_line[0] = operator_dict[split_line[0]]
            split_line[1] = int(split_line[1])
            boot_code.append(split_line)
    
    i = 0
    while True:
        if boot_code[i] == DONE:
            return accumulator_total
        elif boot_code[i][0] == NOP:
            increment = 1
        elif boot_code[i][0] == ACC:
            accumulator_total += boot_code[i][1]
            increment = 1
        elif boot_code[i][0] == JMP:
            increment = boot_code[i][1]
        else:
            print(i, boot_code[i])
        
        boot_code[i] = DONE
        i += increment           

# For part 2
def part_1b(boot_code):
    accumulator_total = 0    
    i = 0
    while True:
        if i >= len(boot_code):
            print('Successfully terminated')   
            return accumulator_total        
        if boot_code[i][0] == DONE:
            return None
        elif boot_code[i][0] == NOP:
            increment = 1
        elif boot_code[i][0] == ACC:
            accumulator_total += boot_code[i][1]
            increment = 1
        elif boot_code[i][0] == JMP:
            increment = boot_code[i][1]
        else:
            print(i, boot_code[i])
        
        boot_code[i][0] = DONE
        i += increment

def part_2():
    boot_code = []
    with open("input.txt") as file:
    #with open("input_test.txt") as file:
        for line in file:
            split_line = re.split(' ', line.rstrip())
            split_line[0] = operator_dict[split_line[0]]
            split_line[1] = int(split_line[1])
            boot_code.append(split_line)

    for i in range(len(boot_code)):
        if boot_code[i][0] == ACC:
            continue
        elif boot_code[i][0] == NOP:
            op = JMP
        else:
            op = NOP

        boot_code_evaluation = deepcopy(boot_code)
        boot_code_evaluation[i][0] = op
        result = part_1b(deepcopy(boot_code_evaluation))

        if result != None:
            return result
    
    print('No solution found')

#print(part_1()) # 1671
print(part_2()) # 892