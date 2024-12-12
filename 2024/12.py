from collections import deque
from aocd.models import Puzzle
from utils import coord_yield_dir, neighbrs_str8, pgriddict, tuple_add

def parse(input):
    return pgriddict(input, str)

def part_a(data):
    regions = list()
    for coord in data:
        if not any(coord in region for region,_ in regions):
            regions.append(find_region(data, coord))
    return sum(len(region) * perimeter for region,perimeter in regions)

def part_b(data):
    regions = list()
    for coord in data:
        if not any(coord in region for region,_ in regions):
            regions.append(find_region(data, coord))
    total = 0
    dirs = [
        ((0,-1), (1,0), (-1,0)),
        ((0,1), (1,0), (-1,0)),
        ((1,0), (0,1), (0,-1)),
        ((-1,0), (0,1), (0,-1))
    ]
    for region,_ in regions:
        sides = 0
        for dir, travel_a, travel_b in dirs:
            visited = set()
            for coord in region:
                n = tuple_add(coord, dir)
                if n not in region and n not in visited:
                    visited.add(n)
                    sides += 1
                    for same_side in coord_yield_dir(coord, travel_a, lambda c: c in region and tuple_add(c, dir) not in region):
                        visited.add(tuple_add(same_side, dir))
                    for same_side in coord_yield_dir(coord, travel_b, lambda c: c in region and tuple_add(c, dir) not in region):
                        visited.add(tuple_add(same_side, dir))
        total += len(region) * sides
    return total

def find_region(data, coord):
    points = set((coord,))
    perimeter = 0
    q = deque([coord])
    while q:
        point = q.popleft()
        for n in neighbrs_str8(point):
            if n not in data or data[n] != data[coord]:
                perimeter += 1
            elif n not in points:
                points.add(n)
                q.append(n)
    return (points, perimeter)

puzzle = Puzzle(2024, 12)
data = parse(puzzle.input_data)
print("part A", part_a(data))
print("part B", part_b(data))
