from aocd.models import Puzzle
from utils import lmap
import sympy

def parse(input):
    return lmap(parseline, input.splitlines())

def parseline(line):
    return [lmap(int, part.split(', ')) for part in line.split(' @ ')]

def part_a(data):
    count = 0
    lower = 200000000000000
    upper = 400000000000000
    lines = [slope_intercept(x, y, x+dx, y+dy) for [[x,y,_],[dx,dy,_]] in data]
    pairs = ((L1, L2) for i,L1 in enumerate(lines) for L2 in lines[i+1:])
    for L1, L2 in pairs:
        if (xy := intersection(L1, L2)) != None and all(lower <= c <= upper for c in xy):
            count += 1
    return count

def slope_intercept(x1,y1,x2,y2):
    # slope-intercept: y = mx + c
    m = (y2 - y1) / (x2 - x1)
    c = y1 - (m * x1)
    return (((x1,y1),(x2,y2), m, c))

def intersection(L1, L2):
    # y = mx + c
    # mx -y + c = 0
    (x1_a, y1_a),(x2_a, y2_a), m1, c1 = L1
    (x1_b, y1_b),(x2_b, y2_b), m2, c2 = L2
    D = m2 - m1
    if D != 0:
        Dx = c1 - c2
        Dy = (c1 * m2) - (c2 * m1)
        x, y = (Dx / D), (Dy / D)
        if not (inpast(x1_a, x2_a, x) or inpast(x1_b, x2_b, x)):
            return x,y

def inpast(x1,x2,x):
    return abs(x - x2) >= abs(x - x1)

def part_b(data):
    times = [*sympy.symbols('t1 t2 t3')]
    x, y, z, vx, vy, vz = sympy.symbols('x y z vx vy vz')
    equations = []
    for i, [[px, py, pz],[dx, dy, dz]] in enumerate(data[:3]):
        equations.append(sympy.Eq(px + dx * times[i], x + vx * times[i]))
        equations.append(sympy.Eq(py + dy * times[i], y + vy * times[i]))
        equations.append(sympy.Eq(pz + dz * times[i], z + vz * times[i]))
    variables = sympy.solve(equations, (x,y,z,vx,vy,vz,*times), dict=True)[0]
    return variables[x] + variables[y] + variables[z]

puzzle = Puzzle(2023, 24)
data = parse(puzzle.input_data)
print("part A", part_a(data))
print("part B", part_b(data))
