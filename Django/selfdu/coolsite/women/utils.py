from women.models import *

menu = [
    {'title': "О сайте", 'url_name': 'about'},
    {'title': "Добавить статью", 'url_name': 'add_page'},
    {'title': "Обратная связь", 'url_name': 'contact'},
    {'title': "Войти", 'url_name': 'login'}
]


class DataMixin:
    # метод создает контект для шаблона
    def get_user_context(self, **kwargs):
        # формируем начальный словарь, который передается функции get_user_context
        context = kwargs
        # формируем список категорий
        cats = Category.objects.all()
        context['menu'] = menu
        context['cats'] = cats
        # если в параметрах определяется ключ 'cats_selected' не передавали , то устанавливаем значение
        if 'cats_selected' not in context:
            context['cat_selected'] = 0
        return context
