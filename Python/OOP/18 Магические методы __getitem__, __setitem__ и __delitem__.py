class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)

    def __getitem__(self, item):  # получение значения по ключу item
        if 0 <= item < len(self.marks):
            return self.marks[item]
        else:
            raise IndexError("Неверный индекс")

    def __setitem__(self, key, value):  # запись значения value по ключу key
        if not isinstance(key, int) or key < 0:
            raise TypeError("Индекс должен быть целым неотрицательным числом")
        if key >= len(self.marks):
            off = key + 1 - len(self.marks)
            self.marks.extend([None] * off)
        self.marks[key] = value

    def __delitem__(self, key):  # удаление элемента по ключу key
        if not isinstance(key, int):
            raise TypeError('Индекс должен быть целым неотрицательным числом')
        del self.marks[key]


s1 = Student("Eduard", [5, 6, 7, 9, 2])
print(s1[2])
s1[2] = 4
print(s1[2])
