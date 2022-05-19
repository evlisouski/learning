# Использование волшебной колекции __slots__ в определении класса позволяет:
# 1. Использовать только атрибуты, указанные в кортеже __slots__
# 2. Сократить расходуемый объем памяти экземпляром класса
# 3. Ускорить работу с указанными в кортеже атрибутами класса
# PS. При использовании __slots__ невозможно использовать __dict__

import timeit


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calc(self):
        self.x += 1
        del self.y
        self.y = 0


class Point2D:
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calc(self):
        self.x += 1
        del self.y
        self.y = 0


p = Point(1, 2)
p2 = Point2D(10, 20)

t1 = timeit.timeit(p.calc)
t2 = timeit.timeit(p2.calc)
print(f"t1 = {t1}, t1 = {t2}",)
