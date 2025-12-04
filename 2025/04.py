from aocd.models import Puzzle
from utils import (
    neighbrs,
    pgriddict,
)

def parse(input):
    return pgriddict(input, str)

def part_a(data):
    removed, _ = step(data)
    return removed

def part_b(data):
    total = 0
    removed, data = step(data)
    while removed > 0:
        total += removed
        removed, data = step(data)
    return total

def step(data):
    new_data = data.copy()
    removed = 0
    for coord in data:
        if data[coord] == "@":
            neighbouring = sum(x in data and data[x] == "@" for x in neighbrs(coord))
            if neighbouring < 4:
                new_data[coord] = "."
                removed += 1
    return removed, new_data

puzzle = Puzzle(2025, 4)
data = parse(puzzle.input_data)
print("part A", part_a(data))
print("part B", part_b(data))
