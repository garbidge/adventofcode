from aocd.models import Puzzle
from utils import plint

def parse(input):
    return plint(input)

def part_a(data):
    return sum(increasing(row) or decreasing(row) for row in data)

def part_b(data):
    return sum(increasing(row) or decreasing(row) or subrow_check(row) for row in data)

def increasing(row):
    return all(a < b <= a + 3 for a,b in zip(row, row[1:]))

def decreasing(row):
    return all(a > b >= a - 3 for a,b in zip(row, row[1:]))

def subrow_check(row):
    subrows = (row[:i] + row[i+1:] for i in range(len(row)))
    return any(increasing(s) or decreasing(s) for s in subrows)

puzzle = Puzzle(2024, 2)
data = parse(puzzle.input_data)
print("part A", part_a(data))
print("part B", part_b(data))
