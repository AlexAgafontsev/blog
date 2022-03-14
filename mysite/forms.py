from django import forms
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Создаём класс формы
class RegistrForm(UserCreationForm):
    # Добавляем новое поле Email
    email = forms.EmailField(max_length=254, help_text='This field is required')

    # Создаём класс Meta
    class Meta:
        # Свойство модели User
        model = User
        # Свойство назначения полей
        fields = ('username', 'email', 'password1', 'password2',)

