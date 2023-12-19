
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
TEST_DATA = 'R 6 (#70c710)\nD 5 (#0dc571)\nL 2 (#5713f0)\nD 2 (#d2c081)\nR 2 (#59c680)\nD 2 (#411b91)\nL 5 (#8ceee2)\nU 2 (#caa173)\nL 1 (#1b58a2)\nU 2 (#caa171)\nR 2 (#7807d2)\nU 3 (#a77fa3)\nL 2 (#015232)\nU 2 (#7a21e3)'

REGEX_STRING = r"(.) (\d+)"
REGEX_STRING_2 = r"\(\#(.*?)(\d)\)"

dir_dict = {
    'R': 1 + 0j,
    'U': 0 + 1j,
    'L': -1 + 0j,
    'D': 0 - 1j,
}

dir_dict_2 = {
    '0': 1 + 0j,
    '1': 0 - 1j,
    '2': -1 + 0j,
    '3': 0 + 1j,
}

class Digger:
    def __init__(self, pos):
       self.pos = pos
       self.dir = None

    def step(self, val):
        self.pos += self.dir * val
        return self.pos

def part_1():
    if USE_TEST_DATA:
        input_list = TEST_DATA.splitlines()
    else:
        with open("input.txt") as _file:
            input_list = [line.strip() for line in _file]

    digger = Digger(0 + 0j)
    corners = [0 + 0j]
    edges = 0 # for the missing corner pieces
    for line in input_list:
        # (dir, val) = re.findall(REGEX_STRING, line)[0]
        (val, dir) = re.findall(REGEX_STRING_2, line)[0]


        val = int(val, 16)
        digger.dir = dir_dict_2[dir]
        pos = digger.step(val)
        edges += val
        corners.append(pos)

    corners.reverse() # To get positive value
    
    # Gauss triangle shoelace method
    # For every line segment, calculate the triangle with origo
    triangle_sum = sum(
        (p1.real * p2.imag - p2.real * p1.imag) / 2
        for p1, p2 in zip(corners, corners[1:])
    )

    triangle_sum += edges / 2 + 1

    print(triangle_sum)

    pass

    


part_1()
