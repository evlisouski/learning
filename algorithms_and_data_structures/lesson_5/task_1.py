"""Коллекция - это обобщенный класс, содержащий набор свойств (полей) одного или разных типов,
при этом позволяющий работать с ними и испольщовать их в спциальных функциях и методах в
зависимости от ее типа
Counter - это подкласс словаря (dict). Неупорядоченная коллекция пар "ключ - значение", где
"значение" - частота вхождения "ключа" """

from collections import Counter

a = Counter()
b = Counter('asdfsdgsdgfsdg')
c = Counter({'red': 2, 'blue': 4})
d = Counter(cats=4, dogs=5)

print(a, b, c, d, sep='\n')

print(b['z'])
b['z'] = 0
print(b)

print(list(b.elements()))
print(b.most_common(2))  # Вывод наиболее часто встречающихся значений. С указанем количества встречаемости

g = Counter(a=4, b=6, c=-2, d=0)
f = Counter(a=1, b=2, c=3, d=-2)
g.subtract(f)  # Вычесть из коллекции g коллекцию f
print(g)
print("*" * 50)
print(set(g))  # Преобразование в множество
print(dict(g))  # Преобразование в словарь
g.clear()
print(g)

print("*" * 50)
x = Counter(a=3, b=1)
y = Counter(a=1, b=2)
print(x + y)
print(x - y)
print(x & y)  # Выведет то количество символов, которое есть в одном и втором операнде (т.е. минимальное среди двух)
print(x | y)  # Выведет наибольшее количество символов среди двух операндов

print('*' * 50)
z = Counter(a=2, b=-4)
print(+z)  # Унарный плюс оставляет только положительные элементы
print(-z)  # Унарный минус оставляет только отрицательные элементы, меняя при этом знак.
