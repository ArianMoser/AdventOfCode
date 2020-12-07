with open("inputs/day1.txt") as f:
    f_content = f.read()
    floor = 0
    print("Task1: ")
    for c in f_content:
        floor = (floor + 1 if c == "(" else floor-1)
    print("Floor {}\n".format(floor+1))

    print("Task2: ")
    floor = 0
    i = 0
    try:
        for c in f_content:
            i = i+1
            floor = (floor + 1 if c == "(" else floor-1)
            if floor == -1:
                raise Exception
    except Exception:
        print("Santa reaches basement at position {} for the first time".format(i))



