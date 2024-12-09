from aocd.models import Puzzle
from utils import flatten

EMPTY_SPACE = -1

def parse(input):
    return [parseline(line) for line in input.splitlines()]

def parseline(line):
    disk = []
    for index in range(len(line)):
        id = index // 2 if index % 2 == 0 else EMPTY_SPACE
        for _ in range(int(line[index])): disk.append(id)
    return disk

def part_a(data):
    return sum(checksum(compact([*disk])) for disk in data)

def part_b(data):
    return sum(checksum(compact2([*disk])) for disk in data)

def compact(disk):
    left, right = 0, len(disk)-1
    while left < right:
        while left < right and disk[left] != EMPTY_SPACE:
            left += 1
        while left < right and disk[right] == EMPTY_SPACE:
            right -= 1
        if left < right:
            disk[left], disk[right] = disk[right], disk[left]
    return disk

def compact2(disk):
    disk_blocks = [*contiguous(disk)]
    right = len(disk_blocks) - 1
    while right > 0:
        left = 0
        while right > 0 and disk_blocks[right][0] == EMPTY_SPACE:
            right -= 1
        while left < right and (disk_blocks[left][0] != EMPTY_SPACE or len(disk_blocks[left]) < len(disk_blocks[right])):
            left += 1
        if left < right:
            size_left, size_right = len(disk_blocks[left]), len(disk_blocks[right])
            inserted = [*disk_blocks[right]]
            for i in range(size_right): disk_blocks[right][i] = EMPTY_SPACE
            if size_right == size_left: disk_blocks.pop(left)
            else: disk_blocks[left] = disk_blocks[left][size_right:]
            disk_blocks.insert(left, inserted)
        right -= 1
    return flatten(disk_blocks)

def contiguous(disk):
    current = []
    for n in disk:
        if not current or n == current[-1]: current.append(n)
        else:
            if current: yield current
            current = [n]
    if current: yield current

def checksum(disk):
    return sum(i * int(n) for i,n in enumerate(disk) if n != EMPTY_SPACE)

puzzle = Puzzle(2024, 9)
data = parse(puzzle.input_data)
print("part A", part_a(data))
print("part B", part_b(data))