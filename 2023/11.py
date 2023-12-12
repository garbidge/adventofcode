from itertools import combinations
from math import dist
from aocd.models import Puzzle
from utils import pgriddict

def parse(input: str):
    split = input.splitlines()
    rows = set(i for i, row in enumerate(split) if all(c == '.' for c in row))
    cols = set(i for i in range(len(split[0])) if all(c == '.' for c in [row[i] for row in split]))
    return (pgriddict(input, str), rows, cols)

def path_sum(grid, rows, cols, expanded_size):
    galaxies = [coord for coord in grid if grid[coord] == '#']
    return sum(dist(*a, *b, rows, cols, expanded_size) for a,b in combinations(galaxies, 2))

def dist(x1, y1, x2, y2, rows, cols, expanded_size):
    num_rows = sum(1 for r in range(min(y1,y2), max(y1,y2)) if r in rows)
    num_cols = sum(1 for c in range(min(x1,x2), max(x1,x2)) if c in cols)
    return abs(x1-x2) + abs(y1-y2) + (expanded_size - 1) * (num_rows + num_cols)

puzzle = Puzzle(2023, 11)
grid, rows, cols = parse(puzzle.input_data) 
print("part A", path_sum(grid, rows, cols, 2))
print("part B", path_sum(grid, rows, cols, 1000000))
