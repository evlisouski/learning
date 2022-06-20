import io

from rest_framework import serializers
from .models import Women

from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer


# class WomenModel:
#     def __init__(self, title, content):
#         # локальные имена должны совпадать с именами класса-серриализатора
#         self.title = title
#         self.content = content

class WomenSerializer(serializers.ModelSerializer):
    # атрибут user из модели который ссылается на текущего авторизированного пользователя
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        # указываем модель, с которой работаем
        model = Women
        # поля, записанные в модели Women, которые будем возвращать клиенту
        # fields = ("title", "content", "cat")
        fields = "__all__"


#region Сериализатора на базе класса Serializer
# class WomenModel:
#     def __init__(self, title, content):
#         # локальные имена должны совпадать с именами класса-серриализатора
#         self.title = title
#         self.content = content
#
# class WomenSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=255)
#     content = serializers.CharField()
#     # read_only = True указывает что поля не обязательны для записи
#     time_create = serializers.DateTimeField(read_only=True)
#     time_update = serializers.DateTimeField(read_only=True)
#     is_published = serializers.BooleanField(default=True)
#     cat_id = serializers.IntegerField()
#
#     def create(self, validated_data):
#         return Women.objects.create(**validated_data)
#
#     # instance ссылка на объект модели Women
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get("title", instance.title)
#         instance.content = validated_data.get("content", instance.content)
#         instance.time_update = validated_data.get("time_update", instance.time_update)
#         instance.is_published = validated_data.get("is_published", instance.is_published)
#         instance.cat_id = validated_data.get("cat_id", instance.cat_id)
#         instance.save()
#         return instance
#endregion

# region Подробный пример обработки данных внутри
# Реализация сериализатора на основании ModelSerializer
# class WomenSerializer(serializers.Serializer):
#     class Meta:
#         model = Women
#         fields = ("title", "content", "cat")

# class WomenSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=255)
#     content = serializers.CharField()


# преобразование в модели в JSON строку
# def encode():
#     model = WomenModel('Angelina Jolie', "content: Angelina Jolie")
#     # создаем объект сериализатора, который создает специальную коллекцию data из атрибутов модели
#     # и представляет в виде словаря
#     model_sr = WomenSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     # JSONRenderer() преобразует объект сериализации в байтовую строку
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
# #
# def decode():
#     # имитация поступления запроса от клиента
#     stream = io.BytesIO(b'{"title":"Angelina Jolie","content":"content: Angelina Jolie"}')
#     # используем парсер
#     data = JSONParser().parse(stream)
#     # преобразовываем data c помощью объекта сериализации
#     serializer = WomenSerializer(data=data)
#     # делаем проверку декодированных данных на корректность
#     serializer.is_valid()
#     print(serializer.validated_data)
# endregion
