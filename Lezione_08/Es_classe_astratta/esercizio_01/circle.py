from shape import Shape
import math

class Circle(Shape):

    def __init__(self, raggio: float):
        self._raggio = raggio

    def get_raggio(self):
        return self._raggio

    def area(self):
        return round(math.pi * self._raggio ** 2,2)

    def perimeter(self):
        return round(math.pi * 2 * self._raggio, 2)