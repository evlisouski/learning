import math
n, k = map(int, input().split())
C_k_n = (math.factorial(n)) / (math.factorial(k) * math.factorial(n - k))
print(int(C_k_n))
