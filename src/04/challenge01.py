
def main():
    print("AdventOfCode - 04 - Challenge 01")
    start_value = 165432
    end_value = 707912
    count = 0

    for number in range(start_value,end_value):
        if check_duplicate(number) and not check_decreasing(number):
            count +=1

    print("Found {0} numbers in the given range".format(count))

def check_duplicate(number):
    index = 0
    str_number = str(number)
    while index < 5:
        if str_number[index] == str_number[index+1]:
            return True
        index += 1
    return False

def check_decreasing(number):
    index = 0
    str_number = str(number)
    while index < 5:
        if str_number[index] > str_number[index+1]:
            return True
        index += 1
    return False


if __name__ == "__main__":
    if check_duplicate(124456):
        print("Duplicate")
    else:
        print("No Duplicate")
    if check_decreasing(124456):
        print("Decreasing")
    else:
        print("Not Decreasing ")
    main()
