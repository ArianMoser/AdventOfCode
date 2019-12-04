import sys
from dataclasses import dataclass
import numpy

class Error(Exception):
    """ Base Exception for other exceptions """
    pass

class ExceptionCouldNotOpenFile(Error):
    """ This Exception will be raised if there occured an error during the read handle of an file"""
    pass

class InvalidDirectionException(Error):
    """ This Exception will be raised if an unknown direction is given"""
    pass

class NoInterceptionException(Error):
    """ This Exception will be raised if there is no interception between the two points"""
    pass

@dataclass
class Vector:
    x: int
    y: int

@dataclass
class Move:
    start_point         : Vector
    end_point           : Vector
    direction_vector    : Vector

def main():
    print("AdventOfCode - 03 - Challenge 01")

    wire1_moves         = []
    wire2_moves         = []
    connections         = []
    default_start_point = Vector(0, 0)
    min_distance = 9999999

    try:
        f = open("input.txt", "r")
        if f.mode == 'r':
            f_content = f.read().split('\n')

            # wire 1
            for move in f_content[0].split(','):
                direction_vector = get_vector(move[:1], int(move[1:]))
                if len(wire1_moves) == 0:
                    start_point = default_start_point
                else:
                    start_point = wire1_moves[-1].end_point
                end_point = add_vectors(start_point, direction_vector, 1)
                wire1_moves.append(Move(start_point, end_point, direction_vector))

            # wire 2
            for move in f_content[1].split(','):
                direction_vector = get_vector(move[:1], int(move[1:]))
                if len(wire2_moves) == 0:
                    start_point = default_start_point
                else:
                    start_point = wire2_moves[-1].end_point
                end_point = add_vectors(start_point, direction_vector, 1)
                wire2_moves.append(Move(start_point, end_point, direction_vector))

            for wire1_move in wire1_moves[1:]:
                for wire2_move in wire2_moves[1:]:
                    try:
                        (func_1, func_2) = get_functions(wire1_move, wire2_move)
                        (x, y) = intersection(func_1, func_2)
                        if x <= 1 and y <= 1 and x >= 0 and y >= 0:
                            connections.append(Vector( 
                              wire2_move.start_point.x + y * wire2_move.direction_vector.x, 
                              wire2_move.start_point.y + y * wire2_move.direction_vector.y))
                    except NoInterceptionException:
                        pass

            print("Found {0} interception points".format(len(connections)))
            sys.stdin.read(1)
            for cp in connections:
                if get_score(cp, default_start_point) < min_distance:
                    min_distance = abs(get_score(cp, default_start_point))
                    print("Minimal distance: {0}".format(min_distance))
        else:
            raise ExceptionCouldNotOpenFile 
    except ExceptionCouldNotOpenFile: 
        print("ERROR: Could not open the input file")
    except Error as error:
        print("ERROR: {1}".format(error.error))

def intersection(func_1, func_2):
    # functions: a1x + b1y = c1
    # {a1, b1, c1}

    D   = func_1[0] * func_2[1] - func_2[0] * func_1[1]
    Dx  = func_1[2] * func_2[1] - func_2[2] * func_1[1]
    Dy  = func_1[0] * func_2[2] - func_2[0] * func_1[2]
    if D != 0: 
        x = Dx/D
        y = Dy/D
        return (x, y)
    else:
       raise NoInterceptionException


def get_functions(line_1, line_2):
    # x
    func_1 = []
    func_1.append(line_1.direction_vector.x)
    func_1.append(-1 * line_2.direction_vector.x)
    func_1.append(line_2.start_point.x - line_1.start_point.x)
    #print("Function 1: {0}x + {1}y = {2}".format(func_1[0], func_1[1], func_1[2]))
    # y
    func_2 = []
    func_2.append(line_1.direction_vector.y)
    func_2.append(-1 * line_2.direction_vector.y)
    func_2.append(line_2.start_point.y - line_1.start_point.y)
    #print("Function 2: {0}x + {1}y = {2}".format(func_2[0], func_2[1], func_2[2]))
    return(func_1, func_2)


def get_vector(direction, length):
    if direction == 'U':
        return Vector(0, length)
    elif direction == 'R':
        return Vector(length, 0)
    elif direction == 'D':
        return Vector(0, -1 * length)
    elif direction == 'L':
        return Vector(-1 * length, 0)
    else:
        raise InvalidDirectionException()
    return Vector(0,0)

def add_vectors(sp, dv, mf):
   return Vector(sp.x + mf*dv.x, sp.y + mf*dv.y)

def get_score(sp, cp):
   return abs(cp.x - sp.x) + abs(cp.y - sp.y)

if __name__ == "__main__":
    main()
