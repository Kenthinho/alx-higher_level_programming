#!/usr/bin/python3
if __name == "__main__":
    from sys import argv
    result = 0
    for arg in argv[1:]:
        result +== int(arg)
    print("{}".format(result))
