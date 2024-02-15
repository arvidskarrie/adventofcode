
from itertools import combinations
from typing import Tuple 

BRICK_SIZE_RANGE = range(5)

def check_row(row_list):
    for num in row_list:
        if not num[1]:
            return 0
    return 1
        
def check_if_bingo(brick, row, col):
    # Check row
    row_list = brick[row]
    col_list = [brick[i][col]  for i in BRICK_SIZE_RANGE]


    return check_row(row_list) or check_row(col_list)

def calc_bingo_value(brick, number):
    sum = 0
    for line in brick:
        for num in line:
            if not num[1]:
                sum += num[0]
    return sum * number


def part_1():
    bingo_bricks = []
    bingo_brick = []

    # initiate list and bricks
    #with open("input_test.txt") as _file:
    with open("input.txt") as _file:
        bingo_numbers = _file.readline().strip().split(',')

        for line in _file:
            if line == '\n':
                if bingo_brick:
                    bingo_bricks.append(bingo_brick)
                    bingo_brick = []
                continue
            
            bingo_line = []
            for number in line.split():
                bingo_line.append([int(number), 0])
            bingo_brick.append(bingo_line)

        bingo_bricks.append(bingo_brick)

    # Start to iterate over bingo_list
    for number in bingo_numbers:
        for brick in bingo_bricks:
            for row in BRICK_SIZE_RANGE:
                for col in BRICK_SIZE_RANGE:
                    if brick[row][col][0] == int(number):
                        brick[row][col][1] = 1
                        if check_if_bingo(brick, row, col):
                            return calc_bingo_value(brick, int(number))

def check_brick(brick, number):
    for row in BRICK_SIZE_RANGE:
        for col in BRICK_SIZE_RANGE:
            if brick[row][col][0] == int(number):
                brick[row][col][1] = 1
                if check_if_bingo(brick, row, col):
                    return True
    return False

                            
def part_2():
    bingo_bricks = []
    bingo_brick = []

    # initiate list and bricks
    #with open("input_test.txt") as _file:
    with open("input.txt") as _file:
        bingo_numbers = _file.readline().strip().split(',')

        for line in _file:
            if line == '\n':
                if bingo_brick:
                    bingo_bricks.append(bingo_brick)
                    bingo_brick = []
                continue
            
            bingo_line = []
            for number in line.split():
                bingo_line.append([int(number), 0])
            bingo_brick.append(bingo_line)

        bingo_bricks.append(bingo_brick)

    # Start to iterate over bingo_list
    for number in bingo_numbers:
        for i in range(len(bingo_bricks)):
            brick = bingo_bricks[i]
            if brick == 0:
                continue

            if check_brick(brick, int(number)):
                if brick == bingo_bricks[1]:
                    print('hej')
                print(calc_bingo_value(brick, int(number)))
                bingo_bricks[i] = 0



    


        

print(part_2())