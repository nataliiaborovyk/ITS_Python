from shape import Shape
import math

class Rectamgle(Shape):

    def __init__(self, a: float, b: float):
        self._a = a
        self._b = b
   
    def get_a(self):
        return self._a
    
    def get_b(self):
        return self._b

    def area(self):
        return round(self._a * self._b, 2)
    
    def perimeter(self):
        return round(2 * self._a + 2 * self._b, 2)
