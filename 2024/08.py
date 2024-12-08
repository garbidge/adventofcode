from itertools import combinations
from aocd.models import Puzzle
from utils import pgriddict

def parse(input):
    return pgriddict(input, str)

def part_a(data):
    possibles = set(v for v in data.values() if v != '.')
    antinodes = set()
    for antenna_type in possibles:
        locations = [coord for coord in data if data[coord] == antenna_type]
        for (x1, y1), (x2, y2) in combinations(locations, 2):
            dx, dy = x2 - x1, y2 - y1
            c1 = (x2 + dx, y2 + dy)
            c2 = (x1 - dx, y1 - dy)
            for n in (c1, c2):
                if n in data: antinodes.add(n)
    return len(antinodes)

def part_b(data):
    possibles = set(v for v in data.values() if v != '.')
    antinodes = set()
    for antenna_type in possibles:
        locations = [coord for coord in data if data[coord] == antenna_type]
        for (x1, y1), (x2, y2) in combinations(locations, 2):
            antinodes.add((x1, y1))
            antinodes.add((x2, y2))
            dx, dy = x2 - x1, y2 - y1
            curr_x, curr_y = x1, y1
            while (n := (curr_x - dx, curr_y - dy)) in data:
                antinodes.add(n)
                curr_x, curr_y = n
            curr_x, curr_y = x2, y2
            while (n := (curr_x + dx, curr_y + dy)) in data:
                antinodes.add(n)
                curr_x, curr_y = n
    return len(antinodes)

puzzle = Puzzle(2024, 8)
data = parse(puzzle.input_data)
print("part A", part_a(data))
print("part B", part_b(data))
