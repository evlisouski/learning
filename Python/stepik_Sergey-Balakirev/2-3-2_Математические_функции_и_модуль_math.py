import math
n, m = map(int, input().split())
max_capacity = 20
total_peoples = n + m
need_buses = math.ceil(total_peoples / max_capacity)
print(need_buses)
