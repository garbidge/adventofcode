from math import prod
from aocd.models import Puzzle

def parse(input):
    lines = input.splitlines()
    line_length = len(lines[0])
    num_lines = len(lines)
    blanks = [col for col in range(line_length) if all(lines[row][col] == ' ' for row in range(num_lines))]
    blanks.append(line_length)
    groups = []
    index = 0
    for end_index in blanks:
        parts = [line[index:end_index] for line in lines]
        nums = [int(n) for n in parts[:-1]]
        operator = parts[-1].strip()
        groups.append((nums, operator))
        index = end_index + 1
    return groups

def parse2(input):
    lines = input.splitlines()
    line_length = len(lines[0])
    num_lines = len(lines)
    blanks = [col for col in range(line_length) if all(lines[row][col] == ' ' for row in range(num_lines))]
    blanks.append(line_length)
    groups = []
    index = 0
    for end_index in blanks:
        parts = [line[index:end_index] for line in lines]
        operator = parts[-1].strip()
        nums = parts[:-1]
        nums = [int(''.join(nums[row][col] for row in range(len(nums)))) for col in range(len(nums[0]))]
        groups.append((nums, operator))
        index = end_index + 1
    return groups

def part_a(data):
    total = 0
    for nums, operator in data:
        if operator == '+':
            total += sum(nums)
        elif operator == '*':
            total += prod(nums)
    return total

def part_b(data):
    return part_a(data)

puzzle = Puzzle(2025, 6)
data = parse(puzzle.input_data)
print("part A", part_a(data))
data = parse2(puzzle.input_data)
print("part B", part_b(data))
