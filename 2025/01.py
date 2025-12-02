from aocd.models import Puzzle

def parse(input):
    return ((1 if x[0] == 'R' else -1) * int(x[1:]) for x in input.splitlines())

def solve(data):
    a, b, dial = 0, 0, 50
    for num in data:
        b += revolutions(dial, num)
        dial = (dial + num) % 100
        a += dial == 0
    return a, b

def revolutions(start, rotations):
    end = start + remainder(rotations, 100)
    return abs(rotations) // 100 + int(start != 0 and (end <= 0 or end >= 100))

def remainder(n, divisor):
    return (abs(n) % divisor) * (1 if n >= 0 else -1)

puzzle = Puzzle(2025, 1)
data = parse(puzzle.input_data)
a,b = solve(data)
print("part A", a)
print("part B", b)