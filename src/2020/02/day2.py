import re
import sys

def task1(file_name):
    with open(file_name) as f:
        valid_passwords = 0
        for line in f:
            splitted_line= line.split(" ")
            c_min = int(splitted_line[0].split("-")[0])
            c_max = int(splitted_line[0].split("-")[1])
            letter = splitted_line[1][0]
            txt = splitted_line[2]
            letter_occurence = re.findall(re.compile(letter), txt)
            if c_min <= len(letter_occurence) <= c_max:
                valid_passwords = valid_passwords+1

        print("Task1: Found {} valid passwords.".format(valid_passwords))

def task2(file_name):
    with open(file_name) as f:
        valid_passwords = 0
        for line in f:
            splitted_line= line.split(" ")
            c_min = int(splitted_line[0].split("-")[0])
            c_max = int(splitted_line[0].split("-")[1])
            letter = splitted_line[1][0]
            txt = splitted_line[2]
            letter_positions = [x.span()[0] for x in re.finditer(re.compile(letter), txt)]
            if bool(c_min-1 in letter_positions) != bool(c_max-1 in letter_positions):
                valid_passwords = valid_passwords+1

        print("Task2: Found {} valid passwords.".format(valid_passwords))

def main():
    # default values
    file_name = "input.txt"
    task2_bool = False
    print("Challenge day 2: \n")
    print("**************************")
    try:
        file_name = sys.argv[1]
        task2_bool = True if sys.argv[2].lower() in ["true", "on", "1", "yes"] else False
    except Exception as e:
        print("(Parameter Usage: dayx.py <<file_name>> <<task2 (True|False)>>)")
    print("Using values: \n  Filename: {} \n  Task2: {}".format(file_name, task2_bool))
    print("**************************\n")
    if task2_bool:
        task2(file_name)
    else:
        task1(file_name)


if __name__ == "__main__":
    main()
