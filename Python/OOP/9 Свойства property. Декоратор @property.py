class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old


    #region Cчитываение и изменение приватных атрибутов класса через геттер и сеттер. ВАРИАНТ 1
    def get_old(self):
        return self.__old

    def set_old(self, old):
        self.__old = old

    old = property(get_old, set_old)  # property позволяет автоматически использовать сеттер и геттер, просто обращаясь к old
    #endregion

    #region Использование геттера и сеттера через property. ВАРИАНТ 2. (нет функционального дублирования)
    @property      #первым должен идти геттер
    def old(self):
        return self.__old

    @old.setter #затем сеттер с АНАЛОГИЧНЫМ именем, как у геттера
    def old(self, old):
        self.__old = old
    #endregion

    @old.deleter
    def old(self):
        del self.__old



p = Person("Сергей", 30)
a = p.old
p.old = 35
print(p.__dict__)
