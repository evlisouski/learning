# Алгоритм Эквлида для нахождения наибольшего делиделя для двух чисел

# Медленно, но верно работает
def gcd(m, n):
    while m != n:
        if m > n:
            m -= n
        else:
            n -= m
    return m


# При переполненнии стека выдаст неверный ответ, рекурсия
def gcd2(m, n):
    if n == 0:
        return m
    return gcd2(n, m % n)


# Оптимальный алгоритм
def gcd3(m, n):
    while n != 0:
        m, n = n, m % n
    return m


if __name__ == '__main__':
    print(gcd(540, 24458732646))
