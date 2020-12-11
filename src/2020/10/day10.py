import sys
from collections import Counter
from dataclasses import dataclass


poss_arr = dict()


def main():
    file_name = "input.txt"
    task2_bool = False
    print("Challenge day 10: \n")
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
        adapters = list(map(int, f.read().split("\n")[:-1]))
        adapters.append(0)
        adapters = bubble_sort(adapters)
        diffs = [adapters[i+1] - adapters[i] for i in range(len(adapters)-1)]
        print(Counter(diffs))
        return (Counter(diffs)[3] + 1) * Counter(diffs)[1]


def task2(file_name):
    with open(file_name) as f:
        adapters = list(map(int, f.read().split("\n")[:-1]))
        adapters.append(0)
        adapters = bubble_sort(adapters)
        return get_possibilities(adapters)
        

def get_possibilities(arr):
    global poss_arr
    num = arr[0]
    ret = 0


    if len(arr) <= 1:
        return 1

    if str(arr) in poss_arr.keys():
        return poss_arr[str(arr)]
    for i in range(1,len(arr)):
        if arr[i] - num > 3:
            break
        ret += get_possibilities(arr[i:])
    poss_arr[str(arr)] = ret
    return ret 


def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j] 
    return arr


if __name__ == "__main__":
    main()

