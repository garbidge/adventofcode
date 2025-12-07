from collections import Counter
from aocd.models import Puzzle
from utils import pgriddict

def parse(input):
    return pgriddict(input, str)

def solve(data):
    splitters = set()
    counts = Counter({next(c for c in data if data[c] == "S"): 1})
    max_y = 0
    for x,y in sorted(data, key=lambda xy: xy[1]):
        max_y = y
        if (x, y - 1) in counts:
            if data[(x, y)] == '^':
                splitters.add((x, y))
                counts[(x - 1, y)] += counts[(x, y - 1)]
                counts[(x + 1, y)] += counts[(x, y - 1)]
            else:
                counts[(x, y)] += counts[(x, y - 1)]
    return len(splitters), sum(count for (x,y),count in counts.items() if y == max_y)

puzzle = Puzzle(2025, 7)
data = parse(puzzle.input_data)
a,b = solve(data)
print("part A", a)
print("part B", b)