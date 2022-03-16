from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .forms import RegistrForm, CommentForm
from .models import Post, Comment
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


# Create your views here.


def index(request):
    return render(request, 'index.html')

def blog(request):
    context = {
        'posts': Post.objects.all().order_by('date')
    }
    return render(request, 'blog.html', context)


def post_page(request, pk):
    post = Post.objects.get(pk=pk)
    # Список активных комментариев к этой записи
    new_comment = None
    if request.method == 'POST':
        # Комментарий был опубликован
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Создайте объект Comment, но пока не сохраняйте в базу данных
            new_comment = comment_form.save(commit=False)
            # Назначить текущий пост комментарию
            new_comment.post = post
            new_comment.author = request.user
            # Сохранить комментарий в базе данных
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request,
                  'post_page.html',
                  {'post': post,
                   'comment' : Comment.objects.filter(post=pk),
                   'new_comment': new_comment,
                   'comment_form': comment_form})

def all_users(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'list_of_users.html', context)

def user_page(request, pk):
    context = {
        'user': User.objects.get(pk=pk)
    }
    return render(request, 'user_page.html', context)

def profile(request):
    return render(request, 'profile.html')






class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'summary']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdate(UpdateView):
    model = Post
    fields = ['title', 'summary']
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
            return redirect('home')
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

