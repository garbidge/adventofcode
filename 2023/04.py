from aocd.models import Puzzle
from itertools import repeat
from utils import lmap

def parse(input):
    for line in input.splitlines():
        a, b = lmap(set, [part.split() for part in line.split(" | ")])
        yield a & b

def part_a(data):
    return sum(2 ** (len(matches) - 1) for matches in data if matches)

def part_b(data):
    counts = [*repeat(1, len(data))]
    for i, intersected_set in enumerate(data):
        for x in range(len(intersected_set)):
            counts[i + x + 1] += counts[i]
    return sum(counts)

puzzle = Puzzle(2023, 4)
data = [*parse(puzzle.input_data)]
print("part A", part_a(data))
print("part B", part_b(data))
