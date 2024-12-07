from aocd.models import Puzzle
from utils import digits, plint

def parse(input):
    return [(n[0], tuple(n[1:])) for n in plint(input)]

def part_a(data):
    return sum(value for value,numbers in data if any(rev_match(value, numbers, False)))

def part_b(data):
    return sum(value for value,numbers in data if any(rev_match(value, numbers, True)))

def rev_match(current, remaining, with_concat):
    if current < 0: yield False
    elif len(remaining) == 0: yield current == 0
    else:
        if with_concat and current % (divisor := pow(10, digits(remaining[-1]))) == remaining[-1]:
            yield from rev_match(current // divisor, remaining[:-1], with_concat)
        if current % remaining[-1] == 0:
            yield from rev_match(current // remaining[-1], remaining[:-1], with_concat)
        yield from rev_match(current - remaining[-1], remaining[:-1], with_concat)

puzzle = Puzzle(2024, 7)
data = parse(puzzle.input_data)
print("part A", part_a(data))
print("part B", part_b(data))
