class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        print("__len__")
        return self.x * self.x + self.y * self.y

    def __bool__(self):  # __bool__ отрабатывает в приоритете перед __len__
        print("__bool__")
        return self.x == self.y


p = Point(0, 0)
if p:
    print("Объект p вернул True")
else:
    print("Объект p вернул False")
print(bool(p))
