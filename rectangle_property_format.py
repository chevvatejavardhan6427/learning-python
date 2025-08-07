''' This class demonstrates the use of the "@property" decorator.
 It formats the output to show 2 decimal places with "m" (meters) as the unit.'''

class Rectangle:
    def __init__(self, length, breadth):
        self._length = length      # Use _length internally
        self._breadth = breadth    # Use _breadth internally

    @property
    def length(self):
        return f"{self._length:.2f}m"

    @property
    def breadth(self):
        return f"{self._breadth:.2f}m"
l = Rectangle(7, 5)
print(l.length)    
print(l.breadth)    
