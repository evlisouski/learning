from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


# Настройка админ панели для модели Women
class WomenAdmin(admin.ModelAdmin):
    # спипок полей которые нужно отобразить в admin панели
    list_display = ('id', 'title', 'time_create', 'photo', 'get_html_photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    # автоматически заполнять поле slug на основании данных из поля name
    prepopulated_fields = {'slug': ('title',)}

    # НАСТРОЙКА ИНТЕРФЕЙСА РЕДАКТИРОВАНИЯ ЗАПИСЕЙ
    # не редактируемые поля
    readonly_fields = ('time_create', 'time_update', 'get_html_photo')
    # порядок и список полей
    fields = (
    'title', 'slug', 'cat', 'content', 'photo', 'get_html_photo', 'is_published', 'time_create', 'time_update')

    # кастомная настройка одного из полей в админ панели
    def get_html_photo(self, object):
        if object.photo:
            # mark_safe указывает не экранировать теги html
            return mark_safe(f"<img src='{object.photo.url}' width=50")

    get_html_photo.short_description = 'Миниатюра'

    # отображать панель сохранения вверху тоже
    save_on_top = True


# Настройка админ панели для модели Category
class CategoryAdmin(admin.ModelAdmin):
    # спипок полей которые нужно отобразить в admin панели
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    # автоматически заполнять поле slug на основании данных из поля name
    prepopulated_fields = {'slug': ('name',)}


# первым параметром указываем класс модели Women, вторым параметром указываем вспомогательный класс WomenAdmin
admin.site.register(Women, WomenAdmin)
# регистрируем панель Category
admin.site.register(Category, CategoryAdmin)

# Настройка надписей панели администратора
admin.site.site_title = 'Админ-панель сайта foxexa'
admin.site.site_header = 'Админ-панель сайта foxexa'
