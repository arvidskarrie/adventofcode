
import os
os.environ["AOC_SESSION"] = "53616c7465645f5feb5f98622da494e1f359f67b2973c8f6a54ed362910e50e251d3f40a7189ffd45624f53a2c2e408b0039c07d21c2423c1ebce73b8d6b4bce"

from itertools import combinations
import aocd
import re


USE_TEST_DATA = 0
TEST_DATA = 'Sensor at x=2, y=18: closest beacon is at x=-2, y=15\nSensor at x=9, y=16: closest beacon is at x=10, y=16\nSensor at x=13, y=2: closest beacon is at x=15, y=3\nSensor at x=12, y=14: closest beacon is at x=10, y=16\nSensor at x=10, y=20: closest beacon is at x=10, y=16\nSensor at x=14, y=17: closest beacon is at x=10, y=16\nSensor at x=8, y=7: closest beacon is at x=2, y=10\nSensor at x=2, y=0: closest beacon is at x=2, y=10\nSensor at x=0, y=11: closest beacon is at x=2, y=10\nSensor at x=20, y=14: closest beacon is at x=25, y=17\nSensor at x=17, y=20: closest beacon is at x=21, y=22\nSensor at x=16, y=7: closest beacon is at x=15, y=3\nSensor at x=14, y=3: closest beacon is at x=15, y=3\nSensor at x=20, y=1: closest beacon is at x=15, y=3'

if USE_TEST_DATA:
    input_list = TEST_DATA.splitlines()
    TEST_LINE = 10
    max_xy = 21
    min_xy = 0
else:
    input_list = aocd.get_data().splitlines()
    TEST_LINE = 2000000
    max_xy = 4000001
    min_xy = 0

input_regex = r'Sensor at x=(.*), y=(.*): closest beacon is at x=(.*), y=(.*)'

class Sensor:
    def __init__(self, value_list):
        self.x = value_list[0]
        self.y = value_list[1]
        self.b_x = value_list[2]
        self.b_y = value_list[3]
        self.beacon_dist = abs(self.x - self.b_x) + abs(self.y - self.b_y)

def is_beacon_possible(x, y, sensors, beacons):
    # If it is a beacon: true
    if (x, y) in beacons:
        return True
    
    # If for any sensor:
    for sensor in sensors:
    #   the distance to the sensor is smaller than or equal to the distance to its beacon: false
        dist = abs(sensor.x - x) + abs(sensor.y - y)
        if dist <= sensor.beacon_dist:
            return False
    
    return True
    # else true

def part_1(part):
    sensors = set()
    beacons = set()
    minimum_y_value = 1e10
    maximum_y_value = -1e10
    for line in input_list:
        terms = re.findall(input_regex, line)
        terms = list(terms[0])
        terms = list(map(int, terms))
        sensor = Sensor(terms)
        sensors.add(sensor)
        beacon = tuple(terms[2:])
        if not beacon in beacons:
            beacons.add(beacon)
        minimum_y_value = min(minimum_y_value, terms[1] - sensor.beacon_dist)
        maximum_y_value = max(maximum_y_value, terms[1] + sensor.beacon_dist)

    minimum_y_value -= 10
    maximum_y_value += 10

    if part == 1:
        impossible_pos_count = 0
        y = TEST_LINE
        for x in range(minimum_y_value, maximum_y_value):
            impossible_pos_count += int(not is_beacon_possible(x, y, sensors, beacons))
        return impossible_pos_count
    elif part == 2:
        # Any available spot will be just outside the area of at least one sensor.
        # We can therefore limit the search to squares just outside sensor area.

        # For every sensor
        for sensor in sensors:
            # create a list of coords with distance one larger than beacon_dist.
            search_dist = sensor.beacon_dist + 1
            search_set = set()

            for t in range(search_dist):
                t_inv = search_dist - t
                search_set.add((sensor.x - t_inv, sensor.y - t))
                search_set.add((sensor.x + t, sensor.y - t_inv))
                search_set.add((sensor.x + t_inv, sensor.y + t))
                search_set.add((sensor.x - t, sensor.y + t_inv))

            for search_coord in search_set:
                # Check if that coord is in any other sensors range
                x = search_coord[0]
                y = search_coord[1]
                if x < min_xy or x > max_xy or y < min_xy or y > max_xy:
                    continue

                if not (x, y) in beacons:
                    if is_beacon_possible(x, y, sensors, beacons):
                        return (x * 4000000 + y)

print(part_1(1))
print(part_1(2))
