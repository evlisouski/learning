import random
class Geom:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)

class Line(Geom):
    pass

class Rect(Geom):
    pass

class Ellipse(Geom):
    pass


elements = []
x, y = 1, 1
for i in range(217):
    a = random.random()
    b = random.random()
    c = random.random()
    d = random.random()
    choice = random.randint(0, 2)
    if choice == 0:
        elements.append(Line(a, b, c, d))
    if choice == 1:
        elements.append(Rect(a, b, c, d))
    if choice == 2:
        elements.append(Ellipse(a, b, c, d))

for i in elements:
    if type(i).__name__ == "Line":
        i.sp = (0, 0)
        i.ep = (0, 0)