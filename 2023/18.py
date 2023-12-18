from aocd.models import Puzzle
from utils import tuple_add

directions = {'U': (0,-1), 'D': (0,1), 'L': (-1,0), 'R': (1, 0)}

def parse(input):
    res = []
    for line in input.splitlines():
        d, num, x = line.split()
        res.append((d, int(num), x.strip("(#)")))
    return res

def part_a(data):
    perimeter = 0
    volume = 0
    points = [*pts(data)]
    for i in range(len(points) - 1):
        (x1,y1), (x2,y2) = points[i], points[i+1]
        perimeter += abs(x1-x2) + abs(y1-y2)
        # shoelace formula
        volume += ((x1 * y2) - (x2 * y1)) / 2
    # pick's theorem
    return int(volume + (perimeter / 2) + 1)

def part_b(data):
    res = []
    for _,_,hex in data:
        dd,nn = hexo(hex)
        res.append((dd,nn,hex))
    return part_a(res)

def pts(data):
    current = (0,0)
    yield current
    for d,num,_ in data:
        dx,dy = directions[d]
        current = tuple_add(current, (num*dx, num*dy))
        yield current

def hexo(hex):
    direction = ['R','D','L','U'][int(hex[-1])]
    length = int(hex[:-1], 16)
    return direction, length

puzzle = Puzzle(2023, 18)
data = parse(puzzle.input_data)
print("part A", part_a(data))
print("part B", part_b(data))
