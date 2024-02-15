
import os
os.environ["AOC_SESSION"] = "53616c7465645f5feb5f98622da494e1f359f67b2973c8f6a54ed362910e50e251d3f40a7189ffd45624f53a2c2e408b0039c07d21c2423c1ebce73b8d6b4bce"

from itertools import combinations
import aocd
import re

USE_TEST_DATA = 0
TEST_DATA = 'R 5\nU 8\nL 8\nD 3\nR 17\nD 10\nL 25\nU 20'

if USE_TEST_DATA:
    input_list = TEST_DATA.splitlines()
else:
    input_list = aocd.get_data().splitlines()

def get_move_vector(move):
    dir = move[0]
    vel = int(move[2:])
    if dir == "U":
        return 0, 1, vel
    if dir == "D":
        return 0, -1, vel
    if dir == "R":
        return 1, 0, vel
    if dir == "L":
        return -1, 0, vel

def get_tail_move_vector(H, T):
    def get_one(val1, val2):
        if val1 == val2:
            return 0
        elif val1 > val2:
            return 1
        else:
            return -1

    # If H, T close, no move.
    if (abs(H[0] - T[0]) <= 1) and (abs(H[1] - T[1]) <= 1):
        return (0, 0, 0)

    # If H, T on the same row, one step that way
    # If H, T diagonal, T will move diagonally towards
    step_x = get_one(H[0], T[0])
    step_y = get_one(H[1], T[1])
    return (step_x, step_y, 1)

def part_1(part):
    tails_pos_dict = {}
    H_pos = [0, 0]
    T_pos = [0, 0]
    for move in input_list:
        # Calculate H position
        (move_x, move_y, times) = get_move_vector(move)
        for _ in range(times):
            H_pos[0] += move_x
            H_pos[1] += move_y

            # Calculate T position
            (move_tx, move_ty, _) = get_tail_move_vector(H_pos, T_pos)
            T_pos[0] += move_tx
            T_pos[1] += move_ty

            # Save T position in a dict
            tails_pos_dict[tuple(T_pos)] = 1

    # Find size of dict
    return(len(tails_pos_dict))


def part_2(part):
    tails_pos_dict = {}
    H_pos = [0, 0]
    T_pos = []

    no_of_tails = 1 if part == 1 else 9
    for i in range(no_of_tails):
        T_pos.append([0,0])
    
    for move in input_list:
        # Calculate H position
        (move_x, move_y, times) = get_move_vector(move)
        for _ in range(times):
            H_pos[0] += move_x
            H_pos[1] += move_y

            # Calculate T position
            prev_tail = H_pos
            for i in range(no_of_tails):
                (move_tx, move_ty, _) = get_tail_move_vector(prev_tail, T_pos[i])
                T_pos[i][0] += move_tx
                T_pos[i][1] += move_ty
                prev_tail = T_pos[i]

            # Save T position in a dict

            tails_pos_dict[tuple(T_pos[0 if part == 1 else 8])] = 1

    # Find size of dict
    return(len(tails_pos_dict))

# print(get_tail_move_vector([10, 8], [9, 9]) == (0,0))
# print(get_tail_move_vector([10, 8], [10, 18]) == (0, -1))
# print(get_tail_move_vector([10, 8], [5, 19]) == (1, -1))
# print(get_tail_move_vector([10, 8], [19, 9]) == (-1, -1))

print(part_2(1) == 6642)
print(part_2(2))
