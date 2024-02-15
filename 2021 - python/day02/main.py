
from itertools import combinations 

def part_1():
    input_list = []
    with open("input.txt") as _file:
            for line in _file:
                input_list.append(line.split())

    coords = [0, 0]
    
    for input in input_list:
        if input[0] == 'up':
            coords[0] += int(input[1])
        elif input[0] == 'down':
            coords[0] -= int(input[1])
        elif input[0] == 'forward':
            coords[1] += int(input[1])
        else:
            breakpoint()
        
    print(coords, coords[0]*coords[1])
            

def part_2():
    input_list = []
    with open("input.txt") as _file:
            for line in _file:
                input_list.append(line.split())

    coords = [0, 0, 0]
    
    for input in input_list:
        if input[0] == 'up':
            coords[2] += int(input[1])
        elif input[0] == 'down':
            coords[2] -= int(input[1])
        elif input[0] == 'forward':
            coords[0] += int(input[1]) * coords[2]
            coords[1] += int(input[1])
        else:
            breakpoint()
        
    print(coords, coords[0]*coords[1])



part_2()