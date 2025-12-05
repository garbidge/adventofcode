from aocd.models import Puzzle

def parse(input):
    ranges, ids = input.split("\n\n")
    ranges = [tuple(int(n) for n in pair.split("-")) for pair in ranges.splitlines()]
    ids = [int(n) for n in ids.splitlines()]
    return ranges, ids

def part_a(ranges, ids):
    return sum(any(r[0] <= i <= r[1] for r in ranges) for i in ids)

def part_b(ranges, _):
    contiguous = []
    for rng in ranges:
        while (other := next((r for r in contiguous if overlaps(rng, r)), None)):
            rng = merge(rng, other)
            contiguous.remove(other)
        contiguous.append(rng)
    return sum(r[1] - r[0] + 1 for r in contiguous)

def overlaps(a, b):
    return not (a[1] < b[0] or b[1] < a[0])

def merge(a, b):
    return (min(a[0], b[0]), max(a[1], b[1]))

puzzle = Puzzle(2025, 5)
data = parse(puzzle.input_data)
print("part A", part_a(*data))
print("part B", part_b(*data))
