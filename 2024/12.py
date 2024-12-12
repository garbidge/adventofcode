from collections import deque
from aocd.models import Puzzle
from utils import coord_dirs_str8, coord_yield_dir, neighbrs_str8, pgriddict, tuple_add

def parse(input):
    grid = pgriddict(input, str)
    return find_regions(grid)

def part_a(regions):
    return sum(len(region) * perimeter for region,perimeter in regions)

def part_b(regions):
    total = 0
    for region,_ in regions:
        sides = 0
        for (dx,dy) in coord_dirs_str8(2):
            visited = set()
            for coord in region:
                n = tuple_add(coord, (dx,dy))
                if n not in region and n not in visited:
                    visited.add(n)
                    sides += 1
                    for parallel in ((dy,dx), (-dy,-dx)):
                        for same_side in coord_yield_dir(coord, parallel, lambda c: c in region and tuple_add(c, (dx,dy)) not in region):
                            visited.add(tuple_add(same_side, (dx,dy)))
        total += len(region) * sides
    return total

def find_regions(data):
    regions = list()
    for coord in data:
        if not any(coord in region for region,_ in regions):
            regions.append(find_region(data, coord))
    return regions

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
