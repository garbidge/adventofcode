from collections import Counter
from aocd.models import Puzzle
from utils import plint

def parse(input):
    left, right = zip(*plint(input))
    return (sorted(left), sorted(right))

def part_a(left, right):
    return sum(abs(a-b) for a,b in zip(left, right))

def part_b(left, right):
    counts = Counter(right)
    return sum(n * counts[n] for n in left)

puzzle = Puzzle(2024, 1)
data = parse(puzzle.input_data)
print("part A", part_a(*data))
print("part B", part_b(*data))
