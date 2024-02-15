
from itertools import combinations 

def part_1():
    input_list = []
    with open("input.txt") as _file:
            for line in _file:
                input_list.append(int(line))

    increase_count = 0
    last_input = -10000

    for input in input_list:
        if last_input is not -10000:
            if input > last_input:
                increase_count += 1
        last_input = input
    
    print(increase_count)
            

def part_2():
    input_list = []
    with open("input.txt") as _file:
            for line in _file:
                input_list.append(int(line))

    increase_count = 0
    input_count = len(input_list)

    for i in range(input_count-3):

        if input_list[i+3] > input_list[i]:
            increase_count += 1
    
    print(increase_count)



part_2()