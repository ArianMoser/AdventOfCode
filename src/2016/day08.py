import os
import sys
import re

INPUT_DIR = os.path.join(os.path.dirname(__file__), 'inputs')
RE_RECT = r'rect (\d+)x(\d+)'
RE_ROTATE_ROW = r'rotate row y=(\d+) by (\d+)'
RE_ROTATE_COLUMN = r'rotate column x=(\d+) by (\d+)'


def prepare_input_file(filename=os.path.basename(__file__).replace('.py',
                       '.txt')):
    file_path = os.path.join(INPUT_DIR, filename)
    with open(file_path, 'r') as f:
        lines = f.read().splitlines()
    return lines


def main():
    if len(sys.argv) == 2:
        lines = prepare_input_file(sys.argv[1])
    else:
        lines = prepare_input_file()
    print(f"Received {len(lines)} lines")

    # initialize screen
    size = (50, 6)  # (width, heigt) (x, y)
    pixels = init_screen(size)

    for instr in lines:
        if re.match(RE_RECT, instr):
            width, height = map(int, re.match(RE_RECT, instr).groups())
            for y in range(height):
                for x in range(width):
                    pixels[(x, y)] = (pixels[(x, y)] + 1) % 2
        elif re.match(RE_ROTATE_COLUMN, instr):  # height
            x, count = map(int, re.match(RE_ROTATE_COLUMN, instr).groups())
            count = count % size[1]
            old_pixels = pixels.copy()
            for pos_y in range(size[1]):
                pixels[(x, pos_y)] = old_pixels[(x, (pos_y - count) % size[1])]
        elif re.match(RE_ROTATE_ROW, instr):
            y, count = map(int, re.match(RE_ROTATE_ROW, instr).groups())
            count = count % size[0]
            old_pixels = pixels.copy()
            for pos_x in range(size[0]):
                pixels[(pos_x, y)] = old_pixels[((pos_x - count) % size[0], y)]

        """
        # show changes on the fly
        print_screen(pixels, size)
        import time
        time.sleep(0.1)
        clear_screen(size)
        """

    print(f"Part 1: {sum(pixels.values())}")
    print("Part 2:")
    print_screen(pixels, size)



def clear_screen(size):
    for line in range(size[1]):
        print("\033[A\033[A")


def init_screen(size):
    pixels = {(x, y) : 0 for x in range(size[0]) for y in range(size[1])}
    return pixels


def print_screen(pixels, size):
    for y in range(size[1]):
        for x in range(size[0]):
            if pixels[(x, y)] == 0:
                print(' ', end='')
            else:
                print('#', end='')
        print()


if __name__ == '__main__':
    main()
