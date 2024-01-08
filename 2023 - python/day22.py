
import os
os.environ["AOC_SESSION"] = "53616c7465645f5f9cd071425b0d21d57535630a0d32e44bb5c7fe32070a07aa9170e67bb82f54f3bb900290fd1cb879c94a1e1230f809a51bec010d7f706512"
from itertools import combinations
import aocd

USE_TEST_DATA = 0
TEST_DATA = '1,0,1~1,2,1\n0,0,2~2,0,2\n0,2,3~2,2,3\n0,0,4~0,2,4\n2,0,5~2,2,5\n0,1,6~2,1,6\n1,1,8~1,1,9'

def let_bricks_fall(bricks, only_small_falls = False):
    number_of_falls = 0

    bricks.sort(key=lambda b: b[0][2])
    all_brick_parts = set(
        part
        for other_brick in bricks
        for part in other_brick
    )

    brick_idx = 0
    while brick_idx < len(bricks):
        if not only_small_falls:
            print("Idx {} / {}".format(brick_idx, len(bricks)))
        brick = bricks[brick_idx]
        for (x, y, z) in brick:
            if z == 1:
                # On the floor
                break
            if not (x, y, z - 1) in brick and (x, y, z - 1) in all_brick_parts:
                break
        else:
            # Nothing in the way
            new_brick = [(x_n, y_n, z_n - 1) for (x_n, y_n, z_n) in brick]
            for part in brick:
                all_brick_parts.remove(part)
            for part in new_brick:
                all_brick_parts.add(part)
            bricks[brick_idx] = new_brick
            if not only_small_falls:
                continue
            else:
                number_of_falls += 1

        brick_idx += 1
        
    return number_of_falls

def part_1():

    if USE_TEST_DATA:
        input_list = TEST_DATA.splitlines()
    else:
        with open("input.txt") as _file:
            input_list = [line.strip() for line in _file]
    bricks = []
    for line in input_list:
        brick_strings = line.split("~")
        
        start_coords = list(map(int, brick_strings[0].split(",")))
        end_coords = list(map(int, brick_strings[1].split(",")))

        # Let a brick contain tuples with all parts of the brick
        brick = [(x, y, z) 
                 for x in range(start_coords[0], end_coords[0] + 1)
                 for y in range(start_coords[1], end_coords[1] + 1)
                 for z in range(start_coords[2], end_coords[2] + 1)
                ]
        brick.sort(key=lambda p: p[2])

        bricks.append(brick)
    
    # Starting from the bottom, no need to pass through multiple times    
    let_bricks_fall(bricks)
    
    # Try to remove every brick and see if anything reacts
    # If nothing reacts, it is desintegrationable
    fallen_bricks = 0
    for brick in bricks:
        bricks.remove(brick)
        fallen_bricks += let_bricks_fall(bricks, True)
        bricks.append(brick)

    print(fallen_bricks)
    print(fallen_bricks == 79144)


part_1()