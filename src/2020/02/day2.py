import re
import sys

def task1(c_min, c_max, letter_occurence):
    if c_min <= len(letter_occurence) <= c_max:
        return 1
    return 0


def task2(c_min, c_max, letter_positions):
    if bool(c_min-1 in letter_positions) != bool(c_max-1 in letter_positions):
        return 1
    return 0


def validate_passwords(file_name, task2_bool):
    valid_passwords = 0
    with open(file_name) as f:
        for line in f:
            splitted_line= line.split(" ")
            c_min = int(splitted_line[0].split("-")[0])
            c_max = int(splitted_line[0].split("-")[1])
            letter = splitted_line[1][0]
            txt = splitted_line[2]
            if task2_bool:
                letter_positions = [x.span()[0] for x in re.finditer(re.compile(letter), txt)]
                valid_passwords = valid_passwords + task2(c_min, c_max, letter_positions)
            else:
                letter_occurence = re.findall(re.compile(letter), txt)
                valid_passwords = valid_passwords + task1(c_min, c_max, letter_occurence)
    print("Found {} valid passwords.".format(valid_passwords))
                    

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
    validate_passwords(file_name, task2_bool)


if __name__ == "__main__":
    main()
