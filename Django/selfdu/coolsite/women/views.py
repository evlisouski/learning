from django.contrib.auth import logout, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView, FormView

from .forms import *
from .utils import *

# region Main menu collection
menu = [
    {'title': "О сайте", 'url_name': 'about'},
    {'title': "Добавить статью", 'url_name': 'add_page'},
    {'title': "Обратная связь", 'url_name': 'contact'},
    {'title': "Войти", 'url_name': 'login'}
]


# endregion

# region HOME page view class
class WomenHome(DataMixin, ListView):
    # брать данные из БД на основании полей следующей модели
    model = Women
    # использовать следующий шаблон
    template_name = 'women/index.html'
    # название списка в шаблонах
    context_object_name = 'posts'

    # extra_context = {'title': 'Главная страница'}

    def get_context_data(self, *, object_list=None, **kwargs):
        # взять все данные контекста из базового класса
        context = super().get_context_data(**kwargs)
        # ипользьуем метод из mixin
        c_def = self.get_user_context(tittle='Главная страница')
        # формируем context в виде словаря, объединив два словаря в виде списков
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    # специальный метод, который отвечает за то, что нужно прочитать из модели model
    def get_queryset(self):
        return Women.objects.filter(is_published=True).select_related('cat')


# endregion

# region ABOUT page view function
def about(request):
    contact_list = Women.objects.all()
    paginator = Paginator(contact_list, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'women/about.html', {'page_obj': page_obj, 'menu': menu, 'title': 'О сайте'})


# endregion

# region ADD PAGE page view class
class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    # артибут form_class указывает на класс AddPostForm
    form_class = AddPostForm
    template_name = 'women/addpage.html'
    success_url = reverse_lazy('home')
    # адрес перенаправления для не авторизированного пользователя
    login_url = reverse_lazy('home')
    # использование оповещения 403 (доступ запрещен) для не авторизованны пользователей
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # ипользьуем метод из mixin
        c_def = self.get_user_context(tittle='Добавление статьи')
        # формируем context в виде словаря, объединив два словаря в виде списков
        context = dict(list(context.items()) + list(c_def.items()))
        return context


# endregion

# region CONTACT page view class
class ContactFormView(DataMixin, FormView):
    form_class = ContactForm
    template_name = 'women/contact.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Обратная связь')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')


# endregion

# region SHOW POST page view class
class ShowPost(DataMixin, DeleteView):
    model = Women
    template_name = 'women/post.html'
    # определим slug, который необходимо использовать из urls
    slug_url_kwarg = 'post_slug'
    # название списка в шаблонах
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # ипользьуем метод из mixin
        c_def = self.get_user_context(tittle=context['post'])
        # формируем context в виде словаря, объединив два словаря в виде списков
        context = dict(list(context.items()) + list(c_def.items()))
        return context


# endregion

# region WOMEN CATEGORY page view class
class WomenCategory(DataMixin, ListView):
    # брать данные из БД на основании полей следующей модели
    model = Women
    # использовать следующий шаблон
    template_name = 'women/index.html'
    # название списка в шаблонах
    context_object_name = 'posts'
    # если в списке нет не одной записи, то генерируем 404
    allow_empty = False

    # extra_context = {'title': 'Главная страница'}

    # метод по slug определяет какие данные вернуть
    def get_queryset(self):
        # через словарь kwargs, который содержит все параметры, обращаемся к параметру 'cat_slug'
        # выбираем все записи которые совпадают с cat__slug и опубликованы is_published
        return Women.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True).select_related('cat')

    def get_context_data(self, *, object_list=None, **kwargs):
        # взять все данные контекста из базового класса ListView
        context = super().get_context_data(**kwargs)
        c = Category.objects.get(slug=self.kwargs['cat_slug'])
        # ипользьуем метод из mixin
        c_def = self.get_user_context(tittle='Категория - ' + str(c.name),
                                      cat_selected=c.pk)
        # формируем context в виде словаря, объединив два словаря в виде списков
        context = dict(list(context.items()) + list(c_def.items()))

        return context


# endregion

# region REGISTER USER page view class
class RegisterUser(DataMixin, CreateView):
    # использование стандартной формы авторизации Django UserCreationForm
    form_class = RegisterUserForm
    template_name = 'women/register.html'
    success_url = reverse_lazy('login')

    # формируем context
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))

    # автоматическая авторизация при успешной регистрации
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


# endregion

# region LOGIN USER page view class
class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'women/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


# endregion

# region LOGOUT USER funcion
def logout_user(request):
    logout(request)
    return redirect('login')


# endregion

# region PAGE NOT FOUND page view funcion
def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
# endregion


# -----------------------------------
# region SUPRESSED and OLDER FUNC

# region INDEX func
# def index(request):
#     posts = Women.objects.all()
#
#     context = {
#         'posts': posts,
#         'menu': menu,
#         'title': 'Главная страница',
#         'cat_selected': 0,
#     }
#
#     return render(request, 'women/index.html', context=context)
# endregion

# region ADD PAGE func
# использование декоротора для функции представления, для ограничения доступа не авторизованым пользователям
# для класов представления используется mixin LoginRequiredMixin
# @login_required
# def addpage(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             # для формы связанной с моделью
#             form.save()
#             return redirect('home')
#             # для формы не связанной с моделью
#             # try:
#             # Women.objects.create(**form.cleaned_data)
#             # return redirect('home')
#             # except:
#             #     form.add_error(None, 'Ошибка добавления поста')
#
#     else:
#         form = AddPostForm()
#     return render(request, 'women/addpage.html', {'form': form, 'menu': menu, 'title': 'Добавление статьи'})
# endregion

# region SHOW POST func
# def show_post(request, post_slug):
#     post = get_object_or_404(Women, slug=post_slug)
#
#     context = {
#         'post': post,
#         'menu': menu,
#         'title': post.title,
#         'cat_selected': post.cat_id,
#     }
#
#     return render(request, 'women/post.html', context=context)


# def show_category(request, cat_id):
#     posts = Women.objects.filter(cat_id=cat_id)
#
#     if len(posts) == 0:
#         raise Http404()
#
#     context = {
#         'posts': posts,
#         'menu': menu,
#         'title': "Отображение по рубрикам",
#         'cat_selected': cat_id,
#     }
#     return render(request, 'women/index.html', context=context)
# endregion

# endregion