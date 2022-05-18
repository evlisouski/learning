class Goods:
    def __init__(self, name, weight, price):
        super().__init__()  # объект-посредник, который делигирует вызов инициализатора соответствующего базового класса
        print("init Goods")
        self.name = name
        self.weight = weight
        self.price = price

    def print_info(self):
        print(f"{self.name}, {self.weight}, {self.price}")


class MixinLog:
    ID = 0

    def __init__(self):  # при использовании множественного наследования желательно использовать в миксинах только ссылку self, без дополнительных параметров
        # если нужно использовать дополнительный параметр, то нужно будет указать его в родительском классе в объекте-посреднике
        print("init MixinLog")
        self.ID += 1
        self.id = self.ID

    def save_sell_log(self):
        print(f"Вызывается метод save_sell_log из MixinLog")

    def print_info(self):
        print(f"{self.name}, {self.weight}, {self.price}")


class NoteBook(Goods, MixinLog):
    pass


n = NoteBook("Acer", 1.5, 30000)
n.print_info()
n.save_sell_log()

# MRO - Method Resolution Order
print(NoteBook.__mro__)

#частный пример, вызова метода print_info
MixinLog.print_info(n)
#но лучше переопределить его в дочернем классе, который наследует множество методов
