
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

CONV_DICT = {
    '2': 2,
    '1': 1,
    '0': 0,
    '-': -1,
    '=': -2
}

def convert(elf_string):
    elf_list = list(elf_string)
    number = 0
    while elf_list:
        number *= 5
        char = elf_list.pop(0)
        number += CONV_DICT[char]
    return number

def reverse_convert(dec_number):
    start_power = int(math.log(dec_number, 5) + 1)
    elf_number = ""
    for power in range(start_power, -1, -1):
        div = pow(5, power)
        num = (dec_number + div // 2) // div
        elf_number += next(key for key, value in CONV_DICT.items() if value == num)
        dec_number -= num * div
    if elf_number[0] == '0': elf_number = elf_number[1:]
    return elf_number


def part_1(part):
    total_sum = 0
    for line in input_list:
        total_sum += convert(line)
    
    # Find this 
    return reverse_convert(total_sum)

print(part_1(1))
