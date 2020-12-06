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
        print("Your Seat ID is: {}".format(task2(file_name)))
    else:
        print("Max Seat ID is: {}".format(max(task1(file_name))))


def task1(file_name):
    seat_ids = []
    with open(file_name) as f:
        for line in f.readlines():
            row = ''
            seat = ''
            for c in line[0:7]:
                if c == 'B':
                    row += ('1')
                else:
                    row += ('0')
            for c in line[7:]:
                if c == 'R':
                    seat += ('1')
                elif c == 'L':
                    seat += ('0')
            seat = int(seat, 2)
            row = int(row, 2)
            seat_ids.append(int(8*row+seat))
    return seat_ids


def task2(file_name):
    seat_ids = set(task1(file_name))
    seats_comp = set(range(min(seat_ids), max(seat_ids)))
    seat_miss = seats_comp.symmetric_difference(seat_ids)
    for seat in seat_miss:
        if seat+1 in seat_ids and seat-1 in seat_ids:
            return seat
    return 0


if __name__ == "__main__":
    main()
