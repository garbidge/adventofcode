from heapq import heappop, heappush
from aocd.models import Puzzle
from utils import maxes, pgriddict, tuple_add

directions = ['l','u','r','d']
dirmap = {'u': (0,-1), 'd': (0,1), 'l': (-1,0), 'r': (1, 0)}

def parse(input):
    return pgriddict(input, int)

def part_a(data):
    h = []
    heappush(h, (0, (0,0), 'r', 0))
    end = maxes(data)
    seen = set(((p, direction, length) for _,p,direction,length in h))
    while h:
        dist, point, direction, length = heappop(h)
        if point == end:
            return dist
        else:
            for next_state in next_nodes(point, direction, length):
                nextp, nextd, nextl = next_state
                if nextp in data and next_state not in seen:
                    seen.add(next_state)
                    heappush(h, (dist + data[nextp], nextp, nextd, nextl))

def next_nodes(point, direction, length):
    if length < 3:
        nextp = tuple_add(point, dirmap[direction])
        yield (nextp, direction, length + 1)
    for d in rotate(direction):
        nextp = tuple_add(point, dirmap[d])
        yield (nextp, d, 1)

def rotate(direction):
    index = directions.index(direction)
    return (directions[i % len(directions)] for i in (index-1, index+1))

def part_b(data):
    h = []
    heappush(h, (sum(data[p] for p in ((1,0), (2,0), (3,0), (4,0))), (4,0), 'r', 4))
    heappush(h, (sum(data[p] for p in ((0,1), (0,2), (0,3), (0,4))), (0,4), 'd', 4))
    end = maxes(data)
    seen = set(((p, direction, length) for _,p,direction,length in h))
    while h:
        dist, point, direction, length = heappop(h)
        if point == end:
            return dist
        else:
            for ndist, npoint, ndir, nlen in next_nodes_b(data, dist, point, direction, length):
                next_state = (npoint, ndir, nlen)
                if npoint in data and next_state not in seen:
                    seen.add(next_state)
                    heappush(h, (ndist, npoint, ndir, nlen))

def next_nodes_b(data, dist, point, direction, length):
    if length < 10:
        nextp = tuple_add(point, dirmap[direction])
        if nextp in data:
            yield (dist + data[nextp], nextp, direction, length + 1)
    for d in rotate(direction):
        nextp = point
        ndist = dist
        for _ in range(4):
            nextp = tuple_add(nextp, dirmap[d])
            if nextp in data: ndist += data[nextp]
        if nextp in data:
            yield (ndist, nextp, d, 4)

puzzle = Puzzle(2023, 17)
data = parse(puzzle.input_data)
print("part A", part_a(data))
print("part B", part_b(data))
