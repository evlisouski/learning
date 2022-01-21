# Сортировка массима на отрицатильные и положительные числа

import random

array = [random.randint(-100, 100) for _ in range(100)]
print(array)

arr_below = []
arr_lager = []

for item in array:
    if item > 0:
        arr_lager.append(item)
    elif item < 0:
        arr_below.append(item)
print(arr_below)
print(arr_lager)

# Плохой кок. Код короче, но вызывается дважды.
arr_below1 = [item for item in array if item < 0]
arr_lager1 = [item for item in array if item < 0]
print(arr_below1)
print(arr_lager1)
