
import os
os.environ["AOC_SESSION"] = "53616c7465645f5feb5f98622da494e1f359f67b2973c8f6a54ed362910e50e251d3f40a7189ffd45624f53a2c2e408b0039c07d21c2423c1ebce73b8d6b4bce"

import aocd
input_list = aocd.get_data(year=2022, day=6).splitlines()

# Return true if all characters in the string are unique, false otherwise.
def is_unique(string):
    return len(string) == len(set(string))

# For a given word, find the first time that a n-character substring appears with n unique letters. Return the index of the last character in that substring, plus one.
# Have n as a parameter.

def find_unique_substring(word, n):
    for i in range(len(word) - n + 1):
        substring = word[i:i+n]
        if is_unique(substring):
            return i+n
    return -1


def main():
    print(find_unique_substring(input_list[0], 4))
    print(find_unique_substring(input_list[0], 14))


    
if __name__ == "__main__":
    main()


