import sys
import os
import parse


def main():
    file_name = f"inputs/{sys.argv[0].replace('py', 'txt')}" if len(sys.argv) == 1 else sys.argv[1]
    if not os.path.isfile(file_name):
        raise Exception(f'{file_name} is not a valid file')
    print(f"Challenge {sys.argv[0].split('.')[0].capitalize()}: \n")
    print("**************************")

    lines = []
    points = set()
    points_overlap = set()
    # read file
    with open(file_name, 'r') as f:
        for line in f.read().splitlines():
            parsed = parse.parse('{x1},{y1} -> {x2},{y2}', line).named
            (x1, y1, x2, y2) = get_attributes(**parsed)
            lines.append((x1, y1, x2, y2))

    for i, el in enumerate(lines):
        if el[2] != el[0] and el[3] == el[1]:
            for x in range(abs(el[2] - el[0]) + 1):
                point = (min(el[2], el[0]) + x, el[1])
                if point not in points: points.add(point)
                else: points_overlap.add(point)
        elif el[3] != el[1] and el[2] == el[0]:
            for y in range(abs(el[3] - el[1]) + 1):
                point = (el[0], min(el[3], el[1]) + y)
                if point not in points: points.add(point)
                else: points_overlap.add(point)
    print(f'Result Task1: {len(points_overlap)}')
            
    for i, el in enumerate(lines):
        if el[2] != el[0] and el[3] != el[1]: 
            for dist in range(abs(el[3] - el[1]) + 1):
                point = (el[0] + dist*(el[2]-el[0])/abs(el[2]-el[0]), el[1] + dist*(el[3]-el[1])/abs(el[3]-el[1]))
                if point not in points: points.add(point)
                else: points_overlap.add(point)
    print(f'Result Task2: {len(points_overlap)}')
    

def get_attributes(x1, y1, x2, y2):
    return (int(x1),int(y1),int(x2),int(y2))

if __name__ == "__main__":
    main()
