from django.forms import model_to_dict
from rest_framework import generics
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from women.models import Women
from women.serializers import WomenSerializer


class WomenAPIView(APIView):
    def get(self, request):
        w = Women.objects.all()
        # преобразование и передача в виде байтовой JSON строки
        return Response({'posts': WomenSerializer(w, many=True).data})

    def post(self, request):
        # создаём сериализатор на основании данных от POST запроса и распаковываем эти данные
        serializer = WomenSerializer(data=request.data)
        # проверяем корректность принятых данных
        serializer.is_valid(raise_exception=True)
        # save() автоматические вызовет метод create из serializers.py и добавит новую запись
        serializer.save()

    def put(self, request, *args, **kwargs):
        # проверка присутствия ключа и записи
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})
        try:
            instance = Women.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})

        # Если получили ключ и запись по этому ключу, то создаем объект сериализатор
        # передаем request.data (данные, которые хотим изменить) и объект instance (запись которую мы хотим поменять)
        serializer = WomenSerializer(data=request.data, instance=instance)
        # проверяем принятые данные
        serializer.is_valid(raise_exception=True)
        # когда создается серриализатор WomenSerializer(data=request.data, instance=instance) с двумя такими параметрами
        # метод serializer.save() автоматически вызовет метод update из serializers.py
        serializer.save()
        # отправляем клиенту данные, которые были изменены
        return Response({"post": serializer.data})

            # post_new = Women.objects.create(
        #     title=request.data['title'],
        #     content=request.data['content'],
        #     cat_id=request.data['cat_id']
        # )


    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method DELETE not allowed"})

        # код для удаления записи

        return Response({"post": "delete post" + str(pk)})





# class WomenAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer


