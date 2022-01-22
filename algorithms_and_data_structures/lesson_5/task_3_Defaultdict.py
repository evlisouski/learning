from collections import defaultdict

a = defaultdict()
print(a)

s = 'sdfsdghnrtshsghsfghfghdgdgh'
b = defaultdict(int)

for i in s:
    b[i] += 1

print(b)

list_1 = [('cat', 1), ('dog', 5), ('cat', 2), ('mouse', 1), ('dog', 1)]
c = defaultdict(list)
for k, v in list_1:
    c[k].append(v)

print(c)

#использование set в качестве default_factory позволяет сохранить только уникальные значения
list_2 = [('cat', 1), ('dog', 5), ('cat', 2), ('cat', 2), ('dog', 1), ('dog', 5)]
d = defaultdict(set)
for k, v in list_2:
    d[k].add(v)
print(d)
