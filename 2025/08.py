import itertools
import math
from aocd.models import Puzzle

def parse(input):
    return [tuple(int(n) for n in line.split(",")) for line in input.splitlines()]

def solve(data):
    ordered = sorted(itertools.combinations(data, 2), key=lambda pair: math.dist(*pair))
    i, circuits = 0, [{pos} for pos in data]
    while len(circuits) > 1:
        if i == 1000:
            yield math.prod(sorted((len(x) for x in circuits), reverse=True)[:3])

        pos_a, pos_b = ordered[i]
        i += 1
        sets = [s for s in circuits if pos_a in s or pos_b in s]
        if len(sets) == 2:
            sets[0] |= sets[1]
            circuits.remove(sets[1])

    yield pos_a[0] * pos_b[0]

puzzle = Puzzle(2025, 8)
data = parse(puzzle.input_data)
a,b = solve(data)
print("part A", a)
print("part B", b)