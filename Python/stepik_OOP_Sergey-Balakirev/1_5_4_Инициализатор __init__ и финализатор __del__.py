class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        a = self.a
        b = self.b
        c = self.c
        check_type = [(True if isinstance(i, (int, float)) else False) for i in [a, b, c]]
        if False in check_type:
            return 1
        check_val = [(i > 0) for i in (a, b, c) ]
        if False in check_type or False in check_val:
            return 1
        if a + b < c or c + b < a or a + c < b:
            return 2
        else:
            return 3

a = 3
b = 4
c = 5

tr = TriangleChecker(a, b, c)
print(tr.is_triangle())


