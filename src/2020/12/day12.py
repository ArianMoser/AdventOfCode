import sys
import math


def main():
    file_name = "input.txt"
    task2_bool = False
    print("Challenge day 4: \n")
    print("**************************")
    try:
        file_name = sys.argv[1]
        task2_bool = True if sys.argv[2].lower() in ["true", "on", "1", "yes"] else False
    except Exception as e:
        print("(Parameter Usage: dayx.py <<file_name>> <<task2 (True|False)>>)")
    print("Using values: \n  Filename: {} \n  Task2: {}".format(file_name, task2_bool))
    print("**************************\n")
    if task2_bool:
        print("Answers given: {}".format(task2(file_name)))
    else:
        print("Answers given: {}".format(task1(file_name)))


def task1(file_name):
    with open(file_name) as f:
        instr_list = f.read().split('\n')[:-1]
        pos = [(0, 0, 90)] # x, y, degree

        for instr in instr_list:
            pos.append(move_step(pos[-1], instr))
            print(pos[-1])
        return abs(pos[-1][0]) + abs(pos[-1][1])
                
def move_step(pos, instr):
    direc, steps = instr[0], int(instr[1:])
    x, y, deg = pos
    if direc == 'N' or (direc == 'F' and deg == 0):
        y += steps
    elif direc == 'E' or (direc == 'F' and deg == 90):
        x += steps
    elif direc == 'S' or (direc == 'F' and deg == 180):
        y -= steps
    elif direc == 'W' or (direc == 'F' and deg == 270):
        x -= steps
    elif direc == 'R':
        deg = (deg + steps) % 360
    elif direc == 'L':
        deg = (deg - steps) % 360
    return (x, y, deg)


def move_step_t2(pos, instr):
    direc, steps = instr[0], int(instr[1:])
    x, y, wp_x, wp_y = pos
    if direc == 'N':
        wp_y += steps
    elif direc == 'E':
        wp_x += steps
    elif direc == 'S':
        wp_y -= steps
    elif direc == 'W':
        wp_x -= steps
    elif direc == 'R':
        deg = math.radians(-1*steps)
        wp_x, wp_y = round(math.cos(deg) * wp_x - math.sin(deg) * wp_y, 2), round(math.sin(deg) * wp_x + math.cos(deg) * wp_y, 2)
    elif direc == 'L':
        deg = math.radians(1*steps)
        wp_x, wp_y = round(math.cos(deg) * wp_x - math.sin(deg) * wp_y, 2), round(math.sin(deg) * wp_x + math.cos(deg) * wp_y, 2)
    elif direc == 'F':
        x += steps*wp_x 
        y += steps*wp_y
    return (x, y, wp_x, wp_y)


def task2(file_name):
    with open(file_name) as f:
        instr_list = f.read().split('\n')[:-1]
        pos = [(0, 0, 10, 1)] # (x, y, wp_x, wp_y)
        for instr in instr_list:
            pos.append(move_step_t2(pos[-1], instr))
            print(pos[-1])
        return abs(pos[-1][0]) + abs(pos[-1][1])


if __name__ == "__main__":
    main()

