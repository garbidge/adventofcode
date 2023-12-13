from aocd.models import Puzzle
from utils import transpose_str

def parse(input):
    return [group.splitlines() for group in input.split('\n\n')]

def part_a(data):
    return sum(reflect(pattern, 0) for pattern in data)

def part_b(data):
    return sum(reflect(pattern, 1) for pattern in data)

def reflect(pattern, target):
    if (horizontal := reflect_index(pattern, target)):
        return 100 * horizontal
    return reflect_index(transpose_str(pattern), target)

def reflect_index(pattern, target):
    for i in range(len(pattern) - 1):
        distance = sum(strdist(*pair) for pair in get_pairs(pattern, i))
        if distance == target:
            return i + 1

def get_pairs(pattern, i):
    current, opposite = i, i+1
    while current >= 0 and opposite < len(pattern):
        yield (pattern[current], pattern[opposite])
        current -= 1
        opposite += 1

def strdist(a, b):
    return sum(a[i] != b[i] for i in range(len(a)))

puzzle = Puzzle(2023, 13)
data = parse(puzzle.input_data)
print("part A", part_a(data))
print("part B", part_b(data))
