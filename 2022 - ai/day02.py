
import os
os.environ["AOC_SESSION"] = "53616c7465645f5feb5f98622da494e1f359f67b2973c8f6a54ed362910e50e251d3f40a7189ffd45624f53a2c2e408b0039c07d21c2423c1ebce73b8d6b4bce"

import aocd
input_list = aocd.get_data(year=2022, day=3).splitlines()

# Split every word in the input list into two halves, and find the character common to both halves. Convert every common character to an integer value, a = 1, b = 2, A = 27, etc. Return the sum of all those integer values.
def find_common_chars(lst):
    total_sum = 0
    for word in lst:
        half_len = len(word) // 2
        left_half = word[:half_len]
        right_half = word[half_len:]
        common_char = list(set(left_half).intersection(set(right_half)))
        if common_char:
            char_value = ord(common_char[0].lower()) - 96 if common_char[0].islower() else ord(common_char[0].lower()) - 64 + 26
            total_sum += char_value
    return total_sum








def sum_common_characters(input_list):
    sum = 0
    for word in input_list:
        first_half = word[:len(word)//2]
        second_half = word[len(word)//2:]
        for i in range(len(first_half)):
            if first_half[i] == second_half[i]:
                if first_half[i].islower():
                    sum += ord(first_half[i]) - 96
                else:
                    sum += ord(first_half[i]) - 64 + 26
    return sum

print(find_common_chars(input_list))
