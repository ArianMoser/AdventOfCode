from intcoder import Intcoder
import sys

class NewIntcoder(Intcoder):
    inputs = []

    def __init__(self, commands, inputs):
        #print("Initializing intcoder\n")
        self.inputs = inputs
        #print("Using input: {0}".format(inputs))
        #print("Press Enter to start the program...")
        self.start(commands)

    def receive_input(self):
        input = self.inputs.pop(0)
        return input


def main():
    print("AdventOfCode - 07 - Challenge 01")
    input = []
    computer_output = []

    f = open("input.txt", "r")
    if f.mode == 'r':
        f_content = f.read()
        commands = list(map(int, f_content.split(',')))
        combinations = get_input_combinations()
        for combination in combinations:
            input_out = 0
            for input_in in combination:
                inputs = [input_in, input_out]
                input_out = NewIntcoder(commands, inputs).output
                #print("Got output {0}".format(input_out))
            computer_output.append(input_out)
        print("Max output is {0}".format(max(computer_output)))

    # get the possible input combinations


def get_input_combinations():
    combinations = []
    numbers = []
    prev = []
    for number in range(0, 5):
        numbers.append(number)
    get_combination(numbers, prev,combinations)
    return combinations


def get_combination(numbers, prev, combinations):
    for index in range(len(numbers)):
        new_prev = prev.copy()
        new_numbers = numbers.copy()
        number = numbers[index]
        new_prev.append(number)
        del new_numbers[index]
        if len(numbers) > 1:
            get_combination(new_numbers, new_prev, combinations)
        else:
            combinations.append(new_prev)

if __name__ == "__main__":
    main()
