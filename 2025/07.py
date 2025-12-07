from aocd.models import Puzzle

def solve(input):
    grid = input.splitlines()
    splitters = set()
    counts = [c == 'S' for c in grid[0]]
    for y,line in enumerate(grid[1:], 1):
        current = [0 for _ in counts]
        for x,char in enumerate(line):
            if (count := counts[x]):
                if char == '^':
                    splitters.add((x, y))
                    current[x - 1] += count
                    current[x + 1] += count
                else:
                    current[x] += count
        counts = current
    return len(splitters), sum(counts)

puzzle = Puzzle(2025, 7)
a,b = solve(puzzle.input_data)
print("part A", a)
print("part B", b)
