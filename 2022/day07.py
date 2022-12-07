
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


global_sum = 0
g_minimum_to_delete = 0
smallest_so_far = 0

def map_one_dir(l_idx):
    local_directory = {}
    while True:     
        if l_idx >= len(input_list):
            return (local_directory, l_idx)

        line = input_list[l_idx]
        if line == '$ cd ..':
            l_idx += 1
            return (local_directory, l_idx)
        elif '$ cd' in line:
            new_dir_name = line[5:]
            l_idx += 1
            (local_directory[new_dir_name], l_idx) = map_one_dir(l_idx)
            continue
        elif line == '$ ls':
            while True:
                l_idx += 1
                if l_idx >= len(input_list):
                    return (local_directory, l_idx)
                line = input_list[l_idx]
                if '$' in line:
                    break
                line = line.split(' ')
                local_directory[line[1]] = line [0]
            continue
        
def get_dir_sum(dir, part):
    global global_sum
    global smallest_so_far
    dir_sum = 0
    for k, v in dir.items():
        if type(v) == dict:
            v = get_dir_sum(v, part)
            if v <= 100000 and part == 1:
                global_sum += v
            if v >= g_minimum_to_delete and v <= smallest_so_far and part == 2:
                smallest_so_far = v
        dir_sum += int(v)
    return dir_sum

def part_1(part):
    global global_sum
    global_sum = 0
    global g_minimum_to_delete
    g_minimum_to_delete = 7e7
    global smallest_so_far
    smallest_so_far = 7e7

    (directory, _) = map_one_dir(l_idx=0)

    dir_sum = get_dir_sum(directory, part)

    if part == 1:
        return global_sum
    elif part == 2:
        g_minimum_to_delete = dir_sum + 3e7 - 7e7
        get_dir_sum(directory, 2)
        return smallest_so_far

print(part_1(1) == 1427048)
print(part_1(2) == 2940614)
