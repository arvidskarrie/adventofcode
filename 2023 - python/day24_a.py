
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
    hails = [tuple(map(int, list(re.findall(NUMBERS_REGEX, line)))) for line in input_list]

    p0x6, p0y6, p0z6, vx6, vy6, vz6, ta, tb, tc = sym.symbols('p0x6,p0y6,pz60,vx6,vy6,vz6,ta,tb,tc')
    equations = []

    t = [ta, tb, tc]

    for hails in combinations(hails, 3):
        for i, hail in enumerate(hails):
            (p0x, p0y, p0z, vx, vy, vz) = hail
           
            equations.append(sym.Eq(p0x + vx * t[i], p0x6 + vx6 * t[i]))
            equations.append(sym.Eq(p0y + vy * t[i], p0y6 + vy6 * t[i]))
            equations.append(sym.Eq(p0z + vz * t[i], p0z6 + vz6 * t[i]))

        answers = sym.solve(equations, (p0x6, p0y6, p0z6, vx6, vy6, vz6, ta, tb, tc), set=True)[1]
        answers = list(answers)
        if len(answers) != 0:
            print(sum(answers[0][0:3]))
            break


        

    


part_1()