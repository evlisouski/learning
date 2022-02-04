from django.contrib import admin

from .models import *


# Настройка админ панели
class WomenAdmin(admin.ModelAdmin):
    # спипок полей которые нужно отобразить в admin панели
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')

# первым параметром указываем класс модели Women, вторым параметром указываем вспомогательный класс WomenAdmin
admin.site.register(Women, WomenAdmin)
