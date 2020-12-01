def main():
    print("AdventOfCode - Challenge02")
    inputs = []
    res = 0
    f = open("input.txt", "r")
    if f.mode == 'r':
        f_content = f.read()
        for line in f_content.splitlines():
            inputs.append(int(line))
        for input in inputs:
            res += calculate_fuel(input)
        print('The result is: ' + str(res))

def calculate_fuel(mass):
    fuel = int(mass/3) - 2
    if fuel > 0:
        return fuel + calculate_fuel(fuel)
    else:
        return 0

if __name__ == "__main__":
    main()
