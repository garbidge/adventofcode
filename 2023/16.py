from collections import deque
from aocd.models import Puzzle
from utils import maxes, pgriddict, tuple_add

directions = {'u': (0,-1), 'd': (0,1), 'l': (-1,0), 'r': (1, 0)}
mutations = {
    ('|', 'l'): ('u','d'),
    ('|', 'r'): ('u','d'),
    ('-', 'u'): ('l','r'),
    ('-', 'd'): ('l','r'),
    ('/', 'u'): 'r',
    ('\\','d'): 'r',
    ('/', 'd'): 'l',
    ('\\','u'): 'l',
    ('/', 'l'): 'd',
    ('\\','r'): 'd',
    ('/', 'r'): 'u',
    ('\\','l'): 'u'
}

def parse(input):
    return pgriddict(input, str)

def part_a(data, start = (0,0), start_dir = 'r'):
    q = deque(((start, d) for d in next_direction(data[start], start_dir)))
    seen = set(q)
    while q:
        coord, d = q.popleft()
        next_coord = tuple_add(coord, directions[d])
        if next_coord in data and (next_coord, d) not in seen:
            seen.add((next_coord, d))
            for next_d in next_direction(data[next_coord], d):
                q.append((next_coord, next_d))
    return len(set(coord for coord,d in seen))

def next_direction(char, d):
    if (char, d) in mutations:
        yield from mutations[(char, d)]
    else: yield d

def part_b(data):
    max_x, max_y = maxes(data)
    return max(
        *(part_a(data, (x,     0), 'd') for x in range(max_x + 1)),
        *(part_a(data, (x, max_y), 'u') for x in range(max_x + 1)),
        *(part_a(data, (0,     y), 'r') for y in range(max_y + 1)),
        *(part_a(data, (max_x, y), 'l') for y in range(max_y + 1))
    )

puzzle = Puzzle(2023, 16)
data = parse(puzzle.input_data)
print("part A", part_a(data))
print("part B", part_b(data))
