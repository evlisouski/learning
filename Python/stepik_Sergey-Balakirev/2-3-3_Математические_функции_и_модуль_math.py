import math

x = int(input())
cash = 500
discount = 0.1
cash = cash + (cash * discount)

max_discount_pens = math.floor(cash / x)
print(max_discount_pens)
