from collections import defaultdict
from aocd.models import Puzzle
from utils import pint

def parse(input):
    return pint(input)

def solve(data):
    total, lookup = 0, defaultdict(int)
    for secret in data:
        window, visited = tuple(), set()
        for _ in range(2000):
            nxt = next_secret(secret)
            bananas = nxt % 10
            diff = bananas - (secret % 10)
            secret = nxt
            if len(window) < 4: window = (*window, diff)
            else: window = (*window[1:], diff)
            if len(window) == 4 and window not in visited:
                visited.add(window)
                lookup[window] += bananas
        total += secret
    return total, max(v for v in lookup.values())

def next_secret(secret):
    secret = prune(mix(secret, secret * 64))
    secret = prune(mix(secret, secret // 32))
    return prune(mix(secret, secret * 2048))

def mix(secret, value):
    return secret ^ value

def prune(secret):
    return secret % 16777216

puzzle = Puzzle(2024, 22)
data = parse(puzzle.input_data)
a,b = solve(data)
print("part A", a)
print("part B", b)
