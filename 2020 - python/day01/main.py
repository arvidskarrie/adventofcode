
from itertools import combinations 

def part_1():
    input_list = []
    with open("input.txt") as _file:
            for line in _file:
                input_list.append(int(line))

    input_combinations = combinations(input_list, 2)

    for combo in input_combinations:
        if sum(combo) == 2020:
            print(combo, combo[0] * combo[1])

def part_2():
    input_list = []
    with open("input.txt") as _file:
            for line in _file:
                input_list.append(int(line))

    input_combinations = combinations(input_list, 3)

    for combo in input_combinations:
        if sum(combo) == 2020:
            print(combo, combo[0] * combo[1] * combo[2])



part_2()