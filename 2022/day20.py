
import os
os.environ["AOC_SESSION"] = "53616c7465645f5feb5f98622da494e1f359f67b2973c8f6a54ed362910e50e251d3f40a7189ffd45624f53a2c2e408b0039c07d21c2423c1ebce73b8d6b4bce"

from itertools import combinations, permutations
from functools import lru_cache
import aocd
import re
import numpy as np


USE_TEST_DATA = 0
TEST_DATA = '1\n2\n-3\n3\n-2\n0\n4'
if USE_TEST_DATA:
    input_list = TEST_DATA.splitlines()
else:
    input_list = aocd.get_data(day=20).splitlines()
INPUT_LEN = len(input_list)

def get_idx(order, ord_list, tup_idx):
    for idx, order_int in enumerate(ord_list):
        if order_int[tup_idx] == order:
            return (idx)

def part_1(part):
    int_input = list(map(int, input_list))
    ord_list = []
    for order, integer in enumerate(int_input):
        ord_list.append((order, integer))


    for order in range(INPUT_LEN):
        # Find index for order
        idx = get_idx(order, ord_list, 0)
        value = ord_list[idx][1]
        if value == 0:
            continue
        dir = 1 if value > 0 else -1

        # Make one move at the time
        for _move in range(abs(value)):
            if dir == 1 and idx == INPUT_LEN - 1:
                ord_list = [ord_list[-1]] + ord_list[:-1]
                idx = 0
            if dir == -1 and idx == 0:
                ord_list = ord_list[1:] + [ord_list[0]]
                idx = INPUT_LEN - 1
            ord_list[idx], ord_list[idx + dir] = ord_list[idx + dir], ord_list[idx]
            idx += dir

    # Calculate the positions 1000, 2000, 3000 after 0
    pos_zero = get_idx(0, ord_list, 1)
    idx_of_relevance = [(1000 + pos_zero) % INPUT_LEN, (2000 + pos_zero) % INPUT_LEN, (3000 + pos_zero) % INPUT_LEN]
        
    return sum(ord_list[idx][1] for idx in idx_of_relevance)



print(part_1(1)) # 8302
