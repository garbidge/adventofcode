from aocd.models import Puzzle
from heapq import heappop, heappush
from utils import pgriddict, tuple_add

DIRECTIONS = [(1, 0), (0,-1), (-1,0), (0,1)]

def parse(input):
    return pgriddict(input, str)

def solve(grid):
    location = next(c for c in grid if grid[c] == 'S')
    h = []
    visited_scores, best_tiles, best_score = dict(), set(), None
    heappush(h, (0, location, set([location]), 0))
    while h:
        score, location, path, di = heappop(h)
        if best_score and score > best_score:
            break
        if grid[location] == 'E':
            best_tiles.update(path)
            best_score = score
            continue
        if (location,di) in visited_scores and score > visited_scores[(location,di)]:
            continue
        visited_scores[(location,di)] = score
        for score_inc,direction_index in ((1, di), (1001, (di+1) % len(DIRECTIONS)), (1001, (di-1) % len(DIRECTIONS))):
            direction = DIRECTIONS[direction_index]
            if grid[(nxt := tuple_add(location, direction))] != '#':
                heappush(h, (score + score_inc, nxt, {*path, nxt}, direction_index))
    return best_score, len(best_tiles)

puzzle = Puzzle(2024, 16)
data = parse(puzzle.input_data)
a,b = solve(data)
print("part A", a)
print("part B", b)