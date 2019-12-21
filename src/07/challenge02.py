from intcoder import Intcoder
import sys

class NewIntcoder(Intcoder):
    inputs = []

    def __init__(self, commands, inputs):
        #print("Initializing intcoder\n")
        self.inputs = inputs
        self.commands = commands
        #print("Using input: {0}".format(inputs))
        #print("Press Enter to start the program...")

    def receive_input(self):
        input = self.inputs.pop(0)
        return input


def main():
    print("AdventOfCode - 07 - Challenge 02")
    input = []
    computer_output = []

    f = open("input-test3.txt", "r")
    if f.mode == 'r':
        f_content = f.read()
        commands = list(map(int, f_content.split(',')))
        combinations = get_input_combinations(5, 9)
        for combination in combinations:
            print(combination)
            input_out = 0
            prev_input_out = -1
            # sett all amplifiers
            amplifiers = []
            for input_in in combination:
                amplifiers.append(NewIntcoder(commands, [input_in]))

            while input_out != prev_input_out:
                prev_input_out = input_out
                for amplifier in amplifiers:
                    amplifier.inputs.append(input_out)
                    try:
                        amplifier.start()
                    except Exception:
                        pass
                    print("OUTPUT: {}".format(amplifier.output))
                    input_out = amplifier.output
                print("Old: {0} New: {1}".format(prev_input_out, input_out))
            computer_output.append(input_out)
        print("Max output is {0}".format(max(computer_output)))

    # get the possible input combinations


def get_input_combinations(min_number, max_number):
    combinations = []
    numbers = []
    prev = []
    for number in range(min_number, max_number+1):
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
