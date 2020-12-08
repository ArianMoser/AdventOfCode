import sys

# global vars
acc = 0
instructions = []
hist = 0


def main():
    file_name = "input.txt"
    task2_bool = False
    print("Challenge day 4: \n")
    print("**************************")
    try:
        file_name = sys.argv[1]
        task2_bool = True if sys.argv[2].lower() in ["true", "on", "1", "yes"] else False
    except Exception as e:
        print("(Parameter Usage: dayx.py <<file_name>> <<task2 (True|False)>>)")
    print("Using values: \n  Filename: {} \n  Task2: {}".format(file_name, task2_bool))
    print("**************************\n")
    if task2_bool:
        print("Answers given: {}".format(task2(file_name)))
    else:
        print("Answers given: {}".format(task1(file_name)))


def task1(file_name):
    hist = instuctions = []
    
    with open(file_name) as f:
        instructions = f.read().split('\n')

    return execute_code(instructions, hist)[-1][1]


def execute_code(instructions, hist):
    if len(hist) == 0:
        nxt = acc = 0
    else:
        nxt, acc = hist[-1]
        hist = hist[:-1]
    while nxt not in [n[0] for n in hist] and nxt < len(instructions):
        hist.append((nxt, acc))
        op, arg = instructions[nxt].split(' ')
        if op == 'jmp':
            nxt += int(arg)
            continue
        if op == 'nop':
            pass
        elif op == 'acc':
            acc += int(arg)
        nxt +=1

    return hist



def task2(file_name):
    hist = instructions = []
    with open(file_name) as f:
        instructions = f.read().split('\n')[:-1]
        instructions.append('nop +1') #todo: makes this clean (fixes bug that acc is not updated in the last step

    hist = execute_code(instructions, hist)
    for i in range(len(hist)):
        inst = instructions[hist[i][0]]
        if inst.split(' ')[0] not in ['nop', 'jmp']:
            continue
        else:
            inst_upd = instructions.copy()
            if inst.startswith('nop'):
                inst_upd[hist[i][0]] = inst.replace('nop', 'jmp')
            elif inst.startswith('jmp'):
                inst_upd[hist[i][0]] = inst.replace('jmp', 'nop')
        
            if execute_code(inst_upd, hist[:i])[-1][0] == len(instructions)-1:
                hist_tmp = execute_code(inst_upd, hist[:i])
                print(hist_tmp)
                return hist_tmp[-1][1]
    return 0


if __name__ == "__main__":
    main()
