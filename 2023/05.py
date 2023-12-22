from functools import reduce
from aocd.models import Puzzle
from utils import chunks, pgrp

class Range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def overlaps(self, other):
        return self.start < other.end and self.end > other.start

    def intersect(self, other):
        start, end = max(self.start, other.start), min(self.end, other.end)
        return Range(start, end)

    def transpose(self, src, dest):
        diff = self.start - src.start
        length = self.end - self.start
        return Range(dest.start + diff, dest.start + diff + length)

    def contains(self, other):
        return self.start <= other.start and self.end >= other.end

    def exclude(self, other):
        if not self.overlaps(other): yield self
        else:
            if other.start > self.start: yield Range(self.start, other.start - 1)
            if other.end < self.end: yield Range(other.end + 1, self.end)

def parse(input):
    groups = pgrp(input)
    seeds = [int(n) for n in groups[0][0].split(": ")[1].split()]
    maps = [parse_group(g) for g in groups[1:]]
    return (seeds, maps)

def parse_group(group):
    return [[int(n) for n in line.split()] for line in group[1:]]

def part_a(data):
    (seeds, maps) = data
    return min(locate(seed, maps) for seed in seeds)

def locate(seed, maps):
    return reduce(lambda value, cur_map: next_val(value, cur_map), maps, seed)

def next_val(value, cur_map):
    for dest, start, length in cur_map:
        diff = value - start
        if diff >= 0 and diff < length:
            return dest + diff
    return value

def part_b(data):
    return min(range_start for range_start in find_range_starts(data))

def ranges(mapping):
    for dest, start, length in mapping:
        yield (Range(start, start + length - 1), Range(dest, dest + length - 1))

def find_range_starts(data):
    (seeds, maps) = data
    init_ranges = [Range(a, a+b) for a,b in chunks(seeds, 2)]
    range_mappings = [list(ranges(m)) for m in maps]
    for r in init_ranges:
        yield from rangesearch(r, range_mappings)

def rangesearch(current_range, range_mappings, depth = 0):
    if depth > len(range_mappings) - 1:
        yield current_range.start
        return
    
    mappings = range_mappings[depth]
    unmapped = [current_range]
    for src,dest in mappings:
        if current_range.overlaps(src):
            intersection = current_range.intersect(src)
            transposed = intersection.transpose(src, dest)
            yield from rangesearch(transposed, range_mappings, depth + 1)

            nx_unmapped = []
            for r in unmapped:
                if intersection.contains(r): continue
                for excluded in r.exclude(intersection):
                    nx_unmapped.append(excluded)
            unmapped = nx_unmapped
    for r in unmapped:
        yield from rangesearch(r, range_mappings, depth + 1)

puzzle = Puzzle(2023, 5)
data = parse(puzzle.input_data)
print("part A", part_a(data))
print("part B", part_b(data))
