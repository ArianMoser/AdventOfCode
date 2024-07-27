import os
import sys
from itertools import combinations, permutations

INPUT_DIR = os.path.join(os.path.dirname(__file__), 'inputs')


def prepare_input_file(filename=os.path.basename(__file__).replace('.py',
                       '.txt')):
    file_path = os.path.join(INPUT_DIR, filename)
    with open(file_path, 'r') as f:
        lines = f.read().splitlines()
    # get array of numbers
    output = []
    for line in lines:
        output.append(list(map(int, line.split())))
    return output


# both versions work but this is quite to complex
def check_triangle_complex(triangle):
    for perm in (list(permutations(triangle))):
        if sum(perm[:2]) <= perm[2]:
            return False
    return True


def check_triangle(triangle):
    triangle.sort()
    if sum(triangle[:2]) > triangle[2]:
        return True
    return False


def main():
    if len(sys.argv) == 2:
        lines = prepare_input_file(sys.argv[1])
    else:
        lines = prepare_input_file()
    print(f"Received {len(lines)} lines")

    # part 1
    part1 = 0
    for line in lines:
        if check_triangle(line):
            part1 += 1

    print(f"Part 1: {part1}")

    # part 2



if __name__ == '__main__':
    main()
