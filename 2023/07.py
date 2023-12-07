from collections import Counter
from functools import cmp_to_key

from aocd.models import Puzzle


def parse(input):
    for line in input.splitlines():
        hand, bet = line.split()
        yield (Counter(hand), hand, int(bet))


def part_a(data):
    mapped = [(hand_type(count), hand, bet) for count, hand, bet in data]
    ordered = list(sorted(mapped, key=cmp_to_key(compare)))
    return sum((i + 1) * bet for i, (_, _, bet) in enumerate(ordered))


def part_b(data):
    mapped = [(hand_type(count, "J"), hand, bet) for count, hand, bet in data]
    ordered = list(sorted(mapped, key=cmp_to_key(lambda a, b: compare(a, b, True))))
    return sum((i + 1) * bet for i, (_, _, bet) in enumerate(ordered))


def compare(group_a, group_b, wild=False):
    type_a, hand_a, _ = group_a
    type_b, hand_b, _ = group_b
    if type_a == type_b:
        card_val = "J123456789TQKA" if wild else "123456789TJQKA"
        a, b = next((a, b) for a, b in zip(hand_a, hand_b) if a != b)
        return card_val.find(a) - card_val.find(b)
    return type_a - type_b


def hand_type(count: Counter, filter=None):
    jokers = count[filter]
    count = {c: count[c] for c in count if c != filter}
    dupes = max((count[c] for c in count), default=0) + jokers
    pairs = len([c for c in count if count[c] == 2])
    if dupes >= 4:
        return dupes + 1
    if dupes == 3:
        return dupes + (pairs - jokers == 1)
    return pairs + jokers


puzzle = Puzzle(2023, 7)
data = [*parse(puzzle.input_data)]
print("part A", part_a(data))
print("part B", part_b(data))
