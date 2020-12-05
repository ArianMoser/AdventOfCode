import sys

def main():
    file_name = "input.txt"
    task2_bool = False
    print("Challenge day 3: \n")
    print("**************************")
    try:
        file_name = sys.argv[1]
        task2_bool = True if sys.argv[2].lower() in ["true", "on", "1", "yes"] else False
    except Exception as e:
        print("(Parameter Usage: dayx.py <<file_name>> <<task2 (True|False)>>)")
    print("Using values: \n  Filename: {} \n  Task2: {}".format(file_name, task2_bool))
    print("**************************\n")
    with open(file_name) as f:
        lines = f.read().split('\n')[:-1]
        f.close()
        if task2_bool:
            print("Task2: ")
            t1 = get_trees(lines, 1, 1)
            t2 = get_trees(lines, 3, 1)
            t3 = get_trees(lines, 5, 1)
            t4 = get_trees(lines, 7, 1)
            t5 = get_trees(lines, 1, 2)
            print("Result: {}".format(t1*t2*t3*t4*t5))
        else:
            print("Task1: ")
            get_trees(lines, 3, 1)
        # print("Encounter {} trees".format(get_trees(lines, 3, 1)))


def get_trees(lines, right, down):
    x_max = len(lines[0])
    x_cood = 0
    trees = 0
    i = 0
    for line in lines:
        if i%down == 0:
            if line[x_cood] == '#':
                trees = trees +1
            x_cood = (x_cood + right) % x_max
        i = i+1
    print("Encounter {} trees".format(trees))
    return trees

if __name__ == "__main__":
    main()
