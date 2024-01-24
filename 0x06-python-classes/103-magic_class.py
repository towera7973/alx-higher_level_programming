import math

class MagicClass:
    def __init__(self, radius):
        self.__radius = 0  # Initialize __radius attribute

        # Check if radius is an integer or float
        if type(radius) is not int or type(radius) is not float:
            raise TypeError('radius must be a number')

        # Assign radius to __radius attribute
        self.__radius = radius

    def area(self):
        return 2 ** self.__radius * math.pi

    def circumference(self):
        return 2 * math.pi * self.__radius

