
import os
os.environ["AOC_SESSION"] = "53616c7465645f5feb5f98622da494e1f359f67b2973c8f6a54ed362910e50e251d3f40a7189ffd45624f53a2c2e408b0039c07d21c2423c1ebce73b8d6b4bce"

from itertools import combinations
import aocd
import re

USE_TEST_DATA = 0
TEST_DATA = \
    '$ cd /\n' + \
    '$ ls\n' + \
    'dir a\n' + \
    '14848514 b.txt\n' + \
    '8504156 c.dat\n' + \
    'dir d\n' + \
    '$ cd a\n' + \
    '$ ls\n' + \
    'dir e\n' + \
    '29116 f\n' + \
    '2557 g\n' + \
    '62596 h.lst\n' + \
    '$ cd e\n' + \
    '$ ls\n' + \
    '584 i\n' + \
    '$ cd ..\n' + \
    '$ cd ..\n' + \
    '$ cd d\n' + \
    '$ ls\n' + \
    '4060174 j\n' + \
    '8033020 d.log\n' + \
    '5626152 d.ext\n' + \
    '7214296 k\n'

if USE_TEST_DATA:
    input_list = TEST_DATA.splitlines()
    NO_OF_STACKS = 3
else:
    input_list = aocd.get_data().splitlines()
    NO_OF_STACKS = 9


l = 0
global_sum = 0
MINIMUM_TO_DELETE = 0
smallest_so_far = 0
def map_one_dir():
    global l
    local_directory = {}
    while True:     
        if l >= len(input_list):
            return local_directory

        line = input_list[l]
        if line == '$ cd ..':
            l += 1
            return local_directory
        elif '$ cd' in line:
            new_dir_name = line[5:]
            l += 1
            local_directory[new_dir_name] = map_one_dir()
            continue
        elif line == '$ ls':
            while True:
                l += 1
                if l >= len(input_list):
                    return local_directory
                line = input_list[l]
                if '$' in line:
                    break
                line = line.split(' ')
                local_directory[line[1]] = line [0]
            continue
        
def get_dir_sum(dir):
    global global_sum
    dir_sum = 0
    for k, v in dir.items():
        if type(v) == dict:
            v = get_dir_sum(v)
            if v <= 100000:
                global_sum += v
        dir_sum += int(v)
    return dir_sum

def get_dir_sum2(dir):
    global smallest_so_far
    dir_sum = 0
    for k, v in dir.items():
        if type(v) == dict:
            v = get_dir_sum2(v)
            if v >= MINIMUM_TO_DELETE and v <= smallest_so_far:
            # if v >= MINIMUM_TO_DELETE:
                print('Larger than min', k, v)
                smallest_so_far = v
        dir_sum += int(v)
    return dir_sum

def part_1(part):
    global l
    global global_sum
    l = 0
    global_sum = 0
    global MINIMUM_TO_DELETE
    global smallest_so_far

    TOTAL_DISK_SPACE = 7e7
    DISK_SPACE_NEEDED = 3e7
    MINIMUM_TO_DELETE = TOTAL_DISK_SPACE
    
    directory = map_one_dir()

    dir_sum = get_dir_sum(directory)
    memory_balance = TOTAL_DISK_SPACE - dir_sum - DISK_SPACE_NEEDED
    MINIMUM_TO_DELETE = -memory_balance
    smallest_so_far = TOTAL_DISK_SPACE

    return global_sum

def part_2(part):
    global l
    global global_sum
    l = 0
    global_sum = 0
    global MINIMUM_TO_DELETE
    TOTAL_DISK_SPACE = 7e7
    DISK_SPACE_NEEDED = 3e7
    MINIMUM_TO_DELETE = TOTAL_DISK_SPACE
    
    directory = map_one_dir()

    dir_sum = get_dir_sum2(directory)

    memory_balance = TOTAL_DISK_SPACE - dir_sum - DISK_SPACE_NEEDED
    MINIMUM_TO_DELETE = -memory_balance
    print(dir_sum, MINIMUM_TO_DELETE)
    dir_sum = get_dir_sum2(directory)

    return 'done'
    # return MINIMUM_TO_DELETE

print(part_1(1))
print(part_1(1))
print(part_2(2))
