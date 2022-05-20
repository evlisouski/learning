# ПРИМЕРЫ ИСПОЛЬЗОВАИЯ МЕТАКЛАССОВ ДЛЯ СОЗДАНИЯ КЛАССОВ

# region Пример создания метакласса через функцию
# МЕТАКЛАСС
# описанная ниже функция описывает как создать данный метакласс
# данный пример для наглядности, лучше использовать отдельный класс для создания метакласса, а не функцию в
def create_class_point(name, base, attrs):
    # name - имя класса
    # base - список базовых классов
    # attrs - список атрибутов класса
    attrs.update({"MAX_COORD": 100, "MIN_COORD": 0})
    return type(name, base, attrs)


# создаем класс на основании метакласса, для этого указываем ссылку наметакласс через metaclass
class Point(metaclass=create_class_point):
    def get_coords(self):
        return (0, 0)


print("Создание метакласса на основании функции")
pt = Point()
print(pt.MAX_COORD)
print(pt.get_coords())


# endregion

# region Пример создания метакласса на основании класса

class Meta(type):
    # cls - ссылка на создаваемый класс
    # name - имя класса
    # base - список базовых классов
    # attrs - список атрибутов класса
    def __init__(cls, name, base, attrs):
        super().__init__(name, base, attrs)
        cls.MAX_COORD = 100
        cls.NIM_COORD = 0


class Point(metaclass=Meta):
    def get_coords(self):
        return (0, 0)


print("Создание метакласса на основании класса")
pt = Point()
print(pt.MAX_COORD)
print(pt.get_coords())


# endregion

# region Пример создания метакласса на основании класса. Вариант с использованием __new__

class Meta(type):
    # cls - ссылка на создаваемый класс
    # name - имя класса
    # base - список базовых классов
    # attrs - список атрибутов класса
    def __new__(cls, name, base, attrs):
        attrs.update({"MAX_COORD": 100, "MIN_COORD": 0})
        return type.__new__(cls, name, base, attrs)


class Point(metaclass=Meta):
    def get_coords(self):
        return (0, 0)


print("Создание метакласса на основании класса. Использование __new__")
pt = Point()
print(pt.MAX_COORD)
print(pt.get_coords())
# endregion
