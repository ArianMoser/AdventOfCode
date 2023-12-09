import os
import sys
import re
from dataclasses import dataclass

@dataclass
class Map:
    dst_start: int
    src_start: int
    length: int
    def calculate_value(self, inp):
        if inp >= self.src_start and inp <= self.src_start + self.length:
            return (inp-self.src_start) + self.dst_start
        return None
    def calculate_formular(self):
        return self.src_start - self.dst_start

def parse_content(f_content):
    splitted = f_content.split("\n\n")
    seeds = list(map(int, splitted[0].split(' ')[1:]))
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
    #lines = f_content.splitlines()

    seeds, maps = parse_content(f_content)
    # task 1
    res = []
    for seed in seeds:
        status = 'seed'
        while status != 'location':
            for map_name, map_values in maps.items():
                if status != map_name.split('-to-')[0]:
                    continue
                for map_value in map_values:
                    if map_value.calculate_value(seed) != None:
                        seed = map_value.calculate_value(seed)
                        break
                status = map_name.split('-to-')[1]
                break
        res.append(seed)

    print(f"Task 1: {min(res)}")

    # calculate formular
    #for map_name, map_values in maps.items():
    #    print(f'{map_name}: {min([map_value.calculate_formular() for map_value in map_values])}')

    seeds, maps = parse_content(f_content)
    new_seeds = []
    for i in range(0, len(seeds), 2):
        print(len(range(seeds[i], seeds[i]+seeds[i+1])))
        new_seeds.append((seeds[1], seeds[i] + seeds[i+1]))
        
    print(new_seeds)


    # task 2
    #res = []
    for map_name, map_values in maps.items():
        print(map_name)
        for seed in new_seeds:
            




    """
    for seed in new_seeds:
        status = 'seed'
        while status != 'location':
            for map_name, map_values in maps.items():
                if status != map_name.split('-to-')[0]:
                    continue
                for map_value in map_values:
                    if map_value.calculate_value(seed) != None:
                        seed = map_value.calculate_value(seed)
                        break
                status = map_name.split('-to-')[1]
                break
        res.append(seed)
    print(f"Task 2: {min(res)}")
    """

if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else: 
        input_file = os.path.join(os.path.dirname(__file__), \
                                'inputs', 
                                sys.argv[0].replace("py", "txt"))
        main(input_file)
