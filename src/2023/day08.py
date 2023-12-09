import os
import sys
import re
import math

def check_nodes(node):
    for n in node:
        if n[2] != 'Z': return True
    return False

def main(input_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        f_content = f.read()
    directions, nodes_raw = f_content.split("\n\n")
    nodes = {} 
    for node in nodes_raw.splitlines():
        nodes[node.split(' ')[0]] = re.search(r'.*?\(([0-9A-Z]{3}), ([0-9A-Z]{3})\)', node).groups()

    # task 1
    """
    res = 0
    node = 'AAA'
    while node != 'ZZZ':
        direction = directions[res % len(directions)] 
        if direction == 'L': node = nodes[node][0]
        elif direction == 'R': node = nodes[node][1]
        res += 1
    print(f"Task 1: {res}")
    """

    # task 2
    res = 0
    node = [n for n in nodes.keys() if n[2] == 'A']
    functions = []

    # check for each node when they reoccure
    for n in node:
        node_rows = []
        res = 0
        while True:
            # check if reoccuring part occured
            #print(res, n, res % len(directions))
            if (n, res % len(directions)) in node_rows: 
                node_rows.append((n, res % len(directions)))
                break
            node_rows.append((n, res % len(directions)))

            # calculate z_offset
            if n[2] == 'Z': 
                z_offset = res


            # calculate next node
            direction = directions[res % len(directions)] 
            if direction == 'L': new_node = nodes[n][0]
            elif direction == 'R': new_node = nodes[n][1]
            res += 1
            n = new_node
        
        # get formular
        for j, el in enumerate(node_rows):
            if el == node_rows[-1]: 
                print(f'f(x)= {res-j}x + {((z_offset-j)+j) % (res-j)}')
                functions.append(res-j)
                break

    print(f'Task 2: {math.lcm(*functions)}')

if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else: 
        input_file = os.path.join(os.path.dirname(__file__), \
                                'inputs', 
                                sys.argv[0].replace("py", "txt"))
        main(input_file)
