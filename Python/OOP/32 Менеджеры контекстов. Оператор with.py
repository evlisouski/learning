# Менеджер контекста (with). Внутри класса менеджера контекста следующие магические методы:
# __enter__() - срабатывает в момент создания объекта менеджера контекста
# __exit__() - срабатывает в момент завершения работы менеджера контекста или возникновения исключения

#region Example 1
fp = None
try:
    with open("myfile.txt") as f:
        for t in fp:
            print(t)
except Exception as e:
    print(e)

v1 = [1, 2, 3]
v2 = [2, 3]
#endregion

#region Example 2
class DefenderVector:
    def __init__(self, v):
        self.__v = v

    def __enter__(self):  # отработает в момент создания менеджера контекста
        self.__temp = self.__v[:]  # создаем копию списка
        return self.__temp  # возвращаем копию списка

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:  # если ошибок нет
            self.__v[:] = self.__temp  # копируем поэлементно список

        return False  # если метод возвращает False, то исключений нет


try:
    with DefenderVector(v1) as dv:
        for i, a in enumerate(dv):
            dv[i] += v2[i]
except:
    print("Ошибка")
print(v1)
#endregion

