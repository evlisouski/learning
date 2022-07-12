class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def clone(self):
        return Point(self.x, self.y)

pt = Point()
pt_clone = pt.clone()
