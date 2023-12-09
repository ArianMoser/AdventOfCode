import os
import sys
import re

def main(input_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        f_content = f.read()
    lines = f_content.splitlines()

    # task 1
    res = 0
    for i, line in enumerate(lines):
        (line_win, line_elf) = line.split('|')
        win_numbers = list(map(int, re.findall('([0-9]+)\s', line_win)))
        elf_numbers = list(map(int, re.findall('\s([0-9]+)', line_elf)))
        points = 0
        for num in elf_numbers:
            if num in win_numbers:
                if points == 0: points = 1
                else: points *= 2
                #print(i, num, points)
        res += points
    print(f"Task 1: {res}")

    # task 2
    res = 0
    scratch_pads = {}
    for i in range(len(lines)):
        scratch_pads[i] = 1

    for i, line in enumerate(lines):
        (line_win, line_elf) = line.split('|')
        win_numbers = list(map(int, re.findall('([0-9]+)\s', line_win)))
        elf_numbers = list(map(int, re.findall('\s([0-9]+)', line_elf)))
        wins = 0
        for num in elf_numbers:
            if num in win_numbers:
                wins += 1
        for win in range(1, 1+wins):
            scratch_pads[i+win] += scratch_pads[i]*1

    res = sum(scratch_pads.values())
            
    print(f"Task 2: {res}")

if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else: 
        input_file = os.path.join(os.path.dirname(__file__), \
                                'inputs', 
                                sys.argv[0].replace("py", "txt"))
        main(input_file)
