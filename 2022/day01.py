
import os
os.environ["AOC_SESSION"] = "53616c7465645f5feb5f98622da494e1f359f67b2973c8f6a54ed362910e50e251d3f40a7189ffd45624f53a2c2e408b0039c07d21c2423c1ebce73b8d6b4bce"

from itertools import combinations
from pathlib import Path
import aocd

p = Path(__file__)
input_path = str(Path(__file__).parent) + "/input.txt"


print(aocd.get_data(day=1, year=2020))

# aocd 1 2020 > input_path
# export AOC_SESSION=53616c7465645f5feb5f98622da494e1f359f67b2973c8f6a54ed362910e50e251d3f40a7189ffd45624f53a2c2e408b0039c07d21c2423c1ebce73b8d6b4bce

def part_1():
    input_list = []
    with open(input_path) as _file:
            for line in _file:
                input_list.append(int(line))

    input_combinations = combinations(input_list, 2)

    for combo in input_combinations:
        if sum(combo) == 2020:
            print(combo, combo[0] * combo[1])

def part_2():
    input_list = aocd.get_data(day=1, year=2020).splitlines()
    input_list = list(map(int, input_list))

    # with open(input_path) as _file:
    #         for line in _file:
    #             input_list.append(int(line))

    input_combinations = combinations(input_list, 3)

    for combo in input_combinations:
        if sum(combo) == 2020:
            print(combo, combo[0] * combo[1] * combo[2])



part_2()