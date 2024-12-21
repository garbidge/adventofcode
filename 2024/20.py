from aocd.models import Puzzle
from utils import neighbrs_str8, pgriddict

def find_path(grid):
    coord = next(c for c in grid if grid[c] == 'S')
    distances, path = {coord: 0}, [coord]
    while grid[coord] != 'E':
        coord = next(c for c in neighbrs_str8(coord) if c not in distances and grid[c] != '#')
        distances[coord] = len(path)
        path.append(coord)
    return distances, path

def cheat_paths(distances, path):
    total_a, total_b = 0, 0
    window = tuple(coords_within_dist(*path[0], 20))
    for ((x1,y1),(x2,y2)) in zip([path[0], *path], path):
        dx,dy = x2-x1, y2-y1
        window = tuple(((x+dx,y+dy), dist) for (x,y),dist in window)
        for c,dist in window:
            if c in distances:
                time_saved = distances[c] - distances[(x2,y2)] - dist
                if time_saved >= 100:
                    if dist <= 2: total_a += 1
                    total_b += 1
    return total_a, total_b

def coords_within_dist(x, y, distance):
    for dx in range(-distance, distance + 1):
        for dy in range(-distance, distance + 1):
            if not (dx == 0 and dy == 0) and (dist := abs(dx) + abs(dy)) <= distance:
                yield ((x + dx, y + dy), dist)

puzzle = Puzzle(2024, 20)
grid = pgriddict(puzzle.input_data, str)
distances, path = find_path(grid)
a, b = cheat_paths(distances, path)
print(f'part A: {a}')
print(f'part B: {b}')