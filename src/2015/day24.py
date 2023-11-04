import os
import sys

groups = []

def main():
    input_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'inputs')
    input_file = os.path.join(input_dir, 'day24.txt')
    with open(input_file, 'r') as f:
        content = f.read()
    packages = list(map(int, content.split('\n')[:-1]))
    weight = int(sum(packages)/3)
    groups = []
    calculate(packages, [], 0, weight, groups)
    print(groups)

def calculate(packages_left, packages_used, weight, dest_weight, groups):
    if weight == dest_weight: 
        groups.append([packages_used, packages_left])
        print(groups[-1])
        return True
    elif weight > dest_weight: return False
    for i, p in enumerate(packages_left):
        calculate([g for g in packages_left if g != p], [*[g for g in packages_used], p], weight+p, dest_weight, groups)
    return False


if __name__ == '__main__':
    main()
