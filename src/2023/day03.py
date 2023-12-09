import os
import sys
import re
import math


def search_for_symbols(coords, x, y, length):
    for yc in range(y-1, y+2):
        for xc in range(x-1, x+length+1):
            try:
                if xc == -1 or yc == -1: raise IndexError
                #print(xc, yc, coords[yc][xc])
                if coords[yc][xc] not in list('0123456789.'):
                    return True
            except IndexError:
                pass


def main(input_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        f_content = f.read()
    lines = f_content.splitlines()

    # create grid
    coords = []
    for y, line in enumerate(lines):
        coords.append([])
        for x, c in enumerate(line):
            coords[y].append(c)

    # task 1
    res = 0
    for y, line in enumerate(lines):
        matches = list(re.finditer('[0-9]+', line))
        for mat in matches:
            length = mat.end() - mat.start()
            if search_for_symbols(coords, mat.start(), y, length):
                res += int(mat.group())
    print(f"Task 1: {res}")

    # task 2
    res = 0
    for y, line in enumerate(lines):
        asteriks = list(re.finditer(r'\*', line))
        for asterik in asteriks:
            res += check_neighbors(asterik.start(), y, lines)

    print(f"Task 2: {res}")


def check_neighbors(x, y, lines):
    numbers = []
    for y in range(y-1, y+2):
        matches = list(re.finditer('[0-9]+', lines[y]))
        for mat in matches:
            if any(xtest in range(x-1, x+2) for xtest in range(mat.start(), mat.end())): 
                numbers.append(int(mat.group()))
    if len(numbers) > 1:
        return math.prod(numbers)
    return 0

if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        input_file = os.path.join(os.path.dirname(__file__), \
                                    'inputs', 
                                    sys.argv[0].replace("py", "txt"))
        main(input_file)
