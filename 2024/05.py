from collections import defaultdict
from aocd.models import Puzzle
from utils import plint

def parse(input):
    rules, pages = [plint(group) for group in input.split('\n\n')]
    rules_grp = defaultdict(set)
    for left,right in rules: rules_grp[left].add(right)
    return (rules_grp, pages)

def part_a(rules_grp, pages):
    return sum(page[len(page) // 2] for page in pages if is_valid(page, rules_grp))

def part_b(rules_grp, pages):
    invalid = [reorder(p, rules_grp) for p in pages if not is_valid(p, rules_grp)]
    return sum(page[len(page) // 2] for page in invalid)

def is_valid(page, rules_grp):
    return not any(rule in page[:i] for i,p in enumerate(page) for rule in rules_grp[p])

def reorder(page, rules_grp):
    mutated, index = [*page], len(page) - 1
    while index > 0:
        rules = rules_grp[mutated[index]]
        indices = [mutated.index(p) for p in rules if p in mutated[:index]]
        if indices:
            value = mutated.pop(index)
            mutated.insert(min(indices), value)
        else: index -= 1
    return mutated

puzzle = Puzzle(2024, 5)
data = parse(puzzle.input_data)
print("part A", part_a(*data))
print("part B", part_b(*data))
