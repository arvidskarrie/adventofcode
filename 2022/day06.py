
import os
os.environ["AOC_SESSION"] = "53616c7465645f5feb5f98622da494e1f359f67b2973c8f6a54ed362910e50e251d3f40a7189ffd45624f53a2c2e408b0039c07d21c2423c1ebce73b8d6b4bce"

import aocd

USE_TEST_DATA = 0
TEST_DATA = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'

if USE_TEST_DATA:
    input_list = TEST_DATA.splitlines()
else:
    input_list = aocd.get_data().splitlines()

def part_1(msg_length):
    for idx in range (msg_length, len(input_list[0])):
        letter_list = str(input_list[0][idx-msg_length:idx])
        if len(set(letter_list)) == len(letter_list):
            return idx

print(part_1(4))
print(part_1(14))
