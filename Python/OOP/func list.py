class A:
    MIN_COORD = 0   #Атрибут MIN_COORD класса A c аргументом 0
    MAX_COORD = 100

    def __new__(cls, *args, **kwargs):  # вызывается перед созданием объекта класса
        return None

    def __init__(self, x=1, y=0):  # инициализатор класса
        return None

    def __del__(self):  # финализатор класса
        return None


    @classmethod    #Метод класса
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    @staticmethod   #статический метод внутри класса
    def norm2(x, y):
        return x*x + y*y

A.__doc__ #документация класса
A.__dict__ #вернуть колекцию атрибутов текущего класса
getattr(A, "attr1") #Вернуть значние указанного атрибута
hasattr(A, "attr1") #Проверить, есть ли указанный атрибут
del A.attr1 #Удалить указанный атрибут
setattr(A, "attr1") #Добавить/изменить указанный атрибут класса
delattr(A, "attr1") #Удалить указанный атрибут