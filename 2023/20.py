from collections import deque
from math import lcm
from aocd.models import Puzzle

def parse(input):
    result = {}
    for line in input.splitlines():
        name, dest = line.split(' -> ')
        if   name[0] == '%': result[name[1:]] = ('%', False, dest.split(', '))
        elif name[0] == '&': result[name[1:]] = ('&', dict(), dest.split(', '))
        else:                result[name]     = ('b', 0, dest.split(', '))
    conjunctions = set(name for name in result if result[name][0] == '&')
    for name in result:
        _, _, dest = result[name]
        for d in dest:
            if d in conjunctions:
                _,memory,_ = result[d]
                memory[name] = False
    return result

def part_a(data):
    sent_lows, sent_highs = 0, 0
    q = deque()
    for _ in range(1000):
        q.append(('broadcaster', False, 'user'))
        while q:
            location, pulse, source = q.popleft()
            sent_lows += not pulse
            sent_highs += pulse
            if location not in data: continue
            
            typ, val, dest = data[location]
            if typ == 'b':
                for d in dest: q.append((d, pulse, location))
            elif typ == '%':
                if pulse == False:
                    data[location] = (typ, not val, dest)
                    for d in dest: q.append((d, not val, location))
            elif typ == '&':
                val[source] = pulse
                pulse = not all(p for p in val.values())
                for d in dest: q.append((d, pulse, location))
    return sent_lows * sent_highs

def part_b(data):
    outputter = next(x for x in data if data[x][-1] == ['rx'])
    typ, val, dest = data[outputter]
    iterations = { key: None for key in val }
    buttons = 0
    q = deque()
    while any(v == None for v in iterations.values()):
        buttons += 1
        q.append(('broadcaster', False, 'user'))
        while q:
            location, pulse, source = q.popleft()
            if location not in data: continue
            
            typ, val, dest = data[location]
            if typ == 'b':
                for d in dest: q.append((d, pulse, location))
            elif typ == '%':
                if pulse == False:
                    data[location] = (typ, not val, dest)
                    for d in dest: q.append((d, not val, location))
            elif typ == '&':
                val[source] = pulse
                if pulse and location == outputter and not iterations[source]:
                    iterations[source] = buttons
                pulse = not all(p for p in val.values())
                for d in dest: q.append((d, pulse, location))
    return lcm(*iterations.values())

puzzle = Puzzle(2023, 20)
data_a, data_b = parse(puzzle.input_data), parse(puzzle.input_data)
print("part A", part_a(data_a))
print("part B", part_b(data_b))
