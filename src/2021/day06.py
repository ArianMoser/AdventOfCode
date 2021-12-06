import sys
import os


def main():
    file_name = f"inputs/{sys.argv[0].replace('py', 'txt')}" if len(sys.argv) == 1 else sys.argv[1]
    if not os.path.isfile(file_name):
        raise Exception(f'{file_name} is not a valid file')
    print(f"Challenge {sys.argv[0].split('.')[0].capitalize()}: \n")
    print("**************************")

    # read file
    numbers = []
    with open(file_name, 'r') as f:
        numbers = list(map(int, f.readline().split(',')))

    for i in range(80):
        for i, number in enumerate(numbers):
            if number == 0:
                numbers[i] = 7
                numbers.append(9)
            numbers[i] = numbers[i] - 1
    print(f'Result Task1: {len(numbers)}')

    number_dict = dict() 
    for i in range(9):
        number_dict[i] = sum(1 if i == number else 0 for number in numbers)

    for j in range(80, 256):
        temp = dict()
        for i in range(9):
            if i == 0: 
                temp[8] = number_dict[0]
                temp[6] = number_dict[0]
            else:
                temp[i-1] = temp[i-1] + number_dict[i] if i-1 in temp.keys() else number_dict[i]
        number_dict = temp.copy()
    print(f'Result Task2: {sum(number_dict[i] for i in number_dict.keys())}')
                


if __name__ == "__main__":
    main()


