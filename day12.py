# Day 12: Leonardo's Monorail

from enum import Enum

class Instruction(Enum):
    cpy = 0
    inc = 1
    dec = 2
    jnz = 3

def main():

    commands = []
    reg = [0 for x in range(0, 4)]

    with open('day12.txt') as f:
        for line in f:
            words = line.strip().split()
            if words[0] == 'cpy':
                commands.append((Instruction.cpy, parse_operand(words[1]), parse_operand(words[2])))
            elif words[0] == 'inc':
                commands.append((Instruction.inc, words[1]))
            elif words[0] == 'dec':
                commands.append((Instruction.dec, words[1]))
            elif words[0] == 'jnz':
                commands.append((Instruction.jnz, parse_operand(words[1]), parse_operand(words[2])))

    next_command = 0
    while next_command < len(commands):
        next_command += execute(commands, reg, next_command)

    print("Part 1: {}".format(reg[0]))

    reg = [0 for x in range(0, 4)]
    reg[2] = 1

    next_command = 0
    while next_command < len(commands):
        next_command += execute(commands, reg, next_command)

    print("Part 2: {}".format(reg[0]))

def execute(commands, reg, idx):
    command = commands[idx]
    if command[0] == Instruction.cpy:
        reg[reg_to_idx(command[2])] = value_from_operand(command[1], reg)
        return 1
    elif command[0] == Instruction.inc:
        reg[reg_to_idx(command[1])] += 1
        return 1
    elif command[0] == Instruction.dec:
        reg[reg_to_idx(command[1])] -= 1
        return 1
    else:
        if value_from_operand(command[1], reg) != 0:
            return command[2]
        else:
            return 1

def parse_operand(operand):
    try:
        n = int(operand)
        return n
    except ValueError:
        return operand

def value_from_operand(operand, registers):
    if isinstance(operand, int):
        return operand
    else:
        return read_register(operand, registers)

def read_register(operand, registers):
    return registers[reg_to_idx(operand)]

def reg_to_idx(reg):
    return ord(reg) - ord('a')

if __name__ == "__main__":
    main()
