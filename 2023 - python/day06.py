
import os
os.environ["AOC_SESSION"] = "53616c7465645f5f9cd071425b0d21d57535630a0d32e44bb5c7fe32070a07aa9170e67bb82f54f3bb900290fd1cb879c94a1e1230f809a51bec010d7f706512"
import aocd
import re
import math

USE_TEST_DATA = 0
TEST_DATA = 'Time:      7  15   30\nDistance:  9  40  200'
NUMBER_REGEX = r'(\d+)'

def part_1():
    if USE_TEST_DATA:
        input_list = TEST_DATA.splitlines()
    else:
        input_list = aocd.get_data(day=6).splitlines()

    times_line_no_space = input_list[0].replace(" ", "")
    times = list(map(int, re.findall(NUMBER_REGEX, times_line_no_space)))
    distances_line_no_space = input_list[1].replace(" ", "")
    distances = list(map(int, re.findall(NUMBER_REGEX, distances_line_no_space)))
    pass

    alternatives_product = 1
    for (time, dist) in zip(times, distances):
        sqrt_factor = math.sqrt(time * time / 4 - dist)
        if time % 2 == 0:
            # Only -1 since we have a center alternative
            number_of_alternatives =  2 * math.ceil(sqrt_factor) - 1
        else:
            # First alternatives already after 0.5 from center
            number_of_alternatives =  2 * math.ceil(sqrt_factor + 0.5) - 2
        alternatives_product *= number_of_alternatives


    print("alternatives_product = {}". format(alternatives_product))
part_1()