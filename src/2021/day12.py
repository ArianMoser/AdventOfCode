import sys
import os
import re

possibilities = 0

def main():
    file_name = f"inputs/{sys.argv[0].replace('py', 'txt')}" if len(sys.argv) == 1 else sys.argv[1]
    if not os.path.isfile(file_name):
        raise Exception(f'{file_name} is not a valid file')
    print(f"Challenge {sys.argv[0].split('.')[0].capitalize()}: \n")
    print("**************************")

    # read file
    with open(file_name, 'r') as f:
        lines_splitted = [line.split('-') for line in f.read().splitlines()]
    pathes = dict()
    for p in lines_splitted:
        if p[0] in pathes.keys(): pathes[p[0]].append(p[1])
        else: pathes[p[0]] = [p[1]]
        if p[0] != 'start':
            if p[1] in pathes.keys(): pathes[p[1]].append(p[0])
            else: pathes[p[1]] = [p[0]]

    # optimization
    del pathes['end']
    
    # task1
    find_pathes(['start'], pathes)
    global possibilities
    print(f"Result Task1: {possibilities}")

    # task 2
    possibilities = 0 
    find_pathes2(['start'], pathes)
    print(f"Result Task2: {possibilities}")

def find_pathes2(visited, pathes):
    if visited[-1] == 'start' and len(visited) > 1: return False
    elif visited[-1] == 'end': 
        global possibilities
        possibilities += 1
        return False
    elif (visited.count(visited[-1]) > 1 and visited[-1].islower()):
        if any(True if visited[:-1].count(p) > 1 else False for p in [p for p in visited if p.islower()]):
            return False
    for path in pathes[visited[-1]]:
        visited.append(path)
        find_pathes2(visited, pathes)
        visited.pop()
        
def find_pathes(visited, pathes):
    global possibilities
    if visited[-1] == 'end': 
        possibilities += 1
        return False
    elif visited.count(visited[-1]) > 1 and re.match('[a-z]+', visited[-1]):
        return False
    for path in pathes[visited[-1]]:
        find_pathes([*[p for p in visited],path], pathes)

if __name__ == "__main__":
    main()


