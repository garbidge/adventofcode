from aocd.examples import Example
from aocd.models import Puzzle
from termcolor import colored
from utils import (  # noqa
    flatten,
    ints,
    lmap,
    lmapsub,
    pgriddict,
    pgridint,
    pgrp,
    pgrpint,
    pgrpints,
    pint,
    plint,
    preg,
    pstrip,
)

def parse(input):
    return []

def part_a(data):
    return 0

def part_b(data):
    return 0

puzzle = Puzzle(2024, 1)
for i, x in enumerate(puzzle.examples):
    example: Example = x
    print("========================================")
    print(f"Example {i+1}\n")
    print(example.input_data, "\n")
    parsed = parse(example.input_data)
    a = part_a(parsed)
    print(
        "a",
        example.answer_a,
        a,
        colored("CORRECT", "green")
        if example.answer_a == str(a)
        else colored("INCORRECT", "red"),
    )
    b = part_b(parsed)
    print(
        "b",
        example.answer_b,
        b,
        colored("CORRECT", "green")
        if example.answer_b == str(b)
        else colored("INCORRECT", "red"),
    )

print("========================================")

data = parse(puzzle.input_data)
a = part_a(data)
print("part A", a)
# puzzle.answer_a = a

b = part_b(data)
print("part B", b)
# puzzle.answer_b = b
