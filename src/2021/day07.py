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
        numbers = list(map(int, f.read().split(',')))

    print(f'Result Task1: {min(sum(abs(n-i) for n in numbers) for i in range(min(numbers), max(numbers)))}')
    print(f'Result Task2: {min(sum(sum(c for c in range(1, abs(n-i)+1)) for n in numbers) for i in range(min(numbers), max(numbers)))}')
        


if __name__ == "__main__":
    main()


