import os
import sys
import re
import math

colours = ['red', 'blue', 'green']

def task1(cube_sets):
    cubes = {}
    for cube_set in cube_sets:
        for colour in colours:
            reg = f'\s([0-9]+)\s{colour}'
            cubes[colour] = sum(map(int, re.findall(reg, cube_set)))
        if cubes['red'] > 12 or cubes['green'] > 13 or cubes['blue'] > 14:
            return False
    return True

def task2(line):
    colour_counter = {}
    for colour in colours:
        reg = f'\s([0-9]+)\s{colour}'
        colour_counter[colour] = max(map(int, re.findall(reg, line)))
    return colour_counter


def main(input_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        f_content = f.read()
    lines = f_content.splitlines()

    # task 1
    res = 0
    for i, line in enumerate(lines):
        #game = line.split(':')[1]
        if task1(line.split(';')):
            res += (i+1)

    print(f"Task 1: {res}")

    # task 2
    res = 0
    for _, line in enumerate(lines):
        colours = task2(line)
        res += math.prod(colours.values())
    print(f"Task 2: {res}")

if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        input_file = os.path.join(os.path.dirname(__file__), \
                                'inputs', 
                                sys.argv[0].replace("py", "txt"))
        main(input_file)
