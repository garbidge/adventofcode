from aocd.models import Puzzle

def parse(input):
    ranges, ids = input.split("\n\n")
    ranges = [tuple(int(n) for n in pair.split("-")) for pair in ranges.splitlines()]
    ids = [int(n) for n in ids.splitlines()]
    return ranges, ids

def part_a(ranges, ids):
    return sum(1 for i in ids if any(r[0] <= i <= r[1] for r in ranges))

def part_b(ranges, _):
    contiguous = []
    for rng in ranges:
        while (other := next((r for r in contiguous if overlaps(rng, r)), None)):
            rng = merge(rng, other)
            contiguous.remove(other)
        contiguous.append(rng)
    return sum(r[1] - r[0] + 1 for r in contiguous)

def overlaps(range1, range2):
    return not (range1[1] < range2[0] or range2[1] < range1[0])

def merge(range1, range2):
    return (min(range1[0], range2[0]), max(range1[1], range2[1]))

puzzle = Puzzle(2025, 5)
data = parse(puzzle.input_data)
print("part A", part_a(*data))
print("part B", part_b(*data))
