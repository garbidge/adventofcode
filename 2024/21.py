from functools import cache
from aocd.models import Puzzle
from utils import coord_yield_dir, sign

KEYBOARD = {
    (0,0): '7', (1,0): '8', (2,0): '9',
    (0,1): '4', (1,1): '5', (2,1): '6',
    (0,2): '1', (1,2): '2', (2,2): '3',
                (1,3): '0', (2,3): 'A',
}
REVERSE_KEYBOARD = {v: k for k, v in KEYBOARD.items()}
KEYPAD = {
                (1,0): '^', (2,0): 'A',
    (0,1): '<', (1,1): 'v', (2,1): '>'
}
REVERSE_KEYPAD = {v: k for k, v in KEYPAD.items()}
REVERSE_DIRECTIONS = {(0, -1): '^', (0, 1): 'v', (-1, 0): '<', (1, 0): '>'}

def part_a(data):
    return sum(code_score(c, 2) for c in data)

def part_b(data):
    return sum(code_score(c, 25) for c in data)

def code_score(code, max_depth):
    min_path = sum(min_length(start,end,0,max_depth) for start,end in zip('A' + code, code))
    return min_path * int(code[:-1])

@cache
def min_length(start, end, depth, max_depth):
    lookup,reverse = (KEYBOARD, REVERSE_KEYBOARD) if depth == 0 else (KEYPAD, REVERSE_KEYPAD)
    paths = get_paths(start, end, lookup, reverse)
    if depth == max_depth: return min(len(path) for path in paths)
    else:
        return min(sum(min_length(s,e,depth+1,max_depth) for s,e in zip('A' + path, path)) for path in paths)

def get_paths(start, end, lookup, reverse):
    if start == end: 
        yield 'A'
        return
    (x1,y1),(x2,y2) = reverse[start], reverse[end]
    dx,dy = sign(x2-x1), sign(y2-y1)
    horizontal = '' if dx == 0 else REVERSE_DIRECTIONS[(dx,0)] * abs(x2-x1)
    vertical = '' if dy == 0 else REVERSE_DIRECTIONS[(0,dy)] * abs(y2-y1)
    if dy != 0 and not passes_empty_horizontal(x1,y1,x2,dx,lookup): yield horizontal + vertical + 'A'
    if dx != 0 and not passes_empty_vertical(x1,y1,y2,dy,lookup): yield vertical + horizontal + 'A'

def passes_empty_horizontal(x1,y1,x2,dx,lookup):
    return any(p not in lookup for p in coord_yield_dir((x1,y1), (dx,0), lambda coord: coord != (x2+dx,y1)))

def passes_empty_vertical(x1,y1,y2,dy,lookup):
    return any(p not in lookup for p in coord_yield_dir((x1,y1), (0,dy), lambda coord: coord != (x1,y2+dy)))

puzzle = Puzzle(2024, 21)
data = puzzle.input_data.splitlines()
print("part A", part_a(data))
print("part B", part_b(data))
