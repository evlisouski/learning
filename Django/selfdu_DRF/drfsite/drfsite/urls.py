"""drfsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from women.views import *

class MyCustomRouter(routers.SimpleRouter):
    routes = [
        # routers - список из наших статей
        routers.Route(
            # шаблон маршрута
            url=r'^{prefix}$',
            # связывает тип запроса с соответствующим методом ViewSet
            mapping={'get': 'list'},
            # название маршрута
            name='{basename}-list',
            # список или отдельная записи
            detail=False,
            # дополнительные аргументы для kwarg, которые передаются конкретному определению
            initkwargs={'suffix': 'List'}
        ),
        # читает статью по ее идентификатору
        routers.Route(
            url=r'^{prefix}/{lookup}$',
            mapping={'get': 'retrieve'},
            name='{basename}-detail',
            detail=True,
            initkwargs={'suffix': 'Detail'}
        ),]



# router = MyCustomRouter()
# # router = routers.DefaultRouter()
# # регистрируем класс WomenViewSet
# router.register(r'women', WomenViewSet, basename="women")


urlpatterns = [
    path('admin/', admin.site.urls),
    # Авторизация на основе сессии
    path('api/v1/drf-auth/', include("rest_framework.urls")),
    path('api/v1/women/', WomenAPIList.as_view()),
    path('api/v1/women/<int:pk>/', WomenAPIUpdate.as_view()),
    path('api/v1/womendelete/<int:pk>/', WomenAPIDDestroy.as_view()),
    # path('api/v1/womenlist/', WomenViewSet.as_view({"get": "list"})),
    # path('api/v1/womenlist/<int:pk>/', WomenViewSet.as_view({"put": "update"})),
    # path('api/v1/', include(router.urls)), # http://127.0.0.0.1:8000/api/v1/women

]
