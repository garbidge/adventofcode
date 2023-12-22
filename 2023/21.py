import time
from aocd.models import Puzzle
from utils import maxes, neighbrs_str8, pgriddict

def parse(input):
    return pgriddict(input, str)

def part_a(data):
    start = next(x for x in data if data[x] == 'S')
    blocked = set(x for x in data if data[x] == '#')
    max_x, max_y = maxes(data)
    active = set((start,))
    for _ in range(64):
        active = step(active, blocked, max_x, max_y)
    return len(active)

def step(active, blocked, max_x, max_y):
    nextactive = set()
    for point in active:
        for nbr in neighbrs_str8(point):
            if nbr not in nextactive and not isblocked(blocked, *nbr, max_x, max_y):
                nextactive.add(nbr)
    return nextactive

def isblocked(blocked, x, y, max_x, max_y):
    x = x % (max_x+1)
    y = y % (max_y+1)
    return (x,y) in blocked

def part_b(data):
    start = next(x for x in data if data[x] == 'S')
    blocked = set(x for x in data if data[x] == '#')
    max_x, max_y = maxes(data)
    active = set((start,))
    size = max_x + 1
    rem = 26501365 % size
    ith_result = 26501365 // size
    points = []
    for iterations in (rem, size, size):
        for _ in range(iterations):
            active = step(active, blocked, max_x, max_y)
        points.append((len(points), len(active)))
    return int(interpolate(points, ith_result))

def interpolate(points, x):
    # lagrange interpolation
    (x0,y0), (x1,y1), (x2,y2) = points
    a = ((x-x1)*(x-x2)) / ((x0-x1)*(x0-x2))
    b = ((x-x0)*(x-x2)) / ((x1-x0)*(x1-x2))
    c = ((x-x0)*(x-x1)) / ((x2-x0)*(x2-x1))
    return a*y0 + b*y1 + c*y2

puzzle = Puzzle(2023, 21)
data = parse(puzzle.input_data)
print("part A", part_a(data))
print("part B", part_b(data))