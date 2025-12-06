import itertools
import math
from aocd.models import Puzzle

from utils import transpose_str

def solve(input):
    ops = { '+': sum, '*': math.prod }
    *numbers, operators = input.splitlines()
    numbers, operators =  transpose_str(numbers), operators.split()
    groupings = [list(group) for key,group in itertools.groupby(numbers, lambda x: x.strip() == '') if not key]
    a = b = 0
    for i,number_group in enumerate(groupings):
        operator = ops[operators[i]]
        a += operator(int(n) for n in transpose_str(number_group))
        b += operator(int(n) for n in number_group)
    return a, b

puzzle = Puzzle(2025, 6)
a,b = solve(puzzle.input_data)
print("part A", a)
print("part B", b)