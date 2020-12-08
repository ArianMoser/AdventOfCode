import sys
import re


bags = dict() 


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
    reg = re.compile("\w+ \w+ bag")
    count = -1 # shiny gold bag should not been count
    global bags

    with open(file_name) as f:
        for line in f.read().split('\n'):
            bag_r = [ x.group() for x in re.finditer(reg, line)]
            try:
                bag_name, bag_content = bag_r[0], bag_r[1:]
            except Exception as e:
                #print(e)
                pass
            bags[bag_name] = bag_content

        for bag in bags.keys():
            if parse_bag(bag):
                count +=1
    return count


def task2(file_name):
    reg = re.compile("(|\d+ )\w+ \w+ bag")
    global bags

    with open(file_name) as f:
        for line in f.read().split('\n'):
            bag_r = [ x.group() for x in re.finditer(reg, line)]
            try:
                bag_name, bag_content = bag_r[0], bag_r[1:]
            except Exception as e:
                #print(e)
                pass
            bags[bag_name] = bag_content


    return parse_bag_t2("shiny gold bag")


def parse_bag(bag_name):
    global bags
    ret = False

    if bag_name == 'no other bag':
        return False
    if bag_name == 'shiny gold bag':
        return True
    for bag in bags[bag_name]:
        if not ret:
            ret = ret or parse_bag(bag)
        else:
            return ret
    return ret
        

def parse_bag_t2(bag_name):
    global bags
    ret = 0

    for bag in bags[bag_name]:
        try:
            bag_c = int(bag[:bag.find(' ')])
            bag_n = bag[(bag.find(' ')+1):]
            ret += bag_c + bag_c * parse_bag_t2(bag_n)
        except Exception as e:
            ret += bag_c # if no number is given -> 'no other bag'
            pass
            
    return ret


if __name__ == "__main__":
    main()
