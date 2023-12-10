from aocd.models import Puzzle
from collections import deque
from utils import pgrp

def parse(input):
    groups = pgrp(input)
    seeds = [int(n) for n in groups[0][0].split(": ")[1].split()]
    maps = [parse_group(g) for g in groups[1:]]
    return (seeds, maps)

def parse_group(group):
    name = group[0]
    ranges = [[int(n) for n in line.split()] for line in group[1:]]
    return (name, ranges)

def part_a(data):
    (seeds, maps) = data
    return min(locate(seed, maps) for seed in seeds)

def locate(seed, maps):
    value = seed
    for m in maps:
        value = nextval(value, m)
    return value

def nextval(value, mp):
    for dest, start, rng in mp[1]:
        diff = value - start
        if diff >= 0 and diff < rng:
            return dest + diff
    return value

def part_b(data):
    return min(x for x in do_q(data))

def do_q(data):
    (seeds, maps) = data
    pairs = [
        (seeds[i], seeds[i] + seeds[i + 1] - 1) for i in range(0, len(seeds) - 1, 2)
    ]
    rngs = [ranges(m) for m in maps]
    q = deque()
    for p in pairs:
        q.append((p[0], p[1], 0))
    while q:
        (start, end, index) = q.popleft()
        for ns, ne, nindex in rangesearch(start, end, index, rngs):
            if nindex == len(rngs):
                yield ns
            else:
                q.append((ns, ne, nindex))

def rangesearch(start, end, index, rngs):
    srange, drange = rngs[index]
    missed = [(start, end)]
    for i in range(len(srange)):
        (ss, se) = srange[i]
        if start < se and end > ss:
            rs, re = max(start, ss), min(end, se)
            diffstart = rs - ss
            diff = re - rs
            ds, de = drange[i]
            yield (ds + diffstart, ds + diffstart + diff, index + 1)

            nx_missed = []
            for s, e in missed:
                if rs <= s and re >= e:
                    continue
                if re < s or rs > e:
                    nx_missed.append((s, e))
                else:
                    if rs > s + 1:
                        nx_missed.append((s, rs - 1))
                    if re < e:
                        nx_missed.append((re + 1, e))
            missed = nx_missed
    for s, e in missed:
        yield (s, e, index + 1)

def ranges(mp):
    sranges = []
    dranges = []
    mn = min(start for dest, start, rng in mp[1])
    if mn > 1:
        sranges.append((0, mn - 1))
        dranges.append((0, mn - 1))
    for dest, start, rng in mp[1]:
        sranges.append((start, start + rng - 1))
        dranges.append((dest, dest + rng - 1))
    return (sranges, dranges)

puzzle = Puzzle(2023, 5)
data = parse(puzzle.input_data)
print("part A", part_a(data))
print("part B", part_b(data))
