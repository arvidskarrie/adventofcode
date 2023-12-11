
import os
os.environ["AOC_SESSION"] = "53616c7465645f5f9cd071425b0d21d57535630a0d32e44bb5c7fe32070a07aa9170e67bb82f54f3bb900290fd1cb879c94a1e1230f809a51bec010d7f706512"
import aocd
import re
import math
import collections
import itertools

USE_TEST_DATA = 0
TEST_DATA = '0 3 6 9 12 15\n1 3 6 10 15 21\n10 13 16 21 30 45'

NUMBER_REGEX = r"(-?\d+)"

def get_next_number(series: list[int]) -> int:        
    if all(map(lambda x: x == 0, series)):
        return 0
    
    new_series = []
    for i in range(len(series) - 1):
        new_series.append(series[i+1] - series[i])
    
    new_diff_for_last = get_next_number(new_series)
    return series[0] - new_diff_for_last


def part_1():
    if USE_TEST_DATA:
        input_list = TEST_DATA.splitlines()
    else:
        input_list = aocd.get_data(day=9).splitlines()

    next_number_sum = 0
    for line in input_list:
        series = (re.findall(NUMBER_REGEX, line))
        series = list(map(int, series))

        next_number_sum += get_next_number(series)

    print("LCM {}".format(next_number_sum)) # 3597659930 too high


part_1()