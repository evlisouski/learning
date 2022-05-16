# Магические методы сравнений

class Clock:
    __DAY = 86400  # число секунд в одно дне

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("Секунды должны быть целыми числами")
        self.seconds = seconds % self.__DAY

    @classmethod
    def __verify_data(cls, other):
        if not isinstance(other, (int, Clock)):
            raise TypeError("Операнд справа должен иметь тип int или Clock")

        return other if isinstance(other, int) else other.seconds

    def __eq__(self, other):  # проверка на равенство и неравенство (not(c1 == c2))
        sc = self.__verify_data(other)
        return self.seconds == sc

    def __lt__(self,
               other):  # проверка на меньше. Если не определен операнд "больше", то данный метод инвертируется при проверке на больше
        sc = self.__verify_data(other)
        return self.seconds < sc


c1 = Clock(1000)
c2 = Clock(2000)
print(c1 == c2)
print(c1 != c2)
print(c1 < c2)
print(c1 > c2)
