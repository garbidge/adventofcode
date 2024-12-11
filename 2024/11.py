from collections import Counter
from aocd.models import Puzzle
from utils import digits, ints

def parse(input):
    return Counter(ints(input))

def simulate(stones, count):
    for _ in range(count): stones = blink(stones)
    return sum(stones.values())

def blink(stones):
    new = Counter()
    for stone,amount in stones.items():
        if stone == 0:
            new[1] += amount
        elif (digit_count := digits(stone)) % 2 == 0:
            divisor = pow(10, digit_count // 2)
            left, right = stone // divisor, stone % divisor
            new[left] += amount
            new[right] += amount
        else:
            new[stone * 2024] += amount
    return new

puzzle = Puzzle(2024, 11)
data = parse(puzzle.input_data)
print("part A", simulate(data, 25))
print("part B", simulate(data, 75))
