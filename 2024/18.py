from collections import deque
from aocd.models import Puzzle
from utils import neighbrs_str8, plint

def parse(input):
    return plint(input)

def part_a(coords):
    grid = get_grid()
    for x,y in coords[:1024]: grid[(x,y)] = '#'
    return find_path(grid)

def part_b(coords):
    grid = get_grid()
    for x,y in coords: grid[(x,y)] = '#'
    for x,y in reversed(coords):
        grid[(x,y)] = '.'
        if find_path(grid): return f'{x},{y}'

def get_grid():
    return {(x,y): '.' for y in range(71) for x in range(71)}

def find_path(grid):
    q = deque([((0,0), 0)])
    visited = set([(0,0)])
    while q:
        coord, length = q.popleft()
        if coord == (70,70): return length
        for n in neighbrs_str8(coord):
            if n in grid and n not in visited and grid[n] != '#':
                visited.add(n)
                q.append((n, length + 1))

puzzle = Puzzle(2024, 18)
data = parse(puzzle.input_data)
print("part A", part_a(data))
print("part B", part_b(data))
