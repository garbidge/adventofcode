from collections import defaultdict, deque
from aocd.models import Puzzle
from utils import flatten

OPERATIONS = {
    'AND': lambda a,b: a & b,
    'OR': lambda a,b: a | b,
    'XOR': lambda a,b: a ^ b,   
}

def parse(input):
    a, b = input.split('\n\n')
    wires = {wire: value == '1' for wire, value in (line.split(': ') for line in a.splitlines())}
    gates = [(gate.split(), output) for gate, output in (line.split(' -> ') for line in b.splitlines())]
    return wires, gates

def part_a(wires, gates):
    q = deque(gates)
    while q:
        (a,op,b),output = q.popleft()
        if a in wires and b in wires: wires[output] = OPERATIONS[op](wires[a], wires[b])
        else: q.append(((a,op,b),output))
    zvals = sorted(((k,v) for k,v in wires.items() if k.startswith('z')), reverse=True)
    return int(''.join(str(int(v)) for k,v in zvals), 2)

def part_b(gates):
    pairs, num_z = [], sum(v.startswith('z') for _,v in gates)
    while len(pairs) < 4:
        carry = ''
        lookup = {output: (a,op,b) for (a,op,b),output in gates}
        reverse_lookup = defaultdict(str, {frozenset(v): k for k,v in lookup.items()})
        for i in range(num_z):
            xi, yi, zi = f'x{i:02}', f'y{i:02}', f'z{i:02}'
            if i == 0:
                adder = reverse_lookup[frozenset(('x00','XOR','y00'))]
                carry = reverse_lookup[frozenset(('x00','AND','y00'))]
            else:
                bit = reverse_lookup[frozenset((xi,'XOR',yi))]
                adder = reverse_lookup[frozenset((bit,'XOR',carry))]
                if adder:
                    c1 = reverse_lookup[frozenset((xi,'AND',yi))]
                    c2 = reverse_lookup[frozenset((bit,'AND',carry))]
                    carry = reverse_lookup[frozenset((c1,'OR',c2))]
                else:
                    a,op,b = lookup[zi]
                    expected = next(n for n in (a,b) if n != carry)
                    swap(pairs, gates, bit, expected)
                    break
            if adder != zi:
                swap(pairs, gates, adder, zi)
                break
    return ','.join(sorted(flatten(pairs)))

def swap(pairs, gates, a, b):
    pairs.append((a,b))
    for i,(x,n) in enumerate(gates):
        if n == a: gates[i] = (x,b)
        elif n == b: gates[i] = (x,a)

puzzle = Puzzle(2024, 24)
wires,gates = parse(puzzle.input_data)
print("part A", part_a(wires, gates))
print("part B", part_b(gates))
