class Point2D:
    # коллекция __slots__ накладывает ограничения только на локальные атрибуты экземпляра класса
    __slots__ = ("x", "y", "__length")

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.length = (x * x + y * y) ** 0.5

    # и не накладывает ограничения на атрибуты самого класса
    @property
    def lenght(self):
        return self.__lenght

    @lenght.setter
    def lenght(self, value):
        self.__length = value


# Данный клас не унаследует __slots__ и может использовать __dict__
# унаследует только если указать явно
class Point3D(Point2D):
    # __slots__ = () # пустой кортеж унаследует x и у из базового класса
    __slots__ = "z",  # или можно добавить новые. Запятая обязательна (кортеж)

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


pt3 = Point3D(10, 20, 30)
print(pt3.x, pt3.y, pt3.z)
