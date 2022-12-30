
import os
os.environ["AOC_SESSION"] = "53616c7465645f5f5db34e7c4783f6c32cc4775884ae8ce61d21bd4408498b634616c2f58df5d26febef14f761e9fc3804220dc57ee470f5508edd9eac9d69fa"

import aocd
import re
from collections import deque
import copy

USE_TEST_DATA = 0
TEST_DATA = '#.######\n#>>.<^<#\n#.<..<<#\n#>v.><>#\n#<^v^^>#\n######.#'
if USE_TEST_DATA:
    input_list = TEST_DATA.splitlines()
else:
    input_list = aocd.get_data(day=24).splitlines()

INPUT_NO_OF_ROWS = len(input_list)
INPUT_NO_OF_COLS = len(input_list[0])
START_SPACE = (0, 1) # row, col
END_SPACE = (INPUT_NO_OF_ROWS - 1, INPUT_NO_OF_COLS - 2)  # row, col

RIGHT_WIND = 1
DOWN_WIND = 2
LEFT_WIND = 4
UP_WIND = 8
WALL = 16
AVAILABLE_SPACE = 32

WIND_LIST =  [RIGHT_WIND, DOWN_WIND, LEFT_WIND, UP_WIND]
WIND_RANGE = range(1, 16)

char_dict = {
    '#': WALL,
    '>': RIGHT_WIND,
    'v': DOWN_WIND,
    '<': LEFT_WIND,
    '^': UP_WIND,
    '.': 0,
    'O': AVAILABLE_SPACE
}

class WindInt(int):
    # def __init__(self, x: int) -> None:
    #     super().__init__()

    def contains(self, __x: int) -> bool:
        assert(__x in [RIGHT_WIND, DOWN_WIND, LEFT_WIND, UP_WIND])
        if __x == RIGHT_WIND: return self % (2 * RIGHT_WIND) >= RIGHT_WIND
        if __x == DOWN_WIND: return self % (2 * DOWN_WIND) >= DOWN_WIND
        if __x == LEFT_WIND: return self % (2 * LEFT_WIND) >= LEFT_WIND
        if __x == UP_WIND: return self % (2 * UP_WIND) >= UP_WIND

class Board:
    def __init__(self, input_list) -> None:
        self.width = len(input_list)
        self.height = len(input_list[0])
        self.possible_spaces = [START_SPACE]
        self.board = []
        self.empty_board = []
        for line in input_list:
            line_list = []
            empty_line_list = []
            for char in line:
                line_list.append(char_dict[char])
                empty_line_list.append(WALL if char == '#' else 0)
            self.board.append(line_list)
            self.empty_board.append(empty_line_list)

    def print(self):
        print()
        for row in self.board:
            row_str = ""
            for col in row:
                if col in WIND_RANGE and not col in WIND_LIST: 
                    row_str += "X"
                else:
                    row_str += next(key for key, value in char_dict.items() if value == col)
            print(row_str)
    
    def move_winds(self):
        new_winds = copy.deepcopy(self.empty_board)
        for row_idx, row in enumerate(self.board):
            for col_idx, col in enumerate(row):
                if col in WIND_RANGE:
                    self.move_winds_in_space(row_idx, col_idx, WindInt(col), new_winds)
        self.board = copy.deepcopy(new_winds)
    
    def move_winds_in_space(self, row_idx, col_idx, winds, new_winds):
        if winds.contains(RIGHT_WIND):
            new_col_idx = 1 if new_winds[row_idx][col_idx + 1] == WALL else col_idx + 1
            new_winds[row_idx][new_col_idx] += RIGHT_WIND
        if winds.contains(DOWN_WIND):
            new_row_idx = 1 if new_winds[row_idx + 1][col_idx] == WALL else row_idx + 1
            new_winds[new_row_idx][col_idx] += DOWN_WIND
        if winds.contains(LEFT_WIND):
            new_col_idx = INPUT_NO_OF_COLS - 2 if new_winds[row_idx][col_idx - 1] == WALL else col_idx - 1
            new_winds[row_idx][new_col_idx] += LEFT_WIND
        if winds.contains(UP_WIND):
            new_row_idx = INPUT_NO_OF_ROWS - 2 if new_winds[row_idx - 1][col_idx] == WALL else row_idx - 1
            new_winds[new_row_idx][col_idx] += UP_WIND
    
    def check_availability(self, test_list):
        proper_list = []
        for row, col in reversed(test_list):
            if self.board[row][col] == 0:
                proper_list.append((row, col))
        return proper_list


def get_neighbours(pos_tuple):
    row, col = pos_tuple
    neigh_list = [(row, col + 1), (row, col), (row, col - 1)]
    if row != 0: neigh_list.append((row - 1, col))
    if row != INPUT_NO_OF_ROWS - 1: neigh_list.append((row + 1, col))
    return neigh_list

def part_1(part):
    board = Board(input_list)

    total_rounds = 0
    for outer_round in range(3):
        curr_end_space = END_SPACE if outer_round in [0, 2] else START_SPACE
        available_spaces = [(START_SPACE)] if outer_round in [0, 2] else [(END_SPACE)]

        for round in range(2000):
            # Move winds
            board.move_winds()

            # Calculate new available spaces
            neighbours_to_test = []
            for av_space in available_spaces:
                neighbours_to_test += get_neighbours(av_space)
            neighbours_to_test = list(dict.fromkeys(neighbours_to_test))
            
            available_spaces = board.check_availability(neighbours_to_test)

            # Check end condition
            if curr_end_space in available_spaces:

                total_rounds += round + 1
                if outer_round == 0: print('For part 1:', round + 1)
                break
    return total_rounds
print(part_1(1))
