from aocd.models import Puzzle
from utils import maxes, pgriddict, tuple_add

def parse(input):
    return pgriddict(input, str)

def part_a(data):
    shift(data, (0, -1))
    return load(data)

def part_b(data):
    maxx, maxy = maxes(data)
    seen = { tostr(data, maxx, maxy): 0 }
    lower, upper = None, None
    for i in range(1000000000):
        cycle(data)
        strd = tostr(data, maxx, maxy)
        if strd in seen:
            lower, upper = (seen[strd], i+1)
            break
        else:
            seen[strd] = i+1
    offset = (1000000000 - lower) % (upper - lower)
    for i in range(offset):
        cycle(data)
    return load(data)

def tostr(data, maxx, maxy):
    out = ""
    for y in range(maxy + 1):
        out += ''.join(data[(x,y)] for x in range(maxx + 1))
    return out

def cycle(data):
    shift(data, (0, -1))
    shift(data, (-1, 0))
    shift(data, (0, 1))
    shift(data, (1, 0))

def shift(data, direction):
    test = [c for c in data if (data[c] == 'O' and (o := tuple_add(c, direction)) in data and data[o] == '.')]
    while test:
        for x in test:
            data[tuple_add(x, direction)] = 'O'
            data[x] = '.'
        test = [c for c in data if (data[c] == 'O' and (o := tuple_add(c, direction)) in data and data[o] == '.')]

def load(data):
    every = [c for c in data if data[c] == 'O']
    maxy = max(y for x,y in data)
    return sum(maxy + 1 - y for x,y in every)

puzzle = Puzzle(2023, 14)
print("part A", part_a(parse(puzzle.input_data)))
print("part B", part_b(parse(puzzle.input_data)))
