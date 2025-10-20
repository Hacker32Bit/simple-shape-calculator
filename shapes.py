import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass


class Circle(Shape):
    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError("Радиус должен быть >= 0")
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2


class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float):
        if any(side <= 0 for side in (a, b, c)):
            raise ValueError("Все стороны должны быть >= 0")
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Нарушено неравенство треугольника")
        self.a, self.b, self.c = a, b, c

    def area(self) -> float:
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def is_right(self) -> bool:
        sides = sorted([self.a, self.b, self.c])
        return math.isclose(sides[0] ** 2 + sides[1] ** 2, sides[2] ** 2, rel_tol=1e-9)


class ShapeFactory:
    _registry = {}

    @classmethod
    def register_shape(cls, name: str, shape_cls):
        cls._registry[name.lower()] = shape_cls

    @classmethod
    def create_shape(cls, name: str, *args, **kwargs) -> Shape:
        shape_cls = cls._registry.get(name.lower())
        if not shape_cls:
            raise ValueError(f"Неизвестный тип фигуры: {name}")
        return shape_cls(*args, **kwargs)


# Register built-in shapes
ShapeFactory.register_shape("circle", Circle)
ShapeFactory.register_shape("triangle", Triangle)


def calculate_area(shape_name: str, *args, **kwargs) -> float:
    shape = ShapeFactory.create_shape(shape_name, *args, **kwargs)
    return shape.area()
