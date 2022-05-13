class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    @classmethod
    def __check_value(self, x): #приватный метод класса
        return type(x) in (int, float)

    def set_coord(self, x, y): #Интерфесный метод (сеттер)
        if self.__check_value(x) and self.__check_value(x):
            self.__x = x
            self.__y = y
        else:
            raise ValueError("Координаты должны быть числами")

    def get_coord(self): #Интерфейсный метод (геттер)
        return self.__x, self.__y

pt = Point(1, 2)
pt.set_coord(10, 20)
print(dir(pt))