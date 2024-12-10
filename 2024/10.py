from collections import deque
from aocd.models import Puzzle
from utils import neighbrs_str8, pgriddict

def parse(input):
    return pgriddict(input, int)

def solve(grid):
    heads = [c for c in grid if grid[c] == 0]
    path_groups = [find_paths(grid, head) for head in heads]
    a = sum(len(exits) for _,exits in path_groups)
    b = sum(len(paths) for paths,_ in path_groups)
    return a,b

def find_paths(grid, head):
    q = deque([(head,)])
    paths, exits = set(), set()
    while q:
        path = q.popleft()
        for n in neighbrs_str8(path[-1]):
            if n in grid and n not in path and grid[n] == grid[path[-1]] + 1:
                npath = tuple([*path, n])
                if grid[n] == 9:
                    paths.add(npath)
                    exits.add(n)
                else: q.append(npath)
    return (paths, exits)

puzzle = Puzzle(2024, 10)
data = parse(puzzle.input_data)
a,b = solve(data)
print("part A", a)
print("part B", b)
