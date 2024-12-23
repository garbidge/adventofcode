from collections import defaultdict
from functools import reduce
from aocd.models import Puzzle

def parse(input):
    lookup = defaultdict(set)
    for a, b in [line.split('-') for line in input.splitlines()]:
        lookup[a].add(b)
        lookup[b].add(a)
    return lookup

def part_a(lookup):
    interconnected = set(frozenset((a,b)) for a in lookup for b in lookup[a])
    interconnected = add_neighbours(lookup, interconnected)
    return sum(any(computer.startswith('t') for computer in group) for group in interconnected)

def part_b(lookup):
    interconnected = set(frozenset((a,b)) for a in lookup for b in lookup[a])
    while len(interconnected) > 1:
        interconnected = add_neighbours(lookup, interconnected)
    return ','.join(sorted(interconnected.pop()))

def add_neighbours(lookup, interconnected):
    result = set()
    for group in interconnected:
        intersection = reduce(set.intersection, (lookup[n] for n in group))
        for n in intersection - group:
            result.add(frozenset(group | {n}))
    return result

puzzle = Puzzle(2024, 23)
data = parse(puzzle.input_data)
print("part A", part_a(data))
print("part B", part_b(data))
