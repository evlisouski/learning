class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)

        
    def __getitem__(self, item):
