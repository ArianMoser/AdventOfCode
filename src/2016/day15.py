import os
import sys
import re

INPUT_DIR = os.path.join(os.path.dirname(__file__), 'inputs')
RE_LINE = r'Disc #(\d+) has (\d+) positions; at time=(\d+), it is at position (\d+).'


def prepare_input_file(filename=os.path.basename(__file__).replace('.py',
                       '.txt')):
    file_path = os.path.join(INPUT_DIR, filename)
    with open(file_path, 'r') as f:
        lines = f.read().splitlines()
    discs = []
    for line in lines:
        discs.append(list(map(int, re.search(RE_LINE, line).groups())))
    return discs


def main():
    if len(sys.argv) == 2:
        discs = prepare_input_file(sys.argv[1])
    else:
        discs = prepare_input_file()
    print(f"Received {len(discs)} discs")

    # part 1
    start = 0
    part1_finished = False
    while not part1_finished:
        for step, disc in enumerate(discs):
            if (disc[0] + disc[3] - disc[2] + start) % disc[1] == 0:
                if step == len(discs)-1:
                    part1_finished = True
                continue
            break
        start += 1
    print(f"Part 1: {start - 1}")

    # part 2
    start = 0
    part2_finished = False
    discs.append([discs[-1][0]+1, 11, 0, 0])

    while not part2_finished:
        for step, disc in enumerate(discs):
            if (disc[0] + disc[3] - disc[2] + start) % disc[1] == 0:
                if step == len(discs)-1:
                    part2_finished = True
                continue
            break
        start += 1
    print(f"Part 2: {start - 1}")


if __name__ == '__main__':
    main()
