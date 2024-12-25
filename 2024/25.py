from aocd.models import Puzzle

def parse(input):
    locks, keys = [],[]
    for group in input.split('\n\n'):
        lines = group.splitlines()
        sizes = [col.count('#') - 1 for col in zip(*lines)]
        if all(c == '#' for c in lines[0]): locks.append(sizes)
        else: keys.append(sizes)
    return (locks,keys)

def part_a(locks, keys):
    return sum(all(a + b <= 5 for a,b in zip(lock,key)) for lock in locks for key in keys)

puzzle = Puzzle(2024, 25)
locks,keys = parse(puzzle.input_data)
print("part A", part_a(locks, keys))