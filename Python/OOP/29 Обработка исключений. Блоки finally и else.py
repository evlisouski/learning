# region Схема try-exept-else-finally
try:
    f = open("myfile.txt")
    f.write("hello")

except FileNotFoundError as z:
    # z в данном случае ссылка на экземпляр класса данного исключения
    print(z)
except:
    print("Другая ошибка")
# Если исключений не было, то выполниться else
else:
    print("Исключений и не произошло")

# finally выполняется всегда
finally:
    if f:
        f.close()
        print("Блок finally выполняется всегда")

# но лучше для закрытия файлов использовать with
# endregion

# region Гарантированное закрытие файла с использованием with
try:
    with open("myfile.txt") as f:
        f.write("hello")

except FileNotFoundError as z:
    print(z)
except:
    print("Другая ошибка")


# endregion

# region Обработка внутри функции
def get_values():
    try:
        x, y = map(int, input().split())
        return x, y
    except ValueError as z:
        print(z)
        return 0, 0
    finally:
        print("finally выполняется до return")

# Оператор return отрабатывает в последнюю очередь
x, y = get_values()
print(x, y)
# endregion
