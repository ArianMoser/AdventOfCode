import sys
import copy


def main():
    file_name = "input.txt"
    task2_bool = False
    print("Challenge day 11: \n")
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
    with open(file_name) as f:
        seats = []
        seats.append([list(l) for l in f.read().split('\n')[:-1]])

        while len(seats) < 2 or not compare_arrays(seats[-2], seats[-1]):
            old_seats = seats[-1]
            new_seats = copy.deepcopy(old_seats)
            for col in range(len(old_seats)):
                for row in range(len(old_seats[col])):
                    occ_seats = check_adjacent_seats(old_seats, col, row)
                    if old_seats[col][row] == 'L' and occ_seats == 0:
                        new_seats[col][row] = "#"
                    elif old_seats[col][row] == '#' and occ_seats >= 4:
                        new_seats[col][row] = 'L'
            seats.append(new_seats)

        return sum([1 for i in range(len(seats[-1])) for j in range(len(seats[-1][i])) if seats[-1][i][j] =='#'])
                            
        
def check_adjacent_seats(seats, col, row):
    occ_seats = 0
    for c in range(col-1, col+2):
        for r in range(row-1, row+2):
            if r >= 0 and c >= 0:
                try:
                    occ_seats += 1 if seats[c][r] == '#' and not (c == col and r == row) else 0
                except Exception as e:
                    pass
    return occ_seats


def check_adjacent_seats_t2(seats, col, row):
    occ_seats = 0
    for c in [-1, 0, 1]:
        for r in [-1, 0, 1]:
            if not(r == 0 and c == 0):
                fac = 1
                try:
                    while seats[col+fac*c][row+fac*r] == '.':
                        fac += 1
                    occ_seats += 1 if seats[col+fac*c][row+fac*r] == '#' and col+fac*c >= 0 and row+fac*r >= 0 else 0
                except Exception as e:
                    pass
    return occ_seats




def print_array(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j], end='')
        print('')

def compare_arrays(old, new):
    for i in range(len(old)):
        for j in range(len(old[i])):
            if old[i][j] != new[i][j]:
                return False
    return True
            
    

def task2(file_name):
    with open(file_name) as f:
        seats = []
        seats.append([list(l) for l in f.read().split('\n')[:-1]])

        while len(seats) < 2 or not compare_arrays(seats[-2], seats[-1]):
            old_seats = seats[-1]
            new_seats = copy.deepcopy(old_seats)
            for col in range(len(old_seats)):
                for row in range(len(old_seats[col])):
                    occ_seats = check_adjacent_seats_t2(old_seats, col, row)
                    if old_seats[col][row] == 'L' and occ_seats == 0:
                        new_seats[col][row] = "#"
                    elif old_seats[col][row] == '#' and occ_seats >= 5:
                        new_seats[col][row] = 'L'
            seats.append(new_seats)
        return sum([1 for i in range(len(seats[-1])) for j in range(len(seats[-1][i])) if seats[-1][i][j] =='#'])


if __name__ == "__main__":
    main()

