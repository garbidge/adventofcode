from aocd.models import Puzzle
from utils import lmap


def parse(input):
    return [lmap(int, line.split()) for line in input.splitlines()]


def part_a(data):
    total = 0
    for d in data:
        predicted = predict(d)
        extrap(predicted)
        total += predicted[0][-1]
    return total


def predict(dat):
    diff = diffs(dat)
    out = [dat, diff]
    while any(d != 0 for d in diff):
        diff = diffs(diff)
        out = [*out, diff]
    return out


def extrap(predicted):
    predicted[-1].append(0)
    for i in reversed(range(len(predicted) - 1)):
        val = predicted[i][-1] + predicted[i + 1][-1]
        predicted[i].append(val)


def baxtrap(predicted):
    predicted[-1].insert(0, 0)
    for i in reversed(range(len(predicted) - 1)):
        val = predicted[i][0] - predicted[i + 1][0]
        predicted[i].insert(0, val)


def diffs(dat):
    return [dat[i + 1] - dat[i] for i in range(len(dat) - 1)]


def part_b(data):
    total = 0
    for d in data:
        predicted = predict(d)
        baxtrap(predicted)
        total += predicted[0][0]
    return total


puzzle = Puzzle(2023, 9)
data = parse(puzzle.input_data)
print("part A", part_a(data))
print("part B", part_b(data))
