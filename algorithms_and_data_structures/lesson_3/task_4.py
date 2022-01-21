'''Вставка числа в массив'''

import random

array = [random.randint(-100, 100) for _ in range(100)]
print(array)

num = int(input('Введите целое число для вставки: '))
pos = int(input('На какую позицию вставить число: '))

# Метод 1. Реализация алгоритма через цикл. Так устроен метод insert() показанный ниже.
# array.append(None)
# i = len(array) - 1
#
# while i > pos:
#     array[i], array[i - 1] = array[i - 1], array[i]
#     i -= 1

# Метод 2. Использование встроенного метода insert()
# array.insert(pos, num)

# Метод 3. Использование нового массива и срезов. Берем все что левее + число + все что правее.
array_new = array[:pos] + [num] + array[pos:]

array[pos] = num
print(array)
