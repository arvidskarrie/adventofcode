
import os
os.environ["AOC_SESSION"] = "53616c7465645f5f9cd071425b0d21d57535630a0d32e44bb5c7fe32070a07aa9170e67bb82f54f3bb900290fd1cb879c94a1e1230f809a51bec010d7f706512"
from itertools import combinations
import aocd
import re


USE_TEST_DATA = 0
TEST_DATA = 'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green\nGame 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue\nGame 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red\nGame 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red\nGame 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green\n'

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

GAME_REGEX = r"^Game (\d+):"
BLUE_REGEX = r" (\d+) blue"
RED_REGEX = r" (\d+) red"
GREEN_REGEX = r" (\d+) green"

def part_1():

    if USE_TEST_DATA:
        input_list = TEST_DATA.splitlines()
    else:
        input_list = aocd.get_data(day=2).splitlines()

    working_games_sum = 0

    for input in input_list:
        game_match = int(re.findall(GAME_REGEX, input)[0])

        blue_matches = re.findall(BLUE_REGEX, input)
        blue_cubes = map(int, blue_matches)
        blue_max = max(blue_cubes)


        red_matches = re.findall(RED_REGEX, input)
        red_cubes = map(int, red_matches)
        red_max = max(red_cubes)

        green_matches = re.findall(GREEN_REGEX, input)
        green_cubes = map(int, green_matches)
        green_max = max(green_cubes)

        working_games_sum += blue_max * red_max * green_max


    print(working_games_sum)

part_1()