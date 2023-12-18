
import os
os.environ["AOC_SESSION"] = "53616c7465645f5f9cd071425b0d21d57535630a0d32e44bb5c7fe32070a07aa9170e67bb82f54f3bb900290fd1cb879c94a1e1230f809a51bec010d7f706512"
import aocd
import re
import math
import collections
import itertools
import functools
import time

USE_TEST_DATA = 0
TEST_DATA = '.|...\\....\n|.-.\\.....\n.....|-...\n........|.\n..........\n.........\\\n..../.\\\\..\n.-.-/..|..\n.|....-|.\\\n..//.|....'

NEW_BEAM_LEFT = 0
NEW_BEAM_DOWN = 1
BEAM_DEAD = 2

class Beam:
    def __init__(self, pos, dir):
        self.pos: complex = pos
        self.dir: complex = dir
    
    def step(self, map):
        self.pos += self.dir

        # kill if out of bounds
        if (not 0 <= self.pos.real < len(map[0])) or \
            (not 0 <= self.pos.imag < len(map)):
            return BEAM_DEAD

        match map[int(self.pos.imag)][int(self.pos.real)]:
            case "/":
                # mirror along y = -x
                self.dir = self.dir.imag + self.dir.real * 1j
                pass
            case "\\":
                # mirror along y = x 
                self.dir = -(self.dir.imag + self.dir.real * 1j)
                pass
            case "-":
                if self.dir.real == 0:
                    # split into two new beams
                    # let this one turn to the right and a new one turn left
                    self.dir = 1 + 0j
                    return NEW_BEAM_LEFT
            case "|":
                if self.dir.imag == 0:
                    # split into two new beams
                    # let this one turn up and a new one turn down
                    self.dir = 0 + 1j
                    return NEW_BEAM_DOWN
                pass

def part_2():
    if USE_TEST_DATA:
        input_list = TEST_DATA.splitlines()
    else:
        with open("input.txt") as _file:
            input_list = [line.strip() for line in _file]

    input_list.reverse()
    best_result = 0

    # Generate all possible starting beams
    assert(len(input_list) == len(input_list[0])) # Assert square
    side_length = len(input_list)
    start_beams = [
        (-1 + k * 1j, 1 + 0j) for k in range(0, side_length)] + [
        (side_length + k * 1j, -1 + 0j) for k in range(0, side_length)] + [
        (k + side_length * 1j, 0 - 1j) for k in range(0, side_length)] + [
        (k - 1j, 0 + 1j) for k in range(0, side_length)]

    for (start_pos, start_dir) in start_beams:
        start_beam = Beam(start_pos, start_dir)
        unfinished_beam_stack = [start_beam]
        squares_done = set()
        while unfinished_beam_stack != []:
            beam = unfinished_beam_stack[0]
            while True:
                # If this identical situation have already been handled, break
                if (beam.pos, beam.dir) in squares_done:
                    unfinished_beam_stack.remove(beam)
                    break
                squares_done.add((beam.pos, beam.dir))

                step_result = beam.step(input_list)
                if step_result == NEW_BEAM_LEFT:
                    unfinished_beam_stack.append(Beam(beam.pos, -1 + 0j))
                if step_result == NEW_BEAM_DOWN:
                    unfinished_beam_stack.append(Beam(beam.pos, 0 - 1j))
                if step_result == BEAM_DEAD:
                    unfinished_beam_stack.remove(beam)
                    break
        
        squares_done.remove((start_pos, start_dir))

        energized_set = set(
            square[0] for square in squares_done
        )
        best_result = max(best_result, len(energized_set))
    print(best_result)


part_2()