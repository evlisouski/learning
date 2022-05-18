# Полиморфизм - это возможность работать с совершенно разными объектами единым образом

#region ВАРИАНТ 1. ИСПОЛЬЗОВАТЬ ОДИНАКОВЫЕ НАЗВАНИЯ МЕТОДОВ.
class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_pr(self):  # метод во всех классах должен называться одинаково
        return 2 * (self.w + self.h)


class Square:
    def __init__(self, a):
        self.a = a

    def get_pr(self):
        return 4 * self.a


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_pr(self):
        return self.a + self.b + self.c


geom = [Rectangle(1, 2),
        Rectangle(3, 4),
        Square(10),
        Square(20),
        Triangle(1, 2, 3),
        Triangle(4, 5, 6)]

for g in geom:
    print(g.get_pr())  # когда в цикле вызывается метод get_pr, он вызывается по ссылкам у соответствующего объекта
#endregion

#region ВАРИАНТ 2. ИСПОЛЬЗОВАНИЕ БАЗОВОГО КЛАССА С ПОСЛЕДУЮЩИМ ПЕРЕОПРЕДЕЛЕНИЕМ МЕТОДА.
class Geom:  # базовый класс, в котором есть метод, который будет унаследован и который можно будет потом переопределить
    def get_pr(self):
        return -1


class Rectangle(Geom):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_pr(self):  # метод во всех классах должен называться одинаково
        return 2 * (self.w + self.h)


class Square(Geom):
    def __init__(self, a):
        self.a = a

    def get_pr(self):
        return 4 * self.a


class Triangle(Geom):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_pr(self):
        return self.a + self.b + self.c


geom = [Rectangle(1, 2),
        Rectangle(3, 4),
        Square(10),
        Square(20),
        Triangle(1, 2, 3),
        Triangle(4, 5, 6)]

for g in geom:
    print(g.get_pr())  # когда в цикле вызывается метод get_pr, он вызывается по ссылкам у соответствующего объекта
#endregion

#region ВАРИАНТ 3. ИСПОЛЬЗОВАНИЕ АССТРАКТНОГО МЕТОДА В РОДИТЕЛЬСКОМ КЛАССЕ. ЛУЧШИЙ ВАРИАНТ
class Geom:
    # Методы, которые не имеют реализации и которые необходимо переопределить, называются абстрактными
    def get_pr(self):
        # Исключение, указывающее, что необходимо переопределить метод get_pr в будущих дочерних классах
        raise NotImplementedError("В дочернем классе должен быть переопределен метод get_pr()")


class Rectangle(Geom):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_pr(self):  # метод во всех классах должен называться одинаково
        return 2 * (self.w + self.h)


class Square(Geom):
    def __init__(self, a):
        self.a = a

    def get_pr(self):
        return 4 * self.a


class Triangle(Geom):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_pr(self):
        return self.a + self.b + self.c


geom = [Rectangle(1, 2),
        Rectangle(3, 4),
        Square(10),
        Square(20),
        Triangle(1, 2, 3),
        Triangle(4, 5, 6)]

for g in geom:
    print(g.get_pr())  # когда в цикле вызывается метод get_pr, он вызывается по ссылкам у соответствующего объекта
#endregion

