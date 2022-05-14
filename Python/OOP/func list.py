class A:
    # cls - это ссылка на класс
    # self - это ссылка на экземпляр класса

    MIN_COORD = 0  # Атрибут MIN_COORD класса A c аргументом 0
    MAX_COORD = 100

    # Имена методов ВНУТРИ класса, тоже называются атрибутами класса
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

    @classmethod
    def set_bound(cls, left):
        cls.MIN_COORD = left  # изменить значение атрибута в классе через ссылку на его cls

    def __getattribute__(self,
                         item):  # Магический метод вызывается каждый раз при обращении к атрибутам экземпляра класса
        if item == "x":  # пример ограничения на изменение атрибута х эеземпляра класса и вызов исключения
            print("Доступ запрещен")
        else:
            return object.__getattribute__(self, item)  # Переопределене метода __getattribute__ базового класса object
            # каждый раз когда будет выполнятьсо обращение к атрибутам экземпляра класса, будет срабатывать данный метод

    def __setattr__(self, key, value):  # автоматически вызывается, когда идет присвоение атрибуту экземпляра класса
        if key == "o":
            raise AttributeError(
                "недопустимое имя атрибута")  # пример использования для ограничения создания атрибута с именем z
        else:
            object.__setattr__(self, key, value)  # вызываем через базовый класс метод с таким же названием и передаем
        # self.x = value #будет вызываться рекурсивно поэтому это делается так:
        # self.__dict__[key] = value

    def __getattr__(self, item):  # вызывается при обращении к несуществующему атрибуту
        print("__getattr__" + item)

    def __delattr__(self, item):  # вызывается каждый раз при удалении атрибута экземпляа класса
        print("__delattr__")
        object.__delattr__(self,
                           item)  # вызов всего остального из базового класса object, для уже непосредственного удаления атрибута


    # region Cчитываение и изменение приватных атрибутов класса через геттер и сеттер. ВАРИАНТ 1
    def get_z(self):
        return self.__z

    def set_z(self, z):
        self.__z = z

    z = property(get_z,
                   set_z)  # property позволяет автоматически использовать сеттер и геттер, просто обращаясь к old

    # endregion

    # region Использование геттера и сеттера через property. ВАРИАНТ 2. (нет функционального дублирования)
    @property  # первым должен идти геттер
    def z(self):
        return self.__z

    @z.setter  # затем сеттер с АНАЛОГИЧНЫМ именем, как у геттера
    def z(self, z):
        self.__z = z

    @z.deleter
    def old(self):
        del self.__old
    # endregion



a = A(1, 2, 3)

A.__doc__  # документация класса
A.__dict__  # вернуть колекцию атрибутов текущего класса
getattr(A, "attr1")  # Вернуть значние указанного атрибута
hasattr(A, "attr1")  # Проверить, есть ли указанный атрибут
del A.attr1  # Удалить указанный атрибут
setattr(A, "attr1")  # Добавить/изменить указанный атрибут класса
delattr(A, "attr1")  # Удалить указанный атрибут

a.z = 4
print(a.__dict__)