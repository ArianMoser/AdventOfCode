import hashlib
import sys


def main():
    if len(sys.argv) < 2:
        inp = 'abc'
    else:
        inp = sys.argv[1]

    # part 1
    part1 = ''
    i = 0
    for _ in range(8):
        while True:
            hashed = hashlib.md5(f"{inp}{str(i)}".encode()).hexdigest()
            if hashed.startswith("00000"):
                part1 += hashed[5]
                break
            i += 1
        print(i, part1)
        i += 1
    print(f"Part 1: {part1}")

    # part 2
    part2 = [' ' for _ in range(8)]
    i = 0
    for _ in range(8):
        while True:
            hashed = hashlib.md5(f"{inp}{str(i)}".encode()).hexdigest()
            if hashed.startswith("00000"):
                pos = hashed[5]
                if pos.isdecimal() and int(pos) < 8 and part2[int(pos)] == ' ':
                    part2[int(pos)] = hashed[6]
                    break
            i += 1
        print(i, ''.join(part2))
        i += 1
    print(f"Part 2: {''.join(part2)}")


if __name__ == '__main__':
    main()
