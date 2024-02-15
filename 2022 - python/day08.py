
import os
os.environ["AOC_SESSION"] = "53616c7465645f5feb5f98622da494e1f359f67b2973c8f6a54ed362910e50e251d3f40a7189ffd45624f53a2c2e408b0039c07d21c2423c1ebce73b8d6b4bce"

from itertools import combinations
import aocd
import re

USE_TEST_DATA = 0
TEST_DATA = '30373\n25512\n65332\n33549\n35390'

if USE_TEST_DATA:
    input_list = TEST_DATA.splitlines()
    NO_OF_STACKS = 3
else:
    input_list = aocd.get_data().splitlines()
    NO_OF_STACKS = 9

INPUT_HEIGHT = len(input_list)
INPUT_LENGTH = len(input_list[0])

def is_tree_visible(idx, line):
    tree = line[idx]
    if idx == 0 or idx == len(line) - 1:
        return 1
    if tree > max(line[0:idx]):
        return 1
    if tree > max(line[idx+1:]):
        return 1
    return 0

def get_visibility_line(line):
    visibility_line = []
    for idx in range(len(line)):
        visibility_line.append(is_tree_visible(idx, line))
    return visibility_line

def calc_sum(mat):
    tot_sum = 0
    for line in mat:
        tot_sum += sum(line)
    return tot_sum

def part_1(part):
    visible_matrix = []
    for _ in range(INPUT_HEIGHT):
        visible_matrix.append([0] * INPUT_HEIGHT)

    # iterate over rows:
    for i in range(INPUT_LENGTH):
        line = input_list[i]

        new_line = get_visibility_line(line)
        for j in range(INPUT_HEIGHT):
            visible_matrix[i][j] |= new_line[j]

    # transpose input, iterate over columns
    transposed_input = list(map(list, zip(*input_list)))
    for j in range(INPUT_HEIGHT):
        line = transposed_input[j]

        new_line = get_visibility_line(line)
        for i in range(INPUT_LENGTH):
            visible_matrix[i][j] |= new_line[i]
    

    return calc_sum(visible_matrix)

def get_trees_seen_in_line(idx, line):
    tree = line[idx]
    first = 0
    second = 0

    #calc tree to the left
    tree_idx = idx-1
    while tree_idx >= 0:
        first += 1
        if line[tree_idx] >= tree:
            break
        tree_idx -= 1
            
    #calc tree to the right
    tree_idx = idx+1
    while tree_idx < len(line):
        second += 1
        if line[tree_idx] >= tree:
            break
        tree_idx += 1

    return first * second

def get_visibility_line2(line):
    visibility_line = [0]
    for idx in range(1, len(line)-1):
        visibility_line.append(get_trees_seen_in_line(idx, line))
    visibility_line.append(0)
    return visibility_line

def calc_max(mat):
    tot_sum = 0
    for line in mat:
        tot_sum = max(tot_sum, max(line))
    return tot_sum
def part_2(part):
    visible_matrix = []
    for _ in range(INPUT_HEIGHT):
        visible_matrix.append([0] * INPUT_HEIGHT)

    # iterate over rows:
    for i in range(INPUT_LENGTH):
        line = input_list[i]

        new_line = get_visibility_line2(line)
        for j in range(INPUT_HEIGHT):
            visible_matrix[i][j] = new_line[j]

    # transpose input, iterate over columns
    transposed_input = list(map(list, zip(*input_list)))
    for j in range(INPUT_HEIGHT):
        line = transposed_input[j]

        new_line = get_visibility_line2(line)
        for i in range(INPUT_LENGTH):
            visible_matrix[i][j] *= new_line[i]
    

    return calc_max(visible_matrix)


print(part_2(1))
