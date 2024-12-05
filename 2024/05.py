from aocd.models import Puzzle
from utils import plint

def parse(input):
    rules, pages = [plint(group) for group in input.split('\n\n')]
    rules_grp = { left: set() for left,right in rules }
    for left,right in rules: rules_grp[left].add(right)
    return (rules_grp, pages)

def part_a(rules_grp, pages):
    return sum(page[len(page) // 2] for page in pages if is_valid(page, rules_grp))

def part_b(rules_grp, pages):
    invalid = [reorder(p, rules_grp) for p in pages if not is_valid(p, rules_grp)]
    return sum(page[len(page) // 2] for page in invalid)

def is_valid(page, rules_grp):
    seen = set()
    for p in page:
        if p in rules_grp and any(r in seen for r in rules_grp[p]):
            return False
        seen.add(p)
    return True

def reorder(page, rules_grp):
    mutated = [*page]
    index = len(page) - 1
    while index >= 0:
        current = mutated[index]
        rules = rules_grp[current] if current in rules_grp else []
        sliced = mutated[:index]
        indices = [mutated.index(p) for p in rules if p in sliced]
        if indices:
            value = mutated.pop(index)
            mutated.insert(min(indices), value)
        else:
            index -= 1
    return mutated

puzzle = Puzzle(2024, 5)
data = parse(puzzle.input_data)
print("part A", part_a(*data))
print("part B", part_b(*data))
