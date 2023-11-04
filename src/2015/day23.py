import os
import sys
from dataclasses import dataclass

@dataclass
class Instruction:
    name: str
    args: []

    def calculate(self, registers, pos):
        if self.name == 'jmp':
            pos += int(self.args[0])
        else:
            if self.args[0] not in registers.keys(): registers[self.args[0]] = 0
            if self.name == 'hlf':
                registers[self.args[0]] /= 2
                pos += 1 
            if self.name == 'tpl':
                registers[self.args[0]] *= 3
                pos += 1 
            if self.name == 'inc':
                registers[self.args[0]] += 1
                pos += 1 
            if self.name == 'jie':
                if registers[self.args[0]] %2 == 0: pos += int(self.args[1])
                else: pos += 1
            if self.name == 'jio':
                if registers[self.args[0]] == 1: pos += int(self.args[1])
                else: pos += 1
        return (registers, pos)


def main():
    input_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'inputs')
    input_file = os.path.join(input_dir, 'day23.txt')
    with open(input_file, 'r') as f:
        content = f.read()
    lines = content.split('\n')[:-1]

    instr = []
    for line in lines:
        comm = line.split(' ')[0]
        args = ''.join(line.split(' ')[1:]).split(',')
        instr.append(Instruction(comm, args))

    registers = dict()
    pos = 0

    try:
        while True:
            registers, pos = instr[pos].calculate(registers, pos)
    except IndexError:
        pass
    print(f'Task 1: {registers["b"]}')
        
    registers = dict()
    registers['a'] = 1
    pos = 0

    try:
        while True:
            registers, pos = instr[pos].calculate(registers, pos)
    except IndexError:
        pass
    print(f'Task 2: {registers["b"]}')


if __name__ == '__main__':
    main()
