from aocd.models import Puzzle

def parse(input):
    return [tuple(int(n) for n in line) for line in input.splitlines()]

def part_a(data):
    return sum(bats(line, 2) for line in data)

def part_b(data):
    return sum(bats(line, 12) for line in data)

def bats(line, digits):
    index, result = 0, ''
    for i in range(digits):
        index = best_index(line, index, digits - i)
        result += str(line[index])
        index += 1
    return int(result)

def best_index(line, start, remaining_digits):
    best_index = start
    for i in range(start + 1, len(line)):
        if len(line) - i < remaining_digits:
            break
        if line[i] > line[best_index]:
            best_index = i
    return best_index

puzzle = Puzzle(2025, 3)
data = parse(puzzle.input_data)
print("part A", part_a(data))
print("part B", part_b(data))
