from collections import defaultdict, deque
from aocd.models import Puzzle
from utils import neighbrs_str8, plint

def parse(input):
    return plint(input)

def part_a(coords):
    grid = get_grid(coords, 1024)
    return len(find_path(grid))

def part_b(coords):
    lower = 0
    upper = len(coords) - 1
    middle = (upper + lower) // 2
    while middle > (lower + 1):
        print(lower, middle, upper)
        grid = get_grid(coords, middle)
        path = find_path(grid)
        if path is None:
            upper = middle
        else:
            lower = middle
        middle = (upper + lower) // 2
    n = lower
    grid = get_grid(coords, n)
    path = find_path(grid)
    print(n, ':', 'none' if path is None else len(path))
    while path is not None:
        n += 1
        grid = get_grid(coords, n)
        path = find_path(grid)
        print(n, ':', 'none' if path is None else len(path), coords[n-1], coords[n], coords[n+1])
    print(n, coords[n-1], coords[n], coords[n+1])
    return coords[n-1]

def get_grid(coords, num):
    grid = defaultdict(str)
    for x in range(71):
        for y in range(71):
            grid[(x,y)] = '.'
    for x,y in coords[:num]:
        grid[(x,y)] = '#'
    return grid

def find_path(grid):
    coord = (0,0)
    target = (70,70)
    q = deque([(coord,[])])
    visited = set([coord])
    while q:
        coord, path = q.popleft()
        if coord == target:
            return path
        for n in neighbrs_str8(coord):
            if n in grid and n not in visited and grid[n] != '#':
                visited.add(n)
                q.append((n, [*path, n]))
    return None

puzzle = Puzzle(2024, 18)
data = parse(puzzle.input_data)
print("part A", part_a(data))
print("part B", part_b(data))
