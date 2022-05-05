def counter_add(n):
    z = n

    def up_own_value(z):
        nonlocal n
        z += n
        print(z)

    return up_own_value


cnt = counter_add(2)
k = int(input())
cnt(k)