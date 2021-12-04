import sys
import os


def main():
    file_name = f"inputs/{sys.argv[0].replace('py', 'txt')}" if len(sys.argv) == 1 else sys.argv[1]
    if not os.path.isfile(file_name):
        raise Exception(f'{file_name} is not a valid file')
    print(f"Challenge {sys.argv[0].split('.')[0].capitalize()}: \n")
    print("**************************")

    # read file
    with open(file_name, 'r') as f:
        numbers = [line for line in f.read().splitlines()]

    gamma = epsilon = ''
    for pos in range(len(numbers[0])):
        gamma = gamma+'1' if sum(1 if n[pos] == '1' else 0 for n in numbers) > len(numbers)/2 else gamma+'0'
    for n in gamma:
        epsilon = epsilon + '1' if n == '0' else epsilon + '0'
    print(f"Result Task1: {int(gamma, 2) * int(epsilon, 2)}")
    print(f"Result Task2: {int(oxygen_gen(numbers), 2) * int(co2_scrubber(numbers), 2)}")

def oxygen_gen(numbers):
    if len(numbers) == 1:
        return numbers[0]
    bit = bit_criteria(numbers, 0)
    return bit + oxygen_gen([n[1:] for n in numbers if n[0] == bit])
    
def co2_scrubber(numbers):
    if len(numbers) == 1:
        return numbers[0]
    bit = bit_criteria_reverse(numbers, 0)
    return bit + co2_scrubber([n[1:] for n in numbers if n[0] == bit])


def bit_criteria(numbers, pos):
    return '1' if sum(1 if n[pos] == '1' else 0 for n in numbers) >= len(numbers)/2 else '0'
    
def bit_criteria_reverse(numbers, pos):
    return '1' if sum(1 if n[pos] == '1' else 0 for n in numbers) < len(numbers)/2 else '0'


if __name__ == "__main__":
    main()


