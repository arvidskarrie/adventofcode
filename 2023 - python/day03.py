
import os
os.environ["AOC_SESSION"] = "53616c7465645f5f9cd071425b0d21d57535630a0d32e44bb5c7fe32070a07aa9170e67bb82f54f3bb900290fd1cb879c94a1e1230f809a51bec010d7f706512"
import aocd
import re


USE_TEST_DATA = 0
TEST_DATA = '467..114..\n...*......\n..35..633.\n......#...\n617*......\n.....+.58.\n..592.....\n......755.\n...$.*....\n.664.598..'
NUMBER_REGEX = r'(\d+)'

NO_STAR_FOUND = (-1, -1)

def get_neighbours(coordinate):
    x, y = coordinate
    neighbours = []

    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            neighbours.append((x + dx, y + dy))
    return neighbours
    
def get_any_adjacent_star(start_idx, match_length, line_idx, input_list):
    for char_idx in range(start_idx, start_idx + match_length):
        neighbours = get_neighbours((char_idx, line_idx))
        for (x, y) in neighbours:
            if 0 <= y < len(input_list) and 0 <= x < len(input_list[y]) and input_list[y][x] == '*':
                return (x, y)
    return NO_STAR_FOUND

def part_1():
    if USE_TEST_DATA:
        input_list = TEST_DATA.splitlines()
    else:
        input_list = aocd.get_data(day=3).splitlines()

    # This dict will store any known stars with the adjacent number as value
    star_dict = {}
    part_sum = 0

    for (line_idx, line) in enumerate(input_list):
        matches = re.finditer(NUMBER_REGEX, line)

        for match in matches:
            start_idx = match.start()
            match_length = len(match.group())
            star_coord = get_any_adjacent_star(start_idx, match_length, line_idx, input_list)

            if NO_STAR_FOUND != star_coord:
                if star_coord in star_dict.keys():
                    # If the star is already in the dict, add the product between new and old number to sum
                    # The old number is removed, even if it could be left as well.
                    previous_part = star_dict.pop(star_coord)
                    part_sum += int(match.group()) * previous_part
                else:
                    # Otherwise store it in the dictionary
                    star_dict[star_coord] = int(match.group())
    
    print(part_sum)


part_1()