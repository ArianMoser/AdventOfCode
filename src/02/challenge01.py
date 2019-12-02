
def main():
    print("AdventOfCode - 02 - Challenge 01")
    inputs = []
    f = open("input.txt", "r")
    if f.mode == 'r':
        f_content = f.read()
        inputs = f_content.split(',')
        pos = 0
        opcode=0
        while opcode!= 99 pos < len(inputs-4):
            opcode =  int(inputs[pos+0])
            value_1 = int(inputs[pos+1])
            value_2 = int(inputs[pos+2])
            res_pos = int(inputs[pos+3])
            pos +=4




if __name__ == "__main__":
    main()
