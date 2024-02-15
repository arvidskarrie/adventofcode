
import os
os.environ["AOC_SESSION"] = "53616c7465645f5feb5f98622da494e1f359f67b2973c8f6a54ed362910e50e251d3f40a7189ffd45624f53a2c2e408b0039c07d21c2423c1ebce73b8d6b4bce"

from itertools import combinations
import aocd

# from pathlib import Path
# p = Path(__file__)
# input_path = str(Path(__file__).parent) + "/input.txt"

# aocd 1 2020 > input_path
# export AOC_SESSION=53616c7465645f5feb5f98622da494e1f359f67b2973c8f6a54ed362910e50e251d3f40a7189ffd45624f53a2c2e408b0039c07d21c2423c1ebce73b8d6b4bce

USE_TEST_DATA = 1
TEST_DATA = "1721\n979\n366\n299\n675\n1456"

def part_1():
    if USE_TEST_DATA:
        input_list = TEST_DATA.splitlines()
    else:
        input_list = aocd.get_data(day=1, year=2020).splitlines()
    input_list = list(map(int, input_list))



    input_combinations = combinations(input_list, 3)

    for combo in input_combinations:
        if sum(combo) == 2020:
            print(combo, combo[0] * combo[1] * combo[2])

part_1()