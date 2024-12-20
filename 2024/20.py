from collections import Counter, deque
from aocd.models import Puzzle
from utils import neighbrs_str8, pgriddict

def parse(input):
    return pgriddict(input, str)

def part_a(grid):
    start = next(c for c in grid if grid[c] == 'S')
    end = next(c for c in grid if grid[c] == 'E')
    q = deque([(start, [start])])
    visited = set()
    real_path = None
    while q:
        coord, path = q.popleft()
        if coord == end:
            real_path = path
            break
        elif coord not in visited:
            visited.add(coord)
            for n in neighbrs_str8(coord):
                if n in grid and grid[n] != '#':
                    q.append((n, [*path,n]))
    counts = Counter()
    for index_a,(x1,y1) in enumerate(real_path):
        for index_b,(x2,y2) in enumerate(real_path):
            if index_b > index_a:
                point_dist = abs(y2-y1) + abs(x2-x1)
                if point_dist <= 2:
                    time_saved = index_b - index_a - point_dist
                    counts[time_saved] += 1
    return sum(count for time,count in counts.items() if time >= 100)

def part_b(grid):
    start = next(c for c in grid if grid[c] == 'S')
    end = next(c for c in grid if grid[c] == 'E')
    q = deque([(start, [start])])
    visited = set()
    real_path = None
    while q:
        coord, path = q.popleft()
        if coord == end:
            real_path = path
            break
        elif coord not in visited:
            visited.add(coord)
            for n in neighbrs_str8(coord):
                if n in grid and grid[n] != '#':
                    q.append((n, [*path,n]))
    counts = Counter()
    for index_a,(x1,y1) in enumerate(real_path):
        for index_b,(x2,y2) in enumerate(real_path):
            if index_b > index_a:
                point_dist = abs(y2-y1) + abs(x2-x1)
                if point_dist <= 20:
                    time_saved = index_b - index_a - point_dist
                    counts[time_saved] += 1
    return sum(count for time,count in counts.items() if time >= 100)

puzzle = Puzzle(2024, 20)
data = parse(puzzle.input_data)
print("part A", part_a(data))
print("part B", part_b(data))
