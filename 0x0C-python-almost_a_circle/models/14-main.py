#!/usr/bin/python3
""" 14-main """
from models.base import Base
from models.rectangle import Rectangle

'''
This script appears to be testing functionality related to JSON serialization in a project involving models for rectangles. Here's a breakdown of what it does:

from models.base import Base: This imports the Base class from the base.py file within the models package. This Base class likely contains methods for JSON serialization.

from models.rectangle import Rectangle: This imports the Rectangle class from the rectangle.py file within the models package. This class represents rectangles and may also have methods for JSON serialization.

if __name__ == "__main__":: This ensures that the following code block is executed only when the script is run directly, not when it's imported as a module.

r1 = Rectangle(10, 7, 2, 8): This creates an instance of the Rectangle class with width 10, height 7, x-coordinate 2, and y-coordinate 8.

dictionary = r1.to_dictionary(): This calls the to_dictionary() method on the Rectangle instance r1 to convert it into a dictionary representation.

json_dictionary = Base.to_json_string([dictionary]): This calls a class method to_json_string() from the Base class, passing a list containing the previously obtained dictionary. This method likely converts a list of dictionaries to a JSON string.

print(dictionary): This prints the dictionary representation of the rectangle.

print(type(dictionary)): This prints the type of the dictionary variable, which should be a standard Python dictionary.

print(json_dictionary): This prints the JSON string representation of the rectangle.

print(type(json_dictionary)): This prints the type of the json_dictionary variable, which should be a string.

Overall, this script tests the functionality of converting a Rectangle object into a dictionary and then serializing it into a JSON string.
'''
if __name__ == "__main__":

    r1 = Rectangle(10, 7, 2, 8)
    dictionary = r1.to_dictionary()
    json_dictionary = Base.to_json_string([dictionary])
    print(dictionary)
    print(type(dictionary))
    print(json_dictionary)
    print(type(json_dictionary))
