class A:
    MIN_COORD = 0  # Атрибут MIN_COORD класса A c аргументом 0
    MAX_COORD = 100

    def __new__(cls, *args, **kwargs):  # вызывается перед созданием объекта класса
        return None

    def __init__(self, x=0, y=1, z=2):  # инициализатор класса
        self.x = x  # атрибут с режимом доступf public
        self._y = y  # атрибут с режимом доступа protected (служит для обращения внутри класса и во всех его дочерних классах
        self.__z = z  # атрибут с режимом доступа private (служит для ображения только внутри класса)
        return None

    def __del__(self):  # финализатор класса
        return None

    @classmethod  # Метод класса
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    @staticmethod  # статический метод внутри класса. Находиться внутри класса, но не зависит от него. Может быть вызван непосредственно в самом классе
    def norm2(x, y):
        return x * x + y * y

    @classmethod
    def __check_value(self, x):  # приватный метод класса для проверки значений передаваемыз в сеттер
        return type(x) in (int, float)

    def set_coord(self, x, y):  # Интерфесный метод (сеттер)
        if self.__check_value(x) and self.__check_value(x):
            self.__x = x
            self.__y = y
        else:
            raise ValueError("Координаты должны быть числами")

    def get_coord(self):  # Интерфейсный метод (геттер)
        return self.__x, self.__y


A.__doc__  # документация класса
A.__dict__  # вернуть колекцию атрибутов текущего класса
getattr(A, "attr1")  # Вернуть значние указанного атрибута
hasattr(A, "attr1")  # Проверить, есть ли указанный атрибут
del A.attr1  # Удалить указанный атрибут
setattr(A, "attr1")  # Добавить/изменить указанный атрибут класса
delattr(A, "attr1")  # Удалить указанный атрибут
