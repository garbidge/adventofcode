from collections import defaultdict, deque
from aocd.models import Puzzle
from utils import maxes, neighbrs_str8, pgriddict, tuple_add

dirmap = { '>': (1,0), '<': (-1,0), '^': (0,-1), 'v': (0,1)}

def parse(input):
    return pgriddict(input, str)

def part_a(data):
    max_x, max_y = maxes(data)
    location = next((x,y) for x,y in data if y == 0 and data[(x,y)] == '.')
    goal = next((x,y) for x,y in data if y == max_y and data[(x,y)] == '.')
    q = deque()
    q.append((location,))
    results = []
    while q:
        path = q.popleft()
        if path[-1] == goal:
            results.append(len(path) - 1)
        else:
            for n in nextnodes(data, path):
                if n not in path:
                    q.append((*path, n))
    return max(results)

def nextnodes(data, path):
    current = path[-1]
    if data[current] in dirmap:
        yield tuple_add(current, dirmap[data[current]])
    else:
        yield from (n for n in neighbrs_str8(current) if n in data and data[n] != '#')

def part_b(data):
    max_x, max_y = maxes(data)
    start = next((x,y) for x,y in data if y == 0 and data[(x,y)] == '.')
    goal = next((x,y) for x,y in data if y == max_y and data[(x,y)] == '.')
    nodes = set((x,y) for x,y in data if data[(x,y)] != '#')
    vertices = set((x,y) for x,y in nodes if len([*neighbours((x,y), nodes)]) > 2)
    vertices.add(start)
    vertices.add(goal)
    weights = defaultdict(lambda: defaultdict(int))
    for v in vertices:
        q = deque()
        q.append((v,))
        while q:
            path = q.pop()
            if len(path) > 1 and path[-1] in vertices:
                s, e = path[0], path[-1]
                weights[s][e] = max(len(path)-1, weights[s][e])
                weights[e][s] = max(len(path)-1, weights[e][s])
            else:
                for n in neighbrs_str8(path[-1]):
                    if n in nodes and n not in path:
                        q.append((*path, n))
    q = deque()
    q.append((0, (start,)))
    maxdist = 0
    while q:
        dist, path = q.pop()
        vertex = path[-1]
        if vertex == goal:
            maxdist = max(dist, maxdist)
        else:
            connected = weights[vertex]
            for v in connected:
                if v not in path:
                    q.append((dist + weights[vertex][v], (*path, v)))
    return maxdist

def neighbours(coord, nodes):
    yield from (n for n in neighbrs_str8(coord) if n in nodes)
    
def nextnodes_b(data, path):
    current = path[-1]
    yield from (n for n in neighbrs_str8(current) if n in data and data[n] != '#')

puzzle = Puzzle(2023, 23)
data = parse(puzzle.input_data)
print("part A", part_a(data))
print("part B", part_b(data))