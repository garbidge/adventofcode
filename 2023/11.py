from math import dist
from aocd.models import Puzzle
from utils import pgriddict

def parse(input: str):
    test = input.splitlines()
    cols, rows = set(), set()
    i = 0
    while i < len(test):
        if all(c == '.' for c in test[i]):
            rows.add(i)
            i += 1
        i += 1
    i = 0
    while i < len(test[0]):
        col = [test[x][i] for x in range(len(test))]
        if all(c == '.' for c in col):
            cols.add(i)
            i += 1
        i += 1
    return (pgriddict(input, str), rows, cols)

def path_sum(grid, rows, cols, expanded_size):
    total = 0
    galaxies = [coord for coord in grid if grid[coord] == '#']
    for i in range(len(galaxies)):
        for j in range(i+1, len(galaxies)):
            total += dist(galaxies[i], galaxies[j], rows, cols, expanded_size)
    return total

def dist(a, b, rows, cols, expanded_size):
    (ax,ay) = a
    (bx,by) = b
    distance = abs(bx-ax) + abs(by-ay)
    for i in range(min(ax,bx), max(ax,bx)+1):
        if i in cols:
            distance += expanded_size - 1
    for i in range(min(ay,by), max(ay,by)+1):
        if i in rows:
            distance += expanded_size - 1
    return distance

puzzle = Puzzle(2023, 11)
grid, rows, cols = parse(puzzle.input_data) 
print("part A", path_sum(grid, rows, cols, 2))
print("part B", path_sum(grid, rows, cols, 1000000))
