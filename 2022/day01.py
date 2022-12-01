
import os
os.environ["AOC_SESSION"] = "53616c7465645f5feb5f98622da494e1f359f67b2973c8f6a54ed362910e50e251d3f40a7189ffd45624f53a2c2e408b0039c07d21c2423c1ebce73b8d6b4bce"

from itertools import combinations
import aocd

USE_TEST_DATA = 0
TEST_DATA = '1000\n2000\n3000\n\n4000\n\n5000\n6000\n\n7000\n8000\n9000\n\n10000'

def part_1():
    if USE_TEST_DATA:
        input_list = TEST_DATA.splitlines()
    else:
        input_list = aocd.get_data().splitlines()
    # input_list = list(map(int, input_list))

    elf_calorie_list = []
    calories = 0
    for input in input_list:
        if input == '':
            elf_calorie_list.append(calories)
            calories = 0
        else:
            calories += int(input)
    elf_calorie_list.append(calories)

    elf_calorie_list.sort(reverse=True)
    print(sum(elf_calorie_list[0:3]), elf_calorie_list) # 11722889
part_1()