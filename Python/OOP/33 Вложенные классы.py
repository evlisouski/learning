class Women:
    title = "объект класса для поля title"
    photo = "объект класса для поля photo"
    ordering = "объект класса для поля ordering"

    def __init__(self, user, psw):
        self._user = user
        self._psw = psw
        self.meta = self.Meta(user + "@" + psw) # для того чтобы был создан класс Meta при создании экземпляра класса Women
                                                # необходимо прописать это в методе инициализации класса Women

    class Meta:
        ordering = ["id"]

        def __init__(self, access):
            self._access = access


w = Women("root", "12345")
print(w.__dict__)
print(w.meta.__dict__)
