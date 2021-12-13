import sys
import os
from dataclasses import dataclass

max_x = max_y = 0
flash_counter = 0

@dataclass
class Octopus:
    coords: (int, int)
    energy: int
    neighbours: list
    flashed: bool
    def calculate_neighbours(self):
        global max_x, max_y
        for x in range(self.coords[0]-1, self.coords[0]+2):
            for y in range(self.coords[1]-1, self.coords[1]+2):
                if 0<=x<=max_x and 0<=y<=max_y and self.coords != (x, y): 
                    self.neighbours.append((x,y))


def main():
    file_name = f"inputs/{sys.argv[0].replace('py', 'txt')}" if len(sys.argv) == 1 else sys.argv[1]
    if not os.path.isfile(file_name):
        raise Exception(f'{file_name} is not a valid file')
    print(f"Challenge {sys.argv[0].split('.')[0].capitalize()}: \n")
    print("**************************")

    # read file
    with open(file_name, 'r') as f:
        lines = f.read().splitlines()

    oc_list = dict()
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            oc_list[(x, y)] = Octopus((x, y), int(c), [], False)

    global max_x, max_y
    max_x, max_y = (max(o[0] for o in oc_list.keys()), max(o[1] for o in oc_list.keys()))

    # calculate neighbours
    for oc in oc_list.keys():
        oc_list[oc].calculate_neighbours()

    counter = 0
    step = 1
    while True:
        for oc in oc_list.values(): oc.energy = oc.energy+1
        check_flashing(oc_list, oc_list.keys())
        for oc in oc_list.values():
            if oc.flashed: 
                oc.energy = 0 
                counter += 1
                oc.flashed = False
        if step == 100: print(f'Result Task1: {counter}')
        if len(oc_list) == len([oc for oc in oc_list.values() if oc.energy == 0]): break
        step += 1
    print(f'Result Task2: {step}')


def check_flashing(oc_list, coords):
    for oc in [oc_list[c] for c in coords]:
        if oc.flashed == False and oc.energy > 9:
            oc.flashed = True
            for el in oc.neighbours: oc_list[el].energy += 1
            check_flashing(oc_list, oc.neighbours)


if __name__ == "__main__":
    main()


