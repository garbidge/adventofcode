from collections import Counter
from itertools import product
from aocd.models import Puzzle
from utils import (
    coord_dirs,
    coord_dirs_diag,
    coord_yield_dir,
    pgriddict
)

def parse(input):
    return pgriddict(input, str)

def part_a(data):
    coords = [coord for coord in data if data[coord] == 'X']
    directions = [d for d in coord_dirs(2) if d != (0,0)]
    count = 0
    for xpos, dir in product(coords, directions):
        path = coord_yield_dir(xpos, dir)
        if data[next(path)] == 'M' and data[next(path)] == 'A' and data[next(path)] == 'S':
            count += 1
    return count

def part_b(data):
    coords = [coord for coord in data if data[coord] == 'M']
    directions = coord_dirs_diag(2)
    counts = Counter()
    for mpos, dir in product(coords, directions):
        path = coord_yield_dir(mpos, dir)
        if data[(apos := next(path))] == 'A' and data[next(path)] == 'S':
            counts[apos] += 1
    return sum(count > 1 for count in counts.values())

puzzle = Puzzle(2024, 4)
data = parse(puzzle.input_data)
print("part A", part_a(data))
print("part B", part_b(data))