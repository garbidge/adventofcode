from aocd.models import Puzzle

from utils import digits

def parse(input):
    return [tuple(int(n) for n in range.split('-')) for range in input.split(',')]

def solve(data):
    a = b = 0
    for lower,upper in data:
        for n in generate_ids(lower, upper):
            if has_two_parts(str(n)): a += n
            b += n
    return a,b

def has_two_parts(number_string):
    mid = len(number_string) // 2
    return number_string[:mid] == number_string[mid:]

def generate_ids(lower, upper):
    lower_digits, upper_digits = digits(lower), digits(upper)
    number = 1
    while int((text := str(number)) * 2) <= upper:
        if not has_repeating_pattern(text):
            for n in range(lower_digits, upper_digits + 1):
                if n % len(text) == 0:
                    value = int(text * (n // len(text)))
                    if lower <= value <= upper:
                        yield value
        number += 1

def has_repeating_pattern(text):
    return any(text[:n] * (len(text) // n) == text for n in range(1, len(text) // 2 + 1))

puzzle = Puzzle(2025, 2)
data = parse(puzzle.input_data)
a,b = solve(data)
print("part A", a)
print("part B", b)
