
from itertools import combinations 
import re
from collections import Counter 

def part_1():
    input_list = []
    number_of_correct_passwords = 0
    with open("input.txt") as _file:
            for line in _file:
                split_line = re.split('-|: | |\n', line.rstrip())
                input_list.append(split_line)

    for password in input_list:
        count = Counter(password[3])
        if count[password[2]] in range(int(password[0]), int(password[1]) + 1):
            number_of_correct_passwords += 1

    print(number_of_correct_passwords)


def part_2():
    input_list = []
    number_of_correct_passwords = 0
    with open("input.txt") as _file:
            for line in _file:
                split_line = re.split('-|: | |\n', line.rstrip())
                input_list.append(split_line)

    for password in input_list:
        char_1 = password[3][int(password[0]) - 1]
        char_2 = password[3][int(password[1]) - 1]

        if (password[2] == char_1) != (password[2] == char_2):
            number_of_correct_passwords += 1

    print(number_of_correct_passwords)

part_2()