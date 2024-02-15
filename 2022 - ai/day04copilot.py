
import os
os.environ["AOC_SESSION"] = "53616c7465645f5feb5f98622da494e1f359f67b2973c8f6a54ed362910e50e251d3f40a7189ffd45624f53a2c2e408b0039c07d21c2423c1ebce73b8d6b4bce"

import aocd
input_list = aocd.get_data(year=2022, day=4).splitlines()

# With two ranges as input, return true if either range is completely contained within the other range.
def is_contained(range1, range2):
    if range1[0] >= range2[0] and range1[1] <= range2[1]:
        return True
    elif range2[0] >= range1[0] and range2[1] <= range1[1]:
        return True
    else:
        return False


# With two ranges as input, return true if the ranges overlap.
def is_overlapping(range1, range2):
    if range1[0] <= range2[0] and range1[1] >= range2[0]:
        return True
    elif range2[0] <= range1[0] and range2[1] >= range1[0]:
        return True
    else:
        return False

def test_is_overlapping():
    assert is_overlapping([1, 5], [2, 4]) == True
    assert is_overlapping([1, 5], [0, 6]) == True
    assert is_overlapping([1, 5], [0, 2]) == True
    assert is_overlapping([1, 5], [4, 6]) == True
    assert is_overlapping([1, 5], [6, 8]) == False
    assert is_overlapping([1, 5], [0, 0]) == False

def test_is_contained():
    assert is_contained([1, 5], [2, 4]) == True
    assert is_contained([1, 5], [0, 6]) == True
    assert is_contained([1, 5], [0, 2]) == False
    assert is_contained([1, 5], [4, 6]) == False

# From a word on form aa-bb,cc-dd, create and return to ranges. The first range is [a, b], and the second range is [c, d].
# The integers a, b, c, and d are all in the range 0-255. Use a regex to find the ranges.
def create_ranges(word):
    import re
    ranges = re.findall(r"\d+", word)
    return [[int(ranges[0]), int(ranges[1])], [int(ranges[2]), int(ranges[3])]]



def test_create_ranges():
    assert create_ranges("1-3,5-7") == [[1, 3], [5, 7]]

# Go through an input list and create ranges for each word. Count the number of times a range is contained within another range.
def count_contained_ranges(input_list):
    count = 0
    for word in input_list:
        ranges = create_ranges(word)
        if is_contained(ranges[0], ranges[1]):
            count += 1
    return count

# Go through an input list and create ranges for each word. Count the number of times a range overlaps with another range.
def count_overlapping_ranges(input_list):
    count = 0
    for word in input_list:
        ranges = create_ranges(word)
        if is_overlapping(ranges[0], ranges[1]):
            count += 1
    return count


def main():
    test_is_contained()
    test_create_ranges()
    test_is_overlapping()
    print(count_contained_ranges(input_list))
    print(count_overlapping_ranges(input_list))


    
if __name__ == "__main__":
    main()


