
import os
os.environ["AOC_SESSION"] = "53616c7465645f5f9cd071425b0d21d57535630a0d32e44bb5c7fe32070a07aa9170e67bb82f54f3bb900290fd1cb879c94a1e1230f809a51bec010d7f706512"
import aocd
import re
import math
import collections
import itertools
import functools
import time

USE_TEST_DATA = 0
TEST_DATA = 'rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'

REGEX_STRING = r"(.*)([=-])(\d?)"

def part_1():
    if USE_TEST_DATA:
        input_list = TEST_DATA.splitlines()
    else:
        input_list = aocd.get_data(day=15).splitlines()
    
    total_sum = 0
    for line in input_list[0].split(","):
        current_value = 0
        for char in line:
            current_value = ((current_value + ord(char)) * 17) % 256
        total_sum += current_value
    print(total_sum)

def get_box_number(line):
    current_value = 0
    for char in line:
        if char in ["-", "="]:
            break
        current_value = ((current_value + ord(char)) * 17) % 256
    return current_value

def part_2():
    if USE_TEST_DATA:
        input_list = TEST_DATA.splitlines()
    else:
        input_list = aocd.get_data(day=15).splitlines()

    input_list = input_list[0].split(",")
    lens_boxes = [[] for _ in range(256)]
    focal_lengths = {}

    for operation in input_list:
        data = re.findall(REGEX_STRING, operation)[0]
        (lens_label, operation, focal_length) = data
        box = lens_boxes[get_box_number(lens_label)]

        if operation == "=":
            # Add operation
            focal_lengths[lens_label] = focal_length
            if lens_label in box:
                existing_idx = box.index(lens_label)
                box[existing_idx] = lens_label
            else:
                box.append(lens_label)
        elif operation == "-":
            # Remove operation
            if lens_label in box:
                box.remove(lens_label)
        else:
            assert(False)

    print("Power = {}".format(
        sum(
            (box_number + 1) * (slot + 1) * int(focal_lengths[label])
            for box_number, box in enumerate(lens_boxes)
            for slot, label in enumerate(box)
        )
    )) # 247153

part_2()