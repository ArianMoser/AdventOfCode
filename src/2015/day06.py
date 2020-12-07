import sys

file_name = "inputs/day6.txt"

if len(sys.argv) > 1:
    file_name = sys.argv[1]


def task1(file_name):
    with open(file_name) as f:
        instructions = f.readlines()
        lights = set()
        for inst in instructions:
            inst_spl = inst.split(' ')
            if inst_spl[0] == 'turn':
                sx, sy = map(int, inst_spl[2].split(','))
                ex, ey = map(int, inst_spl[4].split(','))
                if inst_spl[1] == 'on':
                    for x in range(sx, ex+1):
                        for y in range(sy, ey+1):
                            lights.add((x, y))
                elif inst_spl[1] == 'off':
                    for x in range(sx, ex+1):
                        for y in range(sy, ey+1):
                            lights.discard((x, y))
            elif inst_spl[0] == 'toggle':
                sx, sy = map(int, inst_spl[1].split(','))
                ex, ey = map(int, inst_spl[3].split(','))
                for x in range(sx, ex+1):
                    for y in range(sy, ey+1):
                        if (x, y) in lights:
                            lights.discard((x, y))
                        else:
                            lights.add((x, y))
        print("Task1: {} Lights are turned on".format(len(lights)))
                        
                        
def task2(file_name):         
    with open(file_name) as f:
        instructions = f.readlines()
        lights = []
        for x in range(1000):
            tmp = []
            for y in range(1000):
                tmp.append(0)
            lights.append(tmp)

        for inst in instructions:
            inst_spl = inst.split(' ')
            if inst_spl[0] == 'turn':
                sx, sy = map(int, inst_spl[2].split(','))
                ex, ey = map(int, inst_spl[4].split(','))
                if inst_spl[1] == 'on':
                    for x in range(sx, ex+1):
                        for y in range(sy, ey+1):
                            lights[x][y] += 1
                elif inst_spl[1] == 'off':
                    for x in range(sx, ex+1):
                        for y in range(sy, ey+1):
                            if lights[x][y] > 0:
                                lights[x][y] -= 1
            elif inst_spl[0] == 'toggle':
                sx, sy = map(int, inst_spl[1].split(','))
                ex, ey = map(int, inst_spl[3].split(','))
                for x in range(sx, ex+1):
                    for y in range(sy, ey+1):
                        lights[x][y] += 2
        result = 0
        for x in lights:
            for y in x:
                result += y
        print("Task2: The total brightness is {}".format(result))

            
    
            


task2(file_name)



    
