from functools import cache
from aocd.models import Puzzle
from utils import sign

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

def code_score(code, max_depth):
    length = sum(min_length(start,end,0,max_depth) for start,end in zip('A' + code, code))
    return length * int(code[:-1])

@cache
def min_length(start, end, depth, max_depth):
    lookup,reverse = (KEYBOARD, REVERSE_KEYBOARD) if depth == 0 else (KEYPAD, REVERSE_KEYPAD)
    paths = get_paths(start, end, lookup, reverse)
    if depth == max_depth: return min(len(path) for path in paths)
    else:
        return min(sum(min_length(s,e,depth+1,max_depth) for s,e in zip('A' + path, path)) for path in paths)

def get_paths(start, end, lookup, reverse):
    if start == end: yield 'A'
    else:
        (x1,y1),(x2,y2) = reverse[start], reverse[end]
        dx,dy = sign(x2-x1), sign(y2-y1)
        horizontal = '' if not dx else REVERSE_DIRECTIONS[(dx,0)] * abs(x2-x1)
        vertical = '' if not dy else REVERSE_DIRECTIONS[(0,dy)] * abs(y2-y1)
        if dy and (x2,y1) in lookup: yield horizontal + vertical + 'A'
        if dx and (x1,y2) in lookup: yield vertical + horizontal + 'A'

puzzle = Puzzle(2024, 21)
data = puzzle.input_data.splitlines()
print("part A", sum(code_score(c, 2) for c in data))
print("part B", sum(code_score(c, 25) for c in data))
