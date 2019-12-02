

def main():
    print("AdventOfCode - Challenge01")
    inputs = []
    res = 0
    f = open("input.txt", "r")
    if f.mode == 'r':
        f_content = f.read()
        for line in f_content.splitlines():
            inputs.append(int(line))

        for input in inputs:
            res += int(input/3) - 2

        print('The result is: ' + str(res))

if __name__ == "__main__":
    main()
