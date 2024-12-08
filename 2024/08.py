from itertools import combinations
from aocd.models import Puzzle
from utils import coord_yield_dir, pgriddict, tuple_add, tuple_sub

def parse(input):
    return pgriddict(input, str)

def part_a(data):
    antinodes, antenna_types = set(), set(v for v in data.values() if v != '.')
    for antenna in antenna_types:
        locations = [coord for coord in data if data[coord] == antenna]
        for a, b in combinations(locations, 2):
            dir_a, dir_b = tuple_sub(a, b), tuple_sub(b, a)
            for n in (tuple_add(a, dir_a), tuple_add(b, dir_b)):
                if n in data: antinodes.add(n)
    return len(antinodes)

def part_b(data):
    antinodes, antenna_types = set(), set(v for v in data.values() if v != '.')
    for antenna in antenna_types:
        locations = [coord for coord in data if data[coord] == antenna]
        for a, b in combinations(locations, 2):
            dir_a, dir_b = tuple_sub(a, b), tuple_sub(b, a)
            for start_coord, direction in ((b, dir_a), (a, dir_b)):
                for coord in coord_yield_dir(start_coord, direction, lambda coord: coord in data):
                    antinodes.add(coord)
    return len(antinodes)    

puzzle = Puzzle(2024, 8)
data = parse(puzzle.input_data)
print("part A", part_a(data))
print("part B", part_b(data))
