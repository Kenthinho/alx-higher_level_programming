#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for val in range(len(my_list)):
        print("{:d}".format(int(my_list[val])))
