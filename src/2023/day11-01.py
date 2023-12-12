import os
import sys
from itertools import combinations

def main(input_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        f_content = f.read()
    galaxies = []

    for y, line in enumerate(f_content.splitlines()):
        for x, c in enumerate(line):
            if c == '#': galaxies.append((x, y))
    x_max = max([g[0] for g in galaxies])
    y_max = max([g[1] for g in galaxies])

    # x expansion
    for x in reversed(range(x_max)):
        if x in [g[0] for g in galaxies]: continue
        #galaxies = [(g[0]+1, g[1]) for g in galaxies if g[0] > x]
        for i, g in enumerate(galaxies):
            if g[0] > x: 
                galaxies[i] = (g[0]+1, g[1])

    # y expansion
    for y in reversed(range(y_max)):
        if y in [g[1] for g in galaxies]: continue
        #galaxies = [(g[0]+1, g[1]) for g in galaxies if g[0] > x]
        for i, g in enumerate(galaxies):
            if g[1] > y: galaxies[i] = (g[0], g[1]+1)

    pairs = list(combinations(galaxies, 2))
    # task 1
    res = sum([calculate_distance(*p) for p in pairs])
    print(f"Task 1: {res}")

    # task 2
    res = 0
    print(f"Task 2: {res}")

def calculate_distance(a, b):
    x_diff = abs(a[0] - b[0])
    y_diff = abs(a[1] - b[1])
    return x_diff + y_diff

if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else: 
        input_file = os.path.join(os.path.dirname(__file__), \
                                'inputs', 
                                sys.argv[0].replace("py", "txt"))
        main(input_file)
