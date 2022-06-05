#!/usr/bin/python3
def print_list_integers(my_list=[]):
    '''This prints each number in the list on a new line'''
    for number in range(len(my_list)):
        print("{}".format(my_list[number]))
