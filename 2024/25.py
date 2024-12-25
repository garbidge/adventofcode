from aocd.models import Puzzle

def parse(input):
    return [parse_grid(x) for x in input.split('\n\n')]

def parse_grid(x):
    lines = x.splitlines()
    typ = 'lock' if all(c == '#' for c in lines[0]) else 'key'
    cols = [[line[i] for line in lines] for i in range(len(lines[0]))]
    return typ, [sum(c == '#' for c in col) - 1 for col in cols]

def part_a(data):
    locks = [grid for typ, grid in data if typ == 'lock']
    keys = [grid for typ, grid in data if typ == 'key']
    total = 0
    for lock in locks:
        for key in keys:
            if all(a + b <= 5 for a,b in zip(lock,key)):
                total += 1
    return total

puzzle = Puzzle(2024, 25)
data = parse(puzzle.input_data)
print("part A", part_a(data))