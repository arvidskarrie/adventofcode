
import os
os.environ["AOC_SESSION"] = "53616c7465645f5f9cd071425b0d21d57535630a0d32e44bb5c7fe32070a07aa9170e67bb82f54f3bb900290fd1cb879c94a1e1230f809a51bec010d7f706512"
from itertools import combinations
import aocd
from collections import deque
import re
import math
from numpy import sign
import sympy as sym

NUMBERS_REGEX = r"(-?\d+)"

def part_1():
    with open("input.txt") as _file:
        input_list = [line.strip() for line in _file]

    components = {}
        
    for line in input_list:
        split_line = line.split(": ")
        first_comp = split_line[0]
        other_comps = split_line[1].split(" ")
        if not first_comp in components:
            components[first_comp] = []
        for other_comp in other_comps:
            if not other_comp in components:
                components[other_comp] = []
            components[first_comp].append(other_comp)
            components[other_comp].append(first_comp)
    

    pass
        


        
part_1()