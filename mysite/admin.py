from django.contrib import admin

from .models import Post



admin.site.register(Post)

from .models import Post


class PostAuthor(admin.TabularInline):
    model = Post
    extra = 0








