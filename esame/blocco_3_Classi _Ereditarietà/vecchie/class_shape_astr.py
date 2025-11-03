'''
            Exercise 1: Creating an Abstract Class with Abstract Methods

Start by defining an abstract base class called Shape. This class should include two abstract methods: one named area, which will be responsible for calculating the area of a shape, and another named perimeter, which will calculate the perimeter. Since Shape is abstract, it will not provide specific implementations for these methods. Instead, it sets a blueprint for all shapes that will inherit from it.
Then, create two concrete subclasses, Circle and Rectangle, that both extend the Shape class. Each of these subclasses must provide their own implementation of the area and perimeter methods, based on the geometric formulas appropriate to their shapes.
Finally, write a simple driver program (test code) that creates instances of Circle and Rectangle, calls their area and perimeter methods, and prints the results. This will help verify that your class hierarchy works as intended.
'''


from abc import ABC, abstractmethod
import math

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):

    def __init__(self, r:float) -> None:
        self.radius = r

    def area(self) -> float:
        area = math.pi * self.radius**2
        return area
    
    def perimeter(self) -> float:
        per = 2 * math.pi * self.radius
        return per


class Rectangle(Shape):

    def __init__(self, a:float, b:float) -> None:
        self.a = a
        self.b = b

    def area(self) -> float:
        area = self.a * self.b
        return area
    
    def perimeter(self) -> float:
        per = self.a * 2 + self.b * 2
        return per    

