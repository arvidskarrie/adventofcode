
import os
os.environ["AOC_SESSION"] = "53616c7465645f5feb5f98622da494e1f359f67b2973c8f6a54ed362910e50e251d3f40a7189ffd45624f53a2c2e408b0039c07d21c2423c1ebce73b8d6b4bce"

import aocd
input_list = aocd.get_data(year=2022, day=3).splitlines()

# Go through the input list and for every word: assert that there is an even number of letters; split the word in half; find the letter that exists in both halves; add the letter to a list.
# If there is no letter in both halves, then the word is invalid. If there is more than one letter in both halves, then the word is invalid.
def find_common_characters(input_list):
    common_characters = []
    for word in input_list:
        assert len(word) % 2 == 0
        first_half = word[:len(word)//2]
        second_half = word[len(word)//2:]
        common_char = list(set(first_half).intersection(set(second_half)))
        assert len(common_char) == 1
        common_characters.append(common_char[0])
    return common_characters





# Convert a char to an integer value. a = 1, b = 2, A = 27, B = 28, etc.
def char_to_int(char):
    if char.islower():
        return ord(char) - 96
    else:
        return ord(char) - 64 + 26

def test_char_to_int():
    assert char_to_int('a') == 1
    assert char_to_int('b') == 2
    assert char_to_int('A') == 27
    assert char_to_int('B') == 28

# Sum the integer values of all the common characters in the input list.
def sum_common_characters(input_list):
    return sum(map(char_to_int, input_list))


# Part 2

# Find the letter that appears in all words in the input list. The input list will always have three words, and exactly one letter will always appear in all three words. The letter will not always appear in the same position in all three words.
def find_common_letter(input_list):
    assert len(input_list) == 3
    first_word = input_list[0]
    second_word = input_list[1]
    third_word = input_list[2]
    for i in range(len(first_word)):
        if first_word[i] in second_word and first_word[i] in third_word:
            return first_word[i]
    assert False

def test_find_common_letter():
    assert find_common_letter(['abc', 'abc', 'abc']) == 'a'
    assert find_common_letter(['abc', 'abc', 'abd']) == 'a'
    assert find_common_letter(['abc', 'abc', 'adc']) == 'a'
    assert find_common_letter(['abc', 'abc', 'bbc']) == 'b'
    assert find_common_letter(['abc', 'abc', 'bbc']) == 'b'

# Take an input list, and partition it into groups of three. For each group of three, find the common letter, and add it to a list. Return the list.
def find_common_letters(input_list):
    common_letters = []
    for i in range(0, len(input_list), 3):
        common_letters.append(find_common_letter(input_list[i:i+3]))
    return common_letters


def main():
    test_char_to_int()
    test_find_common_letter()

    common_chars = find_common_letters(input_list)
    print(sum_common_characters(common_chars))

if __name__ == "__main__":
    main()


