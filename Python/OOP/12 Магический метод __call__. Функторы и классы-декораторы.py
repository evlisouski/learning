# __call__ вызывается при вызове класса подобно функции
# обычно используется для построения конструкции схожей с замыканием функций
import math


# класс-декоратор
class Derivate:
    def __init__(self, func):
        self.__fn = func

    def __call__(self, x, dx=0.0001, *args, **kwargs):
        return (self.__fn(x + dx) - self.__fn(x)) / dx


@Derivate  # применен декоратор-класс
def df_sin(x):
    return math.sin(x)


# df_sin = Derivate(df_sin)   #Вариант испоьзования __call__ без декоратора
print(df_sin(math.pi / 3))
