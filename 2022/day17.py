
import os
os.environ["AOC_SESSION"] = "53616c7465645f5feb5f98622da494e1f359f67b2973c8f6a54ed362910e50e251d3f40a7189ffd45624f53a2c2e408b0039c07d21c2423c1ebce73b8d6b4bce"

from itertools import combinations, permutations
from functools import lru_cache
import aocd
import re

USE_TEST_DATA = 0
TEST_DATA = '>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>'
if USE_TEST_DATA:
    input_list = TEST_DATA.splitlines()
    CYCLE_ROUND_COUNT = 35
    CYCLE_POINTS = 53
else:
    input_list = aocd.get_data(day=17).splitlines()
    CYCLE_ROUND_COUNT = 1735
    CYCLE_POINTS = 2695

PUSH_RIGHT = '>'
PUSH_LEFT = '<'
BOARD_WIDTH = 7
NEW_X_POS = 2
NEW_Y_POS = 3

# Positions are defined from lower left pos (regardless if it exists or not)
# Higher x to the right, higher y upwards

class Piece:
    def __init__(self, piece_pos_tuple):
        self.piece_pos_tuple = piece_pos_tuple
        self.width = self.get_width()
    
    def __copy__(self):
        new_copy = Piece(self.piece_pos_tuple.copy())
        return new_copy

    def get_width(self):
        width = 0
        for piece in self.piece_pos_tuple:
            width = max(width, piece[0])
        return width + 1


    def is_move_possible(self, x_diff, y_diff, free_list):
        for piece in self.piece_pos_tuple:
            x = piece[0] + x_diff
            y = piece[1] + y_diff
            if y < 0 or x < 0 or x >= BOARD_WIDTH:
                return False
            if len(free_list) <= y:
                continue
            if free_list[y][x] == False:
                return False
        return True
    
    def move(self, x_diff, board):
        push_possible = self.is_move_possible(x_diff, 0, board.free_squares)
        if push_possible:
            self.update_pos(x_diff, 0)
        return push_possible
    
    def fall(self, board):
        fall_possible = self.is_move_possible(0, -1, board.free_squares)
        if fall_possible:
            self.update_pos(0, -1)
        return fall_possible

    def update_pos(self, x, y):
        for idx, piece in enumerate(self.piece_pos_tuple):
            self.piece_pos_tuple[idx] = (piece[0] + x, piece[1] + y)



class Pieces:
    def __init__(self):
        horiz = Piece([(0, 0), (1, 0), (2, 0), (3, 0)])
        plus  = Piece([(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)])
        j     = Piece([(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)])
        verti = Piece([(0, 0), (0, 1), (0, 2), (0, 3)])
        box   = Piece([(0, 0), (1, 0), (0, 1), (1, 1)])
        self.order = [horiz, plus, j, verti, box]

class Board:
    def __init__(self):
        self.free_squares = []
        self.update_height()
    
    def update_height(self):
        self.max_height = len(self.free_squares)
    def add_empty_row(self):
        self.free_squares.append([True] * BOARD_WIDTH)

    def update(self, new_pieces):
        for piece in new_pieces:
            if piece[1] >= len(self.free_squares) + 1:
                assert(False)
            if piece[1] == len(self.free_squares):
                self.add_empty_row()
            self.free_squares[piece[1]][piece[0]] = False

        self.update_height()

    def print(self):
        self.free_squares.reverse()
        for line in self.free_squares:
            new_str = ""
            for free in line:
                new_str += '.' if free else '#'
            print(new_str)
        self.free_squares.reverse()



def part_1(part):
    # 35 rounds = 53 height points
    # 2022 rounds = 35 rounds + 27 rounds + 56 * 53
        # if round % 35 == 0:
        #     print(round, board.max_height, board.max_height - old_max_height)
        #     old_max_height = board.max_height
    
    # for part 2, 1000000000000 = 35 + (1000000000000/35 - 1) + 1000000000000 % 35
    pieces = Pieces()
    board = Board()
    dir_list = list(input_list[0])
    wind_idx = 0

    old_max = 0
    old_max_inner = 0
    old_round = 0
    for round in range(CYCLE_ROUND_COUNT + part % CYCLE_ROUND_COUNT):            
    # for round in range(5*2022):
        if round % 5 == 0:
            if board.max_height - old_max <= 2:
                print(round, round - old_round, board.max_height, board.max_height - old_max_inner)
                old_max_inner = board.max_height
                old_round = round
            old_max = board.max_height



        new_piece = Piece(pieces.order[round % 5].piece_pos_tuple.copy())
        new_piece.update_pos(NEW_X_POS, board.max_height + NEW_Y_POS)

        while True:
            # Push to the side
            dir = dir_list[wind_idx % len(dir_list)]
            new_piece.move(-1 if dir == PUSH_LEFT else 1, board)
            wind_idx += 1

            # Fall down
            success = new_piece.fall(board)
            if not success:
                break

        # Fill board with the piece
        board.update(new_piece.piece_pos_tuple)

        # board.print()
        # print()
    return board.max_height + CYCLE_POINTS * (part//CYCLE_ROUND_COUNT - 1)






print(part_1(2022)) # == 3068
print(part_1(1000000000000)) # 1514285714288
