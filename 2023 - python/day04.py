
import os
os.environ["AOC_SESSION"] = "53616c7465645f5f9cd071425b0d21d57535630a0d32e44bb5c7fe32070a07aa9170e67bb82f54f3bb900290fd1cb879c94a1e1230f809a51bec010d7f706512"
import aocd
import re


USE_TEST_DATA = 0
TEST_DATA = 'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53\nCard 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19\nCard 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1\nCard 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83\nCard 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36\nCard 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'
NUMBER_REGEX = r'^Card +(\d+): (.*) \| (.*)$'

def part_1():
    if USE_TEST_DATA:
        input_list = TEST_DATA.splitlines()
    else:
        input_list = aocd.get_data(day=4).splitlines()

    total_points = 0

    for (line_idx, line) in enumerate(input_list):
        print(line)
        matches = re.findall(NUMBER_REGEX, line)[0]
        # Card number is match 0
        
        winning_numbers = list(map(int, matches[1].split()))
        elf_numbers = list(map(int, matches[2].split()))
        
        card_score = 0.5
        for num in elf_numbers:
            if num in winning_numbers:
                card_score *= 2

        if card_score > 0.5:
            total_points += card_score

    print(total_points)
part_1()