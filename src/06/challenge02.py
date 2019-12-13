from dataclasses import dataclass

@dataclass
class SpaceObject:
    name: str
    score: int
    previous: int

def main():
    print("AdventOfCode - 06 - Challenge 01")
    f = open("input-example2.txt", "r")
    space_objects = []
    san_road = []
    you_road = []
    if f.mode == 'r':
        f_content = f.read()
        for relationship in f_content.split('\n'):
            try:
                inner_name = relationship.split(')')[0]
                outer_name = relationship.split(')')[1]
                print('{0} - {1}'.format(inner_name, outer_name))
                space_objects, inner_id = get_object_id(space_objects, inner_name)
                space_objects, outer_id = get_object_id(space_objects, outer_name)
                space_objects[outer_id].previous = inner_id
            except Exception as e:
                print(e)
        for space_object in space_objects:
            space_object.score = get_object_score(space_objects, space_object)
        print("Found {0} different objects".format(len(space_objects)))
        final_score = 0
        for space_object in space_objects:
            final_score += space_object.score
            if space_object.name == 'SAN' :
                san_road = get_road(space_objects, space_object)
            elif space_object.name == 'YOU':
                you_road = get_road(space_objects, space_object)
        print("Score: {0}".format(final_score))

        you_road = list(reversed(you_road))
        san_road = list(reversed(san_road))

        for i in range(0, min(len(you_road), len(san_road))):
            if san_road[i] != you_road[i]:
                print("{0} is the first different element".format(i))
                res = (len(san_road) - i) + (len(you_road) - i) 
                print("The result is {0} steps".format(res))
                break
    else:
        print("Error reading the given file name")

def get_object_score(space_objects, space_object):
    if space_object.previous != -1:
        return 1 + get_object_score(space_objects, space_objects[space_object.previous])
    else:
        return 0

def get_road(space_objects, space_object):
    road_array = []
    while space_object.previous != -1:
        road_array.append(space_object.previous)
        space_object = space_objects[space_object.previous]
    return road_array


def get_object_id(space_objects, target_name):
    id = 0
    for space_object in space_objects:
        if space_object.name == target_name:
            return (space_objects, id)
        id += 1
    #print("Adding space_object named {0}".format(target_name))
    space_objects.append(SpaceObject(target_name, 0, -1))
    return (space_objects, id)


if __name__ == '__main__':
    main()
