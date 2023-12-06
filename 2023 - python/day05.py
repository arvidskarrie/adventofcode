
import os
os.environ["AOC_SESSION"] = "53616c7465645f5f9cd071425b0d21d57535630a0d32e44bb5c7fe32070a07aa9170e67bb82f54f3bb900290fd1cb879c94a1e1230f809a51bec010d7f706512"
import aocd
import re


USE_TEST_DATA = 0
TEST_DATA = 'seeds: 79 14 55 13\n\nseed-to-soil map:\n50 98 2\n52 50 48\n\nsoil-to-fertilizer map:\n0 15 37\n37 52 2\n39 0 15\n\nfertilizer-to-water map:\n49 53 8\n0 11 42\n42 0 7\n57 7 4\n\nwater-to-light map:\n88 18 7\n18 25 70\n\nlight-to-temperature map:\n45 77 23\n81 45 19\n68 64 13\n\ntemperature-to-humidity map:\n0 69 1\n1 0 69\n\nhumidity-to-location map:\n60 56 37\n56 93 4'
NUMBER_REGEX = r'(\d+)'

def part_1():
    if USE_TEST_DATA:
        input_list = TEST_DATA.splitlines()
    else:
        input_list = aocd.get_data(day=5).splitlines()

    seed_list_match = re.findall(NUMBER_REGEX, input_list[0])
    seed_list_match = list(map(int, seed_list_match))
    seed_range_list = []
    for seed in range(len(seed_list_match) // 2):
        seed_range_list.append((seed_list_match[2 * seed], seed_list_match[2 * seed] + seed_list_match[2 * seed + 1]))
    seed_range_list.sort(key=lambda x: x[0])

    # For every map, create a transformation 
    transformations_list = []
    current_map = []
    joined_lines = "\n".join(input_list[2:])
    parts = joined_lines.split("\n\n") # Every map is now its own \n-separated string
    for part in parts:
        current_map = []
        split_lines = part.split("\n")
        for line in split_lines[1:]: # skip the first title line
            # Add to the current map
            conv = re.findall(NUMBER_REGEX, line)
            conv = tuple(map(int, conv))
            (soil_start_idx, seed_start_idx, both_range) = conv
            new_conv = (seed_start_idx, seed_start_idx + both_range, soil_start_idx - seed_start_idx)
            current_map.append(new_conv)

        # Save the dict
        current_map.sort(key=lambda x: x[0])
        transformations_list.append(current_map)

    # Go through every stage from seed to location
    for transformations in transformations_list:
        # Do every seed range for every step
        new_seed_range_list = []
        for seed_range in seed_range_list:
            (seed_start, seed_stop) = seed_range
            for transformation in transformations:
                (trans_start, trans_stop, modification_needed) = transformation

                # If the seed range is fully outside transformation range, continue
                if trans_stop <= seed_start or seed_stop <= trans_start:
                    continue
                
                # Adjust if the tranformation start or stop is inside the seed range
                if seed_start < trans_start < seed_stop:
                    # Cut the head of seed range and add it back to seed range list
                    seed_range_list.append((seed_start, trans_start))
                    seed_stop = trans_stop
                if seed_start < trans_stop < seed_stop:
                    # Cut the tail of seed range and add it back to seed range list
                    seed_range_list.append((trans_stop, seed_stop))
                    seed_stop = trans_stop
                    
                new_seed_range_list.append((seed_start + modification_needed, seed_stop + modification_needed))
                break # next seed range

            else:
                # If no match is found, the value should remain.
                # This will only be executed of no break.
                new_seed_range_list.append(seed_range)
        
        seed_range_list = new_seed_range_list
    seed_range_list.sort(key=lambda x: x[0])
    print("lowest of lowest = {}". format(seed_range_list[0][0]))
part_1()