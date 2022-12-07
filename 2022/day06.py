
import os
os.environ["AOC_SESSION"] = "53616c7465645f5feb5f98622da494e1f359f67b2973c8f6a54ed362910e50e251d3f40a7189ffd45624f53a2c2e408b0039c07d21c2423c1ebce73b8d6b4bce"
import aocd

def part_1(msg_length):
    for idx in range (msg_length, len(aocd.get_data())):
        letter_list = str(aocd.get_data()[idx-msg_length:idx])
        if len(set(letter_list)) == len(letter_list):
            return idx

print(part_1(4))
print(part_1(14))
