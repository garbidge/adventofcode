from math import prod

from aocd.models import Puzzle
from utils import lmapsub


def parse(input):
    return lmapsub(int, [line.split()[1:] for line in input.splitlines()])


def part_a(data):
    times, distances = data
    out = []
    for i in range(len(times)):
        out.append(ways(times[i], distances[i]))
    return prod(out)


def ways(time, bestdist):
    count = 0
    for held in range(time):
        speed = held
        remaining = time - held
        dist = speed * remaining
        if dist > bestdist:
            count += 1
    return count


def part_b(data):
    times, distances = data
    time = ""
    dist = ""
    for i in range(len(times)):
        time += str(times[i])
        dist += str(distances[i])
    time = int(time)
    dist = int(dist)
    return ways(time, dist)


puzzle = Puzzle(2023, 6)
data = parse(puzzle.input_data)
print("part A", part_a(data))
print("part B", part_b(data))
