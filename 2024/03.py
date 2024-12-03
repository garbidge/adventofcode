from aocd.models import Puzzle
from utils import flatten, preg

def parse(input):
    return flatten(preg(input, "(do\(\))|(don't\(\))|mul\((\d+),(\d+)\)"))

def part_a(data):
    return sum(int(a) * int(b) for _,_,a,b in data if a and b)

def part_b(data):
    enabled, total = True, 0
    for do,dont,a,b in data:
        if do: enabled = True
        elif dont: enabled = False
        elif enabled: total += int(a) * int(b)
    return total

puzzle = Puzzle(2024, 3)
data = parse(puzzle.input_data)
print("part A", part_a(data))
print("part B", part_b(data))
