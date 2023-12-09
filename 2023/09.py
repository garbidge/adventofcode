from aocd.models import Puzzle
from utils import lmap


def parse(input):
    return [lmap(int, line.split()) for line in input.splitlines()]


def part_a(data):
    return sum(extrap(predict(d))[0][-1] for d in data)


def diffs(dat):
    return [dat[i + 1] - dat[i] for i in range(len(dat) - 1)]


def predict(dat):
    out = [dat, diffs(dat)]
    while any(d != 0 for d in out[-1]):
        out.append(diffs(out[-1]))
    return out


def extrap(predicted):
    predicted[-1].append(0)
    for i in reversed(range(len(predicted) - 1)):
        predicted[i].append(predicted[i][-1] + predicted[i + 1][-1])
    return predicted


def part_b(data):
    return part_a([list(reversed(d)) for d in data])


puzzle = Puzzle(2023, 9)
data = parse(puzzle.input_data)
print("part A", part_a(data))
print("part B", part_b(data))
