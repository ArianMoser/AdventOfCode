import sys
import os


def main():
    file_name = f"inputs/{sys.argv[0].replace('py', 'txt')}" if len(sys.argv) == 1 else sys.argv[1]
    if not os.path.isfile(file_name):
        raise Exception(f'{file_name} is not a valid file')
    print(f"Challenge {sys.argv[0].split('.')[0].capitalize()}: \n")
    print("**************************")

    coords = []
    # read file
    with open(file_name, 'r') as f:
        coords_raw, fold_raw = f.read().split('\n\n')
        #coords = [el.split(',') for el in f.read().splitlines()]
    coords = [tuple(map(int, c.split(','))) for c in coords_raw.split('\n')]
    folds = [(f.split('=')[0][-1], int(f.split('=')[1])) for f in fold_raw.split('\n')[:-1]]
    for i, fold in enumerate(folds):
        #print_coords(coords)
        new_coords = []
        for coord in coords:
            if fold[0] == 'x': 
                if coord[0] < fold[1]: new_coords.append(coord)
                elif 0<= 2*fold[1] - coord[0]: new_coords.append((2*fold[1] - coord[0], coord[1]))
            elif fold[0] == 'y':
                if coord[1] < fold[1]: new_coords.append(coord)
                elif 0<= 2*fold[1] - coord[1]: new_coords.append((coord[0], 2*fold[1]-coord[1]))
        coords = [ coord for coord in new_coords]
        if i == 0:
            print(f"Result Task1: {len(set(coords))}")
    print_coords(coords)


def print_coords(coords):
    #print(coords)
    for y in range(max(coord[1] for coord in coords)+1):
        for x in range(max(coord[0] for coord in coords)+1):
            if (x, y) in coords: print('#', end='')
            else: print(' ', end='')
        print('')
    sys.stdin.read(1)
        

if __name__ == "__main__":
    main()
