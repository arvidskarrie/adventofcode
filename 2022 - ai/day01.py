
import os
os.environ["AOC_SESSION"] = "53616c7465645f5feb5f98622da494e1f359f67b2973c8f6a54ed362910e50e251d3f40a7189ffd45624f53a2c2e408b0039c07d21c2423c1ebce73b8d6b4bce"

import aocd
input_list = aocd.get_data(year=2022, day=1).splitlines()

# Split input list on empty line, then calculate the sum of each group, then return the largest sum
def largest_sum(input_list):
    # Split input list on empty line
    groups = []
    group = []
    for item in input_list:
        if item == '':
            groups.append(group)
            group = []
        else:
            group.append(int(item))
    groups.append(group)

    # Calculate the sum of each group and store in a list
    sums = []
    for group in groups:
        group_sum = sum(group)
        sums.append(group_sum)

    # Find the three largest sums
    largest_sums = sorted(sums, reverse=True)[:3]

    # Return the sum of the three largest sums
    return sum(largest_sums)

# Split input list on empty line, then calculate the sum of each group, then return the sum of the three largest sums
def sum_of_largest_sums(input_list):
    # Split input list on empty line and remove any leading/trailing whitespaces from each group
    groups = [group.strip() for group in "".join(input_list).split("\n\n")]

    # Calculate the sum of each group and store it in a dictionary
    sums_by_group = {}
    for group in groups:
        group_sum = sum(int(x) for x in group.split())
        sums_by_group[group] = group_sum

    # Get the three largest sums and return their sum
    largest_sums = sorted(sums_by_group.values(), reverse=True)[:3]
    return sum(largest_sums)

print(largest_sum(input_list))



#print(max([sum([len(set.intersection(*[set(x) for x in group.splitlines()])) for group in input_list])]))
