from aocd.models import Puzzle
from utils import pgriddict, tuple_add

dirs = [(0,-1), (1,0), (0,1), (-1,0)]

def parse(input):
    return pgriddict(input, str)

def part_a(data):
    pos = next(coord for coord in data if data[coord] == '^')
    _, path = run_to_end(data, pos, 0, set())
    return len(set(p for p,di in path))

def part_b(data):
    pos = next(coord for coord in data if data[coord] == '^')
    di, path, locations, attempted = 0, set(), set(), set()
    while pos in data and (pos, di) not in path:
        path.add((pos, di))
        nxt = tuple_add(pos, dirs[di])
        rotated_di = (di + 1) % len(dirs)
        if nxt in data and data[nxt] == '#': di = rotated_di
        else:
            if nxt in data and nxt not in attempted:
                attempted.add(nxt)
                data[nxt] = '#'
                is_cycle, _ = run_to_end(data, pos, rotated_di, set(path))
                if is_cycle: locations.add(nxt)
                data[nxt] = '.'
            pos = nxt
    return len(locations)

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
