class Cart:
    def __init__(self, goods=[]):
        self.goods = goods[:]

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, indx):
        del self.goods[indx]

    def get_list(self):
        return [f"{i.name}:{i.price}" for i in self.goods]


class Table:
    def __init__(self, name="default_name", price=0):
        self.name = name
        self.price = price


class TV:
    def __init__(self, name="default_name", price=0):
        self.name = name
        self.price = price



class Notebook:
    def __init__(self, name="default_name", price=0):
        self.name = name
        self.price = price



class Cup:
    def __init__(self, name="default_name", price=0):
        self.name = name
        self.price = price

tb = Table("Table", 0)
tv1 = TV("TV1", 0)
tv2 = TV("TV2", 0)
nb1 = Notebook("Notebook1", 0)
nb2 = Notebook("Notebook2", 0)
cup = Cup("Cup", 0)


cart = Cart()
cart.add(tv1)
cart.add(tv2)
cart.add(tb)
cart.add(nb1)
cart.add(nb2)
cart.add(cup)

print(cart.get_list())
