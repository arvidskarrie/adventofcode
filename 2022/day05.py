
import os
os.environ["AOC_SESSION"] = "53616c7465645f5feb5f98622da494e1f359f67b2973c8f6a54ed362910e50e251d3f40a7189ffd45624f53a2c2e408b0039c07d21c2423c1ebce73b8d6b4bce"

from itertools import combinations
import aocd
import re

USE_TEST_DATA = 0
TEST_DATA = '    [D]    \n[N] [C]    \n[Z] [M] [P]\n 1   2   3 \nmove 1 from 2 to 1\nmove 3 from 1 to 3\nmove 2 from 2 to 1\nmove 1 from 1 to 2'

if USE_TEST_DATA:
    input_list = TEST_DATA.splitlines()
    NO_OF_STACKS = 3
else:
    input_list = aocd.get_data().splitlines()
    NO_OF_STACKS = 9

def part_1(part):
    stacks = [[] for i in range(NO_OF_STACKS)]
    operations = []
    parse_stacks = True
    regex_operations = r'move (.*) from (.*) to (.*)'

    for line in input_list:
        if line == '':
            continue
        if parse_stacks:
            # Extract stacks
            if '1' in line:
                parse_stacks = False
                continue
            for stack in range(NO_OF_STACKS):
                char = line[4 * stack + 1]
                if char != ' ':
                    stacks[stack].insert(0, char)
        else:
            # Parse operations
            regex_tuple = re.findall(regex_operations, line)
            regex_list = list(regex_tuple[0])
            regex_list = list(map(int, regex_list))
            operations.append(regex_list)
    
    # Execute operations
    for op in operations:
        amount = op[0]
        from_stack = stacks[op[1] - 1]
        to_stack = stacks[op[2] - 1]
        
        if part == 1:
            for _i in range(amount):
                crate = from_stack.pop()
                to_stack.append(crate)

                # to_stack.append(from_stack[-1])
                # from_stack = from_stack[0:-1]
        if part == 2:
            temp_stack = []
            for _i in range(amount):
                crate = from_stack.pop()
                temp_stack.append(crate)

            for _i in range(amount):
                to_stack.append(temp_stack.pop())

    # Print top letters
    top_letters = ''
    for stack in stacks:
        top_letters += stack.pop()
    return top_letters

print(part_1(1))
print(part_1(2))
