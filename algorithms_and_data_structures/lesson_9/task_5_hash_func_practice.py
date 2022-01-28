import hashlib


# функция сравнивает строки по хэш сумме и возвращает True если они равны
def is_eq_str(a: str, b: str, verbose=False) -> bool:
    assert len(a) > 0 and len(b) > 0, "Строки не могут быть пустые"

    # переводим строку из переменноа а и переводим в utf-8, получаем байт-строку
    # передаем эти байты в алгоритм хэширования sha1, результат представляем в виде 16ричной строки
    ha = hashlib.sha1(a.encode('utf-8')).hexdigest()
    # для строки b все то же самое
    hb = hashlib.sha1(b.encode('utf-8')).hexdigest()

    if verbose:
        print(f"hash 1 = {ha}\nhash 2 = {hb}")

    return ha == hb


s_1 = input("Введите строку 1: ")
s_2 = input("Введите строку 2: ")

print("Строки одинаковые" if is_eq_str(s_1, s_2, True) else 'Строки разные')
