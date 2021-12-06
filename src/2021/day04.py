import sys
import os
import re
from dataclasses import dataclass

class Error(Exception):
    pass
class WinningError(Error):
    pass

@dataclass
class Board:
    lines: []
    numbers: []
    def generate_lines(self):
        # rows
        for i in range(5):
            self.lines.append(self.numbers[i*5:(i+1)*5])
        # columns
        for i in range(5):
            self.lines.append([row[i] for row in self.lines[:5]])
        

def main():
    file_name = f"inputs/{sys.argv[0].replace('py', 'txt')}" if len(sys.argv) == 1 else sys.argv[1]
    if not os.path.isfile(file_name):
        raise Exception(f'{file_name} is not a valid file')
    print(f"Challenge {sys.argv[0].split('.')[0].capitalize()}: \n")
    print("**************************")

    # read file
    with open(file_name, 'r') as f:
        f_content = f.read()

    content_splitted = f_content.split('\n\n')
    #print(bingo_papers)
    numbers = list(map(int, content_splitted[0].split(',')))
    boards = []
    for board_str in content_splitted[1:]:
        boards.append(Board([], list(map(int, re.findall('\d+', board_str)))))
    for board in boards:
        board.generate_lines()

    # task 1
    for i, _ in enumerate(numbers):
        win_board = get_winning_boards(boards, numbers[:i+1])
        if len(win_board) != 0:
            print(f"Result Task1: {sum(n if n not in numbers[:i+1] else 0 for n in win_board[0].numbers) * numbers[i]}")
            break

    for i, _ in enumerate(numbers):
        win_boards = get_winning_boards(boards, numbers[:i+1])
        if win_boards is not None:
            for board in win_boards:
                try:
                    boards.remove(board)
                except ValueError:
                    pass
        if len(boards) == 0:
            print(f"Result Task2: {sum(n if n not in numbers[:i+1] else 0 for n in win_boards[0].numbers) * numbers[i]}")
            break
            

def get_winning_boards(boards, numbers):
    winning_boards = []
    for board in boards:
        for line in board.lines:
            if all(n in numbers for n in line):
                winning_boards.append(board)
    return winning_boards


if __name__ == "__main__":
    main()


