# Enter you module contents here
'''This module contains functions for calculating the hypotenuse and area of a triangle'''
__author__ = "Navaira"
__version__ = "0.1.0"

def hypotenuse(a,b):
    '''Returns the length of the hypotenuse of a right triangle'''

    return (a**2 + b**2)**0.5

def area (b,h):
    '''Returns the area of a triangle'''
    return 0.5*b*h