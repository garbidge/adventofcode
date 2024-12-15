from aocd.models import Puzzle
from utils import flatten, pgriddict, tuple_add

directions = {
    '^': (0,-1),
    '<': (-1,0),
    'v': (0,1),
    '>': (1,0)
}

def parse(input):
    warehouse, movements = input.split('\n\n')
    return pgriddict(warehouse, str), flatten(movements.splitlines())

def parse_wide(input: str):
    warehouse, movements = input.split('\n\n')
    warehouse = warehouse.replace('#', '##').replace('O', '[]').replace('.', '..').replace('@', '@.')
    return pgriddict(warehouse, str), flatten(movements.splitlines())

def part_a(warehouse, movements):
    location = next(coord for coord in warehouse if warehouse[coord] == '@')
    warehouse[location] = '.'
    for move in movements:
        direction = directions[move]
        nxt = tuple_add(location, direction)
        if warehouse[nxt] == '#': continue
        elif warehouse[nxt] == '.': location = nxt
        else:
            current = nxt
            while warehouse[current] != '#' and warehouse[current] != '.':
                current = tuple_add(current, direction)
            if warehouse[current] == '.':
                location = nxt
                warehouse[nxt] = '.'
                warehouse[current] = 'O'
    return sum(100 * y + x for x,y in warehouse if warehouse[(x,y)] == 'O')

def part_b(warehouse, movements):
    location = next(coord for coord in warehouse if warehouse[coord] == '@')
    warehouse[location] = '.'
    for move in movements:
        direction = directions[move]
        nxt = tuple_add(location, direction)
        if warehouse[nxt] == '#': continue
        elif warehouse[nxt] == '.': location = nxt
        else:
            locations = [set(get_pushed(warehouse, location, move, direction))]
            while not any(warehouse[c] == '#' for c in locations[-1]) and not all(warehouse[c] == '.' for c in locations[-1]):
                locations.append(set(flatten(get_pushed(warehouse, c, move, direction) for c in locations[-1] if warehouse[c] in ['[',']'])))
            if all(warehouse[c] == '.' for c in locations[-1]):
                for pushed in reversed(locations[:-1]):
                    for coord in pushed:
                        if warehouse[coord] in ['[',']']:
                            warehouse[tuple_add(coord, direction)] = warehouse[coord]
                            warehouse[coord] = '.'
                location = nxt
    return sum(100 * y + x for x,y in warehouse if warehouse[(x,y)] == '[')

def get_pushed(warehouse, coord, move, direction):
    direct = tuple_add(coord, direction)
    yield direct
    if move in ('^','v'):
        if warehouse[direct] in ('[',']'):
            dx = 1 if warehouse[direct] == '[' else -1
            yield tuple_add(direct, (dx,0))

puzzle = Puzzle(2024, 15)
print("part A", part_a(*parse(puzzle.input_data)))
print("part B", part_b(*parse_wide(puzzle.input_data)))
