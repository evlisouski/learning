#Алгоритм Эквлида для нахождения наибольшего делиделя для двух чисел

def gcd(m, n):
    while m != n:
        if m > n:
            m -= n
        else:
            n -= m
        return m

print(gcd(540, 24458732))