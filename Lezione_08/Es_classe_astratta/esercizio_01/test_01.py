from shape import Shape
from circle import Circle
from rectangle import Rectamgle
import math

c:Circle = Circle(3)
r:Rectamgle = Rectamgle(2,4)

print(f"Cercio con radice {c.get_raggio()}  ha perimetro {c.perimeter()} e area {c.area()}")
print(f"Rettangolo con altezza {r.get_a()} e largezza {r.get_b()} ha perimetro {r.perimeter()} e area {r.area()}")