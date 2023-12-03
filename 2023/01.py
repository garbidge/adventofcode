from aocd.models import Puzzle
from utils import lmapsub, preg

word_lookup = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def parse_a(input):
    return lmapsub(int, preg(input, "\d"))


def parse_b(input):
    group = "|".join(word_lookup.keys()) + "|\d"
    return lmapsub(word_value, preg(input, f"(?=({group}))"))


def word_value(word):
    if word in word_lookup:
        return word_lookup[word]
    return int(word)


def get_sum(data):
    return sum(map(lambda nums: 10 * nums[0] + nums[-1], data))


puzzle = Puzzle(2023, 1)
data_a = parse_a(puzzle.input_data)
data_b = parse_b(puzzle.input_data)
print("part A", get_sum(data_a))
print("part B", get_sum(data_b))
