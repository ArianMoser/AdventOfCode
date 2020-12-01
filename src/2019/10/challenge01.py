from dataclasses import dataclass
import sys

class Error(Exception):
    """ Base Exception for other exceptions """
    pass

class CouldNotSeeAsteroid(Error):
    """ The source asteroid is not able to see the taget asteroid """
    pass

@dataclass
class Vector:
    x: int
    y: int

@dataclass
class Asteroid:
    coords: Vector
    value: int

@dataclass
class LinearFunction:
    m: float
    b: float

def get_asteroids(file_name):
    asteroids = []
    f = open(file_name, "r")
    if f.mode == 'r':
        f_content = f.read()
        y = 0
        for line in f_content.split('\n'):
            x = 0
            for char in line:
                if char == '#':
                    asteroids.append(Asteroid(Vector(x, y), 1))
                x += 1
            y += 1
    print("Found {0} asteroids".format(len(asteroids)))
    return asteroids

def get_linear_function(point_1, point_2):
    m = (point_2.y - point_1.y) / (point_2.x - point_1.x)
    b = point_1.y - point_1.x * m
    return LinearFunction(m, b)

def point_is_on_function(function, coords):
    if function.m * coords.x + function.b == coords.y:
        return True
    else:
        return False

def main():
    print("AdventOfCode - 10 - Challenge 01")
    asteroids = get_asteroids('input-example.txt')

    for source_asteroid in asteroids:
        for target_asteroid in asteroids:
            if target_asteroid == source_asteroid:
                continue
            try:
                # get linear function
                function = get_linear_function(source_asteroid.coords, target_asteroid.coords)
                for other_asteroid in asteroids:
                    if other_asteroid == source_asteroid or other_asteroid == target_asteroid:
                        continue
                    if min(source_asteroid.coords.x, target_asteroid.coords.x) < other_asteroid.coords.x < max(target_asteroid.coords.x, source_asteroid.coords.x):
                        if point_is_on_function(function, other_asteroid.coords):
                            raise CouldNotSeeAsteroid
                    elif source_asteroid.coords.x == target_asteroid.coords.x == other_asteroid.coords.x and min(source_asteroid.coords.y, target_asteroid.coords.y) < other_asteroid.coords.y < max(source_asteroid.coords.y, target_asteroid.coords.y):
                        raise CouldNotSeeAsteroid
                source_asteroid.value += 1
            except CouldNotSeeAsteroid:
                continue
            except ZeroDivisionError:
                pass

    #tmp
    """
    for asteroid in asteroids:
        print("Asteroid: ({0}|{1}) with value {2}".format(asteroid.coords.x, asteroid.coords.y, asteroid.value))
        sys.stdin.read(1)
    """

    # Output
    min_value = 0
    for asteroid in asteroids:
        if asteroid.value > min_value:
            min_value = asteroid.value
            print("Asteroid: ({0}|{1}) with value {2}".format(asteroid.coords.x, asteroid.coords.y, asteroid.value))

if __name__ == "__main__":
    main()
