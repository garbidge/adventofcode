# region imports
import collections  # noqa
import copy
import functools  # noqa
import itertools  # noqa
import math  # noqa
import operator  # noqa
import re  # noqa
from collections import Counter, defaultdict, deque  # noqa
from copy import copy, deepcopy  # noqa
from functools import reduce, cache  # noqa
from itertools import (  # noqa
    product,
    permutations,
    combinations,
    repeat,
    pairwise,
    chain,
    accumulate,
)
from math import (  # noqa
    prod,
    ceil,
    floor,
    trunc,
    sqrt,
    cbrt,
    copysign,
    comb,
    perm,
    factorial,
    gcd,
    lcm,
    cos,
    acos,
    sin,
    asin,
    tan,
    atan,
    dist,  # Euclidean distance
)
from re import (  # noqa
    split,
    findall,
)
from typing import Callable, DefaultDict, List, Any

# endregion

# region parsing

def pstrip(input: str, chars: str | None = None) -> List[str]:
    return [line.strip(chars) for line in input.splitlines()]

def pint(input: str) -> List[int]:
    return [int(n) for n in input.splitlines()]

def plint(input: str) -> List[List[int]]:
    return [ints(line) for line in input.splitlines()]

def pgrp(input: str) -> List[List[str]]:
    return [group.splitlines() for group in input.split("\n\n")]

def pgrpint(input: str) -> List[List[int]]:
    return [[int(n) for n in group] for group in pgrp(input)]

def pgrpints(input: str) -> List[List[List[int]]]:
    return [[ints(line) for line in group] for group in pgrp(input)]

def pgridint(input: str) -> List[List[int]]:
    return [[int(n) for n in line] for line in input.splitlines()]

def pgriddict(input: str, defaultFunc: Callable, valueFunc: Callable = lambda x: x):
    ddict = defaultdict(defaultFunc)
    lines = input.splitlines()
    for row in range(len(lines)):
        for col in range(len(lines[row])):
            ddict[(col, row)] = valueFunc(lines[row][col])
    return ddict

def preg(input: str, pattern: str) -> List[List[Any]]:
    return [re.findall(pattern, line) for line in input.splitlines()]

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

def tuple_sub(tuple_a: tuple, tuple_b: tuple) -> tuple:
    return tuple(map(lambda a, b: a - b, tuple_a, tuple_b))

def print_ddict(ddict: DefaultDict[tuple, str]):
    for y in range(max(y for (x, y) in ddict.keys()) + 1):
        for x in range(max(x for (x, y) in ddict.keys()) + 1):
            print(ddict[(x, y)], end="")
        print()

def transpose(iterable):
    return lmap(list, zip(*iterable))

def transpose_str(collection: List[str]):
    return [''.join(collection[r][c] for r in range(len(collection))) for c in range(len(collection[0]))]

# endregion

# region points and grids

def coord_dirs(dimensions: int):
    return list(itertools.product((-1, 0, 1), repeat=dimensions))

def coord_dirs_diag(dimensions: int):
    return list(itertools.product((-1, 1), repeat=dimensions))

def coord_dirs_str8(dimensions: int):
    return list(
        d
        for d in itertools.product((-1, 0, 1), repeat=dimensions)
        if d.count(0) == dimensions - 1
    )

def neighbrs(coordinate: tuple) -> tuple:
    zeros = tuple(itertools.repeat(0, len(coordinate)))
    return [tuple_add(coordinate, d) for d in coord_dirs(len(coordinate)) if d != zeros]

def neighbrs_diag(coordinate: tuple) -> tuple:
    return [tuple_add(coordinate, d) for d in coord_dirs_diag(len(coordinate))]

def neighbrs_str8(coordinate: tuple) -> tuple:
    return [tuple_add(coordinate, d) for d in coord_dirs_str8(len(coordinate))]

def coord_yield_dir(coord: tuple, direction: tuple, condition: Callable[[tuple], bool]):
    coord = tuple_add(coord, direction)
    while condition(coord):
        yield coord
        coord = tuple_add(coord, direction)

# endregion
