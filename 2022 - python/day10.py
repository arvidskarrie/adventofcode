
import os
os.environ["AOC_SESSION"] = "53616c7465645f5feb5f98622da494e1f359f67b2973c8f6a54ed362910e50e251d3f40a7189ffd45624f53a2c2e408b0039c07d21c2423c1ebce73b8d6b4bce"

from itertools import combinations
import aocd
import re

USE_TEST_DATA = 0
TEST_DATA = 'addx 15\naddx -11\naddx 6\naddx -3\naddx 5\naddx -1\naddx -8\naddx 13\naddx 4\nnoop\naddx -1\naddx 5\naddx -1\naddx 5\naddx -1\naddx 5\naddx -1\naddx 5\naddx -1\naddx -35\naddx 1\naddx 24\naddx -19\naddx 1\naddx 16\naddx -11\nnoop\nnoop\naddx 21\naddx -15\nnoop\nnoop\naddx -3\naddx 9\naddx 1\naddx -3\naddx 8\naddx 1\naddx 5\nnoop\nnoop\nnoop\nnoop\nnoop\naddx -36\nnoop\naddx 1\naddx 7\nnoop\nnoop\nnoop\naddx 2\naddx 6\nnoop\nnoop\nnoop\nnoop\nnoop\naddx 1\nnoop\nnoop\naddx 7\naddx 1\nnoop\naddx -13\naddx 13\naddx 7\nnoop\naddx 1\naddx -33\nnoop\nnoop\nnoop\naddx 2\nnoop\nnoop\nnoop\naddx 8\nnoop\naddx -1\naddx 2\naddx 1\nnoop\naddx 17\naddx -9\naddx 1\naddx 1\naddx -3\naddx 11\nnoop\nnoop\naddx 1\nnoop\naddx 1\nnoop\nnoop\naddx -13\naddx -19\naddx 1\naddx 3\naddx 26\naddx -30\naddx 12\naddx -1\naddx 3\naddx 1\nnoop\nnoop\nnoop\naddx -9\naddx 18\naddx 1\naddx 2\nnoop\nnoop\naddx 9\nnoop\nnoop\nnoop\naddx -1\naddx 2\naddx -37\naddx 1\naddx 3\nnoop\naddx 15\naddx -21\naddx 22\naddx -6\naddx 1\nnoop\naddx 2\naddx 1\nnoop\naddx -10\nnoop\nnoop\naddx 20\naddx 1\naddx 2\naddx 2\naddx -6\naddx -11\nnoop\nnoop\nnoop'

if USE_TEST_DATA:
    input_list = TEST_DATA.splitlines()
else:
    input_list = aocd.get_data(day=10).splitlines()

class Register:
    def __init__(self, input):
        self.input = input
        self.cycle = 0
        self.values = []
        self.pixels = ""
                # self.cycle += 1
    
    def run_instructions(self):
        last_value = 1
        self.values.append(last_value)

        for instr in self.input:
            if instr == 'noop':
                self.values.append(last_value)
            elif instr[0:5] == 'addx ':
                mod_value = int(instr[5:])
                self.values.append(last_value)
                new_value = last_value + mod_value
                self.values.append(new_value)
                last_value = new_value

    def get_pixels(self):
        row_correction = 0
        for idx, value in enumerate(self.values):
            if idx != 0 and idx % 40 == 0:
                self.pixels += '\n'
                row_correction -= 40
            if abs(idx+row_correction-value) <= 1:
                self.pixels += '#'
            else:
                self.pixels += '.'
        return self.pixels
                
            
    
    def get_all_values(self):
        return self.values

    def get_value(self, idx):
        return self.values[idx]

    def get_strength(self, idx):
        return self.values[idx] * idx
    



def part_1(part):
    register = Register(input_list)
    register.run_instructions()
    interest = [20, 60, 100, 140, 180, 220]

    tot_sum = 0
    if part == 1:
        for inter in interest:
            print(register.get_strength(inter))
            tot_sum += register.get_strength(inter)
        return tot_sum
    
    elif part == 2:
        return register.get_pixels()

print(part_1(1))
print(part_1(2))
