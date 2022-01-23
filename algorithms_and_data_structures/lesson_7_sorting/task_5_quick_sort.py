import random

size = 10
array = [i for i in range(size)]
random.shuffle(array)
print(array)


# Сортировка Хоара, быстрая сортировка.
def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = random.choice(array)
    s_ar = []
    m_ar = []
    l_ar = []

    for item in array:

        if item < pivot:
            s_ar.append(item)
        elif item > pivot:
            l_ar.append(item)
        elif item == pivot:
            m_ar.append(item)
        else:
            raise Exception('Случилось непредвиденное')

    print(s_ar, m_ar, l_ar)
    return quick_sort(s_ar) + m_ar + quick_sort(l_ar)


array_new = quick_sort(array)
print(array_new)
