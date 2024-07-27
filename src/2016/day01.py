import os
import sys

INPUT_DIR = os.path.join(os.path.dirname(__file__), 'inputs')
print(INPUT_DIR)


def prepare_input_file(filename=os.path.basename(__file__).replace('.py',
                       '.txt')):
    file_path = os.path.join(INPUT_DIR, filename)
    with open(file_path, 'r') as f:
        f_content = f.read().splitlines()[0]
    return f_content.split(", ")


def make_move(pos, steps, degree):
    if degree == 0:
        pos[1] += steps
    elif degree == 90:
        pos[0] += steps
    elif degree == 180:
        pos[1] -= steps
    elif degree == 270:
        pos[0] -= steps
    return pos


def main():
    if len(sys.argv) == 2:
        moves = prepare_input_file(sys.argv[1])
    else:
        moves = prepare_input_file()
    print(f"Received {len(moves)} moves")

    # part 1
    degree = 0
    pos = [0, 0]  # (x, y)

    for move in moves:
        direction = move[0]
        steps = int(move[1:])
        if direction == 'R':
            degree = (degree + 90) % 360
        elif direction == 'L':
            degree = (degree - 90) % 360
        pos = make_move(pos, steps, degree)

    part1 = abs(pos[0]) + abs(pos[1])
    print(f"Part 1: {part1}")

    # part 2
    degree = 0
    pos = [0, 0]  # (x, y)
    past_pos = [(0, 0)]
    for move in moves:
        direction = move[0]
        steps = int(move[1:])
        if direction == 'R':
            degree = (degree + 90) % 360
        elif direction == 'L':
            degree = (degree - 90) % 360
        for step in range(steps):
            pos = make_move(pos, 1, degree)
            if tuple(pos) in past_pos:
                part2 = abs(pos[0]) + abs(pos[1])
                print(f"Part 2: {part2}")
                exit(1)
            past_pos.append(tuple(pos))



if __name__ == '__main__':
    main()
