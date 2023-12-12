from functools import cache
from aocd.models import Puzzle

def parse(input):
    split = [line.split() for line in input.splitlines()]
    return [(a, tuple(int(n) for n in b.split(","))) for a,b in split]

def part_a(data):
    return sum(cache_perms(line, counts) for line,counts in data)

def part_b(data):
    data = [('?'.join(line for _ in range(5)), counts*5) for line,counts in data]
    return part_a(data)

@cache
def cache_perms(line, counts):
    return sum(perms(line, counts))

def perms(line, counts):
    if len(counts) == 0: yield '#' not in line
    else:
        count = counts[0]
        possibles = ((line[:i], line[i:i+count], line[i+count:]) for i in range(len(line) - count + 1))
        for prefix, removed, suffix in possibles:
            if '#' in prefix: break
            if '.' in removed: continue
            if len(suffix) == 0 or suffix[0] != '#':
                yield cache_perms(suffix[1:], counts[1:])

puzzle = Puzzle(2023, 12)
data = parse(puzzle.input_data)
print("part A", part_a(data))
print("part B", part_b(data))
