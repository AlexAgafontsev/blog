from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Author
from .forms import RegistrForm

# Create your views here.


def index(request):
    return render(request, 'index.html')

def blog(request):
    context = {
        'posts': Post.objects.all().order_by('date')
    }
    return render(request, 'blog.html', context)

def post_page(request, pk):
    context = {
        'post': Post.objects.get(pk=pk)
    }
    return render(request, 'post_page.html', context)

def author_page(request, pk):
    context = {
        'author': Author.objects.get(pk=pk)
    }
    return render(request, 'author_page.html', context)

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class PostCreate(CreateView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy ('blog')

class PostUpdate(UpdateView):
    model = Post
    fields = ['title', 'summary', 'images']
    success_url = reverse_lazy ('blog')

class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy ('blog')

# Функция регистрации
def registr(request):
    # Массив для передачи данных шаблонны
    data = {}
    # Проверка что есть запрос POST
    if request.method == 'POST':
        # Создаём форму
        form = RegistrForm(request.POST)
        # Валидация данных из формы
        if form.is_valid():
            # Сохраняем пользователя
            form.save()
            # Передача формы к рендару
            data['form'] = form
            # Передача надписи, если прошло всё успешно
            data['res'] = "Всё прошло успешно"
            # Рендаринг страницы
            return redirect('')
            return render(request, 'registration/registration.html', data)
        else:
            return redirect('reg')

    else: # Иначе
        # Создаём форму
        form = RegistrForm()
        # Передаём форму для рендеринга
        data['form'] = form
        # Рендаринг страницы
        return render(request, 'registration/registration.html', data)

