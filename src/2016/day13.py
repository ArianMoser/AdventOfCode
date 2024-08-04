import os
import sys

INPUT_DIR = os.path.join(os.path.dirname(__file__), 'inputs')
MAGIC_NUMBER = 0

COORDS = dict()


def prepare_input_file(filename=os.path.basename(__file__).replace('.py',
                       '.txt')):
    file_path = os.path.join(INPUT_DIR, filename)
    with open(file_path, 'r') as f:
        inp = int(f.read())
    return inp

def calculate_pos(x, y):
    global MAGIC_NUMBER
    nr = x*x + 3*x + 2*x*y + y + y*y + MAGIC_NUMBER
    return sum([1 if b == '1' else 0 for b in bin(nr)[2:]]) % 2 == 0


def print_grid():
    """
    This function was used for debugging activity. It is not required to
    solve the problem
    """
    for y in range(max([c[1] for c in COORDS]) + 1):
        for x in range(max([c[0] for c in COORDS]) + 1):
            if (x, y) not in  COORDS.keys():
                print('.', end='')
            elif COORDS[(x, y)] == False:
                print('#', end='')
            else:
                print(COORDS[(x, y)], end='')
        print()


def get_neighbors(start_x, start_y, step):
    neighbors = []
    for x in range(-1, 2, 1):
        for y in range(-1, 2, 1):
            if not (x == 0 or y == 0):
                continue
            neighbor = (start_x + x, start_y + y)
            if neighbor[0] < 0 or neighbor[1] < 0:
                continue
            if neighbor not in COORDS.keys():
                if calculate_pos(*neighbor):
                    COORDS[neighbor] = step
                else:
                    COORDS[neighbor] = False
            if COORDS[neighbor]:
                neighbors.append(neighbor)
    return neighbors


def main():
    global MAGIC_NUMBER, COORDS
    if len(sys.argv) == 2:
        MAGIC_NUMBER = prepare_input_file(sys.argv[1])
    else:
        MAGIC_NUMBER = prepare_input_file()
    print(f"Received magic number {MAGIC_NUMBER}")

    start = (1, 1)
    dest = (31, 39)

    # part 1
    steps = 0
    COORDS[start] = steps

    while dest not in COORDS.keys():
        print(steps, COORDS)
        steps += 1
        for key, value in COORDS.copy().items():
            if value != steps - 1:
                continue
            _ = get_neighbors(*key, steps)

    print(f"Part 1: {COORDS[dest]}")

    # part 2
    count = 1
    for key, value in COORDS.items():
        if value and value <= 50:
            count += 1
    print(f"Part 2: {count}")


if __name__ == '__main__':
    main()
