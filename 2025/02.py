from aocd.models import Puzzle

def parse(input):
    parts = [p.split('-') for p in input.strip().split(',')]
    return [[int(n) for n in part] for part in parts]

def part_a(data):
    total = 0
    for a,b in data:
        count = 0
        for n in range(a, b+1):
            text = str(n)
            if len(text) % 2 != 0:
                continue
            mid = len(text) // 2
            if text[:mid] == text[mid:]:
                count += n
        total += count
    return total

def part_b(data):
    total = 0
    for a,b in data:
        for n in range(a, b+1):
            text = str(n)
            for length in range(1, len(text)//2 + 1):
                if len(text) % length == 0:
                    parts = [text[i:i+length] for i in range(0, len(text), length)]
                    if len(set(parts)) == 1:
                        total += n
                        break
    return total

puzzle = Puzzle(2025, 2)
data = parse(puzzle.input_data)
print("part A", part_a(data))
print("part B", part_b(data))
