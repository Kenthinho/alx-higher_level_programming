#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    no_of_elements = 0
    try:
        for value in my_list[:x]:
            print("{}".format(value), end='')
            no_of_elements += 1
        print()
    except:
        pass
    return no_of_elements
