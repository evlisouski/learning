a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))
m = a
if m < b:
    m = b
if m < c:
    m = c

print(f'Наибольшее число: {m}')
