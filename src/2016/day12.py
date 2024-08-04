import os
import sys
import re

INPUT_DIR = os.path.join(os.path.dirname(__file__), 'inputs')
RE_COPY = r'cpy (\w+) (\w+)'
RE_INC = r'inc (\w+)'
RE_DEC = r'dec (\w+)'
RE_JNZ = r'jnz (\w+) ([\w-]+)'


def prepare_input_file(filename=os.path.basename(__file__).replace('.py',
                       '.txt')):
    file_path = os.path.join(INPUT_DIR, filename)
    with open(file_path, 'r') as f:
        lines = f.read().splitlines()
    return lines


def main():
    if len(sys.argv) == 2:
        lines = prepare_input_file(sys.argv[1])
    else:
        lines = prepare_input_file()
    print(f"Received {len(lines)} lines")

    # part 1
    REGISTERS = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
    i = 0
    while True:
        line = lines[i]
        if re.match(RE_COPY, line):
            src, dest = re.search(RE_COPY, line).groups()
            if src in REGISTERS.keys():
                REGISTERS[dest] = REGISTERS[src]
            else:
                REGISTERS[dest] = int(src)
        elif re.match(RE_INC, line):
            dest = re.search(RE_INC, line).groups()[0]
            REGISTERS[dest] += 1
        elif re.match(RE_DEC, line):
            dest = re.search(RE_DEC, line).groups()[0]
            REGISTERS[dest] -= 1
        elif re.match(RE_JNZ, line):
            check, jmp = re.search(RE_JNZ, line).groups()
            if check in REGISTERS.keys():
                if REGISTERS[check] != 0:
                    i += int(jmp) - 1
            elif int(check) != 0:
                i += int(jmp) - 1
        else:
            print(f"Could not parse line: '{line}'")
        i += 1
        if i > len(lines)-1:
            break

    print(f"Part 1: {REGISTERS['a']}")

    # part 2
    REGISTERS = {'a': 0, 'b': 0, 'c': 1, 'd': 0}
    i = 0
    while True:
        line = lines[i]
        if re.match(RE_COPY, line):
            src, dest = re.search(RE_COPY, line).groups()
            if src in REGISTERS.keys():
                REGISTERS[dest] = REGISTERS[src]
            else:
                REGISTERS[dest] = int(src)
        elif re.match(RE_INC, line):
            dest = re.search(RE_INC, line).groups()[0]
            REGISTERS[dest] += 1
        elif re.match(RE_DEC, line):
            dest = re.search(RE_DEC, line).groups()[0]
            REGISTERS[dest] -= 1
        elif re.match(RE_JNZ, line):
            check, jmp = re.search(RE_JNZ, line).groups()
            if check in REGISTERS.keys():
                if REGISTERS[check] != 0:
                    i += int(jmp) - 1
            elif int(check) != 0:
                i += int(jmp) - 1
        else:
            print(f"Could not parse line: '{line}'")
        i += 1
        if i > len(lines)-1:
            break

    print(f"Part 2: {REGISTERS['a']}")


if __name__ == '__main__':
    main()
