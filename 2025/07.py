from aocd.models import Puzzle

def solve(input):
    grid = input.splitlines()
    splitters = 0
    counts = [c == 'S' for c in grid[0]]
    for line in grid[1:]:
        current = [0] * len(counts)
        for i,char in enumerate(line):
            if (count := counts[i]):
                if char == '^':
                    splitters += 1
                    current[i - 1] += count
                    current[i + 1] += count
                else:
                    current[i] += count
        counts = current
    return splitters, sum(counts)

puzzle = Puzzle(2025, 7)
a,b = solve(puzzle.input_data)
print("part A", a)
print("part B", b)
