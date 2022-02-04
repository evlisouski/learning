from django.contrib import admin

from .models import *


# Настройка админ панели для модели Women
class WomenAdmin(admin.ModelAdmin):
    # спипок полей которые нужно отобразить в admin панели
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')


# Настройка админ панели для модели Category
class CategoryAdmin(admin.ModelAdmin):
    # спипок полей которые нужно отобразить в admin панели
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


# первым параметром указываем класс модели Women, вторым параметром указываем вспомогательный класс WomenAdmin
admin.site.register(Women, WomenAdmin)
# регистрируем панель Category
admin.site.register(Category, CategoryAdmin)
