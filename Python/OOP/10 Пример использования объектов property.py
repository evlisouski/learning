'''Пример использования property '''

from string import ascii_letters


class Person:
    S_RUS = "йцукенгшщзхъфывапролджэячсмитьбю-"
    S_RUS_UPPER = S_RUS.upper()

    def __init__(self, fio, old, ps, weight):
        self.verify_fio(fio)
        self.verify_old(old)
        self.verify_weight(weight)
        self.verify_ps(ps)

        self.__fio = fio.split()
        self.__old = old
        self.__passport = ps
        self.__weight = weight

    @classmethod
    def verify_fio(cls, fio):
        if type(fio) != str:
            raise TypeError("ФИО должно быть строкой")

        f = fio.split()
        if len(f) != 3:
            raise TypeError("Неверный формат ФИО")

        letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER
        for s in f:
            if len(s) < 1:
                raise TypeError("В ФИО должен быть хотя бы один символ")
            if len(s.strip(letters)) != 0:
                raise TypeError("В ФИО можно использовать только буквенные методы и дефис")

    @classmethod
    def verify_old(cls, old):
        if type(old) != int or old < 14 or old > 120:
            raise TypeError("Возраст должен быть целым числом в диапазоне от 14 до 120 лет")

    @classmethod
    def verify_weight(cls, w):
        if type(w) != float or w < 20:
            raise TypeError("Вес должен быть вещественным числом и больше 20 кг")

    @classmethod
    def verify_ps(cls, ps):
        if type(ps) != str:
            raise TypeError("Паспорт должен быть строкой")

        s = ps.split()
        if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
            raise TypeError("Неверный формат паспорт")

        for p in s:
            if not p.isdigit():
                raise TypeError("Серия и номер паспорта должны быть числом")

    @property #Геттер для ФИО
    def fio(self):
        return self.__fio

    @property #геттер для old
    def old(self):
        return self.__old

    @old.setter #сеттер для old
    def old(self, old):
        self.verify_old(old)
        self.__old = old

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.verify_weight(weight)
        self.__weight = weight

    @property
    def passport(self):
        return self.__passport

    @passport.setter
    def passport(self, ps):
        self.verify_ps(ps)
        self.__passport = ps


p = Person("Лис Кис Кис", 30, "1234 567890", 80.9)
p.old = 100
p.passport = "4563 125678"
print(p.__dict__)
