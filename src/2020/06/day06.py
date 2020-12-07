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
    answers = 0
    with open(file_name) as f:
        f_content = f.read()
        groups = f_content.split("\n\n")
        for group in groups:
            group = set(group.replace('\n', ''))
            ans = set(group)
            answers += len(ans)
    return answers


def task2(file_name):
    answers = 0
    with open(file_name) as f:
        f_content = f.read()
        groups = f_content.split("\n\n")
        for group in groups:
            person = group.split("\n")
            ans = None
            for p in person: 
                if p != '':
                    if ans is None:
                        ans = set(p)
                    else:
                        ans.intersection_update(set(p))
            answers += len(ans)
    return answers


if __name__ == "__main__":
    main()
