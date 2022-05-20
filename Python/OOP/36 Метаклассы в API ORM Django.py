class Meta(type):  # метаклассы должны быть унаследованы от type
    # метод инициализатор создаваемого класса (Women)
    def create_local_attrs(self, *args, **kwargs):
        for key, value in self.class_attrs.items():
            self.__dict__[key] = value

    def __init__(cls, name, bases, attrs):
        cls.class_attrs = attrs
        cls.__init__ = Meta.create_local_attrs


class Women(metaclass=Meta):
    title = "заголовок"
    content = "контент"
    photo = "путь к фото"


w = Women()
print(w.__dict__)


# Описанная выше реализация аналогична, если бы мы написали такой вот класс

# class Women(metaclass=Meta):
#     class_attrs = {"title": "заголовок", "content": "контент", "photo": "путь к фото"}
#     title = "заголовок"
#     content = "контент"
#     photo = "путь к фото"
#
#     def __init__(self, *args, **kwargs):
#         for key, value in self.class_attrs.items():
#             self.__dict__[key] = value
