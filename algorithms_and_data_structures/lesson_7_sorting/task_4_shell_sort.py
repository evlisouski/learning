import random

size = 100
array = [i for i in range(size)]
random.shuffle(array)
print(array)


# Сортировка Шелла. Эффективна для массивов размером менее 4000
def shell_sort(array):
    assert len(array) < 4000, 'Массив слишком большой. Используйте другую сортировку'

    def new_increment(array):

        inc = [1, 4, 10, 23, 57, 132, 301, 701, 1750]  # длина шаков

        while len(array) <= inc[-1]:  # проверка дины массива и исключение из inc шагов которые больше длины массива
            inc.pop()

        while len(inc) > 0:  # пока в списке есть последнее значение возвращаем значение
            yield inc.pop()

    for increment in new_increment(array):  # increment - шаг с которым будем обходить массив для сортировки
        for i in range(increment, len(array)):  #
            for j in range(i, increment - 1, -increment):
                if array[j - increment] <= array[j]:
                    break
                array[j], array[j - increment] = array[j - increment], array[j]
                print(array)


shell_sort(array)
print(array)
