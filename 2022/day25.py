
import os
os.environ["AOC_SESSION"] = "53616c7465645f5f5db34e7c4783f6c32cc4775884ae8ce61d21bd4408498b634616c2f58df5d26febef14f761e9fc3804220dc57ee470f5508edd9eac9d69fa"

import aocd
import re
from collections import deque
import copy
import math

USE_TEST_DATA = 0
TEST_DATA = '1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n15\n20\n2022\n12345\n314159265'
if USE_TEST_DATA:
    input_list = TEST_DATA.splitlines()
else:
    input_list = aocd.get_data(day=25).splitlines()

CONV = {
    '2': 2,
    '1': 1,
    '0': 0,
    '-': -1,
    '=': -2
}
REV_CONV = {
    2: '2',
    1: '1',
    0: '0',
    -1: '-',
    -2: '=',
}

def get_val_rest(part_sum):
    if part_sum > 2:
        return REV_CONV[part_sum - 5], 1
    if part_sum < -2:
        return REV_CONV[part_sum + 5], -1
    return REV_CONV[part_sum], 0

def add(num1, num2):
    # num1 shall be bigger or equal to num2
    if len(num2) > len(num1): num1, num2 = num2, num1
    num1, num2 = list(num1), list(num2)

    # Add zeroes to num2 if necessary
    len_diff = len(num1) - len(num2)
    num2 = ['0'] * len_diff + num2
    
    # Reverse both strings to process
    power = 0
    new_number = ""
    carry = 0
    for n1, n2 in zip(reversed(num1), reversed(num2)):
        part_sum = CONV[n1] + CONV[n2] + carry
        val, carry = get_val_rest(part_sum)
        new_number = val + new_number
    if carry == 1:
        new_number = '1' + new_number
    return new_number

def part_1(part):
    total_sum = "0"
    for line in input_list:
        total_sum = add(total_sum, line)
    return total_sum

print(part_1(1))
