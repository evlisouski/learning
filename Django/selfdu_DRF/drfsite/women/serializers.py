import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from women.models import Women


class WomenModel:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    # серриализатор
class WomenSerializer(serializers.Serializer):
    # имена атрибутов должны быть одинаковые с моделью
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()

# преобразование в модели в JSON строку
def encode():
    model = WomenModel('Angelina Jolie', "content: Angelina Jolie")
    # создаем объект серриализатора, который создает специальную коллекцию data из атрибутов модели
    # и представляет в виде словаря
    model_sr = WomenSerializer(model)
    print(model_sr.data, type(model_sr.data), sep='\n')
    # JSONRenderer() преобразует объект серриализации в байтовую строку
    json = JSONRenderer().render(model_sr.data)
    print(json)

def decode():
    # имитация поступления запроса от клиента
    stream = io.BytesIO(b'{"title":"Angelina Jolie","content":"content: Angelina Jolie"}')
    # используем парсер
    data = JSONParser().parse(stream)
    # преобразовываем data c помощью объекта сериализации
    serializer = WomenSerializer(data=data)
    # делаем проверку декодированных данных на корректность
    print(serializer.validated_data)
