
import os
os.environ["AOC_SESSION"] = "53616c7465645f5feb5f98622da494e1f359f67b2973c8f6a54ed362910e50e251d3f40a7189ffd45624f53a2c2e408b0039c07d21c2423c1ebce73b8d6b4bce"

from itertools import combinations
import aocd
import re

USE_TEST_DATA = 0
TEST_DATA = '2-4,6-8\n2-3,4-5\n5-7,7-9\n2-8,3-7\n6-6,4-6\n2-6,4-8'

if USE_TEST_DATA:
    input_list = TEST_DATA.splitlines()
else:
    input_list = aocd.get_data().splitlines()

def is_fully_contained(pair):
    return (pair[0] >= pair[2] and pair[1] <= pair[3]) or (pair[0] <= pair[2] and pair[1] >= pair[3])

def is_part_contained(pair):
    if (pair[0] <= pair[2] and pair[2] <= pair[1]) or (pair[2] <= pair[0] and pair[0] <= pair[3]):
        return True
    return False

'00xxx00'
'000xxx0'


def part_1(part):
    regex_two_elves = r'(.*)-(.*),(.*)-(.*)'
    assignments = []
    for line in input_list:
        char_line = list(re.findall(regex_two_elves, line)[0])
        
        assignments.append(list(map(int, char_line)))
    
    
    assign_sum = 0
    for pair in assignments:
        if part == 1:
            assign_sum += is_fully_contained(pair)
        if part == 2:
            if is_part_contained(pair):
                assign_sum += 1
                print(assign_sum, pair)
    
    return assign_sum

print(part_1(1))
print(part_1(2))
