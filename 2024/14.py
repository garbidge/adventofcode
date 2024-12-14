from itertools import count
from math import prod
from aocd.models import Puzzle
from utils import plint

MAX_X = 101
MAX_Y = 103

def parse(input):
    return plint(input)

def part_a(robots):
    for _ in range(100): robots = step(robots)
    return score(robots)

def part_b(robots):
    for i in count():
        if distinct(robots): return i
        robots = step(robots)

def step(robots):
    return [((x + vx) % MAX_X, (y + vy) % MAX_Y, vx, vy) for x,y,vx,vy in robots]

def score(robots):
    quadrants = [0,0,0,0]
    for x,y,_,_ in robots:
        if x != (middle_x := MAX_X // 2) and y != (middle_y := MAX_Y // 2):
            quadrants[(x > middle_x) + 2 * (y > middle_y)] += 1
    return prod(quadrants)

def distinct(robots):
    return len(set((px,py) for px,py,_,_ in robots)) == len(robots)

puzzle = Puzzle(2024, 14)
data = parse(puzzle.input_data)
print("part A", part_a(data))
print("part B", part_b(data))
