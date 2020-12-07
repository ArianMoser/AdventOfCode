import sys
import re

def check_doubles(word):
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            return True
    return False

file_name = "inputs/day5.txt"
nice_strings = 0

if len(sys.argv) > 1:
    file_name = sys.argv[1]

with open(file_name) as f:
    words = f.read().splitlines()
    # task1
    for word in words:
        try:
            if not re.compile("(.*[aeiou]){3}").match(word):
                raise Exception("{}: Not three vocals".format(word))
            if not re.compile(".*([a-z])\\1.*").match(word):
            #if not check_doubles(word):
                raise Exception("{}: No double char".format(word))
            if re.compile(".*(ab|cd|pq|xy).*").match(word):
                raise Exception("{}: Forbidden string".format(word))
            #print(word)
            nice_strings += 1
        except Exception as e:
            #print(e)
            pass
    print("Task 1: Found {} nice words".format(nice_strings))

    #task2
    nice_strings = 0
    for word in words:
        try:
            if not re.compile(".*(([a-z][a-z]).*)\\2.*").match(word):
                raise Exception("{}: No pair that occures twice ".format(word))
            if not re.compile(".*([a-z]).\\1.*").match(word):
                raise Exception("{}: No letter that repeats with one letter between them".format(word))
            #print(word)
            nice_strings += 1
        except Exception as e:
            #print(e)
            pass
    print("Task 2: Found {} nice words".format(nice_strings))
                
    
