num = int(input("Введиде целое число: "))
ans = input("Перевести в байты - 'b', в килобайты - 'k' : ")

ans = ans.lower()

if ans == "b":
    print(f"{num} Кб = {num * 1024} байт")
elif ans == 'k':
    print(f"{num} Кб = {num / 1024} байт")
else:
    print('Неверный ввод')

