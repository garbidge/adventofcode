from collections import deque
from functools import reduce
from aocd.models import Puzzle
from utils import neighbrs_str8, pgriddict

def parse(input):
    return pgriddict(input, int)

def solve(grid):
    heads = [c for c in grid if grid[c] == 0]
    counts = [path_counts(grid, head) for head in heads]
    return sum(a for a,_ in counts), sum(b for _,b in counts)

def path_counts(grid, head):
    q = deque([(head, set())])
    exits = list()
    while q:
        coord, visited = q.popleft()
        for n in neighbrs_str8(coord):
            if n in grid and n not in visited and grid[n] == grid[coord] + 1:
                if grid[n] == 9: exits.append(n)
                else: q.append((n, {*visited, n}))
    return (len(set(exits)), len(exits))

puzzle = Puzzle(2024, 10)
data = parse(puzzle.input_data)
a,b = solve(data)
print("part A", a)
print("part B", b)
