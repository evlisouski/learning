# пример хеш словаря для английского алфавита размеров в 26 символов
h_list = [None] * 26


def my_append(value):
    index = ord(value[0]) - ord('a')
    h_list[index] = value
    print(h_list)


a = 'apriocot'
my_append(a)

b = 'banana'
my_append(b)

# 'apple' становится в ячейку с 'apriocot', пример колизии
c = 'apple'
my_append(c)

# пример позиционной системы счисления, но схожей система можно получить хеш
print(4625 == 4 * 10 ** 3 + 6 * 10 ** 2 + 2 * 10 ** 1 + 5 * 10 ** 0)


# пример расчета хеша для слова с использованием следующей хеш функции
# word_hash += (ord(char) - ord('a') + 1) * letter ** i
def my_index(value):
    letter = 26
    word_hash = 0
    # ограничить размер хеша 10000 комбинаций
    size = 10000

    # i - индекс буквы, char - текущий символ
    for i, char in enumerate(value):
        # для каждого символа высчитываем хеш и приболяем у предыдущему значению. В итоге получаем хеш сумму символов
        word_hash += (ord(char) - ord('a') + 1) * letter ** i
        # ограничить размер хеша 10000 комбинаций
    return word_hash % size


print(my_index(a))
print(my_index(b))
print(my_index(c))
