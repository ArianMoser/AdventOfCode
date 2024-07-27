import os
import sys
from collections import Counter

INPUT_DIR = os.path.join(os.path.dirname(__file__), 'inputs')


def prepare_input_file(filename=os.path.basename(__file__).replace('.py',
                       '.txt')):
    file_path = os.path.join(INPUT_DIR, filename)
    with open(file_path, 'r') as f:
        lines = f.read().splitlines()
    columns = []
    for i in range(len(lines[0])):
        columns.append([line[i] for line in lines])
    return columns


def main():
    if len(sys.argv) == 2:
        columns = prepare_input_file(sys.argv[1])
    else:
        columns = prepare_input_file()
    print(f"Received {len(columns)} columns")

    # part 1
    part1 = ''

    for column in columns:
        part1 += Counter(sorted(column)).most_common()[0][0]

    print(f"Part 1: {part1}")

    # part 2
    part2 = ''

    for column in columns:
        part2 += Counter(sorted(column)).most_common()[-1][0]

    print(f"Part 2: {part2}")


if __name__ == '__main__':
    main()
