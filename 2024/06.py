from copy import deepcopy
from aocd.models import Puzzle
from utils import pgriddict, tuple_add

dirs = [
    (0,-1),
    (1,0),
    (0,1),
    (-1,0)
]

def parse(input):
    return pgriddict(input, str)

def part_a(data):
    return len(work(data))

def part_b(data):
    start = next(coord for coord in data if data[coord] == '^')
    path = work(data)
    total = 0
    mx = len(path)
    for i,point in enumerate(path):
        if point == start: continue
        print(i, '/', mx)
        clone = deepcopy(data)
        clone[point] = '#'
        if isloop(clone):
            total += 1
    return total

def work(data):
    pos = next(coord for coord in data if data[coord] == '^')
    path = set([pos])
    di = 0
    while pos in data:
        nxt = tuple_add(pos, dirs[di])
        if nxt in data:
            if data[nxt] == '#':
                di = (di + 1) % len(dirs)
            else:
                pos = nxt
                path.add(pos)
        else: pos = nxt
    return path

def isloop(data):
    pos = next(coord for coord in data if data[coord] == '^')
    di = 0
    path = set([(pos, dirs[di])])
    while pos in data:
        nxt = tuple_add(pos, dirs[di])
        key = (nxt, dirs[di])
        if key in path:
            return True
        if nxt in data:
            if data[nxt] == '#':
                di = (di + 1) % len(dirs)
            else:
                pos = nxt
                path.add(key)
        else: pos = nxt
    return False

puzzle = Puzzle(2024, 6)
data = parse(puzzle.input_data)
print("part A", part_a(data))
print("part B", part_b(data))
