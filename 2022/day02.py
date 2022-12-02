
import os
os.environ["AOC_SESSION"] = "53616c7465645f5feb5f98622da494e1f359f67b2973c8f6a54ed362910e50e251d3f40a7189ffd45624f53a2c2e408b0039c07d21c2423c1ebce73b8d6b4bce"

from itertools import combinations
import aocd

USE_TEST_DATA = 0
TEST_DATA = 'A Y\nB X\nC Z'

if USE_TEST_DATA:
    input_list = TEST_DATA.splitlines()
else:
    input_list = aocd.get_data().splitlines()

YOU_ROCK = 1
YOU_PAPER = 2
YOU_SCISSOR = 3
ME_ROCK = 1 # ME_TIE
ME_PAPER = 2 # ME_WIN
ME_SCISSOR = 3 # ME_LOSE

class my_int(int):
    def __mod__(self, n):
        return (self - 1) % n + 1

choice_dict = {
    'A': YOU_ROCK,
    'B': YOU_PAPER,
    'C': YOU_SCISSOR,
    'X': ME_ROCK,
    'Y': ME_PAPER,
    'Z': ME_SCISSOR,
}

def calc_win_points(part, they, me):
    def internal_calc_win_points():
        return (me - they + 1) % 3 # normal mod

    if part == 1:
        return internal_calc_win_points() * 3
    if part == 2:
        return (me % 3) * 3

def calc_choice_points(part, they, me):
    if part == 1:
        return my_int(me) % 3
    if part == 2:
        # return my_int(they + me + 2) % 3
        return my_int(me - 2 * they + 2) % 3

def calc_points(part, round):
    win_points = calc_win_points(part, round[0], round[1])
    choice_points = calc_choice_points(part, round[0], round[1])

    return win_points + choice_points

def play(part):
    round_list = list(map(lambda line: [choice_dict[line[0]], choice_dict[line[2]] - int(part == 2)], input_list))

    return sum(calc_points(part, round) for round in round_list)


print(play(1) == 10718, play(1))
print(play(2) == 14652, play(2))