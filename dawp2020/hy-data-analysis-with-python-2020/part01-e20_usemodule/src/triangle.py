__doc__     = "Right-angled triangle module"
__author__  = "Binh D. Nguyen"
__version__ = '1.0'

from math import sqrt

def hypothenuse(x, y):
    """
    Returns the length of the hypothenuse when given the lengths of two other sides of a right-angled triangle
    """
    return sqrt(x**2 + y**2)

def area(x, y):
    """
    Returns the area of the right-angled triangle, when two sides, perpendicular to each other, are given as parameters
    """
    return x * y / 2