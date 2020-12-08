import sys
import re

equ = dict()
file_name = 'inputs/day07.txt'
if len(sys.argv) > 1:
    file_name = sys.argv[1]

def solve(e):
    global equ
    try:
        op = [o.group() for o in re.finditer(re.compile('[A-Z]+'), equ[e])]
    except Exception as ex:
        try:
            return int(e)
        except Exception:
            return solve(equ[e])
        
    if len(op) == 0:
        try:
            return int(e)
        except Exception:
            return solve(equ[e])
    else:
        ret = 0
        inp = [i.group() for i in re.finditer(re.compile('([a-z]+|[0-9]+)'), equ[e])]
        if op[0] == 'NOT':
            ret = ~solve(inp[0])
        elif op[0] == 'AND':
            ret = solve(inp[0]) & solve(inp[1])
        elif op[0] == 'OR':
            ret = solve(inp[0]) | solve(inp[1])
        elif op[0] == 'RSHIFT':
            ret = solve(inp[0]) >> solve(inp[1])
        elif op[0] == 'LSHIFT':
            ret = solve(inp[0]) << solve(inp[1])
        print(f"{e}: {ret}")
        equ[e] = int(ret)
        return ret
        

with open(file_name) as f:
    instr = f.read().split('\n')[:-1]
    for i in instr:
        n, e = i.split('->')
        equ[e.strip()] = n.strip()

    for e in equ.keys():
        solve(e)

    print(f"a: {equ['a']}")




