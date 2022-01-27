import hashlib

# Для байтовой строки используем функцию хеширования, рузультат представляем в виде 16-ти ричного числа
print(hashlib.sha1(b'Hello World!').hexdigest())
# меняем одну букву и получаем совершенно другой хеш
print(hashlib.sha1(b'Hello WorlR!').hexdigest())

# пример использования секретного дополнительного слова 'fdgsdgfdhfgjhfg', которое знают только отправитель и получатель,
# в письме данное слово не фигурирует в таком случае злоумышленнику трудно подсчитать хеш.
print(hashlib.sha1(b'fdgsdgfdhfgjhfg' + b'Hello WorlR!').hexdigest())

# сохраняем текст письма в переменную и считаем хеш
s = hashlib.sha1(b'Hello World.').hexdigest()

# переводим полученный хеш из byte в utf-8
print(s.encode('utf-8'))

# использование хеш кода для хеш подписи письма.
# в начале идет секретное слово, далее хеш полученный на основании письма, затем переводив в 16-ти ричный формат
print(hashlib.sha1(b'dfsdgsdg' + bytes(s.encode('utf-8'))).hexdigest())