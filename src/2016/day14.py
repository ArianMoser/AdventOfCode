import os
import sys
import hashlib

INPUT_DIR = os.path.join(os.path.dirname(__file__), 'inputs')
HASHES = dict()


def prepare_input_file(filename=os.path.basename(__file__).replace('.py',
                       '.txt')):
    file_path = os.path.join(INPUT_DIR, filename)
    with open(file_path, 'r') as f:
        inp = f.read()[:-1]
    return inp


def main():
    if len(sys.argv) == 2:
        inp = prepare_input_file(sys.argv[1])
    else:
        inp = prepare_input_file()
    print(f"Received '{inp}' as input")

    # part 1
    step = 0
    valid_keys = dict()
    last_hashes = 1000

    while len(valid_keys.keys()) < 64 or last_hashes >= 0:
        # calculate hash
        HASHES[step] = generate_hash(f'{inp}{str(step)}', 1)

        # check generated hash for five of a kind
        for i in range(0, len(HASHES[step]) - 4):
            if HASHES[step][i:i+5] == HASHES[step][i]*5:
                # check the last 1000 hashes for a three of a kind of the same
                # char
                for valid_key in check_for_valid_keys(step, HASHES[step][i]):
                    valid_keys[valid_key] = HASHES[valid_key]
        step += 1

        # ensure that there are not more valid keys in the next 1000 hashes
        if len(valid_keys.keys()) >= 64:
            last_hashes -= 1

    print(f"Task 1: {sorted(valid_keys, key=lambda k: k)[63]}")

    # part 2
    step = 0
    valid_keys = dict()
    last_hashes = 1000

    while len(valid_keys.keys()) < 64 or last_hashes >= 0:
        # calculate hash
        HASHES[step] = generate_hash(f'{inp}{str(step)}', 2017)

        # check generated hash for five of a kind
        for i in range(0, len(HASHES[step]) - 4):
            if HASHES[step][i:i+5] == HASHES[step][i]*5:
                # check the last 1000 hashes for a three of a kind of the same
                # char
                for valid_key in check_for_valid_keys(step, HASHES[step][i]):
                    valid_keys[valid_key] = HASHES[valid_key]
        step += 1

        # ensure that there are not more valid keys in the next 1000 hashes
        if len(valid_keys.keys()) >= 64:
            last_hashes -= 1

    print(f"Task 2: {sorted(valid_keys, key=lambda k: k)[63]}")


def check_for_valid_keys(start_step, char):
    valid_keys = []
    for step in range(start_step - 1, start_step - 1001, -1):
        if step < 0:
            break
        for i in range(0, len(HASHES[step]) - 2):
            if HASHES[step][i:i+3] == HASHES[step][i]*3:
                if HASHES[step][i] == char:
                    valid_keys.append(step)
                else:
                    break
    return valid_keys


def generate_hash(inp, times):
    for i in range(times):
        inp = hashlib.md5(inp.encode()).hexdigest()
    return inp


if __name__ == '__main__':
    main()
