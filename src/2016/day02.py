import os
import sys

INPUT_DIR = os.path.join(os.path.dirname(__file__), 'inputs')
NUMBER_PAD = {
        (-1,  1): 1,
        ( 0,  1): 2,
        ( 1,  1): 3,
        (-1,  0): 4,
        ( 0,  0): 5,
        ( 1,  0): 6,
        (-1, -1): 7,
        ( 0, -1): 8,
        ( 1, -1): 9,
}


def prepare_input_file(filename=os.path.basename(__file__).replace('.py',
                       '.txt')):
    file_path = os.path.join(INPUT_DIR, filename)
    with open(file_path, 'r') as f:
        lines = f.read().splitlines()
    return lines


def calculate_coords(coords, instructions):
    for instr in instructions:
        new_coords = coords.copy()
        if instr == 'U':
            new_coords[1] += 1
        elif instr == 'D':
            new_coords[1] -= 1
        elif instr == 'R':
            new_coords[0] += 1
        elif instr == 'L':
            new_coords[0] -= 1
        if abs(new_coords[0]) < 2 and abs(new_coords[1]) < 2:
            coords = new_coords
    return coords


def main():
    if len(sys.argv) == 2:
        lines = prepare_input_file(sys.argv[1])
    else:
        lines = prepare_input_file()
    print(f"Received {len(lines)} lines")

    # part 1
    coords = [0, 0]
    part1 = ''
    for line in lines:
        coords = calculate_coords(coords, line)
        part1 += str(NUMBER_PAD[tuple(coords)])
    print(f"Part 1: {part1}")


if __name__ == '__main__':
    main()
