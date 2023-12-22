from collections import defaultdict
from copy import deepcopy
from aocd.models import Puzzle
from utils import lmap

def parse(input):
    bricks = []
    for line in input.splitlines():
        left,right = line.split('~')
        left = lmap(int, left.split(','))
        right = lmap(int, right.split(','))
        bricks.append((left, right))
    return fall(bricks)

def fall(bricks):
    count = 99
    while count > 0:
        count = 0
        grid = fill(bricks)
        for i in range(len(bricks)):
            (sx,sy,sz),(ex,ey,ez) = bricks[i]
            if sz == 1: continue
            
            if not isblocked(grid, sx,sy,sz, ex,ey,ez):
                bricks[i] = ((sx,sy,sz-1),(ex,ey,ez-1))
                count += 1
    return bricks

def isblocked(grid, sx,sy,sz, ex,ey,ez):
    for x in range(sx, ex+1):
        for y in range(sy, ey+1):
            if grid[(x,y,sz-1)]: return True
    return False

def fill(bricks):
    grid = defaultdict(bool)
    for (sx,sy,sz),(ex,ey,ez) in bricks:
        for x in range(sx, ex+1):
            for y in range(sy, ey+1):
                for z in range(sz, ez+1):
                    grid[(x,y,z)] = True
    return grid

def solve(bricks):
    supportmap = defaultdict(list)
    reversemap = defaultdict(list)
    for i in range(len(bricks)):
        (sx_a, sy_a, sz_a),(ex_a, ey_a, ez_a) = bricks[i]
        for j in range(len(bricks)):
            if i != j:
                (sx_b, sy_b, sz_b),(ex_b, ey_b, ez_b) = bricks[j]
                if sz_a != ez_b + 1: continue
                if sx_a <= ex_b and ex_a >= sx_b and sy_a <= ey_b and ey_a >= sy_b:
                    supportmap[j].append(i)
                    reversemap[i].append(j)
    singles = set(reversemap[x][0] for x in reversemap if len(reversemap[x]) == 1)
    a = len(bricks) - len(singles)
    b = chain(reversemap, singles)
    return a,b

def chain(reversemap, singles):
    total = 0
    for x in singles:
        total += fallers(reversemap, x)
    return total

def fallers(reversemap, val):
    clone = deepcopy(reversemap)
    for x in clone:
        clone[x] = [v for v in clone[x] if v != val]
    fallen = set()
    changed = 99
    while changed > 0:
        changed = 0
        for x in clone:
            if x not in fallen and len(clone[x]) == 0:
                fallen.add(x)
                changed += 1
        for x in clone:
            clone[x] = [v for v in clone[x] if v not in fallen]
    return len(fallen)

puzzle = Puzzle(2023, 22)
data = parse(puzzle.input_data)
a,b = solve(data)
print("part A", a)
print("part B", b)
