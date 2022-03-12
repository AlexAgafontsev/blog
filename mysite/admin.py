from django.contrib import admin
from .models import Author, Post


class PostAuthor(admin.TabularInline):
    model = Post
    extra = 0


class AuthorAdmin(admin.ModelAdmin):
    model = Author
    inlines = [PostAuthor]


admin.site.register(Author, AuthorAdmin)


admin.site.register(Post)



