from collections import deque
from copy import deepcopy
from functools import reduce
from aocd.models import Puzzle

def parse(input):
    rules, parts = input.split('\n\n')
    rule_dict = {}
    for r in rules.splitlines():
        name, val = r.split('{')
        rule_dict[name] = val[:-1].split(',')
    part_list = []
    for p in parts.splitlines():
        p_dict = {}
        for subpart in p.strip('{}').split(','):
            cat, val = subpart.split('=')
            p_dict[cat] = int(val)
        part_list.append(p_dict)
        p_dict.values()
    return (rule_dict, part_list)

def part_a(data):
    rule_dict, part_list = data
    accepted = []
    for p in part_list:
        result = follow(rule_dict, p, 'in')
        if result == 'A': accepted.append(p)
    return sum(sum(p.values()) for p in accepted)

def follow(rule_dict, part, rule_name):
    rule = rule_dict[rule_name]
    for r in rule:
        if len(r) > 1 and r[1] in ['<', '>']:
            cat, op, rest = r[0], r[1], r[2:]
            val, out = rest.split(':')
            partval = part[cat]
            if op == '<' and partval < int(val):
                return returnfrom(rule_dict, part, out)
            elif op == '>' and partval > int(val):
                return returnfrom(rule_dict, part, out)
        else:
            return returnfrom(rule_dict, part, r)

def returnfrom(rule_dict, part, outname):
    if outname in ['A','R']: return outname
    else: return follow(rule_dict, part, outname)

def part_b(data):
    rule_dict, _ = data
    total = 0
    q = deque()
    q.append(('in', {'x': (1, 4000), 'm': (1, 4000), 'a': (1, 4000), 's': (1, 4000)}))
    while q:
        location, ranges = q.pop()
        if location == 'A':
            total += reduce(lambda accum, range: accum * (range[1] + 1 - range[0]), ranges.values(), 1)
        elif location != 'R':
            rule = rule_dict[location]
            for r in rule:
                if len(r) > 1 and r[1] in ['<', '>']:
                    cat, op, rest = r[0], r[1], r[2:]
                    val, out = rest.split(':')
                    lower,upper = ranges[cat]
                    if op == '<':
                        clone = deepcopy(ranges)
                        newupper = min(upper, int(val) - 1)
                        if lower <= newupper:
                            clone[cat] = (lower, newupper)
                            q.append((out, clone))

                        inverse = int(val)
                        lower = max(lower, inverse)
                        if lower > upper:
                            ranges[cat] = (0,-1)
                        else:
                            ranges[cat] = (lower, upper)
                    elif op == '>':
                        clone = deepcopy(ranges)
                        newlower = max(lower, int(val) + 1)
                        if newlower <= upper:
                            clone[cat] = (newlower, upper)
                            q.append((out, clone))

                        inverse = int(val)
                        upper = min(upper, inverse)
                        if lower > upper:
                            ranges[cat] = (0,-1)
                        else:
                            ranges[cat] = (lower, upper)
                else:
                    q.append((r, ranges))
    return total

puzzle = Puzzle(2023, 19)
data = parse(puzzle.input_data)
print("part A", part_a(data))
print("part B", part_b(data))
