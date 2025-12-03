from aocd.models import Puzzle

def parse(input):
    return [tuple(int(n) for n in line) for line in input.splitlines()]

def batteries(line, digits):
    index, result = 0, 0
    for d in range(digits):
        index = best_index(line, index, digits - d)
        result = (10 * result) + line[index]
        index += 1
    return result

def best_index(line, start, remaining_digits):
    end = len(line) - remaining_digits
    return max(range(start, end + 1), key=lambda i: line[i])

puzzle = Puzzle(2025, 3)
data = parse(puzzle.input_data)
print("part A", sum(batteries(line, 2) for line in data))
print("part B", sum(batteries(line, 12) for line in data))
