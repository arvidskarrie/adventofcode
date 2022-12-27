
import os
os.environ["AOC_SESSION"] = "53616c7465645f5feb5f98622da494e1f359f67b2973c8f6a54ed362910e50e251d3f40a7189ffd45624f53a2c2e408b0039c07d21c2423c1ebce73b8d6b4bce"

import aocd
import re
from collections import deque

USE_TEST_DATA = 0
TEST_DATA = '....#..\n..###.#\n#...#.#\n.#...##\n#.###..\n##.#.##\n.#..#..'
REAL_DATA = '.##.#.#......###..######...##.##.#..#.#.#.#######.###.#####...#...#..#\n#...######.#.#.#.##....#..##.###.#..##.#..#.....##.....#....###.##.##.\n.##.#.##..#.....#...###..#...##.##...........#.#..###.###...####.##..#\n##.#.##.#.####......#####..#.....#..#....###..#..####.##.#.###....####\n.....#...#.######...###..#....##.#.####.###.#..###...#.#.#..###.##...#\n#.#...#.##.....#..#######..##.###.###.####.#.##..##........#.#####..#.\n.#..###..#.....#..##.....#..#.##....#....##..###..#####.#....##.#.#..#\n#..##.##.#.##.#..#.#.#.#..#.#.#..#.#...######.###.#..##.##...##.#.##.#\n.##....#....#..#..#.###.......##.#..###..#....#.####....##.#.##...###.\n.....#.###.#....##.....#...###...##.#.#.#.....###.#..#..##..#..##.#.##\n..#..####..#####.####..#...#####..###.#..###.#.#####.####..##...###...\n..#.#.#.##.##.#.##.###.....##...##...#....#...#...##...#.#..####.#.###\n.##.#..##..........##.#....###..##....##.#.##....##.##.##.#.#.###.##..\n..###....#.#.#.....#.##.#.....#####.#.#...##..#..##.#....##.....##....\n###..##.#.#.#...#.#..#.#.#.##.#.#.....#..##.##.....##.#.#.##..###..###\n#....#.#...#..##.###...###.#.#####...#.###...##.####..##.####.#..##..#\n##..#.#.#####.#..######..###.......#..##..#..#.#.###.###.#..#.#..###..\n..####.#.##.###.#...##.##.......#...#...##.#.##..#.#.#.#.#...#..#..###\n..#..##...#.#.#.#..#...###..#.....###.##.####.#..#.#..#.....##.##.#.##\n.#.##.####..#.#.#...#.#.##....###.#.##....###...###.#...#####.##.#.#..\n..##....###...#.#..######.##.#...#.##.##..#.#.##..#.######..#.#.#..##.\n..#.......#...##.#...##.##...#####...##..##.#.#.##...###...#.#..####.#\n#.##..#####.......#.#.#.####..##..##...####...#...###.....##..#.#....#\n..#...#####.#.#..##.#..#.#.#.####..##....######..##........##..#.#...#\n###....#..###..#.###.####...##..#..##..##.#..##.###....#.####.#....##.\n.#.##.###.#.#####.#.#.#.#...#.#.#....#####.###.#.##..#.....##.#..###..\n#.##..##.#.####....#..##.#.#####...#.##....####...##.##.#..##......#..\n.#..........####....#.#.###...#....#.#.##...#.#...#...#...##.#.......#\n..#.#...#..#..#...#.#..##..##.#.....#...##.##.##.###.##.#.###.##.#.#..\n..##..##..#.#..#..#...##.##......#.#..#.#..##..#.##.####...####..#.#.#\n###...#....#.##.....###...#..#.#.....#.#..###.#..#####..#.#.#..#.##...\n#.#..#.###..##.##.#.#######.#.#..#.....#.#...########..####.##.#.#####\n.#.###.....##..##...####.##.###.....###....#.#....##.#.###..###.##.#.#\n######.#....##..##.#.##.##.###.####.##.###..#..##...###.#....#.#.#....\n#..###...#####.....##..##.#.#....#.######.####....##..#..###...#.#.#..\n......#.###....#...##.##.###.#.#....##...#..#..#..####.#.#..#.###.#.#.\n.##........#...#########.##...##.#..##..#.#..#.##.####..##....###.####\n#.#.###.#....#.##.##.#...##..######..#.#..####..#.####.#...#..#.##..#.\n####..##...##..#.####.#.#.#.....##...###.#.#....##....##.###.##.....#.\n#.####..#....####.#.#.##.....##.#####.#.#.####.##...##..#####.....##..\n.##.##.....##..#.....##.###.##.###.#.#..##..####.###..##..##...##.#..#\n.....#...#.##.#.#.....#.#.#.#..######..#..#.##.#.#......#....#..#..###\n.#..#...##.#..#.###....#..##..###...##.##.#.#..##..##...#.#.##.###...#\n..#.#.#.####.#.####....#.#....#..###....#..#.##.#....##..#.#..###..##.\n.#..#.####..#.....##.######.#.##..##..#.##.##..##.#..##.#.####..#..##.\n####.#...##..########..#.#..#...#.#.#####.#..#.......##.###..###.###.#\n.###.###....#..#..###.....#.#.#.#...#.###.#.##.##.####.#.###..##..#..#\n...##.#.#.######..##..#.#.#..#.#.#....#.....#.#..##.#......##..#####.#\n#####.#.#.#.##..####.####.....##...#.#####...#.###..#...#...#######..#\n...####..##..##....####.........#.#.#.##.#..#.###...##..###..#...#...#\n.#..##...###.####.##.....#..#..#....#.#.#.#####.#...##....#####.####..\n###.#..##.#.#.##......#.##.####...#...#..##..#..####..###...##.#..####\n####.#...#.....##..#....#........###.#..#.#...#..##..#..#.#...####.#..\n#.#...###.##.##..#####.##....##.#....#.##....####...###.....##.#.#.###\n#.#..#.###.......#.###..#....###..#...##.###.###..###........#..#.##.#\n.##.#..##..#..##..###.#...#.#.#.#.#.#.##.###.#.##.#######.#.##...#...#\n#.####..###.#.....#........#...###..#..#.#.#.#..#.##....##.#...#...##.\n##..###..###...#..#.######....###.##...##..##.#....#.....##..##..##..#\n##.#....#.##.###..###.######.#..#.#..#.##..#.#....##.#.##..#......###.\n.##..##.#..#.#.##..##..#..#..###....#..#.#.###.#....##.#..###..#.#..##\n..#..########.###.#########.##.#####.....#....#####....#.#...#.#..#.##\n..####...#####.#..###.#.#.###.####.###...##..#..#..##.......###.###..#\n.#.####.#..##.#####.###.#########.#...#...###.###.#.##...##.#####..#.#\n##...#..#..#.##.####....#....##.#.###.#....#.#.....###..#.###.#..#.##.\n.#.##.....#...#...#......#..#.##..###....#.##..###......#..#.####..#.#\n#.##.##.#####.##........####.##.#.###...##..####.#....#.##..##.#####..\n#..#.###.##.####..#..#.##.#.#####..##...#######.#.##.####.#.#.....#.#.\n###........#...#...####...#.############.#...#...#..#.#.#..#.....##.#.\n...##...#...#.##...###..#..###.##....#.###.....####....##..#.#..#..##.\n###...###.####.###..#.#..###.####..#.##..#..#...##.###........#.##..#.'
# TEST_DATA = '.....\n..##.\n..#..\n.....\n..##.\n.....'
if USE_TEST_DATA:
    input_list = TEST_DATA.splitlines()
else:
    input_list = REAL_DATA.splitlines()

ELF = '#'
NOT_ELF = '.'

NORTH = ((0, 1), [(-1, 1), (0, 1), (1, 1)])
SOUTH = ((0, -1), [(-1, -1), (0, -1), (1, -1)])
WEST = ((-1, 0), [(-1, -1), (-1, 0), (-1, 1)])
EAST = ((1, 0), [(1, -1), (1, 0), (1, 1)])
PRIO_LIST = [NORTH, SOUTH, WEST, EAST]
NO_SUGGESTION = -2

def set_proposal(coords, elf_dict, prio_list):
    x, y = coords
    for test_dir in prio_list:
        if is_dir_okay(coords, elf_dict.keys(), test_dir):
            elf_dict[coords] = (x + test_dir[0][0], y + test_dir[0][1])
            return True
    return False

def has_any_neighbour(coords, elf_dict_keys):
    # Get neighbour coords list:
    x, y = coords
    neigh_coords = [(x+1, y+0), (x+1, y+1), (x+0, y+1), (x-1, y+1), (x-1, y+0), (x-1, y-1), (x+0, y-1), (x+1, y-1)]

    for other_elf in elf_dict_keys:
        if other_elf in neigh_coords:
            return True
    return False

def is_dir_okay(coords, elf_dict, dir):
    for test_positions in dir[1]:
        x = coords[0] + test_positions[0]
        y = coords[1] + test_positions[1]
        if (x, y) in elf_dict:
            return False
    return True

def set_suggested_pos(coords, sugg, elf_dict):
    elf_dict[sugg] = NO_SUGGESTION
    del elf_dict[coords]

def part_1(part):
    elf_dict = {}
    for y_value, row in enumerate(input_list):
        for x_value, char in enumerate(row):
            if char == '#':
                inverse_y_value = -y_value # Positiv y upwards
                elf_dict[(x_value, inverse_y_value)] = NO_SUGGESTION

    for round in range(10000):
        print(round, len(elf_dict))
        # Set correct prio based on round
        prio_list = deque(PRIO_LIST)
        prio_list.rotate(-round) # check
        prio_list = list(prio_list)

        # Insert all proposals in elf_dict
        for coords, sugg in elf_dict.items():
            # stand still if no neighbours or no possible move
            elf_dict[coords] = NO_SUGGESTION
            if has_any_neighbour(coords, elf_dict.keys()):
                set_proposal(coords, elf_dict, prio_list)

        someone_moved = False
        old_elf_dict = elf_dict.copy()
        for coords, sugg in old_elf_dict.items():
            if sugg == NO_SUGGESTION:
                continue
            # If no other elf has the suggested position, make the move
            if sum(map(lambda x: x == sugg, elf_dict.values())) == 1:
                set_suggested_pos(coords, sugg, elf_dict)
                someone_moved = True

        if someone_moved:
            pass
        else:
            return round+1

print(part_1(1)) # 29243 too high
