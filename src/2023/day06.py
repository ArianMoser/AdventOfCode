import os
import sys
import re
import math

def main(input_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        f_content = f.read()
    # parse input
    numbers = [] 
    for line in f_content.splitlines():
        numbers.append(list(map(int, re.findall(r'\s(\d+)\s?', line))))
    races = list(zip(*numbers))

    # task 1
    res = math.prod([calculate_winning_strategies(*race) for race in races])
    print(f"Task 1: {res}")

    race = [int(''.join(re.findall(r'\d+', line))) for line in f_content.splitlines()]
    
    # task 2
    res = calculate_winning_strategies(*race) 

    print(f"Task 2: {res}")

def calculate_winning_strategies(time, distance):
    poss = 0
    for t in range(time):
        if (time - t) * t > distance: 
            poss +=1
    return poss


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        input_file = os.path.join(os.path.dirname(__file__), \
                                'inputs', 
                                sys.argv[0].replace("py", "txt"))
        main(input_file)
