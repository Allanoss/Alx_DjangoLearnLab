import math

# Base Class - Shape
class Shape:
    """A base class representing a generic shape."""
    def area(self):
        """Method to calculate area, should be overridden by derived classes."""
        raise NotImplementedError("Subclasses must implement this method")

# Derived Class - Rectangle
class Rectangle(Shape):
    """A class to represent a rectangle, inheriting from Shape."""
    def __init__(self, length, width):
        """Initialize the rectangle's dimensions."""
        self.length = length
        self.width = width

    def area(self):
        """Calculate the area of the rectangle."""
        return self.length * self.width

# Derived Class - Circle
class Circle(Shape):
    """A class to represent a circle, inheriting from Shape."""
    def __init__(self, radius):
        """Initialize the circle's radius."""
        self.radius = radius

    def area(self):
        """Calculate the area of the circle."""
        return math.pi * (self.radius ** 2)
