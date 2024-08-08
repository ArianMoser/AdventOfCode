import os
import sys

INPUT_DIR = os.path.join(os.path.dirname(__file__), 'inputs')


def prepare_input_file(filename=os.path.basename(__file__).replace('.py',
                       '.txt')):
    file_path = os.path.join(INPUT_DIR, filename)
    with open(file_path, 'r') as f:
        inp = f.read().splitlines()[0]
    return inp


def generate_checksum(check_string):
    checksum = ''
    for i in range(0, len(check_string), 2):
        if check_string[i] == check_string[i+1]:
            checksum += '1'
        else:
            checksum += '0'
    return checksum


def generate_data(new_data):
    copy = new_data[::-1]
    new_copy = ''
    for c in copy:
        if c == '0': new_copy += '1'
        elif c == '1': new_copy += '0'
    return f'{new_data}0{new_copy}'


def main():
    if len(sys.argv) == 2:
        inp = prepare_input_file(sys.argv[1])
    else:
        inp = prepare_input_file()
    print(f"Received {inp} input")

    # task 1
    disk_length = 272
    new_data = inp

    # not enough data -> generate data
    while len(new_data) < disk_length:
        new_data = generate_data(new_data)

    # shrink data to disk size
    new_data = new_data[:disk_length]

    # generate checksum
    checksum = new_data
    while len(checksum) % 2 == 0:
        checksum = generate_checksum(checksum)

    print(f"Part 1: {checksum}")

    # task 2
    disk_length = 35651584
    new_data = inp

    # not enough data -> generate data
    while len(new_data) < disk_length:
        new_data = generate_data(new_data)

    # shrink data to disk size
    new_data = new_data[:disk_length]

    # generate checksum
    checksum = new_data
    while len(checksum) % 2 == 0:
        checksum = generate_checksum(checksum)

    print(f"Part 2: {checksum}")




if __name__ == '__main__':
    main()
