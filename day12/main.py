
from itertools import combinations 
import re
from collections import Counter
import string
from copy import deepcopy

EAST = 0
SOUTH = 1
WEST = 2
NORTH = 3
FORWARD = 4
RIGHT = 5


direction_map = {
    'E': EAST,
    'S': SOUTH,
    'W': WEST,
    'N': NORTH,
    'F': FORWARD,
    'R': RIGHT}


def turn(current_direction, angle):
    return (current_direction + angle // 90) % 4

def part_1():
    instruction_list = []
    current_direction = EAST
    movement = {
        EAST: 0,
        NORTH: 0}
    
    with open("input.txt") as file:
    #with open("input_test.txt") as file:
        for line in file:
            direction = line[0]
            value = int(line[1:].rstrip())
            if direction == 'L':
                direction = 'R'
                value = (-value) % 360
            instruction_list.append([direction_map[direction], value])

    for [direction, value] in instruction_list:
        if direction == RIGHT:
            current_direction = turn(current_direction, value)
            continue
        elif direction == FORWARD:
            direction = current_direction
        
        if direction == SOUTH:
            direction = NORTH
            value *= -1
        elif direction == WEST:
            direction = EAST
            value *= -1

        movement[direction] += value

    return abs(movement[EAST]) + abs(movement[NORTH])

def part_2():
    instruction_list = []
    movement = {
        EAST: 0,
        NORTH: 0}
    waypoint = {
        EAST: 10,
        NORTH: 1}
    
    with open("input.txt") as file:
    #with open("input_test.txt") as file:
        for line in file:
            direction = line[0]
            value = int(line[1:].rstrip())
            if direction == 'L':
                direction = 'R'
                value = (-value) % 360
            instruction_list.append([direction_map[direction], value])

    for [direction, value] in instruction_list:
        if direction == RIGHT:
            # Rotate waypoint
            if value == 90:
                new_east = waypoint[NORTH]
                new_north = -waypoint[EAST]
            if value == 180:
                new_east = -waypoint[EAST]
                new_north = -waypoint[NORTH]
            if value == 270:
                new_east = -waypoint[NORTH]
                new_north = waypoint[EAST]

            waypoint[EAST] = new_east
            waypoint[NORTH] = new_north            
            continue

        if direction == FORWARD:
            difference_east = waypoint[EAST]
            difference_north = waypoint[NORTH]

            movement[EAST] += value * difference_east
            movement[NORTH] += value * difference_north

            continue
        
        if direction == SOUTH:
            direction = NORTH
            value *= -1
        elif direction == WEST:
            direction = EAST
            value *= -1

        waypoint[direction] += value

    return abs(movement[EAST]) + abs(movement[NORTH])



print(part_1()) # 2487
print(part_2()) # 892cd 