from functools import cache
from aocd.models import Puzzle

def parse(input):
    parsed = {}
    for line in input.splitlines():
        device, outputs = line.split(': ')
        parsed[device] = set(outputs.split(' '))
    return parsed

def part_a(data):
    @cache
    def cached_search(current):
        if current == 'out':
            return 1
        return sum(cached_search(connected) for connected in data[current])

    return cached_search('you')

def part_b(data):
    @cache
    def cached_search(current, visited_fft, visited_dac):
        if current == 'out':
            return visited_fft and visited_dac

        visited_fft |= current == 'fft'
        visited_dac |= current == 'dac'
        return sum(cached_search(connected, visited_fft, visited_dac) for connected in data[current])

    return cached_search('svr', False, False)

puzzle = Puzzle(2025, 11)
data = parse(puzzle.input_data)
print("part A", part_a(data))
print("part B", part_b(data))
