from collections import defaultdict, deque

from aocd.models import Puzzle
from utils import neighbrs_str8, pgriddict


def parse(input):
    return pgriddict(input, str)


def part_a(data):
    start = next(coord for coord in data if data[coord] == "S")
    seen = set((start,))
    q = deque()
    q.append(((start,), 0))
    maxdist = 0
    while q:
        path, dist = q.popleft()
        coord = path[-1]

        if dist > maxdist:
            maxdist = dist

        for n in neighbours(data, coord):
            if n in data and data[n] != "." and n not in seen:
                seen.add(n)
                q.append(((*path, n), dist + 1))

    return maxdist


def neighbours(data, coord):
    x, y = coord
    if data[coord] == "S":
        results = []
        c = data[(x, y - 1)]
        if c == "|" or c == "7" or c == "F":
            results.append((x, y - 1))
        c = data[(x, y + 1)]
        if c == "|" or c == "L" or c == "J":
            results.append((x, y + 1))
        c = data[(x - 1, y)]
        if c == "-" or c == "L" or c == "F":
            results.append((x - 1, y))
        c = data[(x + 1, y)]
        if c == "-" or c == "J" or c == "7":
            results.append((x + 1, y))
        return results
    if data[coord] == "|":
        return ((x, y - 1), (x, y + 1))
    if data[coord] == "-":
        return ((x - 1, y), (x + 1, y))
    if data[coord] == "L":
        return ((x, y - 1), (x + 1, y))
    if data[coord] == "J":
        return ((x, y - 1), (x - 1, y))
    if data[coord] == "7":
        return ((x, y + 1), (x - 1, y))
    if data[coord] == "F":
        return ((x, y + 1), (x + 1, y))
    return ()


def bfsloop(data):
    start = next(coord for coord in data if data[coord] == "S")
    q = deque()
    q.append(((start,), 0))
    while q:
        path, dist = q.popleft()
        coord = path[-1]

        for n in neighbours(data, coord):
            if dist > 1 and data[n] == "S":
                data[start] = "7"  # aaaaaaaaaaa
                return path
            if n in data and data[n] != "." and n not in path:
                q.append(((*path, n), dist + 1))


def part_b(data):
    path = bfsloop(data)
    loopset = set(path)

    maxx, maxy = max(x for (x, y) in data), max(y for (x, y) in data)

    bigger = defaultdict(str)
    for x in range(maxx + 1):
        for y in range(maxy + 1):
            coord = (x, y)
            setbiggun(bigger, coord, data[coord] if coord in loopset else ".")

    maxx, maxy = max(x for (x, y) in bigger), max(y for (x, y) in bigger)
    q = deque(((0, 0), (maxx, 0), (0, maxy), (maxx, maxy)))
    seen = set(((0, 0), (maxx, 0), (0, maxy), (maxx, maxy)))
    while q:
        c = q.popleft()
        bigger[c] = " "
        for n in neighbrs_str8(c):
            if n in bigger and n not in seen and bigger[n] == ".":
                seen.add(n)
                q.append(n)

    return len([(x, y) for x, y in bigger if bigger[(x, y)] == "." and x % 3 == 1 and y % 3 == 1])


def setbiggun(big, coord, value):
    x, y = coord
    x *= 3
    y *= 3
    if value == ".":
        for dx, dy in (
            (0, 0),
            (1, 0),
            (2, 0),
            (0, 1),
            (1, 1),
            (2, 1),
            (0, 2),
            (1, 2),
            (2, 2),
        ):
            big[(x + dx, y + dy)] = "."
    elif value == "|":
        for dx, dy in ((0, 0), (2, 0), (0, 1), (2, 1), (0, 2), (2, 2)):
            big[(x + dx, y + dy)] = "."
        for dx, dy in ((1, 0), (1, 1), (1, 2)):
            big[(x + dx, y + dy)] = "█"
    elif value == "-":
        for dx, dy in ((0, 0), (1, 0), (2, 0), (0, 2), (1, 2), (2, 2)):
            big[(x + dx, y + dy)] = "."
        for dx, dy in ((0, 1), (1, 1), (2, 1)):
            big[(x + dx, y + dy)] = "█"
    elif value == "L":
        for dx, dy in (
            (0, 0),
            (2, 0),
            (0, 1),
            (0, 2),
            (1, 2),
            (2, 2),
        ):
            big[(x + dx, y + dy)] = "."
        for dx, dy in ((1, 0), (1, 1), (2, 1)):
            big[(x + dx, y + dy)] = "█"
    elif value == "J":
        for dx, dy in (
            (0, 0),
            (2, 0),
            (2, 1),
            (0, 2),
            (1, 2),
            (2, 2),
        ):
            big[(x + dx, y + dy)] = "."
        for dx, dy in ((1, 0), (1, 1), (0, 1)):
            big[(x + dx, y + dy)] = "█"
    elif value == "7":
        for dx, dy in (
            (0, 0),
            (1, 0),
            (2, 0),
            (2, 1),
            (0, 2),
            (2, 2),
        ):
            big[(x + dx, y + dy)] = "."
        for dx, dy in ((0, 1), (1, 1), (1, 2)):
            big[(x + dx, y + dy)] = "█"
    elif value == "F":
        for dx, dy in (
            (0, 0),
            (1, 0),
            (2, 0),
            (0, 1),
            (0, 2),
            (2, 2),
        ):
            big[(x + dx, y + dy)] = "."
        for dx, dy in ((2, 1), (1, 1), (1, 2)):
            big[(x + dx, y + dy)] = "█"


puzzle = Puzzle(2023, 10)
data = parse(puzzle.input_data)
print("part A", part_a(data))
print("part B", part_b(data))
