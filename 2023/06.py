from aocd.models import Puzzle
from math import ceil, floor, prod, sqrt
from utils import lmapsub

def parse(input):
    return lmapsub(int, [line.split()[1:] for line in input.splitlines()])

def part_a(data):
    return prod(quadratic_solve(time, distance) for time,distance in zip(*data))

def part_b(data):
    time, distance = [int("".join(map(str, numbers))) for numbers in data]
    return quadratic_solve(time, distance)

def quadratic_solve(time, best_dist):
    # For T=time, D=dist:
    #   x * (T - x) = D
    #   Tx - x^2 = D
    #   x^2 - Tx + D = 0
    sqrtDiscriminant = sqrt((time**2) - (4 * best_dist))
    lower = (time - sqrtDiscriminant) / 2
    upper = (time + sqrtDiscriminant) / 2
    return ceil(upper - 1) - floor(lower + 1) + 1

puzzle = Puzzle(2023, 6)
data = parse(puzzle.input_data)
print("part A", part_a(data))
print("part B", part_b(data))
