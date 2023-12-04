from math import prod

from aocd.models import Puzzle
from utils import flatten, neighbrs, pgriddict, tuple_add


def parse(input):
    return pgriddict(input, str)


def part_a(data):
    symbs = [coord for coord in data if issymbol(data[coord])]
    neighs = set(flatten([neighbrs(coord) for coord in symbs]))
    zones = set(getzone(data, coord) for coord in neighs if data[coord].isdigit())
    return sum(getnum(data, zone) for zone in zones)


def issymbol(char: str):
    return char != "." and not char.isdigit()


def getzone(data, coord):
    out = (coord,)
    temp = tuple_add(coord, (1, 0))
    while temp in data and data[temp].isdigit():
        out = (*out, temp)
        temp = tuple_add(temp, (1, 0))
    temp = tuple_add(coord, (-1, 0))
    while temp in data and data[temp].isdigit():
        out = (temp, *out)
        temp = tuple_add(temp, (-1, 0))
    return out


def getnum(data, zone):
    out = ""
    for coord in zone:
        out += data[coord]
    return int(out)


def part_b(data):
    tot = 0
    symbs = [coord for coord in data if data[coord] == "*"]
    for s in symbs:
        neighs = neighbrs(s)
        zones = set([getzone(data, coord) for coord in neighs if data[coord].isdigit()])
        if len(zones) == 2:
            tot += prod(getnum(data, zone) for zone in zones)
    return tot


puzzle = Puzzle(2023, 3)

data = parse(puzzle.input_data)
print("part A", part_a(data))
print("part B", part_b(data))
