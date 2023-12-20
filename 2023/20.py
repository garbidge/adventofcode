from collections import defaultdict, deque
from math import lcm
from aocd.models import Puzzle

def parse(input):
    result = {}
    for line in input.splitlines():
        name, dest = line.split(' -> ')
        if name[0] == '%':
            result[name[1:]] = ('%', False, dest.split(', '))
        elif name[0] == '&':
            result[name[1:]] = ('&', defaultdict(bool), dest.split(', '))
        else:
            result[name] = ('b', 0, dest.split(', '))
    for name in result:
        if name != 'broadcaster':
            _, _, dest = result[name]
            for d in dest:
                if d in result:
                    t,maybememory,_ = result[d]
                    if t == '&':
                        maybememory[name] = False
    return result

def part_a(data):
    sent_lows, sent_highs = 0, 0
    for _ in range(1000):
        q = deque()
        q.append(('broadcaster', False, 'user'))
        sent_lows += 1
        while q:
            location, pulse, source = q.popleft()
            if location not in data: continue
            
            typ, val, dest = data[location]
            if typ == 'b':
                for d in dest:
                    q.append((d, pulse, location))
                    sent_lows += 1
            elif typ == '%':
                if pulse == False:
                    data[location] = (typ, not val, dest)
                    for d in dest:
                        q.append((d, not val, location))
                        if val: sent_lows += 1
                        else:   sent_highs += 1
            elif typ == '&':
                val[source] = pulse
                pulse = not all(p for p in val.values())
                for d in dest:
                    q.append((d, pulse, location))
                    if pulse: sent_highs += 1
                    else:     sent_lows += 1
    return sent_lows * sent_highs

def part_b(data):
    outputter = next(x for x in data if data[x][-1] == ['rx'])
    typ, val, dest = data[outputter]
    iterations = { key: None for key in val }
    buttons = 0
    while any(v == None for v in iterations.values()):
        buttons += 1
        q = deque()
        q.append(('broadcaster', False, 'user'))
        while q:
            location, pulse, source = q.popleft()
            if location not in data: continue
            
            typ, val, dest = data[location]
            if typ == 'b':
                for d in dest:
                    q.append((d, pulse, location))
            elif typ == '%':
                if pulse == False:
                    data[location] = (typ, not val, dest)
                    for d in dest:
                        q.append((d, not val, location))
            elif typ == '&':
                val[source] = pulse
                if location == outputter and pulse and not iterations[source] and buttons > 3700:
                    iterations[source] = buttons
                pulse = not all(p for p in val.values())
                for d in dest:
                    q.append((d, pulse, location))
    return lcm(*iterations.values())

puzzle = Puzzle(2023, 20)
data = parse(puzzle.input_data)
print("part A", part_a(data))
data = parse(puzzle.input_data)
print("part B", part_b(data))
