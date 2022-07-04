#!/usr/bin/python3
'''A module for working with geometry
'''


class BaseGeometry:
    '''A base class for all geometry objects
    '''
    def area(self):
        '''Computes the area of the geometry object
        Return:
            float - The area of this geometry object.
        '''
        raise Exception('area() is not implemented')
