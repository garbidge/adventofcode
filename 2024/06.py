from aocd.models import Puzzle
from utils import pgriddict, tuple_add

dirs = [(0,-1), (1,0), (0,1), (-1,0)]

def parse(input):
    return pgriddict(input, str)

def part_a(data):
    di, pos = 0, next(coord for coord in data if data[coord] == '^')
    _, path = run_to_end(data, pos, di, set())
    return len(set(p for p,di in path))

def part_b(data):
    di, pos = 0, next(coord for coord in data if data[coord] == '^')
    _, path = run_to_end(data, pos, di, set())
    distinct = set(p for p,di in path)
    total = 0
    for p in distinct:
        data[p] = '#'
        is_cycle, _ = run_to_end(data, pos, di, set())
        if is_cycle: total += 1
        data[p] = '.'
    return total

def run_to_end(data, pos, di, path):
    while pos in data and (pos, di) not in path:
        path.add((pos, di))
        nxt = tuple_add(pos, dirs[di])
        if nxt in data and data[nxt] == '#': di = (di + 1) % len(dirs)
        else: pos = nxt
    is_cycle = (pos, di) in path
    return (is_cycle, path)

puzzle = Puzzle(2024, 6)
data = parse(puzzle.input_data)
print("part A", part_a(data))
print("part B", part_b(data))
