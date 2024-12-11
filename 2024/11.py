from collections import defaultdict
from aocd.models import Puzzle
from utils import digits, ints

def parse(input):
    amounts = defaultdict(int)
    for n in ints(input):
        amounts[n] += 1
    return amounts

def simulate(amounts, count):
    for _ in range(count):
        amounts = blink(amounts)
    return sum(amounts.values())

def blink(amounts):
    new = defaultdict(int)
    for n in amounts:
        value = amounts[n]
        if value > 0:
            if n == 0:
                new[1] += value
            elif (count := digits(n)) % 2 == 0:
                divisor = pow(10, count // 2)
                left, right = n // divisor, n % divisor
                new[left] += value
                new[right] += value
            else:
                new[n * 2024] += value
    return new

puzzle = Puzzle(2024, 11)
data = parse(puzzle.input_data)
print("part A", simulate(data, 25))
print("part B", simulate(data, 75))
