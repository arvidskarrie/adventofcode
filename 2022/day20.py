
import os
os.environ["AOC_SESSION"] = "53616c7465645f5feb5f98622da494e1f359f67b2973c8f6a54ed362910e50e251d3f40a7189ffd45624f53a2c2e408b0039c07d21c2423c1ebce73b8d6b4bce"

from itertools import combinations, permutations
from functools import lru_cache
import aocd
import re
import numpy as np
from collections import deque


USE_TEST_DATA = 1
TEST_DATA = '15\n2\n-10\n3\n-2\n0\n4'
if USE_TEST_DATA:
    input_list = TEST_DATA.splitlines()
else:
    input_list = aocd.get_data(day=20).splitlines()
INPUT_LEN = len(input_list)

def get_idx(order, ord_list, tup_idx):
    for idx, order_int in enumerate(ord_list):
        if order_int[tup_idx] == order:
            return (idx)

def custom_mod(val, modifier):
    while val <= -modifier:
        val += modifier
    while val >= modifier:
        val -= modifier
    return val


def part_1(part):
    int_input = list(map(int, input_list))
    ord_list = []
    for order, integer in enumerate(int_input):
        ord_list.append((order, integer))

    for order in range(INPUT_LEN):
        # Find index for order
        idx = get_idx(order, ord_list, 0)
        value = custom_mod(ord_list[idx][1], INPUT_LEN)
        if value == 0:
            continue
        dir = 1 if value > 0 else -1

        dest_idx = idx + value

        # Rotate so that idx is in idx 0: OR
        # Rotate so that dest_idx is in position 0:
        ord_list = deque(ord_list)
        ord_list.rotate((-idx) if dir == 1 else (-dest_idx))
        ord_list = list(ord_list)

        # Rotate first element to value OR
        # Rotate value element to 0
        start_ord_list = deque(ord_list[0:abs(value)+1])
        start_ord_list.rotate(-dir)
        end_ord_list = ord_list[abs(value)+1:]
        ord_list = list(start_ord_list) + end_ord_list

        # print(value, list(val[1] for val in ord_list))
        



    # Calculate the positions 1000, 2000, 3000 after 0
    pos_zero = get_idx(0, ord_list, 1)

    ord_list = deque(ord_list)
    ord_list.rotate(-pos_zero)
    ord_list = list(ord_list)
    idx_of_relevance = [1000 % INPUT_LEN, 2000 % INPUT_LEN, 3000 % INPUT_LEN]
        
    tot_sum = 0
    for idx in idx_of_relevance:
        tot_sum += ord_list[idx][1]
        print(ord_list[idx][1])
    print(value, list(val[1] for val in ord_list))

    return tot_sum



print(part_1(1)) # 8302
