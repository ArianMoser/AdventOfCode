import sys

class Error(Exception):
    """ Base Exception for other exceptions """
    pass

class ExceptionFoundValue(Error):
    """ This Exception will be raised when the target value is reached """
    pass

class ExceptionInvalidOpcode(Error):
    """ This Exception will be raised when an unknown opcode is given """
    pass

def main():
    print("AdventOfCode - 02 - Challenge 02")
    target_value = 19690720
    def_inputs = []
    f = open("input.txt", "r")
    if f.mode == 'r':
        f_content = f.read()
        def_inputs = list(map(int,f_content.split(',')))
    try:
        for noun in range(0, 99):
            for verb in range(0, 99):
                    print("Testing noun {0} and verb {1}".format(noun, verb))
                    # resets inputs to initial state
                    inputs = def_inputs.copy()
                    # initial values
                    inputs[1] = noun
                    inputs[2] = verb
                    pos = 0
                    opcode=0
                    while opcode != 99 and pos < len(inputs)-4 :
                        opcode =  inputs[pos+0]
                        inputs = compute_intcode(opcode, inputs[pos+1], 
                        inputs[pos+2], inputs[pos+3], inputs)
                        pos +=4
                    if inputs[0] == target_value:
                        raise ExceptionFoundValue()

    except ExceptionFoundValue:
        print("Reached the target value {0} with noun={1} and verb={2}".format( 
        target_value, noun, verb))
        print("The result is {0}".format((100 * noun + verb)))
    except ExceptionInvalidOpcode:
        print("Error. Received unknown opcode '{0}'".format(opcode))
    except Error:
        print(Error.error)

def compute_intcode(opcode, pos_value_1, pos_value_2, pos_res, inputs):
    #print("{0}: ({1}|{2}) -> {3}".format(opcode, pos_value_1, pos_value_2, pos_res))
    if opcode == 1:
        inputs[pos_res] = inputs[pos_value_1] + inputs[pos_value_2]
    elif opcode == 2:
        inputs[pos_res] = inputs[pos_value_1] * inputs[pos_value_2]
    elif opcode == 99:
        #print("Finished.\nOn position 0 is {0}".format(str(inputs[0])))
        pass
    else:
        raise ExceptionInvalidOpcode()
    return inputs

if __name__ == "__main__":
    main()
