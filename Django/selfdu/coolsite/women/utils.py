from django.db.models import Count

from women.models import *

menu = [
    {'title': "О сайте", 'url_name': 'about'},
    {'title': "Добавить статью", 'url_name': 'add_page'},
    {'title': "Обратная связь", 'url_name': 'contact'},
    # {'title': "Войти", 'url_name': 'login'}
]


class DataMixin:
    paginate_by = 5


    # метод создает контект для шаблона
    def get_user_context(self, **kwargs):
        # формируем начальный словарь, который передается функции get_user_context
        context = kwargs
        # формируем список категорий, который из-за count еще и содержить поле количество статей для каждой категории
        cats = Category.objects.annotate(Count('women'))

        # делаем копию словаря menu и сохраняем копию в переменной user_menu
        user_menu = menu.copy()
        # проверяем, если пользователь не авторизован, то
        if not self.request.user.is_authenticated:
            # удаляем из меню "Добавить статью" по индексу 1
            user_menu.pop(1)


        context['menu'] = user_menu
        context['cats'] = cats
        # если в параметрах определяется ключ 'cats_selected' не передавали , то устанавливаем значение
        if 'cats_selected' not in context:
            context['cat_selected'] = 0
        return context
