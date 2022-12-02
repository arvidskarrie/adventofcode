
import os
os.environ["AOC_SESSION"] = "53616c7465645f5feb5f98622da494e1f359f67b2973c8f6a54ed362910e50e251d3f40a7189ffd45624f53a2c2e408b0039c07d21c2423c1ebce73b8d6b4bce"

from itertools import combinations
import aocd

USE_TEST_DATA = 0
TEST_DATA = 'A Y\nB X\nC Z'

YOU_ROCK = 1
YOU_PAPER = 2
YOU_SCISSOR = 3
ME_ROCK = 4
ME_PAPER = 5
ME_SCISSOR = 6
ME_LOSE = 4
ME_TIE = 5
ME_WIN = 6

# choice_dict = {
#     'A': YOU_ROCK,
#     'B': YOU_PAPER,
#     'C': YOU_SCISSOR,
#     'X': ME_ROCK,
#     'Y': ME_PAPER,
#     'Z': ME_SCISSOR,

choice_dict = {
    'A': YOU_ROCK,
    'B': YOU_PAPER,
    'C': YOU_SCISSOR,
    'X': ME_LOSE,
    'Y': ME_TIE,
    'Z': ME_WIN,
}

def calc_points(round):
    result = (round[1] - round[0]) % 3
    own_extra_score = (round[1] - 1) % 3 + 1
    if result == 0:
        return 3 + own_extra_score
    if result == 1:
        return 6 + own_extra_score
    if result == 2:
        return own_extra_score
    breakpoint

def calc_points2(round):
    result = (round[1] - 4) * 3
    own_extra_score = (round[1] - 2 * round[0]) % 3 + 1
    return result + own_extra_score

# 14 0 0
# 15 1 1 (diff - round[0]) % 3 +1
# 16 2 2
# 24 2 1
# 25 0 2 (diff - round[0]) % 3 +1
# 26 1 0
# 34 1 2
# 35 2 0 (diff - round[0]) % 3 +1
# 36 0 1


def part_1():
    if USE_TEST_DATA:
        input_list = TEST_DATA.splitlines()
    else:
        input_list = aocd.get_data().splitlines()
    round_list = list(map(lambda line: [choice_dict[line[0]], choice_dict[line[2]]], input_list))

    sum_points = 0
    for round in round_list:
        sum_points += calc_points(round)
    print(sum_points)

def part_2():
    if USE_TEST_DATA:
        input_list = TEST_DATA.splitlines()
    else:
        input_list = aocd.get_data().splitlines()
    round_list = list(map(lambda line: [choice_dict[line[0]], choice_dict[line[2]]], input_list))

    sum_points = 0
    for round in round_list:
        sum_points += calc_points2(round)
    print(sum_points)

# part_1() 10718
part_2() #10718