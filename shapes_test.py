import math
import pytest
from shapes import Circle, Triangle, calculate_area, ShapeFactory


def test_circle_area():
    c = Circle(3)
    assert math.isclose(c.area(), math.pi * 9, rel_tol=1e-9)


def test_circle_invalid_radius():
    with pytest.raises(ValueError):
        Circle(0)


def test_triangle_area():
    t = Triangle(3, 4, 5)
    assert math.isclose(t.area(), 6.0, rel_tol=1e-9)


def test_triangle_invalid_sides():
    with pytest.raises(ValueError):
        Triangle(1, 2, 10)


def test_triangle_is_right():
    t = Triangle(3, 4, 5)
    assert t.is_right()

    t2 = Triangle(3, 3, 3)
    assert not t2.is_right()


def test_calculate_area_circle():
    result = calculate_area("circle", 2)
    assert math.isclose(result, math.pi * 4, rel_tol=1e-9)


def test_calculate_area_triangle():
    result = calculate_area("triangle", 3, 4, 5)
    assert math.isclose(result, 6.0, rel_tol=1e-9)


def test_unknown_shape():
    with pytest.raises(ValueError):
        calculate_area("hexagon", 1, 2, 3)


def test_register_new_shape():
    class Square:
        def __init__(self, side):
            self.side = side

        def area(self):
            return self.side ** 2

    ShapeFactory.register_shape("square", Square)
    s = ShapeFactory.create_shape("square", 5)
    assert s.area() == 25
