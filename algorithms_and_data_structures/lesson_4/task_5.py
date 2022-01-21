"""Пример реализации построения чисел Фибоначи с функцией memorize (ранее высчетанные значения сохраняются в словарь
 и по возможности беруться из списка, если в списке нет указанного значаения, то оно высчитывается и добавляется
  в список)"""
import cProfile


def test_fib(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Test {i} OK')


def fib_list(n):
    fib_l = [None] * 1000
    fib_l[:2] = [0, 1]

    def _fib_list(n):
        if fib_l[n] is None:
            fib_l[n] = _fib_list(n - 1) + _fib_list(n - 2)
        return fib_l[n]

    return _fib_list(n)


# test_fib(fib_list)


# PS C:\home\foxexa\learning\algorithms_and_data_structures\lesson_4> python.exe -m timeit -n 1000 -s "import task_4" "task_4.fib_dict(10)"
# 1000 loops, best of 5: 1.92 msec per loop
# PS C:\home\foxexa\learning\algorithms_and_data_structures\lesson_4> python.exe -m timeit -n 1000 -s "import task_4" "task_4.fib_dict(20)"
# 1000 loops, best of 5: 6.59 usec per loop

cProfile.run('fib_list(500)')
