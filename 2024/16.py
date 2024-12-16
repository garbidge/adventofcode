from aocd.models import Puzzle
from heapq import heappop, heappush
from utils import pgriddict, tuple_add

dirmap = [(1, 0), (0,-1), (-1,0), (0,1)]

def parse(input):
    return pgriddict(input, str)

def part_a(grid):
    location = next(c for c in grid if grid[c] == 'S')
    h = []
    visited = set()
    heappush(h, (0, location, 0))
    while h:
        score, location, di = heappop(h)
        if grid[location] == 'E':
            return score
        if (location,di) in visited:
            continue
        visited.add((location,di))
        direction = dirmap[di]
        nxt = tuple_add(location, direction)
        if grid[nxt] != '#':
            heappush(h, (score + 1, nxt, di))
        heappush(h, (score + 1000, location, (di + 1) % len(dirmap)))
        heappush(h, (score + 1000, location, (di - 1) % len(dirmap)))

def part_b(grid):
    location = next(c for c in grid if grid[c] == 'S')
    h = []
    visited_scores = dict()
    best_tiles = set()
    best_score = -1
    heappush(h, (0, location, set([location]), 0))
    while h:
        score, location, path, di = heappop(h)
        if best_score != -1 and score > best_score:
            continue
        if grid[location] == 'E':
            best_tiles.update(path)
            best_score = score
            continue
        if (location,di) in visited_scores:
            if score > visited_scores[(location,di)]:
                continue
        if (location,di) not in visited_scores or visited_scores[(location,di)] > score:
            visited_scores[(location,di)] = score
        direction = dirmap[di]
        nxt = tuple_add(location, direction)
        if grid[nxt] != '#':
            heappush(h, (score + 1, nxt, {*path, nxt}, di))
        heappush(h, (score + 1000, location, path, (di + 1) % len(dirmap)))
        heappush(h, (score + 1000, location, path, (di - 1) % len(dirmap)))
    return len(best_tiles)

puzzle = Puzzle(2024, 16)
data = parse(puzzle.input_data)
print("part A", part_a(data))
print("part B", part_b(data))