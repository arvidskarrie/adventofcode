
import os
os.environ["AOC_SESSION"] = "53616c7465645f5feb5f98622da494e1f359f67b2973c8f6a54ed362910e50e251d3f40a7189ffd45624f53a2c2e408b0039c07d21c2423c1ebce73b8d6b4bce"

import aocd
import re

USE_TEST_DATA = 0
TEST_DATA = '        ...#\n        .#..\n        #...\n        ....\n...#.......#\n........#...\n..#....#....\n..........#.\n        ...#....\n        .....#..\n        .#......\n        ......#.\n\n10R5L5R10L4R5L5'
if USE_TEST_DATA:
    input_list = TEST_DATA.splitlines()
else:
    input_list = aocd.get_data(day=22).splitlines()

FLOOR = '.'
WALL = '#'
VOID = ' '

DIR_R = '>'
DIR_L = '<'
DIR_U = '^'
DIR_D = 'v'
ROTATION_LIST = [DIR_R, DIR_D, DIR_L, DIR_U]

TURN_CW = 'R'
TURN_CCW = 'L'


regex_instr = r'(\d+)(\w)?'

class Position():
    def __init__(self, row, col, dir_idx) -> None:
        self.row = row
        self.col = col
        self.dir_idx = dir_idx
        self.dir = ROTATION_LIST[self.dir_idx]

    def rotate(self, dir):
        self.dir_idx += 1 if dir == TURN_CW else -1
        self.dir_idx %= 4
        self.dir = ROTATION_LIST[self.dir_idx]
    
    def attempt_move(self, map, curr_row = None, curr_col = None):
        if curr_row == None:
            curr_row = self.row
        if curr_col == None:
            curr_col = self.col
        row_mod = 0
        col_mod = 0
        if self.dir == DIR_R: col_mod = 1
        elif self.dir == DIR_L: col_mod = -1
        elif self.dir == DIR_D: row_mod = 1
        elif self.dir == DIR_U: row_mod = -1

        new_col = (curr_col + col_mod) % len(map[curr_row])
        new_row = (curr_row + row_mod) % len(map)

        # If next tile is floor, go to it
        if map[new_row][new_col] == FLOOR:
            self.row = new_row
            self.col = new_col
            return True

        # If it's a wall, break
        if map[new_row][new_col] == WALL:
            return False

        # If it's void, see if it's floor or wall further on
        if map[new_row][new_col] == VOID:
            return self.attempt_move(map, new_row, new_col)
        
        

def part_1():

    map = []
    instructions = []
    max_no_of_columns = 0
    for line in input_list:
        if line:
            if line[0] in [FLOOR, WALL, VOID]:
                max_no_of_columns = max(max_no_of_columns, len(line))
                map.append(list(line))
            else:
                instructions_regex = re.findall(regex_instr, line)
                for instr in instructions_regex:
                    instructions.append(int(instr[0]))
                    if instr[1] != '':
                        instructions.append(instr[1])

    # Extend every row to maximum length
    for row in map:
        row += [' '] * (max_no_of_columns - len(row))

    # Find first position
    for idx, tile in enumerate(map[0]):
        if tile in [FLOOR, WALL]:
            curr_pos = Position(0, idx, 0)
            break

    # Follow each instruction
    for instruction in instructions:
        # If it's a move, loop over the value
        print(instruction)
        if type(instruction) == int:
            for _num_moves in range(instruction):
                if curr_pos.attempt_move(map):
                    pass
                else:
                    break

        # Otherwise, rotate
        else:
            curr_pos.rotate(instruction)

    # Adjust for 0-indexed map
    return 1000 * (curr_pos.row + 1) + 4 * (curr_pos.col + 1) + curr_pos.dir_idx


print(part_1()) # 353837700405464 / 152
# print(part_1(2)) # 8302
