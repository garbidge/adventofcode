from collections import defaultdict, deque
from copy import deepcopy
from itertools import product
from aocd.models import Puzzle
from utils import lmap

def parse(input):
    bricks = []
    for line in input.splitlines():
        left,right = [lmap(int, side.split(',')) for side in line.split('~')]
        bricks.append((left, right))
    return fall(bricks)

def fall(bricks):
    grid = fill(bricks)
    unblocked = [(i, *brick) for i,brick in enumerate(bricks) if not isblocked(grid, brick)]
    while len(unblocked):
        for i,(sx,sy,sz),(ex,ey,ez) in unblocked:
            bricks[i] = ((sx,sy,sz-1),(ex,ey,ez-1))
        grid = fill(bricks)
        unblocked = [(i, *brick) for i,brick in enumerate(bricks) if not isblocked(grid, brick)]
    return bricks

def fill(bricks):
    grid = defaultdict(bool)
    for (sx,sy,sz),(ex,ey,ez) in bricks:
        for x,y,z in product(range(sx, ex+1), range(sy, ey+1), range(sz, ez+1)):
            grid[(x,y,z)] = True
    return grid

def isblocked(grid, brick):
    (sx,sy,sz), (ex,ey,ez) = brick
    return sz == 1 or any(grid[(x,y,sz-1)] for x,y in product(range(sx, ex+1), range(sy, ey+1)))

def solve(bricks):
    supportmap = defaultdict(list)
    reversemap = defaultdict(list)
    for a,b in product(range(len(bricks)), range(len(bricks))):
        if a == b: continue
        (sx_a, sy_a, sz_a),(ex_a, ey_a, ez_a) = bricks[a]
        (sx_b, sy_b, sz_b),(ex_b, ey_b, ez_b) = bricks[b]
        if sz_a != ez_b + 1: continue
        if sx_a <= ex_b and ex_a >= sx_b and sy_a <= ey_b and ey_a >= sy_b:
            supportmap[b].append(a)
            reversemap[a].append(b)
    singles = set(reversemap[x][0] for x in reversemap if len(reversemap[x]) == 1)
    a = len(bricks) - len(singles)
    b = sum(fallers(supportmap, reversemap, val) for val in singles)
    return a,b

def fallers(supportmap, reversemap, val):
    clone = deepcopy(reversemap)
    q = deque((val,))
    fallen = set()
    while q:
        current = q.popleft()
        for supporting in supportmap[current]:
            clone[supporting] = [v for v in clone[supporting] if v != current]
            if supporting not in fallen and len(clone[supporting]) == 0:
                fallen.add(supporting)
                q.append(supporting)
    return len(fallen)

puzzle = Puzzle(2023, 22)
data = parse(puzzle.input_data)
a,b = solve(data)
print("part A", a)
print("part B", b)
