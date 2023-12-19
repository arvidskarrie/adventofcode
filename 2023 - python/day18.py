
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
TEST_DATA = '2413432311323\n3215453535623\n3255245654254\n3446585845452\n4546657867536\n1438598798454\n4457876987766\n3637877979653\n4654967986887\n4564679986453\n1224686865563\n2546548887735\n4322674655533'

REGEX_STRING = r"(.) (\d+)"
dir_dict = {
    'R': 1 + 0j,
    'U': 0 + 1j,
    'L': -1 + 0j,
    'D': 0 - 1j,
}

class Digger:
    def __init__(self, pos):
       self.pos = pos
       self.dir = None

    def step(self):
        self.pos += self.dir
        return self.pos

def part_1():
    if USE_TEST_DATA:
        input_list = TEST_DATA.splitlines()
    else:
        with open("input.txt") as _file:
            input_list = [line.strip() for line in _file]

    digger = Digger(0 + 0j)
    dug_squares = set()
    inside_list = []
    for line in input_list:
        (dir, val) = re.findall(REGEX_STRING, line)[0]

        digger.dir = dir_dict[dir]
        for _ in range(int(val)):
            pos = digger.step()
            if pos in dug_squares:
                assert False
            dug_squares.add(pos)

            test_pos = pos + digger.dir * (-1j)
            inside_list.append(test_pos)
    
    # Find limits in all directions
    # Fill in the hole by iterating inwards from the existing
    idx = 0
    while len(inside_list) > 0:
        print(len(dug_squares), len(inside_list) - idx)
        potential_inside = inside_list.pop()
        if potential_inside not in dug_squares:
            dug_squares.add(potential_inside)
            
            for n in [potential_inside + 1, potential_inside - 1, potential_inside + 1j, potential_inside - 1j]:
                if n not in dug_squares:
                    inside_list.append(n)
        
    for line in range(3, -12, -1):
        line_str = ""
        for row in range(-5, 12):
            if (row + line * 1j) in dug_squares:
                line_str += "#"
            else:
                line_str += "."
        print(line_str)
    print(len(dug_squares))

    


part_1()
