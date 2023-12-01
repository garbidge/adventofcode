# region imports
import collections  # noqa
import copy  # noqa
import functools  # noqa
import itertools  # noqa
import math  # noqa
import operator  # noqa
import re  # noqa
from collections import Counter, defaultdict, deque  # noqa
from copy import copy, deepcopy  # noqa
from functools import reduce, cache  # noqa
from itertools import (
    product,  # noqa
    permutations,  # noqa
    combinations,  # noqa
    repeat,  # noqa
    pairwise,  # noqa
    chain,  # noqa
    accumulate,  # noqa
)
from math import (
    prod,  # noqa
    ceil,  # noqa
    floor,  # noqa
    trunc,  # noqa
    sqrt,  # noqa
    cbrt,  # noqa
    copysign,  # noqa
    comb,  # noqa
    perm,  # noqa
    factorial,  # noqa
    gcd,  # noqa
    lcm,  # noqa
    cos,  # noqa
    acos,  # noqa
    sin,  # noqa
    asin,  # noqa
    tan,  # noqa
    atan,  # noqa
    dist,  # noqa Euclidean distance
)
from re import (
    split,  # noqa
    findall,  # noqa
)
from typing import List, Any

# endregion


# region parsing
def pgrp(input: str) -> List[List[str]]:
    return [group.splitlines() for group in input.split("\n\n")]


def pgrpint(input: str) -> List[List[int]]:
    return [[int(n) for n in group] for group in pgrp(input)]


def pstrip(input: str) -> List[str]:
    return [line.strip() for line in input.splitlines()]


def pint(input: str) -> List[int]:
    return [int(n) for n in input.splitlines()]


def plint(input: str) -> List[List[int]]:
    return [ints(line) for line in input.splitlines()]


def pgridint(input: str) -> List[List[int]]:
    return [[int(n) for n in line] for line in pstrip(input)]


def preg(input: str, pattern: str) -> List[str]:
    return [flatten(re.findall(pattern, line)) for line in input.splitlines()]


# endregion

# region helpers


def ints(line: str) -> List[int]:
    return lmap(int, re.findall(r"-?\d+", line))


def lmap(func, collection: List[Any]) -> List:
    return list(map(func, collection))


def lmapsub(func, collection: List[List[Any]]) -> List:
    return lmap(lambda sub: [func(item) for item in sub], collection)


def flatten(collection: List[List[Any]]) -> List[Any]:
    return [i for x in collection for i in x]


def tuple_add(tuple_a: tuple, tuple_b: tuple) -> tuple:
    return tuple(map(lambda a, b: a + b, tuple_a, tuple_b))


# endregion

# region points and grids


def neighbrs(coordinate: tuple) -> tuple:
    zeros = tuple(itertools.repeat(0, len(coordinate)))
    directions = itertools.product(*itertools.repeat([-1, 0, 1], len(coordinate)))
    return [tuple_add(coordinate, d) for d in directions if d != zeros]


def neighbrs_diag(coordinate: tuple) -> tuple:
    directions = itertools.product(*itertools.repeat([-1, 1], len(coordinate)))
    return [tuple_add(coordinate, d) for d in directions]


def neighbrs_str8(coordinate: tuple) -> tuple:
    directions = itertools.product(*itertools.repeat([-1, 0, 1], len(coordinate)))
    return [
        tuple_add(coordinate, d)
        for d in directions
        if d.count(0) == len(coordinate) - 1
    ]


# endregion
