
import os
os.environ["AOC_SESSION"] = "53616c7465645f5feb5f98622da494e1f359f67b2973c8f6a54ed362910e50e251d3f40a7189ffd45624f53a2c2e408b0039c07d21c2423c1ebce73b8d6b4bce"

from itertools import combinations, permutations
from functools import lru_cache
import aocd
import re

import sys
sys.setrecursionlimit(10000)

USE_TEST_DATA = 0
TEST_DATA = '2,2,2\n1,2,2\n3,2,2\n2,1,2\n2,3,2\n2,2,1\n2,2,3\n2,2,4\n2,2,6\n1,2,5\n3,2,5\n2,1,5\n2,3,5'
if USE_TEST_DATA:
    input_list = TEST_DATA.splitlines()
else:
    input_list = aocd.get_data(day=18).splitlines()

class Droplet:
    def __init__(self, pos_list):
        self.x = pos_list[0]
        self.y = pos_list[1]
        self.z = pos_list[2]
    
    def get_neighbours_list(self):
        x_mod = [1, -1, 0, 0, 0, 0]
        y_mod = [0, 0, 1, -1, 0, 0]
        z_mod = [0, 0, 0, 0, 1, -1]
        neighbours = []
        for idx in range(6):
            neighbours.append((self.x + x_mod[idx], self.y + y_mod[idx], self.z + z_mod[idx]))
        return neighbours
def calc_max_min(pos_list, min_max_xyz):
    for idx in range(3):
        min_max_xyz[idx * 2] = min(min_max_xyz[idx * 2], pos_list[idx])
        min_max_xyz[idx * 2 + 1] = max(min_max_xyz[idx * 2 + 1], pos_list[idx])

def part_1(part):
    droplets = []
    droplets_pos = {}
    min_max_xyz = [1e10, 0, 1e10, 0, 1e10, 0]
    for line in input_list:
        pos_list = list(map(int, line.split(',')))
        pos_tuple = (pos_list[0], pos_list[1], pos_list[2])
        droplets.append(Droplet(pos_list))
        droplets_pos[pos_tuple] = 1
        calc_max_min(pos_list, min_max_xyz)
    if part == 1:
        total_surfaces = 6 * len(droplets)
        for drop in droplets:
            for neigh in drop.get_neighbours_list():
                if neigh in droplets_pos:
                    total_surfaces -= 1
        return total_surfaces

    # part 2
    for idx in range(6):
        min_max_xyz[idx] += -1 if idx %2 == 0 else 1
    air_particles = {}
    air_and_neighbour_particles = {}
    def map_neighbours(coord_tuple):
        x, y, z = coord_tuple
        def is_in_bounds(neigh_tuple):
            for dim in range(3):
                if neigh_tuple[dim] < min_max_xyz[dim*2] or min_max_xyz[dim*2 + 1] < neigh_tuple[dim]:
                    return False
            return True
        x_mod = [1, -1, 0, 0, 0, 0]
        y_mod = [0, 0, 1, -1, 0, 0]
        z_mod = [0, 0, 0, 0, 1, -1]

        for idx in range(6):
            neigh_tuple = (x + x_mod[idx], y + y_mod[idx], z + z_mod[idx])
            if not is_in_bounds(neigh_tuple):
                continue
            elif neigh_tuple in droplets_pos:
                if (x, y, z) in air_and_neighbour_particles:
                    air_and_neighbour_particles[(x, y, z)] += 1
                else:    
                    air_and_neighbour_particles[(x, y, z)] = 1
            elif not neigh_tuple in air_particles:
                air_particles[neigh_tuple]  = 1
                map_neighbours(neigh_tuple)
        
    # Initiate an air particle
    start_air_particle = (min_max_xyz[0], min_max_xyz[2], min_max_xyz[4])

    # Find all air particles using recursion and save any air particle that is neighbour with the droplet
    air_particles[start_air_particle] = 1
    map_neighbours(start_air_particle)

    # Count all the surfaces
    return sum(air_and_neighbour_particles.values())



        




print(part_1(1) == 64)
print(part_1(2))
