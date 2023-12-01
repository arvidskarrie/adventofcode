
import os
os.environ["AOC_SESSION"] = "53616c7465645f5f9cd071425b0d21d57535630a0d32e44bb5c7fe32070a07aa9170e67bb82f54f3bb900290fd1cb879c94a1e1230f809a51bec010d7f706512"
from itertools import combinations
import aocd

USE_TEST_DATA = 0
TEST_DATA = 'two1nine\neightwothree\nabcone2threexyz\nxtwone3four\n4nineeightseven2\nzoneight234\n7pqrstsixteen'

help_dict = {
    'one': "one1one",
    'two': "two2two",
    'three': "three3three",
    'four': "four4four",
    'five': "five5five",
    'six': "six6six",
    'seven': "seven7seven",
    'eight': "eight8eight",
    'nine': "nine9nine",
    # 'zero': "0",
}

def part_1():

    if USE_TEST_DATA:
        input_list = TEST_DATA.splitlines()
    else:
        input_list = aocd.get_data().splitlines()

    calibration_sum = 0

    for input in input_list:
        for (num_str, num_val) in help_dict.items():
            input = input.replace(num_str, num_val)
                    
        new_input = input.strip("abcdefghijklmnopqrstuvwxyz")
        print(10 * (int)(new_input[0]) + (int)(new_input[-1]))
        calibration_sum += 10 * (int)(new_input[0]) + (int)(new_input[-1])

    print(calibration_sum)

part_1()