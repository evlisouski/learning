# import io

from rest_framework import serializers
from .models import Women


# from rest_framework.parsers import JSONParser
# from rest_framework.renderers import JSONRenderer


# class WomenModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content

# Реализация сериализатора на основании ModelSerializer
class WomenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Women
        fields = ("title", "content", "cat")







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


# # преобразование в модели в JSON строку
# def encode():
#     model = WomenModel('Angelina Jolie', "content: Angelina Jolie")
#     # создаем объект сериализатора, который создает специальную коллекцию data из атрибутов модели
#     # и представляет в виде словаря
#     model_sr = WomenSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     # JSONRenderer() преобразует объект сериализации в байтовую строку
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
# 
# def decode():
#     # имитация поступления запроса от клиента
#     stream = io.BytesIO(b'{"title":"Angelina Jolie","content":"content: Angelina Jolie"}')
#     # используем парсер
#     data = JSONParser().parse(stream)
#     # преобразовываем data c помощью объекта сериализации
#     serializer = WomenSerializer(data=data)
#     # делаем проверку декодированных данных на корректность
#     print(serializer.validated_data)
