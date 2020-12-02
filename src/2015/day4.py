import hashlib
import sys

if len(sys.argv) > 2:
    secret_key = sys.argv[1]
    dest = sys.argv[2]
    i = 0
    result = ''
    while not result.startswith(dest, 0, len(dest)):
        i+=1
        key = secret_key + str(i)
        result = str(hashlib.md5(key.encode()).hexdigest())
    print(i)
else:
    print("Pass the secret key as first parameter")
    print("Pass the dest startstring as second parameter")
