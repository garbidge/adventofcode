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
from typing import Callable, DefaultDict, Generator, Iterable, List, Any, Sequence

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

def pgriddict(input: str, defaultFunc: Callable[[str], Any]) -> DefaultDict[tuple[int, int], Any]:
    ddict = defaultdict(defaultFunc)
    lines = input.splitlines()
    for row in range(len(lines)):
        for col in range(len(lines[row])):
            ddict[(col, row)] = defaultFunc(lines[row][col])
    return ddict

def preg(input: str, pattern: str) -> List[List[Any]]:
    return [re.findall(pattern, line) for line in input.splitlines()]

# endregion

# region helpers

def ints(line: str) -> List[int]:
    return lmap(int, re.findall(r"-?\d+", line))

def lmap(func: Callable, collection: List[Any]) -> List:
    return list(map(func, collection))

def lmapsub(func: Callable, collection: List[List[Any]]) -> List:
    return lmap(lambda sub: [func(item) for item in sub], collection)

def flatten(collection: List[List[Any]]) -> List[Any]:
    return [i for x in collection for i in x]

def tuple_add(tuple_a: tuple, tuple_b: tuple) -> tuple:
    return tuple(a + b for a,b in zip(tuple_a, tuple_b))

def tuple_sub(tuple_a: tuple, tuple_b: tuple) -> tuple:
    return tuple(a - b for a,b in zip(tuple_a, tuple_b))

def print_ddict(ddict: DefaultDict[tuple, str]) -> None:
    min_x, min_y = mins(ddict)
    max_x, max_y = maxes(ddict)
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            print(ddict[(x, y)], end="")
        print()

def transpose(iterable: Iterable[Sequence[Any]]) -> List[List[Any]]:
    return lmap(list, zip(*iterable))

def transpose_str(collection: List[str]) -> List[str]:
    return [''.join(collection[r][c] for r in range(len(collection))) for c in range(len(collection[0]))]

def maxes(iterable: Iterable[tuple]) -> tuple:
    listified = [*iterable]
    return tuple(max(tup[i] for tup in listified) for i in range(len(listified[0])))

def mins(iterable: Iterable[tuple]) -> tuple:
    listified = [*iterable]
    return tuple(min(tup[i] for tup in listified) for i in range(len(listified[0])))

def chunks(collection: Sequence[Any], size: int) -> Generator[Sequence[Any], None, None]:
    for i in range(0, len(collection), size):
        yield collection[i:i+size]

def digits(number: int) -> int:
    s = str(number)
    return len(s) - (1 if number < 0 else 0)

def sign(x: int) -> int:
    return (x > 0) - (x < 0)

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# endregion

# region points and grids

def coord_dirs(dimensions: int) -> List[tuple]:
    return list(itertools.product((-1, 0, 1), repeat=dimensions))

def coord_dirs_diag(dimensions: int) -> List[tuple]:
    return list(itertools.product((-1, 1), repeat=dimensions))

def coord_dirs_str8(dimensions: int) -> List[tuple]:
    return list(
        d
        for d in itertools.product((-1, 0, 1), repeat=dimensions)
        if d.count(0) == dimensions - 1
    )

def neighbrs(coordinate: tuple) -> List[tuple]:
    zeros = tuple(itertools.repeat(0, len(coordinate)))
    return [tuple_add(coordinate, d) for d in coord_dirs(len(coordinate)) if d != zeros]

def neighbrs_diag(coordinate: tuple) -> List[tuple]:
    return [tuple_add(coordinate, d) for d in coord_dirs_diag(len(coordinate))]

def neighbrs_str8(coordinate: tuple) -> List[tuple]:
    return [tuple_add(coordinate, d) for d in coord_dirs_str8(len(coordinate))]

def coord_yield_dir(coord: tuple, direction: tuple, condition: Callable[[tuple], bool] = lambda _: True) -> Generator[tuple, None, None]:
    coord = tuple_add(coord, direction)
    while condition(coord):
        yield coord
        coord = tuple_add(coord, direction)

# endregion
