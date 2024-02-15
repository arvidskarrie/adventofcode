
from itertools import combinations 
import re
from collections import Counter
import string

def get_binary_data(data):

    decimal_seating_id = 0
    for char in data:
        decimal_seating_id *= 2
        decimal_seating_id += int(char == 'B') or int(char == 'R')
        
    return decimal_seating_id

def part_1():
    seating_data = []
    highest_numbered_seat = 0

    with open("input.txt") as _file:
    #with open("input_test.txt") as _file:
        for line in _file:
            seating = get_binary_data(line.rstrip())
            seating_data.append(seating)
            if seating > highest_numbered_seat:
                highest_numbered_seat = seating

    return highest_numbered_seat

def part_2():
    seating_data = []
    highest_numbered_seat = 0

    with open("input.txt") as _file:
    #with open("input_test.txt") as _file:
        for line in _file:
            seating = get_binary_data(line.rstrip())
            seating_data.append(seating)

    seating_data.sort()

    for i in range(len(seating_data)-1):
        if seating_data[i] + 1 != seating_data [i+1]:
            return seating_data[i]
            

print(part_1()) # 894
print(part_2()) # 578