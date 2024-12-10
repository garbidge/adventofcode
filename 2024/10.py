from collections import deque
from aocd.models import Puzzle
from utils import neighbrs_str8, pgriddict

def parse(input):
    return pgriddict(input, int, lambda v: int(v))

def part_a(grid):
    heads = [c for c in grid if grid[c] == 0]
    return sum(score(grid, head) for head in heads)

def part_b(grid):
    heads = [c for c in grid if grid[c] == 0]
    return sum(rating(grid, head) for head in heads)

def score(grid, head):
    q = deque([head])
    visited, exits = set(), set()
    while q:
        point = q.popleft()
        for n in neighbrs_str8(point):
            if n in grid and n not in visited and grid[n] == grid[point] + 1:
                visited.add(n)
                if grid[n] == 9:
                    exits.add(n)
                else:
                    q.append(n)
    return len(exits)

def rating(grid, head):
    q = deque()
    q.append(tuple([head]))
    paths = set()
    while q:
        path = q.popleft()
        for n in neighbrs_str8(path[-1]):
            if n in grid and n not in path and grid[n] == grid[path[-1]] + 1:
                npath = tuple([*path, n])
                if grid[n] == 9:
                    paths.add(npath)
                else:
                    q.append(npath)
    return len(paths)

puzzle = Puzzle(2024, 10)
data = parse(puzzle.input_data)
print("part A", part_a(data))
print("part B", part_b(data))
