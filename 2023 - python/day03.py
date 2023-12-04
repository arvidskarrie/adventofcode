
import os
os.environ["AOC_SESSION"] = "53616c7465645f5f9cd071425b0d21d57535630a0d32e44bb5c7fe32070a07aa9170e67bb82f54f3bb900290fd1cb879c94a1e1230f809a51bec010d7f706512"
from itertools import combinations
import aocd
import re


USE_TEST_DATA = 1
TEST_DATA = '467..114..\n...*......\n..35..633.\n......#...\n617*......\n.....+.58.\n..592.....\n......755.\n...$.*....\n.664.598..'
NUMBER_REGEX = r'(\d+)'

def get_neighbours(z):
    x, y = z.real, z.imag
    return [
        complex(x + 1, y),     # Right
        complex(x - 1, y),     # Left
        complex(x, y + 1),     # Up
        complex(x, y - 1),     # Down
        complex(x + 1, y + 1), # Up-right
        complex(x - 1, y - 1), # Down-left
        complex(x + 1, y - 1), # Down-right
        complex(x - 1, y + 1)  # Up-left
    ]

def any_neighbour_is_symbol(z, symbol_list):
    for neigh in get_neighbours(z):
        if neigh in symbol_list:
            return True
    return False
    
def part_1():
    if USE_TEST_DATA:
        input_list = TEST_DATA.splitlines()
    else:
        input_list = aocd.get_data(day=3).splitlines()

    part_dict = {}
    symbol_list = []

    input_list.reverse()
    for (line_idx, line) in enumerate(input_list):
        matches = re.findall(NUMBER_REGEX, line)

        for match in matches:
            start_idx = line.find(match)
            part_dict[int(match)] = []
            for i in range(start_idx, start_idx + len(match)):
                part_dict[int(match)].append(i + line_idx * 1j)
        
        for (c_idx, c) in enumerate(line):
            if not c.isdigit() and c != '.':
                symbol_list.append(c_idx + line_idx * 1j)
    

    print(part_dict)
    # For each part, add to sum if there are any neightbours that are symbols
    part_sum = 0
    for (part, part_coords) in part_dict.items():
        for coord in part_coords:
            print("Coord: {}: {}".format(coord, get_neighbours(coord)))
            if any_neighbour_is_symbol(coord, symbol_list):
                part_sum += part
                break
    
    print(part_sum) # 307158 too low


part_1()