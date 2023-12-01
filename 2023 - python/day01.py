
import os
os.environ["AOC_SESSION"] = "53616c7465645f5f9cd071425b0d21d57535630a0d32e44bb5c7fe32070a07aa9170e67bb82f54f3bb900290fd1cb879c94a1e1230f809a51bec010d7f706512"
from itertools import combinations
import aocd

USE_TEST_DATA = 0
TEST_DATA = '1000\n2000\n3000\n\n4000\n\n5000\n6000\n\n7000\n8000\n9000\n\n10000'

def part_1():

    if USE_TEST_DATA:
        input_list = TEST_DATA.splitlines()
    else:
        input_list = aocd.get_data().splitlines()

    calibration_sum = 0

    for input in input_list:
        new_input = input.strip("abcdefghijklmnopqrstuvwxyz")
        calibration_sum += 10 * (int)(new_input[0]) + (int)(new_input[-1])

    print(calibration_sum)

part_1()