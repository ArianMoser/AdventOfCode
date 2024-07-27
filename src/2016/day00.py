import os
import sys

INPUT_DIR = os.path.join(os.path.dirname(__file__), 'inputs')


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


if __name__ == '__main__':
    main()
