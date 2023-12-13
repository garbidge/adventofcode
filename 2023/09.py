from aocd.models import Puzzle
from utils import lmap

def parse(input):
    return [lmap(int, line.split()) for line in input.splitlines()]

def part_a(data):
    return sum(extrapolate(d) for d in data)

def part_b(data):
    return sum(extrapolate(d, True) for d in data)

def diffs(dat):
    return [dat[i + 1] - dat[i] for i in range(len(dat) - 1)]

def extrapolate(dat, fromStart=False):
    if all(d == 0 for d in dat): return 0
    if fromStart:
        return dat[0] - extrapolate(diffs(dat), fromStart)
    return dat[-1] + extrapolate(diffs(dat))

puzzle = Puzzle(2023, 9)
data = parse(puzzle.input_data)
print("part A", part_a(data))
print("part B", part_b(data))
