
import os
os.environ["AOC_SESSION"] = "53616c7465645f5f9cd071425b0d21d57535630a0d32e44bb5c7fe32070a07aa9170e67bb82f54f3bb900290fd1cb879c94a1e1230f809a51bec010d7f706512"
import aocd
import re
import math
import collections
import itertools

USE_TEST_DATA = 0
TEST_DATA = 'LLR\n\nAAA = (BBB, BBB)\nBBB = (AAA, ZZZ)\nZZZ = (ZZZ, ZZZ)'

NODE_REGEX = r"(.*) = \((.*), (.*)\)"

# Stolen form chat-gpt
def lcm(numbers):
    def lcm_of_two(a, b):
        return abs(a*b) // math.gcd(a, b)

    current_lcm = 1
    for number in numbers:
        current_lcm = lcm_of_two(current_lcm, number)
    return current_lcm

def part_1():
    if USE_TEST_DATA:
        input_list = TEST_DATA.splitlines()
    else:
        input_list = aocd.get_data(day=8).splitlines()

    instructions = input_list[0]
    node_dict = {}
    for line in input_list[2:]:
        (first, second, third) = tuple(re.findall(NODE_REGEX, line)[0])
        node_dict[first] = (second, third)
    
    start_nodes = list(filter(lambda node: node.endswith('A'), node_dict.keys()))

    iterations_needed = 1
    for current_node in start_nodes:
        start_name = current_node
        for i in itertools.count(start=0): # endless loop with counter
            instruction = instructions[i % len(instructions)]
            instr_idx = 0 if instruction == 'L' else 1
            current_node = node_dict[current_node][instr_idx]
            if current_node.endswith('Z'):
                print("Number of steps needed for {}: {}".format(start_name, i + 1))
                # Update the iterations needed as we go, since that process can be iterative just as well.
                iterations_needed = lcm([iterations_needed, i + 1])
                break
    
    print("LCM {}".format(iterations_needed))


part_1()