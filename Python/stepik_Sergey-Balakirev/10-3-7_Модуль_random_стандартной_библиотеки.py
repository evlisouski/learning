import random

# установка "зерна" датчика случайных чисел, чтобы получались одни и те же случайные величины
random.seed(1)
# начальная инициализация поля (переменные P и N не менять, единицы записывать в список P)
N = int(input())
P = [[0] * N for i in range(N)]


def is_isolate():
    global P
    P = [[0] * N for i in range(N)]
    c = 0
    while sum(map(lambda x: sum(x), P)) < 10:
        P_i = range(len(P))
        P_j = range(len(P[0]))
        temp = random.randint(0, 1)
        P[random.choice(P_i)][random.choice(P_j)] = temp
        if temp == 1:
            c += 1
    print(P)
    flg_bool = True
    i = -1
    j = -1
    for row in range(len(P) - 1):
        i += 1
        j = -1
        for col in range(len(P[0]) - 1):
            j += 1
            if P[i][j] + P[i][j + 1] + P[i + 1][j] + P[i + 1][j + 1] > 1:
                flg_bool = False
                break
    return (True if flg_bool == True else False)


while True:
    if is_isolate() == True:
        break

# здесь продолжайте программу