"""Тестирование скорости выполнения программы"""

# -m "модуль timeit" -т "количество раз" -s "тестируемый модуль"
# .\algorithms_and_data_structures\lesson_4> python.exe -m timeit -n 100 -s "import task_1"


import timeit

x = 2 + 2
print(timeit.timeit('x = 2 + 2'))
print(timeit.timeit('x = sum(range(10))'))
