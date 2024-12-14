from aocd.models import Puzzle
from utils import plint

def parse(input):
    return [parse_group(g) for g in input.split('\n\n')]

def parse_group(group):
    button_a, button_b, prize = plint(group)
    return (button_a, button_b, prize)

def part_a(groups):
    tokens = (solve(*g) for g in groups)
    return sum(t for t in tokens if t)

def part_b(groups):
    tokens = (solve(a, b, (px + 10000000000000, py + 10000000000000)) for a,b,(px,py) in groups)
    return sum(t for t in tokens if t)

def solve(button_a, button_b, prize):
    (ax,ay) = button_a
    (bx,by) = button_b
    (px,py) = prize
    
    # linear equations
    # ax * A + bx * B = px
    # ay * A + by * B = py
    B, mod_b = divmod((py * ax - ay * px), (ax * by - ay * bx))
    A, mod_a = divmod((px - bx * B), ax)
    if mod_a == 0 and mod_b == 0:
        return int(A * 3 + B)

puzzle = Puzzle(2024, 13)
data = parse(puzzle.input_data)
print("part A", part_a(data))
print("part B", part_b(data))
