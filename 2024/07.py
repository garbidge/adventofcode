import operator
from aocd.models import Puzzle
from utils import plint

def parse(input):
    return [(n[0], tuple(n[1:])) for n in plint(input)]

def part_a(data):
    return sum(value for value,numbers in data if matches(value, numbers, [operator.add, operator.mul]))

def part_b(data):
    return sum(value for value,numbers in data if matches(value, numbers, [operator.add, operator.mul, lambda a,b: int(str(a) + str(b))]))

def matches(value, numbers, operations):
    return any(value == p for p in possibles(0, numbers, operations))

def possibles(current, remaining, operations):
    if len(remaining) == 0:
        yield current
    else:
        for new_value in (op(current,remaining[0]) for op in operations):
            yield from possibles(new_value, remaining[1:], operations)

puzzle = Puzzle(2024, 7)
data = parse(puzzle.input_data)
print("part A", part_a(data))
print("part B", part_b(data))
