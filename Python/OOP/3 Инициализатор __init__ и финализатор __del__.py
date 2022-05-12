class Point:
    color = "red"
    circle = 2

    def __init__(self, x=1, y=0): #инициализатор объекта класса
        print("вызов init")
        self.x = x
        self.y = y

    def __del__(self): #финализатор класса
        print("Удаление экземпляра:" + str(self))

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return self.x, self.y



