import sys


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
        numbers = list(map(int, f.read().split('\n')[:-1]))

        for i in range(len(numbers)-25):
            preamble = numbers[i:i+25]
            n = numbers[i+25]
            if len(get_poss_add_of_two_nums(preamble, n)) == 0:
                return n
    return 0


def get_poss_add_of_two_nums(inp, dest):
    return [(i, j) for i in inp for j in inp if i+j==dest]


def task2(file_name):
    with open(file_name) as f:
        numbers = list(map(int, f.read().split('\n')[:-1]))
        inv_nr = task1(file_name)
        (i_min, i_max) = get_poss_add_of_mult_nums(numbers, inv_nr)
        return min([numbers[x] for x in range(i_min, i_max)]) + max([numbers[x] for x in range(i_min, i_max)]) 

    return 0


def get_poss_add_of_mult_nums(inp, dest):
    for start_i in range(len(inp)):
        add = 0
        for i in range(start_i, len(inp)):
            add += inp[i]
            #print(f"{i}: {inp[i]} ({add}) -> {dest}")
            if add > dest:
                break
            elif add == dest:
                return (start_i, i)
    return (0, 0)


if __name__ == "__main__":
    main()

