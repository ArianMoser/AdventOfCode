import os
import sys
import re

re_task1_first = r'[0-9]'
re_task1_last = r'[0-9]'

def task1(line):
    return int(re.findall(re_task1_first, line)[0] +\
            re.findall(re_task1_last, line)[-1])

re_task2_first = r'.*?([0-9]|one|two|three|four|five|six|seven|eight|nine)'
re_task2_last = r'.*([0-9]|one|two|three|four|five|six|seven|eight|nine)'
number_mapping = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
        '1': '1',
        '2': '2',
        '3': '3',
        '4': '4',
        '5': '5',
        '6': '6',
        '7': '7',
        '8': '8',
        '9': '9',
        }


def task2(line):
    return int(number_mapping[re.findall(re_task2_first, line)[0]] +\
            number_mapping[re.findall(re_task2_last, line)[0]])

def main(input_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        f_content = f.read()
    lines = f_content.splitlines()

    # task 1
    res = 0
    for line in lines:
        res += task1(line)
    print(f"Task 1: {res}")

    # task 2
    res = 0
    for line in lines:
        res += task2(line)
    print(f"Task 2: {res}")


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    input_file = os.path.join(os.path.dirname(__file__), \
                                'inputs', 
                                sys.argv[0].replace("py", "txt"))
    main(input_file)
