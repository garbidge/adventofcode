from aocd.models import Puzzle

def parse(input):
    return [parseline(line) for line in input.splitlines()]

def parseline(line):
    disk = []
    index = 0
    while index < len(line):
        size = int(line[index])
        character = str(index // 2) if index % 2 == 0 else '.'
        for _ in range(size):
            disk.append(character)
        index += 1
    return disk

def part_a(data):
    return sum(checksum(compact([*disk])) for disk in data)

def part_b(data):
    return sum(checksum(compact2([*disk])) for disk in data)

def compact(disk):
    left, right = 0, len(disk)-1
    while left < right:
        while left < right and disk[left] != '.':
            left += 1
        while left < right and disk[right] == '.':
            right -= 1
        if left < right:
            disk[left], disk[right] = disk[right], disk[left]
    return disk

def compact2(disk):
    right2 = len(disk)-1
    while right2 >= 0:
        while right2 >= 0 and disk[right2] == '.':
            right2 -= 1
        right1 = right2
        while right1 >= 0 and disk[right1] == disk[right2]:
            right1 -= 1
        size = right2 - right1
        if disk[right2] != '.' and (start_index := findblock(disk, size)) != None and start_index < right1:
            character = disk[right2]
            for i in range(size):
                disk[start_index + i] = character
                disk[right1 + 1 + i] = '.'
        else:
            right2 = right1
    return disk

def findblock(disk, size):
    index = 0
    while index < len(disk):
        if disk[index] == '.':
            end = index
            while end < len(disk) and disk[end] == '.':
                end += 1
            blocksize = end - index
            if blocksize >= size:
                return index
            else:
                index = end
        else:
            index += 1

def checksum(disk):
    return sum(i * int(n) for i,n in enumerate(disk) if n != '.')

puzzle = Puzzle(2024, 9)
data = parse(puzzle.input_data)
print("part A", part_a(data))
print("part B", part_b(data))