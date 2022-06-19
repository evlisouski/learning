from django.contrib import admin

from .models import Women

# Регистрация приложения в admin панели для отображения записей в admin панели
admin.site.register(Women)
