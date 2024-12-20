from collections import Counter, deque
from aocd.models import Puzzle
from utils import neighbrs_str8, pgriddict

def parse(input):
    return pgriddict(input, str)

def find_path(grid):
    start = next(c for c in grid if grid[c] == 'S')
    q = deque([(start, [start])])
    visited = set()
    while q:
        coord, path = q.popleft()
        if grid[coord] == 'E': return path
        elif coord not in visited:
            visited.add(coord)
            for n in neighbrs_str8(coord):
                if n in grid and grid[n] != '#':
                    q.append((n, [*path,n]))

def cheat(path, distance):
    total = 0
    for index_a,(x1,y1) in enumerate(path):
        for index_b,(x2,y2) in enumerate(path):
            if index_b > index_a:
                point_dist = abs(y2-y1) + abs(x2-x1)
                if point_dist <= distance and index_b - index_a - point_dist >= 100:
                    total += 1
    return total

puzzle = Puzzle(2024, 20)
grid = parse(puzzle.input_data)
path = find_path(grid)
print("part A", cheat(path, 2))
print("part B", cheat(path, 20))
