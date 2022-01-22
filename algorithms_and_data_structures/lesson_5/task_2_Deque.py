from collections import deque

a = deque()
b = deque("sdfsdgas")
c = deque([1, 2, 3, 4, 5])
print(a, b, c, sep='\n')

b = deque("sdfsdgas", maxlen=3)
c = deque([1, 2, 3, 4, 5], maxlen=4)
c.clear()
print(b, c, sep='\n')

print("*" * 50)
d = deque([i for i in range(5)])
d.append(5)
d.appendleft(6)
print(d)
d.extend([7, 8, 9])
d.extendleft([10, 11, 12])
print(d)

##############################

import random

array = [random.randint(-100, 100) for _ in range(10)]
print(array)

deq = deque()

for item in array:

    if item > 0:
        deq.append(item)
    elif item < 0:
        deq.appendleft(item)

print(deq)




