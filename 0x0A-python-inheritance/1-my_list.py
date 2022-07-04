#!/usr/bin/python3
'''prints a list in sorted form
'''


class MyList(list):
    '''Custom made list
    '''
    def print_sorted(self):
        '''Prints the list, but sorted (ascending sort)
        '''
        print(sorted(self))
