import sys
import re

required_fields = {
  'byr': '^(19[2-9][0-9])|(200[0-2])$', 
  'iyr': '^20(1[0-9]|20)$', 
  'eyr': '^20(2[0-9]|30)$', 
  'hgt': '^(1[5-8][0-9]|19[0-4])cm|(59|6[0-9]|7[0-6])in$', 
  'hcl': '^#[0-9a-f]{6}$', 
  'ecl': '^(amb)|(blu)|(brn)|(gry)|(grn)|(hzl)|(oth)$', 
  'pid': '^[0-9]{9}$'
  } 
#  'cid']
  

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
        print("Found {} valid passports".format(task2(file_name)))
    else:
        print("Found {} valid passports".format(task1(file_name)))


def task2(file_name):
    with open(file_name) as f:
        valid_passports = 0
        passports_raw = f.read().split('\n\n')
        f.close()
        for passport_raw in passports_raw:
            passport = {}
            passport_raw = passport_raw.replace(' ', '\n')
            for line in passport_raw.split('\n'):
                try:
                    passport[line.split(':')[0]] = line.split(':')[1]
                except Exception as e:
                    pass
            try:
                for field in required_fields.keys():
                    if not re.compile(required_fields[field]).match(passport[field]):
                        raise Exception("{}: invalid: {}".format(field, passport[field]))
                valid_passports = valid_passports + 1
            except Exception as e:
                print(e)
    return valid_passports
            
        

def task1(file_name):
    with open(file_name) as f:
        valid_passports = 0
        passports_raw = f.read().split('\n\n')
        f.close()
        for passport_raw in passports_raw:
            passport = {}
            passport_raw = passport_raw.replace(' ', '\n')
            for line in passport_raw.split('\n'):
                try:
                    passport[line.split(':')[0]] = line.split(':')[1]
                except Exception as e:
                    pass
            try:
                for field in required_fields.keys():
                    passport[field]
                valid_passports = valid_passports + 1
            except Exception as e:
                pass

    return valid_passports
    

if __name__ == "__main__":
    main()
