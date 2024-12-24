from collections import defaultdict
from aocd.models import Puzzle

def parse(input):
    a,b = input.split('\n\n')
    wires = defaultdict(bool)
    for wire,value in (line.split(': ') for line in a.splitlines()):
        wires[wire] = value == '1'
    gates = []
    for gate,output in (line.split(' -> ') for line in b.splitlines()):
        parts = gate.split()
        gates.append((parts, output))
    return wires, gates

def part_a(wires, gates):
    changed = True
    while changed:
        changed = False
        for (a,op,b),output in gates:
            if a in wires and b in wires:
                result = None if output not in wires else wires[output]
                if op == 'AND':
                    result = wires[a] & wires[b]
                elif op == 'OR':
                    result = wires[a] | wires[b]
                elif op == 'XOR':
                    result = wires[a] ^ wires[b]
                if output not in wires or wires[output] != result:
                    wires[output] = result
                    changed = True
    keys = reversed(sorted(k for k in wires if k.startswith('z')))
    vals = [wires[k] for k in keys]
    joined = ''.join('1' if v else '0' for v in vals)
    intval = int(joined, 2)
    return intval

def part_b(gates):
    num_z = sum(v.startswith('z') for _,v in gates)
    pairs = []
    bit,adder,c1,c2,carry = ['___' for _ in range(5)]
    while len(pairs) < 4:
        lookup = {output: (a,op,b) for (a,op,b),output in gates}
        reverse_lookup = defaultdict(str, {frozenset((a,op,b)): output for (a,op,b),output in gates})
        for i in range(num_z):
            if i == 0:
                adder = reverse_lookup[frozenset(('x00','XOR','y00'))]
                carry = reverse_lookup[frozenset(('x00','AND','y00'))]
            else:
                bit = reverse_lookup[frozenset((f'x{i:02}','XOR',f'y{i:02}'))]
                adder = reverse_lookup[frozenset((bit,'XOR',carry))]
                if adder:
                    c1 = reverse_lookup[frozenset((f'x{i:02}','AND',f'y{i:02}'))]
                    c2 = reverse_lookup[frozenset((bit,'AND',carry))]
                    carry = reverse_lookup[frozenset((c1,'OR',c2))]
            if not adder:
                a,op,b = lookup[f'z{i:02}']
                if frozenset((a,'XOR',carry)) in reverse_lookup:
                    pairs.append((bit, a))
                    swap(gates, bit, a)
                    break
                if frozenset((b,'XOR',carry)) in reverse_lookup:
                    pairs.append((bit, b))
                    swap(gates, bit, b)
                    break
            elif adder != f'z{i:02}':
                pairs.append((adder, f'z{i:02}'))
                swap(gates, adder, f'z{i:02}')
                break
    return ','.join(list(sorted([x for y in pairs for x in y])))

def swap(gates, a, b):
    for i,(x,n) in enumerate(gates):
        if n == a: gates[i] = (x,b)
        elif n == b: gates[i] = (x,a)

puzzle = Puzzle(2024, 24)
wires,gates = parse(puzzle.input_data)
print("part A", part_a(wires, gates))
print("part B", part_b(gates))
