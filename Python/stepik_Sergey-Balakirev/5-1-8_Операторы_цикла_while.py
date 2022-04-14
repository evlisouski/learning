t = int(input())
n = 1
if t // 3 >= 1:
    while t // 3 >= 1:
        n = n * 2
        t -= 3
    print(n)
else:
    print(1)