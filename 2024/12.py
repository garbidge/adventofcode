from collections import deque
from aocd.models import Puzzle
from utils import coord_dirs_str8, coord_yield_dir, neighbrs_str8, pgriddict, tuple_add

def parse(input):
    grid = pgriddict(input, str)
    regions = list()
    for coord in grid:
        if not any(coord in region for region,_,_ in regions):
            regions.append(find_region(grid, coord))
    return regions

def part_a(regions):
    return sum(len(region) * perimeter for region,perimeter,_ in regions)

def part_b(regions):
    return sum(len(region) * sides for region,_,sides in regions)

def find_region(grid, coord):
    points, perimeter, sides = set((coord,)), 0, 0
    q = deque([coord])
    directions = coord_dirs_str8(2)
    side_map = {d: set() for d in directions}
    while q:
        point = q.popleft()
        for direction in directions:
            n = tuple_add(point, direction)
            if n not in grid or grid[n] != grid[coord]:
                perimeter += 1
                sides += add_edges(grid, side_map[direction], point, *direction)
            elif n not in points:
                points.add(n)
                q.append(n)
    return (points, perimeter, sides)

def add_edges(grid, edge_set, coord, dx, dy):
    if coord not in edge_set:
        edge_set.add(coord)
        for parallel in ((dy,dx), (-dy,-dx)):
            for same_side in coord_yield_dir(coord, parallel, lambda point: is_matching(grid, coord, point, (dx,dy))):
                edge_set.add(same_side)
        return 1
    return 0

def is_matching(grid, original_coord, point, direction):
    adjacent = tuple_add(point, direction)
    return point in grid and grid[point] == grid[original_coord] and (adjacent not in grid or grid[adjacent] != grid[original_coord])

puzzle = Puzzle(2024, 12)
data = parse(puzzle.input_data)
print("part A", part_a(data))
print("part B", part_b(data))
