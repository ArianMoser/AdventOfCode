import os
import sys
import re
from collections import Counter

INPUT_DIR = os.path.join(os.path.dirname(__file__), 'inputs')
INPUT_RE = r'([a-z\-]+?)(\d+)\[([a-z]+)\]'


def prepare_input_file(filename=os.path.basename(__file__).replace('.py',
                       '.txt')):
    file_path = os.path.join(INPUT_DIR, filename)
    with open(file_path, 'r') as f:
        lines = f.read().splitlines()
    rooms = []
    for line in lines:
        result = re.search(INPUT_RE, line)
        rooms.append(result.groups())
    return rooms


def is_real_room(room):
    encrypted_name = room[0].replace('-', '')
    occurencies = Counter(sorted(encrypted_name)).most_common()
    checksum = ''
    for el in occurencies[:5]:
        checksum += el[0]
    return checksum == room[2]


def decrypt_room_name(room):
    rotation = int(room[1]) % 26

    offset = 97
    decrypted_name = ''
    for c in room[0]:
        if c == '-':
            decrypted_name += ' '
            continue
        decrypted_name += chr(((ord(c) - offset + rotation) % 26) + offset)
    return decrypted_name


def main():
    if len(sys.argv) == 2:
        rooms = prepare_input_file(sys.argv[1])
    else:
        rooms = prepare_input_file()
    print(f"Input: Received {len(rooms)} rooms")

    # part 1
    part1 = 0
    for room in rooms:
        if is_real_room(room):
            part1 += int(room[1])

    print(f"Part 1: {part1}")

    # part 2
    for room in rooms:
        if is_real_room(room):
            if 'north' in decrypt_room_name(room):
                print(f"Part 2: {room[1]} ({decrypt_room_name(room)})")


if __name__ == '__main__':
    main()
