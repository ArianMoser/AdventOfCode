import os
import sys
import re
from dataclasses import dataclass

@dataclass
class Map:
    start: int
    end: int
    formular: int
    def __init__(self, dst_start, src_start, length):
        self.start = src_start
        self.end = src_start + length -1
        self.formular = dst_start - src_start
    def calculate_range(self, start, end):
        length = end - start
        pre_range = mid_range = post_range = ()
        # calculate pre range
        if end < self.start:
            pre_range = (start, end)
            return (pre_range, (), ())
        if start < self.start:
            pre_range = (start, self.start-1)
        # calculate mid range
        if self.start <= start and end <= self.end:
            mid_range = (start + self.formular, end + self.formular)
            return ((), mid_range, ())
        mid_range = (max(self.start, start) + self.formular, \
                    min(self.end, end) + self.formular)
        # calculate post range
        if start > self.end: 
            post_range = (start, end)
            return ((), (), post_range)
        if end > self.end:
            post_range = (self.end + 1, end)
        return (pre_range, mid_range, post_range)
        
        

def parse_content(f_content):
    splitted = f_content.split("\n\n")
    seeds = list(map(int, splitted[0].split(' ')[1:]))
    seeds = list((seeds[i], seeds[i] + seeds[i+1]-1) for i in range(0, len(seeds), 2))
    maps = {}
    for split in splitted[1:]:
        new_map = []
        lines = split.splitlines()
        for line in lines[1:]:
            mapping = Map(*map(int, line.split(' ')))
            new_map.append(mapping)
        maps[lines[0].split(" ")[0]] = new_map
    return seeds, maps


def main(input_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        f_content = f.read()

    # task 2
    seeds, maps = parse_content(f_content)
    res = []
    for map_name, map_values in maps.items():
        new_seeds = []
        for seed in seeds:
            if seed == (): continue
            pre = mid = post = ()
            for map_value in map_values:
                pre, mid, post = map_value.calculate_range(*seed)
                if mid != (): 
                    new_seeds.append(mid)
                    seeds.append(pre)
                    seeds.append(post)
                    break
            if mid == ():
                new_seeds.append(seed)
        seeds = list(set(new_seeds))

    print(f'Task 2: {min([min(seed) for seed in seeds if seed != ()])}')


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else: 
        input_file = os.path.join(os.path.dirname(__file__), \
                                'inputs', 
                                sys.argv[0].replace("py", "txt"))
