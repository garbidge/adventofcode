from collections import defaultdict
from aocd.models import Puzzle

def parse(input):
    return input.split(',')

def part_a(data):
    return sum(hash(s) for s in data)

def hash(string):
    value = 0
    for c in string:
        value = (17 * (value + ord(c))) % 256
    return value

def part_b(data):
    mp = defaultdict(list)
    for step in data:
        if step[-1] == '-':
            lens = step[:-1]
            box = hash(lens)
            found = next((i for i, (L,N) in enumerate(mp[box]) if L == lens), None)
            if found != None:
                mp[box].pop(found)
        else:
            lens, num = step.split('=')
            num = int(num)
            box = hash(lens)
            index = next((i for i, (L, N) in enumerate(mp[box]) if L == lens), None)
            if index != None:
                mp[box][index] = (lens, num)
            else:
                mp[box].append((lens, num))
    power = 0
    for box in range(256):
        for i, (lens, num) in enumerate(mp[box]):
            power += focus(box, i+1, num)
    return power

def focus(box, slot, focal):
    return (1+box) * slot * focal

puzzle = Puzzle(2023, 15)
data = parse(puzzle.input_data)
print("part A", part_a(data))
print("part B", part_b(data))
