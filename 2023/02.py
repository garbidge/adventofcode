from collections import defaultdict
from math import prod

from aocd.models import Puzzle
from utils import preg


def parse(input):
    return [
        (i + 1, parse_game(pairs)) for i, pairs in enumerate(preg(input, "(\d+) (\w+)"))
    ]


def parse_game(pairs):
    largest = defaultdict(int)
    for num, colour in pairs:
        largest[colour] = max(largest[colour], int(num))
    return largest


def part_a(data):
    return sum(game for game, largest in data if valid(largest))


def valid(largest):
    lims = {"red": 12, "green": 13, "blue": 14}
    return all(largest[colour] <= lims[colour] for colour in largest.keys())


def part_b(data):
    return sum(prod(largest.values()) for game, largest in data)


puzzle = Puzzle(2023, 2)
data = parse(puzzle.input_data)
print("part A", part_a(data))
print("part B", part_b(data))
