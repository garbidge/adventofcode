import itertools
from aocd.models import Puzzle

def parse(input):
    return [tuple(int(n) for n in line.split(",")) for line in input.splitlines()]

def solve(data):
    a, b = 0, 0
    for p1, p2 in itertools.combinations(data, 2):
        area = rect_area(*p1, *p2)
        a = max(a, area)
        if area > b and viable_rect(*p1, *p2, data):
            b = area
    return a, b

def rect_area(x1, y1, x2, y2):
    return (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)

def viable_rect(x1, y1, x2, y2, locations):
    min_x, max_x = sorted((x1, x2))
    min_y, max_y = sorted((y1, y2))
    for i, (cx1, cy1) in enumerate(locations):
        cx2, cy2 = locations[(i + 1) % len(locations)]
        min_cx, max_cx = sorted((cx1, cx2))
        min_cy, max_cy = sorted((cy1, cy2))

        x_intersects = min_x < max_cx and max_x > min_cx
        y_intersects = min_y < max_cy and max_y > min_cy
        if x_intersects and y_intersects:
            return False
    return True

puzzle = Puzzle(2025, 9)
data = parse(puzzle.input_data)
a,b = solve(data)
print("part A", a)
print("part B", b)