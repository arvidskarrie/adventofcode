
from itertools import combinations 
import re
from collections import Counter
import string
from copy import deepcopy
from math import gcd

MASK = 'mask'
MEM = 'mem'

def part_1():
    instructions = []
    memory = {}

    #with open("input_test.txt") as file:
    with open("input.txt") as file:
        for line in file:
            line = re.split(' = ', line.rstrip())
            if line[0] != MASK:
                
                line.append((int(line[1])))
                line[2] = '{0:036b}'.format(line[2])
                line[1] = int(line[0][4:-1])
                line[0] = MEM

            instructions.append(line)    


    for instr in instructions:
        if instr[0] == MASK:
            mask = instr[1]
        else:
            mem_place = instr[1]
            value = instr[2]
            new_value = ""
            for bit in range(len(value)):
                if mask[bit] != 'X':
                    new_value += mask[bit]
                else:
                    new_value += value[bit]
            memory[mem_place] = int(new_value, 2)

    return sum(memory.values())

def part_2():
    instructions = []
    memory = {}

    #with open("input_test.txt") as file:
    with open("input.txt") as file:
        for line in file:
            line = re.split(' = ', line.rstrip())
            if line[0] != MASK:
                
                line.append((int(line[1])))
                line[1] = int(line[0][4:-1])
                line[1] = '{0:036b}'.format(line[1])
                line[0] = MEM

            instructions.append(line)    

    
    for instr in instructions:
        if instr[0] == MASK:
            mask = instr[1]
        else:
            mem_place = instr[1]
            new_mem_place = [""]
            for bit in range(len(mem_place)):
                new_instances = []
                for mem_instance_idx in range(len(new_mem_place)):
                    if mask[bit] == '0':
                        new_mem_place[mem_instance_idx] += mem_place[bit]
                    elif mask[bit] == '1':
                        new_mem_place[mem_instance_idx] += mask[bit]
                    else: # 'X'
                        new_instances.append(new_mem_place[mem_instance_idx])
                        new_mem_place[mem_instance_idx] += '0'
                    
                    # if all lines have been processed
                    if new_instances != [] and mem_instance_idx == len(new_mem_place) - 1:
                        for new_instance_idx in range(len(new_instances)):
                            new_instances[new_instance_idx] += '1'
                            new_mem_place.append(new_instances[new_instance_idx])

            for place in new_mem_place:
                mem_place = int(place, 2)
                memory[mem_place] = instr[2]

    return sum(memory.values())

#print(part_1()) # 13556564111697
print(part_2()) # 29839 