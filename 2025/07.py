from collections import Counter
from aocd.models import Puzzle

def solve(input):
    grid = input.splitlines()
    splitters = set()
    counts = Counter({(grid[0].index('S'), 0): 1})
    for y,line in enumerate(grid):
        for x,char in enumerate(line):
            if (x, y - 1) in counts:
                if char == '^':
                    splitters.add((x, y))
                    counts[(x - 1, y)] += counts[(x, y - 1)]
                    counts[(x + 1, y)] += counts[(x, y - 1)]
                else:
                    counts[(x, y)] += counts[(x, y - 1)]
    return len(splitters), sum(count for (x,y),count in counts.items() if y == len(grid) - 1)

puzzle = Puzzle(2025, 7)
a,b = solve(puzzle.input_data)
print("part A", a)
print("part B", b)