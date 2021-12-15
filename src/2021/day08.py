import sys
import os
import math

SEG_DIG = {
    0 : set("abcefg"),
    1 : set("cf"),
    2 : set("acdeg"),
    3 : set("acdfg"),
    4 : set("bcdf"),
    5 : set("abdfg"),
    6 : set("abdefg"),
    7 : set("acf"),
    8 : set("abcdefg"),
    9 : set("abcdfg")
}


def main():
    global SEG_DIG
    file_name = f"inputs/{sys.argv[0].replace('py', 'txt')}" if len(sys.argv) == 1 else sys.argv[1]
    if not os.path.isfile(file_name):
        raise Exception(f'{file_name} is not a valid file')
    print(f"Challenge {sys.argv[0].split('.')[0].capitalize()}: \n")
    print("**************************")

    # read file
    with open(file_name, 'r') as f:
        lines = f.read().splitlines()

    segments = []
    outputs = []
    for line in lines:
        seg, output = line.split(' | ')
        output = output.split(' ')
        outputs.append(output)
        seg = seg.split(' ')
        segments.append(seg)

    print(f"Result Task1:  {sum(1 if len(seg) in [2, 3, 4, 7] else 0 for el in outputs for seg in el)}")

    res = 0
    for i, el in enumerate(zip(segments, outputs)):
        seg_map = dict()
        let_map = dict()
        seg_map[1] = [segment for segment in el[0] if len(segment) == 2][0]
        seg_map[7] = [segment for segment in el[0] if len(segment) == 3][0]
        seg_map[4] = [segment for segment in el[0] if len(segment) == 4][0]
        seg_map[8] = [segment for segment in el[0] if len(segment) == 7][0]
        let_map['a'] = [letter for letter in seg_map[7] if letter not in seg_map[1]][0]
        let_map['f'] = [letter for letter in seg_map[1] if all(True if letter in segment else False for segment in el[0] if len(segment) == 6)][0]
        let_map['c'] = [letter for letter in seg_map[1] if letter != let_map['f']][0]
        seg_map[6] = [segment for segment in el[0] if len(segment) == 6 and not all(True if letter in segment else False for letter in seg_map[7])][0]
        seg_map[3] = [segment for segment in el[0] if len(segment) == 5 and all(True if letter in segment else False for letter in seg_map[7])][0]
        let_map['g'] = [letter for letter in seg_map[3] if letter not in let_map.values() and all(True if letter else False in segment for segment in el[0] if len(segment) in [5, 6])][0]
        let_map['d'] = [letter for letter in seg_map[3] if letter not in let_map.values()][0]
        let_map['b'] = [letter for letter in seg_map[4] if letter not in let_map.values()][0]
        let_map['e'] = [letter for letter in seg_map[6] if letter not in let_map.values()][0]
        for seg in SEG_DIG.keys():
            if seg not in seg_map.keys():
                seg_map[seg] = set([let_map[letter] for letter in SEG_DIG[seg]])
            else:
                seg_map[seg] = set(seg_map[seg])

        res = res + sum(seg_el * math.pow(10, len(el[1])-i-1) for i, seg in enumerate(el[1]) for seg_el in seg_map.keys() if seg_map[seg_el] == set(seg))
        
    print(f"Result Task2:  {res}")


if __name__ == "__main__":
    main()


