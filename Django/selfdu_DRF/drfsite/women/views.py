from django.forms import model_to_dict
from rest_framework import generics, viewsets
from django.shortcuts import render
from rest_framework.response import Response
# от APIView наследуются все остальные классы представлений DRF
from rest_framework.views import APIView

from women.models import Women
from women.serializers import WomenSerializer


class WomenViewSet(viewsets.ModelViewSet):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer

#region ВАРИАНТ 2. Представления на основании классов представлений
# # ListCreateAPIView реализует GET/POST запросы
# class WomenAPIList(generics.ListCreateAPIView):
#     # ссылка на список записей возвращаемых клиенту
#     queryset = Women.objects.all()
#     # сериализатор, который применяется к queryset
#     serializer_class = WomenSerializer
#
#
# class WonenAPIUpdate(generics.UpdateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
#
# class WomenAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer

#region ВАРИАНТ 1. Использование WomenAPIView
# class WomenAPIView(APIView):
#     def get(self, request):
#         w = Women.objects.all()
#         # преобразование и передача в виде байтовой JSON строки
#         return Response({'posts': WomenSerializer(w, many=True).data})
#
#     def post(self, request):
#         post_new = Women.objects.create(
#             title=request.data["title"],
#             content=request.data["content"],
#             cat_id=request.data["cat_id"]
#         )
#         return Response({"post": model_to_dict(post_new)})
#         # создаём сериализатор на основании данных от POST запроса и распаковываем эти данные
#         serializer = WomenSerializer(data=request.data)
#         # проверяем корректность принятых данных
#         serializer.is_valid(raise_exception=True)
#         # save() автоматические вызовет метод create из serializers.py и добавит новую запись
#         serializer.save()
#
#     def put(self, request, *args, **kwargs):
#         # проверка присутствия ключа и записи
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
#         try:
#             instance = Women.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does not exists"})
#         # Если получили ключ и запись по этому ключу, то создаем объект сериализатор
#         # передаем request.data (данные, которые хотим изменить) и объект instance (запись которую мы хотим поменять)
#         serializer = WomenSerializer(data=request.data, instance=instance)
#         # проверяем принятые данные
#         serializer.is_valid(raise_exception=True)
#         # когда создается серриализатор WomenSerializer(data=request.data, instance=instance) с двумя такими параметрами
#         # метод serializer.save() автоматически вызовет метод update из serializers.py
#         serializer.save()
#         # отправляем клиенту данные, которые были изменены
#         return Response({"post": serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method DELETE not allowed"})
#         # код для удаления записи
#         return Response({"post": "delete post" + str(pk)})
#endregion