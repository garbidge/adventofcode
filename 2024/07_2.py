from aocd.models import Puzzle
from utils import digits, plint

def parse(input):
    return [(n[0], tuple(n[1:])) for n in plint(input)]

def part_a(data):
    return sum(value for value,numbers in data if has_match(value, numbers, False))

def part_b(data):
    return sum(value for value,numbers in data if has_match(value, numbers, True))

def has_match(target, remaining, with_concat):
    return any(rev_match(target, target, remaining, with_concat))

def rev_match(target, current, remaining, with_concat):
    if current < 0: yield False
    elif len(remaining) == 0: yield current == 0
    else:
        if with_concat:
            yield from rev_concat(target, current, remaining[-1], remaining)
        if current % remaining[-1] == 0:
            yield from rev_match(target, current // remaining[-1], remaining[:-1], with_concat)
        yield from rev_match(target, current - remaining[-1], remaining[:-1], with_concat)

def rev_concat(target, current, value, remaining):
    if current % 10 == value % 10 and digits(current) > (length := digits(value)):
        next_value = current // pow(10, length)
        yield from rev_match(target, next_value, remaining[:-1], True)

puzzle = Puzzle(2024, 7)
data = parse(puzzle.input_data)
print("part A", part_a(data))
print("part B", part_b(data))
