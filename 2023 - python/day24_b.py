
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

    xy_min, xy_max = 200000000000000, 400000000000000
    no_of_insides = 0

    # px,py,pz,vx,v y,vz,t0,t1,t2 = sym.symbols('px,py,pz,vx,vy,vz,t0,t1,t2')
    for hail_a, hail_b in combinations(hails, 2):
        (p0xa, p0ya, p0za, vxa, vya, vza) = hail_a
        (p0xb, p0yb, pzb0, vxb, vyb, vzb) = hail_b

    
        pxa,pya,pxb,pyb,ta,tb = sym.symbols('pxa,pya,pxb,pyb,ta,tb')

        
        equations = []
        equations.append(sym.Eq(pxa, p0xa + vxa * ta))
        equations.append(sym.Eq(pya, p0ya + vya * ta))
        equations.append(sym.Eq(pxb, p0xb + vxb * tb))
        equations.append(sym.Eq(pyb, p0yb + vyb * tb))
        equations.append(sym.Eq(pxa, pxb))
        equations.append(sym.Eq(pya, pyb))

        answers = sym.solve(equations, (pxa,pya,pxb,pyb,ta,tb), set=True)[1]
        pass
        answers = list(answers)
        if answers:
            assert len(answers) == 1
            (pxa,pya,pxb,pyb,ta,tb) = answers[0]
            if ta >= 0 and tb >= 0 and xy_min <= pxa <= xy_max and xy_min <= pya <= xy_max:
                no_of_insides += 1
                print(no_of_insides)

        

    


part_1()