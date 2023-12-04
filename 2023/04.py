from collections import defaultdict

from aocd.models import Puzzle


def parse(input):
    lines = input.splitlines()
    numparts = [line.split(": ")[1] for line in lines]
    for part in numparts:
        nums = [[int(n) for n in p.split()] for p in part.split(" | ")]
        yield nums


def part_a(data):
    total = 0
    for winners, mine in data:
        lookup = set(winners)
        count = len([n for n in mine if n in lookup])
        value = 0
        while count > 0:
            value = 1 if value == 0 else value * 2
            count -= 1
        total += value
    return total


def part_b(data):
    results = defaultdict(int)
    counts = defaultdict(int)
    for i, (winners, mine) in enumerate(data):
        lookup = set(winners)
        count = len([n for n in mine if n in lookup])
        results[i] = count
        counts[i] = 1
    for i in range(len(data) - 1):
        count = results[i]
        if count > 0:
            cards = counts[i]
            for x in range(count):
                index = i + 1 + x
                if index in counts:
                    counts[index] += cards
    return sum(counts.values())


puzzle = Puzzle(2023, 4)
data = [*parse(puzzle.input_data)]
print("part A", part_a(data))
print("part B", part_b(data))
