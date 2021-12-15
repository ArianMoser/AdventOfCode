import sys
import os

max_y = 0
max_x = 0

def main():
    file_name = f"inputs/{sys.argv[0].replace('py', 'txt')}" if len(sys.argv) == 1 else sys.argv[1]
    if not os.path.isfile(file_name):
        raise Exception(f'{file_name} is not a valid file')
    print(f"Challenge {sys.argv[0].split('.')[0].capitalize()}: \n")
    print("**************************")

    # read file
    with open(file_name, 'r') as f:
        lines = f.read().splitlines()

    points = dict()
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            points[(x, y)] = int(c)

    global max_x, max_y
    max_x = max(p[0] for p in points.keys())
    max_y = max(p[1] for p in points.keys())

    low_points = [(x, y) for (x, y) in points.keys() if all(True if points[(x, y)] < points[(x+x_d, y+y_d)] else False for (x_d, y_d) in [(-1, 0),(1, 0),(0, -1),(0, 1)] if 0<=x+x_d<=max_x and 0<=y+y_d<=max_y)]

    # task 1
    print(f'Result Task1: {sum(1+points[(x, y)] for (x, y) in low_points)}')

    # calculate basin
    basins = sorted([ len(set(find_basin_neighbours(*l, points))) for l in low_points ])
    for l in low_points:
        print(set(find_basin_neighbours(*l, points)))
        sys.stdin.read(1)
    print(basins)
    print(f'Result Task2: {basins[-1]*basins[-2]*basins[-3]}')


def find_basin_neighbours(x, y, points):
    global max_x, max_y
    if points[(x,y)] >= 8:
        return [(x, y)]
    #return [(x, y), *[find_basin_neighbours(x+x_d, y+y_d, points) for (x_d, y_d) in [(-1, 0), (1, 0), (0, -1), (0, 1)] if 0 <= x + x_d<= max_x and 0 <= y + y_d <= max_y and points[(x,y)]+1 == points[(x+x_d, y+y_d)]]]  
    res = [(x, y)]
    for (x_d, y_d) in  [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if 0 <= x + x_d<= max_x and 0 <= y + y_d <= max_y and points[(x,y)]+1 == points[(x+x_d, y+y_d)]:
            for f in find_basin_neighbours(x+x_d, y+y_d, points): res.append(f)
    return res
            

if __name__ == "__main__":
    main()
