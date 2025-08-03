# Project 2: Polymorphic Shape Drawing System
# What you will build:
# An abstract base class Shape with abstract methods:
# area() — calculate area of the shape
# perimeter() — calculate perimeter of the shape
# draw() — print a message describing the shape drawing
# Concrete subclasses:
# Circle (needs radius)
# Rectangle (needs width and height)
# Triangle (needs lengths of three sides)
# Each subclass will override the abstract methods to give shape-specific results.
# You will create a list of different shape objects and call the same methods polymorphically.

from abc import ABC , abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
    @abstractmethod
    def draw(self):
        pass
class Circle(Shape):
    pi = 3.14
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return self.radius * self.radius * self.pi
        
    def perimeter(self):
        return self.radius *2* self.pi
    def draw(self):
        return f"This is circle with radius {self.radius}"
        
class Rectangle(Shape):
    def __init__(self, width , height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.height * self.width
        
    def perimeter(self):
        return 2* (self.height + self.width)
    def draw(self):
        return f"This is rectangle with area {self.width * self.height}"
        
class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def area(self):
        # Using Heron's formula
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        
    def perimeter(self):
        return self.a + self.b +self.c
        
    def draw(self):
        return f"This is traingle with one side {self.a}"
        
shapes = [
    Triangle(2,3,4),
    Circle(2),
    Rectangle(3,4)
    ]

for shape in shapes:
    print(shape.draw())
    print(f"Area: {shape.area():.2f}")
    print(f"Perimeter: {shape.perimeter():.2f}")
    print()
    
        
        