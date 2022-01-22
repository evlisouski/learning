from collections import ChainMap

d_1 = {'a': 2, 'b': 4, 'c': 6}
d_2 = {'a': 10, 'b': 20, 'd': 40}

d_map = ChainMap(d_1, d_2)
print(d_map)
d_2['a'] = 100
print(d_map)

print(d_map['a'])  # вернул первое подходящее значение, в данном случае в словаре d_1
print(d_map['d'])  # вернул первое подходящее значение, в данном случае в словаре d_2

print('*' * 50)
# x = d_map.new_child()  # добавить пустой словарь в начало
x = d_map.new_child({'a': 111, 'b': 222, 'c': 333, 'd': 444})  # добавить новый словарь
print(x)

print(x.maps[0])  # вернуть первый словарь из chainMap
print(x.maps[-1])  # вернуть последний словарь из chainMap

print(x.parents)  # позволяет узнать родителей при создании коллекции методом new_child

print('*' * 50)

y = d_map.new_child()
print(y)
print(y['a'])
y['a'] = 1  # добавиться в первый словарь т.к. в нем нет ключа "a"
print(y)

print(list(y))
print(list(y.values()))



