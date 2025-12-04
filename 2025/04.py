from aocd.models import Puzzle
from utils import pgriddict, neighbrs

def parse(input):
    grid = pgriddict(input, str)
    return {
        coord: sum(n in grid and grid[n] == "@" for n in neighbrs(coord))
        for coord in grid if grid[coord] == "@"
    }

def step(data):
    removed = [c for c in data if data[c] < 4]
    for coord in removed:
        del data[coord]
        for n in neighbrs(coord):
            if n in data: data[n] -= 1
    return len(removed)

puzzle = Puzzle(2025, 4)
data = parse(puzzle.input_data)
print("part A", len([c for c in data if data[c] < 4]))
print("part B", sum(iter(lambda: step(data), 0)))