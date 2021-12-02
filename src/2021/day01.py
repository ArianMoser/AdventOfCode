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
        f_content = f.read()

    numbers = []
    for line in f_content.split('\n')[:-1]:
        numbers.append(int(line))

    print(f'Task1 Result: {sum(1 if numbers[i] > numbers[i-1] else 0 for i in range(1, len(numbers)))}')
    print(f'Task2 Result: {sum(1 if sum(n for n in numbers[i-1:i+2]) < sum(n for n in numbers[i:i+3]) else 0 for i in range(1, len(numbers)-2))}')
        
if __name__ == "__main__":
    main()


