import sys

# Errors
class Error(Exception):
    """ Base Exception for other exceptions """
    pass

class NoInputFile(Error):
    """ This Exception will be raised when no input file was given"""
    pass

class NoResultFound(Error):
    """ This Exception will be raised when no right solution was found in the given inputs"""
    pass


def main():
    print("*****Day 1 Challenge 1*****")

    # Opening passed file
    try:
        if len(sys.argv) > 1:
            inputs = get_inputs(sys.argv[1])
            print("Result of Task 1: {}".format(task1(inputs)))
            print("Result of Task 2: {}".format(task2(inputs)))
        else:
            raise NoInputFileError("No input file given. Please pass as first argument the input file")
    except Exception as e:
        print(str(e))


def task1(inputs):
    for pos1 in range(len(inputs)):
        num1 = inputs[pos1]
        for pos2 in range(pos1, len(inputs)):
            num2 = inputs[pos2]
            if num1 + num2 == 2020:
                return num1 * num2
    raise NoResultFound

def task2(inputs):
    for pos1 in range(len(inputs)):
        num1 = inputs[pos1]
        for pos2 in range(pos1, len(inputs)):
            num2 = inputs[pos2]
            for pos3 in range(pos2, len(inputs)):
                num3 = inputs[pos3]
                if num1 + num2 + num3 == 2020:
                    return num1 * num2 * num3
    raise NoResultFound
    

def get_inputs(file_name):
    inputs = []
    f = open(file_name, "r")
    if f.mode == 'r':
        f_content = f.read()
        for line in f_content.splitlines():
            inputs.append(int(line))
    return inputs



if __name__ == "__main__":
    main()
