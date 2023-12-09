import os
import sys

def main(input_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        f_content = f.read()
    lines = f_content.splitlines()
    reports = [list(map(int, line.split(' '))) for line in lines]
    

    # task 1
    res = sum([predict_next(report) for report in reports])
    print(f"Task 1: {res}")

    # task 2
    res = sum([predict_next_p2(report) for report in reports])
    print(f"Task 2: {res}")

def predict_next(report):
    if all(val == 0 for val in report):
        return 0
    else:
        diff = [pair[1] - pair[0] for pair in zip(report, report[1:])]
        return report[-1] + predict_next(diff)

def predict_next_p2(report):
    if all(val == 0 for val in report):
        return 0
    else:
        diff = [pair[1] - pair[0] for pair in zip(report, report[1:])]
        return report[0] - predict_next_p2(diff)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else: 
        input_file = os.path.join(os.path.dirname(__file__), \
                                'inputs', 
                                sys.argv[0].replace("py", "txt"))
        main(input_file)
