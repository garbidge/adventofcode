from aocd.models import Puzzle
from collections import defaultdict, deque
from math import ceil
from utils import maxes, neighbrs_str8, pgriddict

def parse(input):
    return pgriddict(input, str)

def solve(data):
    path = find_path(data)
    a = ceil(len(path) / 2)
    b = contained_tiles(data, path)
    return (a,b)

def neighbours(data, x, y):
    match data[(x, y)]:
        case '|': yield from ((x, y-1), (x, y+1))
        case '-': yield from ((x - 1, y), (x + 1, y))
        case 'L': yield from ((x, y - 1), (x + 1, y))
        case 'J': yield from ((x, y - 1), (x - 1, y))
        case '7': yield from ((x, y + 1), (x - 1, y))
        case 'F': yield from ((x, y + 1), (x + 1, y))
        case 'S':
            if (c := data[(x, y - 1)]) == "|" or c == "7" or c == "F":
                yield (x, y - 1)
            if (c := data[(x, y + 1)]) == "|" or c == "L" or c == "J":
                yield (x, y + 1)
            if (c := data[(x - 1, y)]) == "-" or c == "L" or c == "F":
                yield (x - 1, y)
            if (c := data[(x + 1, y)]) == "-" or c == "J" or c == "7":
                yield (x + 1, y)

def find_path(data):
    start = next(coord for coord in data if data[coord] == "S")
    current, end = neighbours(data, *start)
    seen = set((start, current))
    path = [start, current]
    while current != end:
        current = next(n for n in neighbours(data, *current) if n not in seen)
        seen.add(current)
        path.append(current)
    return path

def contained_tiles(data, path):
    bigger = expand(data, path)
    q = deque(((0, 0),))
    seen = set(q)
    while q:
        c = q.popleft()
        bigger[c] = " "
        for n in neighbrs_str8(c):
            if n not in seen and bigger[n] == ".":
                seen.add(n)
                q.append(n)
    return sum(bigger[(x, y)] == "." for x, y in bigger if x % 3 == 1 and y % 3 == 1)

def expand(data, path):
    path = set(path)
    maxx, maxy = maxes(data)
    bigger = defaultdict(str)
    for x in range(maxx + 1):
        for y in range(maxy + 1):
            value = data[(x, y)] if (x, y) in path else '.'
            for dx,dy in expanded('S'):
                bigger[(3*x + dx, 3*y + dy)] = "."
            for dx,dy in expanded(value):
                bigger[(3*x + dx, 3*y + dy)] = "█"
    return bigger

def expanded(value):
    match value:
        case 'S': return ((0, 0),(1, 0),(2, 0),(0, 1),(1, 1),(2, 1),(0, 2),(1, 2),(2, 2))
        case '|': return ((1, 0), (1, 1), (1, 2))
        case '-': return ((0, 1), (1, 1), (2, 1))
        case 'L': return ((1, 0), (1, 1), (2, 1))
        case 'J': return ((1, 0), (1, 1), (0, 1))
        case '7': return ((0, 1), (1, 1), (1, 2))
        case 'F': return ((2, 1), (1, 1), (1, 2))
    return ()


puzzle = Puzzle(2023, 10)
parsed = parse(puzzle.input_data)
a,b = solve(parsed)
print("part A", a)
print("part B", b)
