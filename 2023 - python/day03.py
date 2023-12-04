
import os
os.environ["AOC_SESSION"] = "53616c7465645f5f9cd071425b0d21d57535630a0d32e44bb5c7fe32070a07aa9170e67bb82f54f3bb900290fd1cb879c94a1e1230f809a51bec010d7f706512"
from itertools import combinations
import aocd
import re


USE_TEST_DATA = 0
TEST_DATA = '467..114..\n...*......\n..35..633.\n......#...\n617*......\n.....+.58.\n..592.....\n......755.\n...$.*....\n.664.598..'
NUMBER_REGEX = r'(\d+)'

def get_neighbours(coordinate, max_length, max_width):
    x, y = coordinate
    neighbours = []

    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue  # Skip the original coordinate itself

            nx, ny = x + dx, y + dy

            # Check if the new coordinates are within the boundaries
            if 0 <= nx < max_width and 0 <= ny < max_length:
                neighbours.append((nx, ny))

    return neighbours
    
def is_adjacent_to_symbol(start_idx, match_length, line_idx, input_list, input_length, input_width):
    for char_idx in range(start_idx, start_idx + match_length):
        neighbours = get_neighbours((char_idx, line_idx), input_length, input_width)
        for (x, y) in neighbours:
            if (not input_list[y][x].isdigit()) and (input_list[y][x] != '.'):
                return True
    return False

def part_1():
    if USE_TEST_DATA:
        input_list = TEST_DATA.splitlines()
    else:
        input_list = aocd.get_data(day=3).splitlines()

    input_length = len(input_list)
    input_width = len(input_list[0])

    part_sum = 0
    for (line_idx, line) in enumerate(input_list):
        matches = re.finditer(NUMBER_REGEX, line)

        for match in matches:
            start_idx = match.start()
            match_length = len(match.group())
            if is_adjacent_to_symbol(start_idx, match_length, line_idx, input_list, input_length, input_width):
                part_sum += int(match.group())
    
    print(part_sum)


part_1()