import sys


def main():
    file_name = "input.txt"
    task2_bool = False
    print("Challenge day 13: \n")
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
    with open(file_name) as f:
       f_content = f.read()
    timestamp = int(f_content.split('\n')[0])
    bus_list = [int(bus) for bus in f_content.split('\n')[1].split(',') if bus !='x']
    bus_plan = dict()
    for bus in bus_list: 
        bus_plan[bus] = (int(timestamp/bus) + 1) * bus - timestamp 
    return min(bus_plan, key=bus_plan.get) * bus_plan[min(bus_plan, key=bus_plan.get)]



def task2(file_name):
    with open(file_name) as f:
       f_content = f.read()
    inp_list = f_content.split('\n')[1].split(',')
    dep_plan = dict() 
    for t in range(len(inp_list)):
        if inp_list[t] != 'x':
            dep_plan[int(inp_list[t])] = int(t)
    print(dep_plan)

    i = 1
    max_value = max(dep_plan)
    print(max_value)
    while True:
        timestamp = i * max_value - dep_plan[max_value]
        if check_dep_plan(dep_plan, timestamp):
            print(i)
            break
        i += 1
    return i

    
def check_dep_plan(dep_plan, timestamp):
    for bus in dep_plan.keys(): 
        if (timestamp + dep_plan[bus]) % bus != 0:
            return False
    return True
    


if __name__ == "__main__":
    main()

