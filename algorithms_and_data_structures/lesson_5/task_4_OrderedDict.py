from collections import OrderedDict

# сортировка по ключу
a = {'cat': 5, 'dog': 4, 'mouse': 2}
new_a = OrderedDict(sorted(a.items(), key=lambda x: x[0]))  # x[0] указывает на ключ из словаря а
print(new_a)

# сортировка по значению
a = {'cat': 5, 'dog': 4, 'mouse': 2}
new_b = OrderedDict(sorted(a.items(), key=lambda x: x[1]))  # x[0] указывает на значение из словаря а
print(new_b)

print(new_a == new_b)

new_b.move_to_end('mouse')
print(new_b)

new_b.popitem(last=False)
print(new_b)

new_b['cow'] = 1
print(new_b)

new_b['cat'] = 8  # значение cat изменилось, а порядок остался тот же
print(new_b)

print('*' * 50)
new_c = OrderedDict(sorted(a.items(), key=lambda x: len(x[0])))  # сортировка по длине ключа
print(new_c)

for key in reversed(new_c):  # вывод в обратном порядке
    print(key, new_c[key])
