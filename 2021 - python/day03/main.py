
from itertools import combinations 

def part_1():
    input_list = []
    #with open("input_test.txt") as _file:
    with open("input.txt") as _file:
        for line in _file:
            input_list.append(line.strip())

    no_of_inputs = len(input_list)
    no_of_bits = len(input_list[0])
    sum_list = [0 for _ in range(no_of_bits)]

    for input in input_list:
        for i in range(no_of_bits):
            sum_list[i] += int(input[i])

    sum_1 = 0
    sum_2 = 0
    for i in range(no_of_bits):
        sum_1 = sum_1 * 2 + int(sum_list[i] > no_of_inputs/2)
        sum_2 = sum_2 * 2 + int(sum_list[i] < no_of_inputs/2)

    print(sum_1 * sum_2)
    


        
            

def part_2():
    input_list = []
    oxygen = 0
    #with open("input_test.txt") as _file:
    with open("input.txt") as _file:
        for line in _file:
            input_list.append(line.strip())

    while(True):
        # Find the most common start value
        no_of_inputs = len(input_list)
        no_of_bits = len(input_list[0])
        sum_list = 0

        for input in input_list:
            sum_list += int(input[0])

        most_common = '1' if sum_list >= no_of_inputs/2 else '0'
        #oxygen = oxygen * 2 + int(sum_list >= no_of_inputs/2)
        oxygen = oxygen * 2 + int(sum_list < no_of_inputs/2)
        # Remove bad values
        new_input_list = []
        for input in input_list:
            if input[0] != most_common:
            #if input[0] == most_common:
                new_input_list.append(input[1:])

        if len(new_input_list) == 1:
            for char in new_input_list[0]:
                oxygen = oxygen * 2 + int(char)
            break
        else:
            input_list = new_input_list
        
        

    print(oxygen) # 3583
    print(3583*1601)

part_2()