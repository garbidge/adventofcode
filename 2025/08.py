import math
from aocd.models import Puzzle

def parse(input):
    return [tuple(int(n) for n in line.split(",")) for line in input.splitlines()]

def solve(data):
    a, b, dist_map = 0, 0, map_distances(data)
    ordered = sorted(dist_map, key=lambda indexpair: dist_map[indexpair])
    circuits = [set([pos]) for pos in data]
    for count,(i,j) in enumerate(ordered):
        if count == 1000:
            a = math.prod(sorted([len(x) for x in circuits], reverse=True)[:3])
        combine_sets(circuits, data[i], data[j])
        if len(circuits) == 1:
            break
    (x1,y1,z1) = data[i]
    (x2,y2,z2) = data[j]
    b = x1 * x2
    return a,b

def map_distances(data):
    dist_map = {}
    for i,pos in enumerate(data):
        for j,other in enumerate(data[i+1:], start=i+1):
            dist_map[(i,j)] = math.dist(pos, other)
    return dist_map

def combine_sets(circuits, pos_a, pos_b):
    set_a = next(s for s in circuits if pos_a in s)
    set_b = next(s for s in circuits if pos_b in s)
    if set_a != set_b:
        circuits.remove(set_a)
        circuits.remove(set_b)
        circuits.append(set_a.union(set_b))

puzzle = Puzzle(2025, 8)
data = parse(puzzle.input_data)
a,b = solve(data)
print("part A", a)
print("part B", b)