class Geom:
    pass


class Line(Geom):
    pass


class Vector(list):  # расширение базовых возможностей list в классе Vector
    def __str__(self):
        return " ".join(str, self)


g = Geom()
l = Line()
print(issubclass(int, object))
print(isinstance(Geom, object))
