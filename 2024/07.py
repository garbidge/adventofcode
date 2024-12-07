import operator
from aocd.models import Puzzle
from utils import plint

def parse(input):
    return [(n[0], tuple(n[1:])) for n in plint(input)]

def part_a(data):
    operations = (operator.add, operator.mul)
    return sum(value for value,numbers in data if is_match(value, 0, numbers, operations))

def part_b(data):
    operations = (operator.add, operator.mul, lambda a,b: int(str(a) + str(b)))
    return sum(value for value,numbers in data if is_match(value, 0, numbers, operations))

def is_match(target, current, remaining, operations):
    if current > target:
        return False
    if len(remaining) == 0:
        return target == current
    next_values = (op(current,remaining[0]) for op in operations)
    return any(is_match(target, new_value, remaining[1:], operations) for new_value in next_values)

puzzle = Puzzle(2024, 7)
data = parse(puzzle.input_data)
print("part A", part_a(data))
print("part B", part_b(data))
