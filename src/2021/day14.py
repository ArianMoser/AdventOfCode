import sys
import os
import re
from collections import defaultdict
import string

def main():
    file_name = f"inputs/{sys.argv[0].replace('py', 'txt')}" if len(sys.argv) == 1 else sys.argv[1]
    if not os.path.isfile(file_name):
        raise Exception(f'{file_name} is not a valid file')
    print(f"Challenge {sys.argv[0].split('.')[0].capitalize()}: \n")
    print("**************************")

    # read file
    with open(file_name, 'r') as f:
        polymer, rules_raw = f.read().split('\n\n')

    pol = polymer
    rules = dict()
    rule_list = [r.split(' -> ') for r in rules_raw.split('\n')][:-1]
    for rule in rule_list: rules[rule[0]] = rule[1]

    # task 1
    for step in range(10):\
        # get pairs
        pairs = [list(p) for p in zip(polymer, polymer[1:])]

        polymer = ''.join([p[0] + rules[''.join(p)] for p in pairs]) + pairs[-1][-1]
        print(f'{step+1:2}. Step: {len(polymer)}')

    res= max(polymer.count(l) for l in set(polymer)) - min(polymer.count(l) for l in set(polymer))
    print(f'Result Task1: {res}')

    # task 2
    freq = dict()
    for rule in rules.keys():
        freq[rule] = pol.count(rule)

    for step in range(40):
        # create new freq table and set default values
        new_freq = dict()
        for rule in rules.keys(): new_freq[rule] = 0

        # iterate over freq table
        for f in freq.keys(): 
            new_freq[f[0] + rules[f]] += freq[f]
            new_freq[rules[f] + f[1]] += freq[f]

        freq = new_freq.copy()
        print(f'{step+1:2}. Step: {sum(f for f in freq.values())}')

    elements = defaultdict(lambda: 0, dict())
    for pair in freq.keys():
        elements[pair[0]] += freq[pair]
        elements[pair[1]] += freq[pair]
    for el in elements.keys():
        elements[el] = round(elements[el]/2 + 0.1)
    res = max(el for el in elements.values()) - min(el for el in elements.values())
        
    print(f'Result Task2: {res}')
            

if __name__ == "__main__":
    main()
