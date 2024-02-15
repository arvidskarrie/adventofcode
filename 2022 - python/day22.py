
import os
os.environ["AOC_SESSION"] = "53616c7465645f5feb5f98622da494e1f359f67b2973c8f6a54ed362910e50e251d3f40a7189ffd45624f53a2c2e408b0039c07d21c2423c1ebce73b8d6b4bce"

import aocd
import re

USE_TEST_DATA = 0
TEST_DATA = '        ...#\n        .#..\n        #...\n        ....\n...#.......#\n........#...\n..#....#....\n..........#.\n        ...#....\n        .....#..\n        .#......\n        ......#.\n\n10R5L5R10L4R5L5'
if USE_TEST_DATA:
    input_list = TEST_DATA.splitlines()
    SIDE_LENGTH = 4
else:
    input_list = aocd.get_data(day=22).splitlines()
    SIDE_LENGTH = 50

FLOOR = '.'
WALL = '#'
VOID = ' '

DIR_R = '>'
DIR_D = 'v'
DIR_L = '<'
DIR_U = '^'
ROTATION_LIST = [DIR_R, DIR_D, DIR_L, DIR_U]

TURN_CW = 'R'
TURN_CCW = 'L'
TURN_AROUND = 'U'
TURN_DICT = {TURN_CW: 1, TURN_CCW: -1, TURN_AROUND: 2}

regex_instr = r'(\d+)(\w)?'

class Position():
    def __init__(self, row, col, dir_idx) -> None:
        self.row = row
        self.col = col
        self.dir_idx = dir_idx
        self.dir = ROTATION_LIST[self.dir_idx]
        self.side = 1 if USE_TEST_DATA else 2

    def rotate(self, turn):
        self.dir_idx += TURN_DICT[turn]
        self.dir_idx %= 4
        self.dir = ROTATION_LIST[self.dir_idx]

    def make_transfer(self, side, row, col, dir):
        if USE_TEST_DATA:
            if side == 1:
                if   dir == DIR_R: return (False, 6, 11 - row, col + 4, TURN_AROUND)
                elif dir == DIR_D: side = 4
                elif dir == DIR_L: return (False, 3, 4, 4 + row, TURN_CCW) 
                elif dir == DIR_U: return (False, 2, 4, 11 - col, TURN_AROUND)
            elif side == 2:
                if   dir == DIR_R: side = 3
                elif dir == DIR_D: return (False, 5, 11, 11 - col, TURN_AROUND)
                elif dir == DIR_L: return (False, 6, 11, 19 - row, TURN_CW)
                elif dir == DIR_U: return (False, 1, 0, 11 - col, TURN_AROUND)
            elif side == 3:
                if   dir == DIR_R: side = 4
                elif dir == DIR_D: return (False, 5, 15 - col, 8, TURN_CCW)
                elif dir == DIR_L: side = 2
                elif dir == DIR_U: return (False, 1, col - 4, 8, TURN_CW)
            elif side == 4:
                if   dir == DIR_R: return (False, 6, 8, 19 - row, TURN_CW)
                elif dir == DIR_D: side = 5
                elif dir == DIR_L: side = 3
                elif dir == DIR_U: side = 1
            elif side == 5:
                if   dir == DIR_R: side = 6
                elif dir == DIR_D: return (False, 2, 7, 11 - col, TURN_AROUND)
                elif dir == DIR_L: return (False, 3, 7, 15 - row, TURN_CW)
                elif dir == DIR_U: side = 4
            elif side == 6:
                if   dir == DIR_R: return (False, 1, 11 - row, 11, TURN_AROUND)
                elif dir == DIR_D: return (False, 2, 19 - col, 0, TURN_CCW)
                elif dir == DIR_L: side = 5
                elif dir == DIR_U: return (False, 4, 19 - col, 11, TURN_CW)
        else:
            if side == 1:
                if   dir == DIR_R: return (False, 4, 149 - row, 99, TURN_AROUND)
                elif dir == DIR_D: return (False, 3, col - 50, 99, TURN_CW)
                elif dir == DIR_L: side = 2
                elif dir == DIR_U: return (False, 6, 199, col - 100, 0)
            elif side == 2:
                if   dir == DIR_R: side = 1
                elif dir == DIR_D: side = 3
                elif dir == DIR_L: return (False, 5, 149 - row, 0, TURN_AROUND)
                elif dir == DIR_U: return (False, 6, col + 100, 0, TURN_CW)
            elif side == 3:
                if   dir == DIR_R: return (False, 1, 49, 50 + row, TURN_CCW)
                elif dir == DIR_D: side = 4
                elif dir == DIR_L: return (False, 5, 100, row - 50, TURN_CCW)
                elif dir == DIR_U: side = 2
            elif side == 4:
                if   dir == DIR_R: return (False, 1, 149 - row, 149, TURN_AROUND)
                elif dir == DIR_D: return (False, 6, col + 100, 49, TURN_CW)
                elif dir == DIR_L: side = 5
                elif dir == DIR_U: side = 3
            elif side == 5:
                if   dir == DIR_R: side = 4
                elif dir == DIR_D: side = 6
                elif dir == DIR_L: return (False, 2, 149 - row, 50, TURN_AROUND)
                elif dir == DIR_U: return (False, 3, col + 50, 50, TURN_CW)
            elif side == 6:
                if   dir == DIR_R: return (False, 4, 149, row - 100, TURN_CCW)
                elif dir == DIR_D: return (False, 1, 0, col + 100, 0)
                elif dir == DIR_L: return (False, 2, 0, row - 100, TURN_CCW)
                elif dir == DIR_U: side = 5

        # Only side changed, nothing else
        return (True, side, row, col, 0)

    def is_transfer_needed(self, curr_row, curr_col, curr_dir):
        if curr_dir == DIR_R:
            return curr_col % SIDE_LENGTH == SIDE_LENGTH - 1
        elif curr_dir == DIR_L:
            return curr_col % SIDE_LENGTH == 0
        elif curr_dir == DIR_D:
            return (curr_row % SIDE_LENGTH == SIDE_LENGTH - 1)
        elif curr_dir == DIR_U:
            return curr_row % SIDE_LENGTH == 0
    
    def attempt_move(self, map):
        continue_as_normal = True
        new_side = 0
        rotation = 0
        if self.is_transfer_needed(self.row, self.col, self.dir):
            continue_as_normal, new_side, new_row, new_col, rotation = self.make_transfer(self.side, self.row, self.col, self.dir)
        
        if continue_as_normal:
            new_col = self.col
            new_row = self.row

            if   self.dir == DIR_R: new_col += 1
            elif self.dir == DIR_L: new_col -= 1
            elif self.dir == DIR_D: new_row += 1
            elif self.dir == DIR_U: new_row -= 1

        # If next tile is floor, go to it
        if map[new_row][new_col] == FLOOR:
            self.row = new_row
            self.col = new_col
            if new_side:
                self.side = new_side
            if rotation:
                self.rotate(rotation)
            return True

        # If it's a wall, break
        if map[new_row][new_col] == WALL:
            return False
        
        

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


print(part_1()) # 5031

# 122104 too high