import math
from aocd.models import Puzzle

def parse(input):
    return [tuple(int(n) for n in line.split(",")) for line in input.splitlines()]

def part_a(data):
    dist_map = {}
    for i,pos in enumerate(data):
        for j,other in enumerate(data[i+1:], start=i+1):
            dist_map[(i,j)] = math.dist(pos, other)
    ordered = sorted(dist_map, key=lambda indexpair: dist_map[indexpair])
    circuits = [set([pos]) for pos in data]
    for i,j in ordered[:1000]:
        set_a = next(s for s in circuits if data[i] in s)
        set_b = next(s for s in circuits if data[j] in s)
        circuits.remove(set_a)
        if set_a is not set_b: circuits.remove(set_b)
        circuits.append(set_a.union(set_b))
    results = sorted([len(x) for x in circuits], reverse=True)
    return math.prod(results[:3])

def part_b(data):
    dist_map = {}
    for i,pos in enumerate(data):
        for j,other in enumerate(data[i+1:], start=i+1):
            if i != j:
                dist_map[(i,j)] = math.dist(pos, other)
    ordered = sorted(dist_map, key=lambda indexpair: dist_map[indexpair])
    circuits = [set([pos]) for pos in data]
    last_i, last_j = -1, -1
    for i,j in ordered:
        if len(circuits) == 1:
            break
        set_a = next(s for s in circuits if data[i] in s)
        set_b = next(s for s in circuits if data[j] in s)
        circuits.remove(set_a)
        if set_a is not set_b: circuits.remove(set_b)
        circuits.append(set_a.union(set_b))
        last_i, last_j = i, j
    (x1,y1,z1) = data[last_i]
    (x2,y2,z2) = data[last_j]
    return x1 * x2

puzzle = Puzzle(2025, 8)
data = parse(puzzle.input_data)
print("part A", part_a(data))
print("part B", part_b(data))