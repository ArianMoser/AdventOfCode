import os
import sys
import re

INPUT_DIR = os.path.join(os.path.dirname(__file__), 'inputs')
RE_IN_SQUARE_BRACKETS = r'\[[a-z]+?\]'
RE_SQUARE_BRACKETS_CONTENT = r'\[([a-z]+?)\]'


def prepare_input_file(filename=os.path.basename(__file__).replace('.py',
                       '.txt')):
    file_path = os.path.join(INPUT_DIR, filename)
    with open(file_path, 'r') as f:
        lines = f.read().splitlines()
    return lines


def check_tls_support(ip):
    ip_splitted_without_square = re.split(RE_IN_SQUARE_BRACKETS, ip)

    # check for abba
    if not check_for_abba(ip_splitted_without_square):
        return False

    # check for abba not in square
    ip_square_splited = re.findall(RE_SQUARE_BRACKETS_CONTENT, ip)
    return not check_for_abba(ip_square_splited)


def check_for_abba(ip_parts):
    for ip_part in ip_parts:
        for i in range(len(ip_part)-3):
            ip_part_string = ''.join(ip_part[i:i+4])
            if ip_part_string == ip_part_string[::-1] and \
                    ip_part[i] != ip_part[i+1]:
                return True
    return False


def check_ssl_support(ip):
    # check for aba
    ip_splitted_without_square = re.split(RE_IN_SQUARE_BRACKETS, ip)
    aba_parts = get_all_aba_part(ip_splitted_without_square)

    # check for abba not in square
    ip_square_splited = re.findall(RE_SQUARE_BRACKETS_CONTENT, ip)
    bab_parts = get_all_aba_part(ip_square_splited)

    # switch the bab_parts
    for i, bab_part in enumerate(bab_parts):
        bab_parts[i] = ''.join([bab_part[1], bab_part[0], bab_part[1]])

    return len(set(aba_parts).intersection(set(bab_parts))) > 0


def get_all_aba_part(ip_parts):
    parts = []
    for ip_part in ip_parts:
        for i in range(len(ip_part)-2):
            ip_part_string = ''.join(ip_part[i:i+3])
            if ip_part_string == ip_part_string[::-1] and \
                    ip_part[i] != ip_part[i+1]:
                parts.append(ip_part_string)
    return parts


def main():
    if len(sys.argv) == 2:
        lines = prepare_input_file(sys.argv[1])
    else:
        lines = prepare_input_file()
    print(f"Received {len(lines)} lines")

    # part 1
    part1 = 0
    for line in lines:
        if check_tls_support(line):
            part1 += 1
    print(f"Part 1: {part1}")

    # part 2
    part2 = 0
    for line in lines:
        if check_ssl_support(line):
            part2 += 1
    print(f"Part 2: {part2}")


if __name__ == '__main__':
    main()
