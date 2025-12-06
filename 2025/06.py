import itertools
import math
from aocd.models import Puzzle

def transpose(x):
    return list(map(''.join, zip(*x)))

def solve(input):
    ops = {'+': sum, '*': math.prod}
    *numbers, operators = input.splitlines()
    numbers, operators =  transpose(numbers), operators.split()
    numbers = [list(group) for key,group in itertools.groupby(numbers, lambda x: x.strip() == '') if not key]
    a = b = 0
    for i,nums in enumerate(numbers):
        vertical = [int(n) for n in nums]
        horizontal = [int(n) for n in transpose(nums)]
        operator = ops[operators[i]]
        a += operator(horizontal)
        b += operator(vertical)
    return a, b

puzzle = Puzzle(2025, 6)
a,b = solve(puzzle.input_data)
print("part A", a)
print("part B", b)