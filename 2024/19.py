from functools import cache
from aocd.models import Puzzle

def parse(input):
    patterns, designs = input.split('\n\n')
    return patterns.split(', '), designs.splitlines()

def part_a(patterns, designs):
    return sum(possible_count(towel, get_parts(towel, patterns)) > 0 for towel in designs)

def part_b(patterns, designs):
    return sum(possible_count(towel, get_parts(towel, patterns)) for towel in designs)

def get_parts(towel, patterns):
    return tuple(p for p in patterns if p in towel)

@cache
def possible_count(towel, parts):
    if len(towel) == 0: return 1
    return sum(possible_count(towel[len(p):], parts) for p in parts if towel.startswith(p))

puzzle = Puzzle(2024, 19)
data = parse(puzzle.input_data)
print("part A", part_a(*data))
print("part B", part_b(*data))
