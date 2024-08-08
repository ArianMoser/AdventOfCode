import os
import sys
import hashlib

INPUT_DIR = os.path.join(os.path.dirname(__file__), 'inputs')
DIRECTION_MAPPER = {
    (-1, 0): 'L',
    (1, 0):  'R',
    (0, -1): 'U',
    (0, 1):  'D',
}

inp = ''
size = (0, 0)
MAX_PATH = 999999
DEST_PATHES = []


def prepare_input_file(filename=os.path.basename(__file__).replace('.py',
                       '.txt')):
    file_path = os.path.join(INPUT_DIR, filename)
    with open(file_path, 'r') as f:
        inp = f.read().splitlines()[0]
    return inp


def check_available_pos(pos, size):
    available_pos = []
    for x in range(-1, 2):
        for y in range(-1, 2):
            if abs(x) == abs(y): continue
            if pos[0] + x < 0 or pos[0] + x > size[0]: continue
            if pos[1] + y < 0 or pos[1] + y > size[1]: continue
            available_pos.append(DIRECTION_MAPPER[(x, y)])
    return available_pos


OPEN_CHARS = ['b', 'c', 'd', 'e', 'f']
PATH_ORDER = ['U', 'D', 'L', 'R']

def check_open_path(inp):
    pathes = []
    for i, c in enumerate(inp[:4]):
        if str(c).lower() in OPEN_CHARS:
            pathes.append(PATH_ORDER[i])
    return pathes


def main():
    global inp, size, MAX_PATH, DEST_PATHES
    if len(sys.argv) == 2:
        inp = prepare_input_file(sys.argv[1])
    else:
        inp = prepare_input_file()
    print(f"Received '{inp}' as input")

    pos = (0, 0)
    size = (3, 3)
    ways = []

    # part 1
    part1(pos, ways)
    print(f"Part 1: {sorted(DEST_PATHES, key=len)[0]}")

    # part 2
    MAX_PATH = 0
    DEST_PATHES = []
    part2(pos, ways)
    print(f"Part 2: {MAX_PATH}")


def part1(pos, ways):
    global MAX_PATH, DEST_PATHES
    if len(ways) > MAX_PATH:
        return False
    if pos == size:
        MAX_PATH = len(ways)
        DEST_PATHES.append(''.join(ways))
        return True
    # generate_hash
    hsh = hashlib.md5(f"{inp}{''.join(ways)}".encode()).hexdigest()
    # check available pos
    av_pos = check_available_pos(pos, size)
    # check open path
    pathes = check_open_path(hsh)
    # check common ways
    for path in list(set(av_pos).intersection(pathes)):
        # get the relative position of the direction path
        rel_pos = (0, 0)
        for dir_pos, direction in DIRECTION_MAPPER.items():
            if path == direction:
                rel_pos = dir_pos
        new_pos = (pos[0] + rel_pos[0], pos[1] + rel_pos[1])
        part1(new_pos, ways.copy() + list(path))
    return False


def part2(pos, ways):
    global MAX_PATH, DEST_PATHES
    if pos == size:
        if MAX_PATH < len(ways):
            MAX_PATH = len(ways)
        DEST_PATHES.append(''.join(ways))
        return True
    # generate_hash
    hsh = hashlib.md5(f"{inp}{''.join(ways)}".encode()).hexdigest()
    # check available pos
    av_pos = check_available_pos(pos, size)
    # check open path
    pathes = check_open_path(hsh)
    # check common ways
    for path in list(set(av_pos).intersection(pathes)):
        # get the relative position of the direction path
        rel_pos = (0, 0)
        for dir_pos, direction in DIRECTION_MAPPER.items():
            if path == direction:
                rel_pos = dir_pos
        new_pos = (pos[0] + rel_pos[0], pos[1] + rel_pos[1])
        part2(new_pos, ways.copy() + list(path))
    return False


if __name__ == '__main__':
    main()
