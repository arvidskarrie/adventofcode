
import os
os.environ["AOC_SESSION"] = "53616c7465645f5feb5f98622da494e1f359f67b2973c8f6a54ed362910e50e251d3f40a7189ffd45624f53a2c2e408b0039c07d21c2423c1ebce73b8d6b4bce"

from itertools import combinations
import aocd

USE_TEST_DATA = 0
TEST_DATA = 'vJrwpWtwJgWrhcsFMMfFFhFp\njqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\nPmmdzqPrVvPwwTWBwg\nwMqvLMZHhHMvwLHjbvcjnnSBnvTQFn\nttgJtRGJQctTZtZT\nCrZsJsPPZsGzwwsLwLmpwMDw'

if USE_TEST_DATA:
    input_list = TEST_DATA.splitlines()
else:
    input_list = aocd.get_data(day=3).splitlines()

def part_1():
    contents = []
    for line in input_list:
        if (len(line) % 2 != 0):
            breakpoint
        half_length = len(line) // 2
        contents.append([line[0:half_length], line[half_length:]])
    
    char_sum = 0
    for compartments in contents:
        for comp_char in compartments[0]:
            if comp_char in compartments[1]:
                char_value = ord(comp_char) - ord('a') + 1
                if char_value <= 0: char_value += 26 + ord('a') - ord('A')
                char_sum += char_value
                break

    return char_sum

def part_2():
    contents = []
    group = []
    count = 0
    for line in input_list:
        group.append(line)
        count += 1
        if count % 3 == 0:
            contents.append(group)
            group = []
    
    char_sum = 0
    for compartments in contents:
        for comp_char in compartments[0]:
            if comp_char in compartments[1] and comp_char in compartments[2]:
                char_value = ord(comp_char) - ord('a') + 1
                if char_value <= 0: char_value += 26 + ord('a') - ord('A')
                char_sum += char_value
                break

    return char_sum

print(part_2())
