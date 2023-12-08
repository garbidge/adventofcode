from math import lcm

from aocd.models import Puzzle


def parse(input):
    dirs, maps = input.split("\n\n")
    maps = [parse_line(line) for line in maps.splitlines()]
    maps = {source: dest for source, dest in maps}
    return dirs, maps


def parse_line(line):
    source, dest = line.split(" = ")
    dest = dest[1:-1].split(", ")
    return (source, dest)


def part_a(data):
    dirs, maps = data
    steps = 0
    current = "AAA"
    while current != "ZZZ":
        node = maps[current]
        LR = 0 if dirs[steps % len(dirs)] == "L" else 1
        current = node[LR]
        steps += 1
    return steps


def part_b(data):
    dirs, maps = data
    current = [node for node in maps if node[-1] == "A"]
    times = [0 for _ in range(len(current))]
    steps = 0
    while any(t == 0 for t in times):
        LR = 0 if dirs[steps % len(dirs)] == "L" else 1
        steps += 1
        for i in range(len(current)):
            node = maps[current[i]]
            current[i] = node[LR]
            if current[i].endswith("Z"):
                times[i] = steps
    return lcm(*times)


puzzle = Puzzle(2023, 8)
data = parse(puzzle.input_data)
print("part A", part_a(data))
print("part B", part_b(data))
