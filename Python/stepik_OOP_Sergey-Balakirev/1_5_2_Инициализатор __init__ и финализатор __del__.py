class Point:
    def __init__(self, x, y, color="black"):
        self.x = x
        self.y = y
        self.color = color


points = []
x, y = 1, 1
for i in range(1000):
    points.append(Point(x, y))
    x += 2
    y += 2
points[1].color = "yellow"