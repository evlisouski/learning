class Point:
    MIN_COORD = 0
    MAX_COORD = 100

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        if self.MIN_COORD <= x <= self.MAX_COORD:
            self.x = x
            self.y = y

    @classmethod
    def set_bound(cls, left):
        cls.MIN_COORD = left

    def __getattribute__(self, item): #Магический метод вызывается каждый раз при обращении к атрибутам экземпляра класса
        if item == "x":                #пример ограничения на изменение атрибута х эеземпляра класса и вызов исключения
            print("Доступ запрещен")
        else:
           return object.__getattribute__(self, item)  #Переопределене метода __getattribute__ базового класса object
                                                      # каждый раз когда будет выполнятьсо обращение к атрибутам экземпляра класса, будет срабатывать данный метод
    def __setattr__(self, key, value): #автоматически вызывается, когда идет присвоение атрибуту экземпляра класса
        if key == "o":
            raise AttributeError("недопустимое имя атрибута") #пример использования для ограничения создания атрибута с именем z
        else:
            object.__setattr__(self, key, value)    #вызываем через базовый класс метод с таким же названием и передаем
           #self.x = value #будет вызываться рекурсивно поэтому это делается так:
           #self.__dict__[key] = value

    def __getattr__(self, item): #вызывается при обращении к несуществующему атрибуту
        print("__getattr__" + item)

    def __delattr__(self, item): #вызывается каждый раз при удалении атрибута экземпляа класса
        print("__delattr__")
        object.__delattr__(self, item) #вызов всего остального из базового класса object, для уже непосредственного удаления атрибута



pt1 = Point(1, 2)
pt2 = Point(10, 20)
pt1.set_bound(-100)
print(pt1.__dict__)
print(Point.__dict__)


