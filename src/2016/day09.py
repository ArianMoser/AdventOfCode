import os
import sys
import re

INPUT_DIR = os.path.join(os.path.dirname(__file__), 'inputs')
RE_MARKER = r'\((\d+x\d+)\)'


def prepare_input_file(filename=os.path.basename(__file__).replace('.py',
                       '.txt')):
    file_path = os.path.join(INPUT_DIR, filename)
    with open(file_path, 'r') as f:
        lines = f.read().splitlines()
    return lines[0]


def main():
    if len(sys.argv) == 2:
        inp = prepare_input_file(sys.argv[1])
    else:
        inp = prepare_input_file()
    print(f"Received {len(inp)} chars")

    # part 1
    part1 = ''
    i = 0

    while i < len(inp):
        marker_check = re.search(RE_MARKER, inp[i:])
        if marker_check is not None and marker_check.span()[0] == 0:
            chars, repeat = list(map(int, marker_check.groups()[0].split('x')))
            part1 += \
                inp[i+marker_check.span()[1]:i+marker_check.span()[1]+chars] \
                * repeat
            i += marker_check.span()[1] + chars - 1
        else:
            part1 += inp[i]
        i += 1

    print(f"Part 1: {len(part1)}")

    # part 2
    part2 = decompress(inp)
    print(f"Part 2: {part2}")


def decompress(inp):
    i = 0
    res = 0
    while i < len(inp):
        marker_check = re.search(RE_MARKER, inp[i:])
        if marker_check is None:
            res += len(inp)
            break
        elif marker_check.span()[0] == 0:
            chars, repeat = list(map(int, marker_check.groups()[0].split('x')))
            res += decompress(inp[i+marker_check.span()[1]: \
                           i+marker_check.span()[1]+chars]) * repeat
            i += marker_check.span()[1] + chars - 1
        else:
            res += 1
        i += 1
    return res


if __name__ == '__main__':
    main()
