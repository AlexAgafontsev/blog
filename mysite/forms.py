from django import forms
<<<<<<< HEAD
from .models import Post
=======
from .models import Author
>>>>>>> origin/main
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
<<<<<<< HEAD
        fields = ('username', 'email', 'password1', 'password2',)

=======
        fields = ('username', 'email', 'password1', 'password2',)
>>>>>>> origin/main
