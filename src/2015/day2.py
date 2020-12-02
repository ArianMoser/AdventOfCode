with open("inputs/day2.txt") as f:
    # Task 1
    print("Task2: ")
    result = 0
    for line in f:
        l, w, h = list(map(int, line.split("x")))
        result = result + 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)
    print("{} sqare feet of wrapping paper is needed".format(result))

with open("inputs/day2.txt") as f:
    # Task 2
    print("\nTask2: ")
    result = 0
    for line in f:
        sides = list(map(int, line.split("x")))
        # bubble sort
        for i in range(len(sides)-1):
            if sides[i] > sides[i+1]:
                tmp = sides[i]
                sides[i] = sides[i+1]
                sides[i+1] = tmp
        result = result + sides[0]*sides[1]*sides[2] + 2*sides[0] + 2*sides[1]
    print("{} feet of ribbon needed".format(result))



        

