from collections import deque, OrderedDict, defaultdict

N = 3000
with open('big_log.txt', 'r', encoding='utf-8') as f:
    log = deque(f, N)

print(log)

data = OrderedDict()
spam = defaultdict(int)

for item in log:
    ip = item[:-1]

    if not ip.startswith('192.168'):  # если ip начинается не с 192.168 то сохраняем
        spam[ip] += 1  # считает количество запросов по указанному ip адрессу
        data[ip] = 1  # сохраняет порядок ip адрессов

print(spam)
print(data)

data.update(spam)  # добавить в словарь data значения из spam
print(data)

with open('data.txt', 'w', encoding='utf-8') as f:  # сохранение в файл data.txt
    for key, value in data.items():
        f.write(f'{key} - {value}\n')
