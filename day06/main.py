
from itertools import combinations 
import re
from collections import Counter
import string

def part_1():
    group_answers = {}
    number_of_answers = 0

    with open("input.txt") as _file:
    #with open("input_test.txt") as _file:
        for line in _file:
            if line == '\n':
                #Save group
                number_of_answers += len(group_answers)
                group_answers = {}

            for char in line.rstrip():
                group_answers[char] = 1
    number_of_answers += len(group_answers)

    return number_of_answers
            

def part_2():
    group_answers = 'EMPTY'
    number_of_answers = 0

    with open("input.txt") as _file:
        for line in _file:
            if line == '\n':
                #Save group
                print(group_answers, len(group_answers))
                number_of_answers += len(group_answers)
                group_answers = 'EMPTY'
                continue

            if group_answers == 'EMPTY':
                group_answers = line.rstrip()
            else:
                new_group_answers = ''
                for char in line.rstrip():
                    if char in group_answers:
                        new_group_answers += char
                group_answers = new_group_answers

    print(group_answers, len(group_answers))
    number_of_answers += len(group_answers)

    return number_of_answers

print(part_1()) # 6443
print(part_2()) # 3232