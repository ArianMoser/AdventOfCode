
def main():
    print("AdventOfCode - 02 - Challenge 01")
    inputs = []
    f = open("input_challenge1.txt", "r")
    if f.mode == 'r':
        f_content = f.read()
        inputs = f_content.split(',')
        pos = 0
        opcode=0
        while opcode != 99 and pos < len(inputs)-4 :
            opcode =  int(inputs[pos+0])
            inputs = compute_intcode(opcode, int(inputs[pos+1]), 
              int(inputs[pos+2]), int(inputs[pos+3]), inputs)
            pos +=4

def compute_intcode(opcode, pos_value_1, pos_value_2, pos_res, inputs):
    print("{0}: ({1}|{2}) -> {3}".format(opcode, pos_value_1, pos_value_2, pos_res))
    if opcode == 1:
        inputs[pos_res] = int(inputs[pos_value_1]) + int(inputs[pos_value_2])
    elif opcode == 2:
        inputs[pos_res] = int(inputs[pos_value_1]) * int(inputs[pos_value_2])
    elif opcode == 99:
        print("Finished.\nOn position 0 is {0}".format(str(inputs[0])))
    else:
        print("Error. Received unknown opcode '{0}'".format(opcode))
    return inputs

if __name__ == "__main__":
    main()
