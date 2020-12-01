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

class ExceptionFinishedOpcode(Error):
    """ This Exception will be raised when the opcode 99 were received"""
    pass


class Intcoder:
    output = -1
    commands = []
    
    def __init__(self, commands):
        print("Initializing intcoder\n")
        print("Press Enter to start the program...")
        sys.stdin.read(1)
        self.start(commands)

    def start(self):
        #print("Starting intcoder")
        pos = 0
        try:
            while True:
                (self.commands, pos) = self.compute_intcode(self.commands, pos)
        except ExceptionFinishedOpcode:
            #print("The progam finished. Please see output above to get the result")
            pass
        except ExceptionInvalidOpcode:
            print("Error. Received unknown opcode '{0}'".format(self.commands[pos]))
        except Error:
            print(Error.error)

    def compute_intcode(self, inputs, pos):
        instruction = inputs[pos]
        (op_code, mode_1, mode_2, mode_3) = self.convert_opcode(instruction)
        # get value 1
        value_1 = pos+1
        if mode_1 == 0:
            value_1 = inputs[value_1]

        if op_code == 99:
            # stop program
            raise ExceptionFinishedOpcode
        elif op_code == 1 or op_code == 2:
            # addition and multiplication

            # three inputs
            value_2 = pos+2
            if mode_2 == 0:
                value_2 = inputs[value_2]
            value_3 = pos+3
            if mode_3 == 0:
                value_3 = inputs[value_3]

            if op_code == 1:
                inputs[value_3] = inputs[value_1] + inputs[value_2]
            elif op_code == 2:
                inputs[value_3] = inputs[value_1] * inputs[value_2]
            pos += 4

        elif op_code == 3 or op_code == 4:
            # input and output

            # one input
            if op_code == 3:
                inputs[value_1] = self.receive_input()
            elif op_code == 4:
                #print(inputs[value_1])
                self.output = inputs[value_1]
            pos += 2

        elif op_code == 5 or op_code == 6:
            # jump if true/false

            # two inputs
            value_2 = pos+2
            if mode_2 == 0:
                value_2 = inputs[value_2]

            if op_code == 5:
                if inputs[value_1] != 0:
                    pos = inputs[value_2]
                else:
                    pos += 3
            elif op_code == 6:
                if inputs[value_1] == 0:
                    pos = inputs[value_2]
                else:
                    pos += 3

        elif op_code == 7 or op_code == 8:
            # less than or equals

            # three inputs
            value_2 = pos+2
            if mode_2 == 0:
                value_2 = inputs[value_2]
            value_3 = pos+3
            if mode_3 == 0:
                value_3 = inputs[value_3]

            if op_code == 7:
                if inputs[value_1] < inputs[value_2]:
                    inputs[value_3] = 1
                else:
                    inputs[value_3] = 0
            elif op_code == 8:
                if inputs[value_1] == inputs[value_2]:
                    inputs[value_3] = 1
                else:
                    inputs[value_3] = 0
            pos += 4
        else:
            raise ExceptionInvalidOpcode()
        return (inputs, pos)

    def receive_input(self):
        return int(input("Please insert a input: "))

    def convert_opcode(self, instruction):
        opcode      = instruction%100
        instruction = int(instruction / 100)
        param_1     = instruction%10
        instruction = int(instruction / 10)
        param_2     = instruction%10
        instruction = int(instruction / 10)
        param_3     = instruction%10
        return(opcode, param_1, param_2, param_3)
