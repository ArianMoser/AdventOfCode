def uniq(lst):
    last = object()
    for item in lst:
        if item == last:
            continue
        yield item
        last = item

def main():
    with open("inputs/day3.txt") as f:
        f_content = f.read()
        # Task 1
        x, y = 0, 0
        presents = []
        for c in f_content:
            if c == "^":
                y=y+1
            elif c == "v":
                y=y-1
            elif c == ">":
                x=x+1
            elif c == "<":
                x=x-1
            presents.append([x,y])
        print(len(set(map(tuple, presents))))

        # Task 2
        x, y, xr, yr = 0, 0, 0, 0
        presents = []
        i = 0
        for c in f_content:
            if i%2 == 0:
                if c == "^":
                    y=y+1
                elif c == "v":
                    y=y-1
                elif c == ">":
                    x=x+1
                elif c == "<":
                    x=x-1
                presents.append([x,y])
            else:
                if c == "^":
                    yr=yr+1
                elif c == "v":
                    yr=yr-1
                elif c == ">":
                    xr=xr+1
                elif c == "<":
                    xr=xr-1
                presents.append([xr,yr])
            i = i+1
        print(len(set(map(tuple, presents))))

if __name__ == "__main__":
    main()
