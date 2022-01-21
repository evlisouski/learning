"""Пример реализации построения чисел Фибоначи с функцией memorize (ранее высчетанные значения сохраняются в словарь
 и по возможности беруться из словаря, если в словаре нет указанного значаения, то оно высчитывается и добавляется
  в словарь)"""
import cProfile


def test_fib(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Test {i} OK')


def fib_dict(n):
    fib_d = {0: 0, 1: 1}

    def _fib_dict(n):
        if n in fib_d:
            return fib_d[n]
        fib_d[n] = _fib_dict(n - 1) + _fib_dict(n - 2)
        return fib_d[n]

    return _fib_dict(n)


# test_fib(fib_dict)


# PS C:\home\foxexa\learning\algorithms_and_data_structures\lesson_4> python.exe -m timeit -n 1000 -s "import task_4" "task_4.fib_dict(10)"
# 1000 loops, best of 5: 1.92 msec per loop
# PS C:\home\foxexa\learning\algorithms_and_data_structures\lesson_4> python.exe -m timeit -n 1000 -s "import task_4" "task_4.fib_dict(20)"
# 1000 loops, best of 5: 6.59 usec per loop

cProfile.run('fib_dict(2000)')
