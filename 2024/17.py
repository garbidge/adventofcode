from aocd.models import Puzzle
from utils import flatten, plint

def parse(input):
    registers, program = input.split('\n\n')
    return flatten(plint(registers)), flatten(plint(program))

def part_a(registers, program):
    return ','.join(map(str, run(registers, program)))

def part_b(registers, program):
    total = 0
    for _ in range(len(program)):
        total <<= 3
        registers[0] = total
        while not all(a == b for a,b in zip(reversed(run(registers, program)), reversed(program))):
            registers[0] = total = total + 1
    return total

def run(registers, program):
    reg = [n for n in registers]
    pointer, output = 0, []
    while pointer < len(program):
        instr, operand = program[pointer], program[pointer+1]
        match instr:
            case 0: reg[0] //= 2 ** combo(reg, operand)
            case 1: reg[1] ^= operand
            case 2: reg[1] = combo(reg, operand) % 8
            case 3: 
                if reg[0] != 0: pointer = operand - 2
            case 4: reg[1] ^= reg[2]
            case 5: output.append(combo(reg, operand) % 8)
            case 6: reg[1] = reg[0] // 2 ** combo(reg, operand)
            case 7: reg[2] = reg[0] // 2 ** combo(reg, operand)
        pointer += 2
    return output

def combo(registers, n):
    return n if n <= 3 else registers[n-4]

puzzle = Puzzle(2024, 17)
data = parse(puzzle.input_data)
print("part A", part_a(*data))
print("part B", part_b(*data))
