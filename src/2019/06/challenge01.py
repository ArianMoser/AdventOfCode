from dataclasses import dataclass

@dataclass
class SpaceObject:
    name: str
    score: int
    previous: int

def main():
    print("AdventOfCode - 06 - Challenge 01")
    f = open("input.txt", "r")
    space_objects = []
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
            #print("{0} after {1} with {2}".format(space_object.name, space_objects[space_object.previous].name, space_object.score))
        print("Score: {0}".format(final_score))
    else:
        print("Error reading the given file name")

def get_object_score(space_objects, space_object):
    if space_object.previous != -1:
        return 1 + get_object_score(space_objects, space_objects[space_object.previous])
    else:
        return 0



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
