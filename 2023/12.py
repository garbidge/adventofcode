from functools import cache
from aocd.models import Puzzle

def parse(input):
    split = [line.split() for line in input.splitlines()]
    return [(a, tuple(int(n) for n in b.split(","))) for a,b in split]

def part_a(data):
    return sum(cache_perms(line, counts) for line,counts in data)

@cache
def cache_perms(line, counts, index=0):
    return sum(perms(line, counts, index))

def perms(line, counts, index=0):
    if index >= len(counts):
        yield '#' not in line
    else:
        count = counts[index]
        possibles = ((line[:i], line[i:i+count], line[i+count:]) for i in range(len(line) - count + 1))
        for prefix, removed, suffix in possibles:
            if '#' in prefix: break
            if '.' in removed: continue
            if (len(suffix) == 0 or suffix[0] != '#') and (len(prefix) == 0 or prefix[-1] != '#'):
                yield cache_perms(suffix[1:], counts, index + 1)

def part_b(data):
    data = [('?'.join(line for _ in range(5)), counts*5) for line,counts in data]
    return part_a(data)

puzzle = Puzzle(2023, 12)
data = parse(puzzle.input_data)
print("part A", part_a(data))
print("part B", part_b(data))
