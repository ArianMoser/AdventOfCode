import sys
import os


def main():
    file_name = f"inputs/{sys.argv[0].replace('py', 'txt')}" if len(sys.argv) == 1 else sys.argv[1]
    if not os.path.isfile(file_name):
        raise Exception(f'{file_name} is not a valid file')
    print(f"Challenge {sys.argv[0].split('.')[0].capitalize()}: \n")
    print("**************************")

    # read file
    with open(file_name, 'r') as f:
        f_content = f.read()

    cmds = []

    for line in f_content.split('\n')[:-1]:
        (cmd, unit) = line.split(' ')
        unit = -1*int(unit) if cmd == 'up' else int(unit)
        cmds.append((cmd, unit))

    x = depth = 0 
    for c in cmds:
        (x, depth) = (x+c[1], depth) if c[0] == 'forward' else (x, depth + c[1]) 
    print(f'Result Task1: {x*depth}')

    x = depth = aim = 0 
    for c in cmds:
        aim = aim + c[1] if c[0] in ['up', 'down'] else aim 
        (x, depth) = (x+c[1], depth+aim*c[1]) if c[0] == 'forward' else (x, depth)
    print(f'Result Task2: {x*depth}')



if __name__ == "__main__":
    main()


