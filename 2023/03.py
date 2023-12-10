from aocd.models import Puzzle
from math import prod
from utils import flatten, neighbrs, pgriddict

def parse(input):
    return pgriddict(input, str)

def part_a(data):
    symbols = [xy for xy in data if data[xy] != "." and not data[xy].isdigit()]
    return sum(get_num(data, *zone) for zone in number_neighbours(symbols))

def part_b(data):
    gears = [xy for xy in data if data[xy] == "*"]
    zone_groups = filter(
        lambda group: len(group) == 2,
        [number_neighbours([xy]) for xy in gears]
    )
    return sum(prod(get_num(data, *zone) for zone in group) for group in zone_groups)

def number_neighbours(coordinates):
    neighbours = set(flatten([neighbrs(xy) for xy in coordinates]))
    return set(get_zone(data, *xy) for xy in neighbours if data[xy].isdigit())

def get_zone(data, x, y):
    start, end = (x, x)
    while (start - 1, y) in data and data[(start - 1, y)].isdigit():
        start -= 1
    while (end + 1, y) in data and data[(end + 1, y)].isdigit():
        end += 1
    return (start, end, y)

def get_num(data, lower_x, upper_x, y):
    return int("".join([data[(x, y)] for x in range(lower_x, upper_x + 1)]))

puzzle = Puzzle(2023, 3)
data = parse(puzzle.input_data)
print("part A", part_a(data))
print("part B", part_b(data))
