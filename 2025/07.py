from collections import Counter, deque
from aocd.models import Puzzle
from utils import pgriddict, tuple_add

def parse(input):
    return pgriddict(input, str)

def part_a(data):
    start = next(c for c in data if data[c] == "S")
    q = deque([start])
    splitters = set()
    visited = set()
    while q:
        current = q.popleft()
        if current in visited:
            continue
        visited.add(current)
        down = tuple_add(current, (0, 1))
        if down in data:
            if data[down] == '^':
                splitters.add(down)
                q.append(tuple_add(down, (-1, 0)))
                q.append(tuple_add(down, (1, 0)))
            else:
                q.append(down)
    return len(splitters)

def part_b(data):
    start = next(c for c in data if data[c] == "S")
    q = deque([start])
    counts = Counter()
    counts[start] = 1
    visited = set()
    max_y = max(y for x,y in data)
    while q:
        (x,y) = q.popleft()
        if (x,y) in visited:
            continue
        visited.add((x,y))
        if (x, y+1) in data:
            if data[(x, y+1)] == '^':
                q.append((x-1, y+1))
                q.append((x+1, y+1))
                counts[(x-1, y+1)] += counts[(x, y)]
                counts[(x+1, y+1)] += counts[(x, y)]
            else:
                q.append((x, y+1))
                counts[(x, y+1)] += counts[(x, y)]
    return sum(v for k,v in counts.items() if k[1] == max_y)

puzzle = Puzzle(2025, 7)
data = parse(puzzle.input_data)
print("part A", part_a(data))
print("part B", part_b(data))
