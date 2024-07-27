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
            hashed = hashlib.md5(f"{inp}{str(i)}".encode())
            if hashed.hexdigest().startswith("00000"):
                part1 += hashed.hexdigest()[5]
                break
            i += 1
        print(i, part1)
        i += 1
    print(f"Part 1: {part1}")


if __name__ == '__main__':
    main()
