from django import forms
from django.core.exceptions import ValidationError

from .models import *


# форма, не связаннаяя с моделью
# class AddPostForm(forms.Form):
#     title = forms.CharField(max_length=255, label="Заголовок", widget=forms.TextInput(attrs={'class': 'form-input'}))
#     slug = forms.SlugField(max_length=255, label="URL")
#     content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label="Контент")
#     is_published = forms.BooleanField(label="Публикация", required=False, initial=True)
#     cat = forms.ModelChoiceField(queryset=Category.objects.all(), label="Категории", empty_label="Категория не выбрана")


# форма, связанная с моделью
class AddPostForm(forms.ModelForm):
    # создаем конструктор который сразу
    def __init__(self, *args, **kwargs):
        # вызывает конструктор базового класса, чтобы выполнить все автоматические действия
        super().__init__(*args, **kwargs)
        # устанавливаем свойство для 'cat' вместо дефолтного
        self.fields['cat'].empty_label = 'Категория не выбрана'

    class Meta:
        # связь этой формы с моделью
        model = Women
        # отобразить следующие поля
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'cat']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }

        # методы, которые отвечают за валидацию, должны начинаться с 'clean_' дальше название поля для которого
        # делаем валидацию 'title'
    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Длина превышает 200 символов')
        return title
