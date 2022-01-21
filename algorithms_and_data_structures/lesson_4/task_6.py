"""Пример реализации построения чисел Фибоначи с функцией memorize без использования рекурсии"""
import cProfile


def test_fib(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Test {i} OK')


def fib_loop(n):
    if n < 2:
        return n

    first, second = 0, 1
    for i in range(2, n + 1):
        first, second = second, first + second
    return second


# test_fib(fib_loop)
cProfile.run('fib_loop(1000)')

# PS C:\home\foxexa\learning\algorithms_and_data_structures\lesson_4> python.exe -m timeit -n 1000 -s "import task_6" "task_6.fib_loop(10)"
# 1000 loops, best of 5: 605 nsec per loop
# PS C:\home\foxexa\learning\algorithms_and_data_structures\lesson_4> python.exe -m timeit -n 1000 -s "import task_6" "task_6.fib_loop(20)"
# 1000 loops, best of 5: 952 nsec per loop
# PS C:\home\foxexa\learning\algorithms_and_data_structures\lesson_4> python.exe -m timeit -n 1000 -s "import task_6" "task_6.fib_loop(10000)"
# 1000 loops, best of 5: 1.94 msec per loop
