import sys
import os
import re
import statistics

point_dict = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,

}


def main():
    file_name = f"inputs/{sys.argv[0].replace('py', 'txt')}" if len(sys.argv) == 1 else sys.argv[1]
    if not os.path.isfile(file_name):
        raise Exception(f'{file_name} is not a valid file')
    print(f"Challenge {sys.argv[0].split('.')[0].capitalize()}: \n")
    print("**************************")

    # read file
    with open(file_name, 'r') as f:
        lines = f.read().splitlines()

    print(f"Result Task1: {sum(check_syntax(line) for line in lines)}")
    print(f"Result Task2: {statistics.median(autocomplete_syntax(line) for line in lines if autocomplete_syntax(line) != 0)}")


def check_syntax(inp):
    global point_dict
    bracket_pair = re.search('(<[ ]*>)|(\{[ ]*\})|(\([ ]*\))|(\[[ ]*\])', inp)
    if bracket_pair is None: 
        incorrect_pair = re.search('[<\(\[\{][ ]*[>\)\]\}]', inp)
        if incorrect_pair is None: return 0
        return point_dict[incorrect_pair.group()[-1]]
    return check_syntax(inp[:bracket_pair.start()] + len(bracket_pair.group())*' ' + inp[bracket_pair.end():])

def autocomplete_syntax(inp):
    global point_dict
    bracket_pair = re.search('(<[ ]*>)|(\{[ ]*\})|(\([ ]*\))|(\[[ ]*\])', inp)
    if bracket_pair is None: 
        incorrect_pair = re.search('[<\(\[\{][ ]*[>\)\]\}]', inp)
        if incorrect_pair is not None: return 0
        res = 0
        for c in reversed(inp):
            if c == '(': res = res*5+1
            if c == '[': res = res*5+2
            if c == '{': res = res*5+3
            if c == '<': res = res*5+4
        return res
    return autocomplete_syntax(inp[:bracket_pair.start()] + len(bracket_pair.group())*' ' + inp[bracket_pair.end():])


    


if __name__ == "__main__":
    main()


