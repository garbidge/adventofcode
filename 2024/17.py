from aocd.models import Puzzle
from utils import flatten, plint

def parse(input):
    registers, program = input.split('\n\n')
    return flatten(plint(registers)), flatten(plint(program))

def part_a(registers, program):
    return ','.join(map(str, run(registers, program)))

def part_b(registers, program):
    total = 0
    for n in reversed(program):
        total <<= 3
        registers[0] = total
        result = run(registers, program)
        while result[0] != n:
            total += 1
            registers[0] = total
            result = run(registers, program)
    return total

def run(registers, program):
    reg = [n for n in registers]
    output = []
    pointer = 0
    while pointer < len(program):
        instr, operand = program[pointer], program[pointer+1]
        if instr == 0: reg[0] = int(reg[0] / pow(2, combo(reg, operand)))
        elif instr == 1: reg[1] = reg[1] ^ operand
        elif instr == 2: reg[1] = combo(reg, operand) % 8
        elif instr == 3:
            if reg[0] != 0:
                pointer = operand - 2
        elif instr == 4: reg[1] = reg[1] ^ reg[2]
        elif instr == 5:
            output.append(combo(reg, operand) % 8)
        elif instr == 6: reg[1] = int(reg[0] / pow(2, combo(reg, operand)))
        elif instr == 7: reg[2] = int(reg[0] / pow(2, combo(reg, operand)))
        pointer += 2
    return output

def combo(registers, n):
    if n <= 3: return n
    return registers[n-4]

puzzle = Puzzle(2024, 17)
data = parse(puzzle.input_data)
print("part A", part_a(*data))
print("part B", part_b(*data))
