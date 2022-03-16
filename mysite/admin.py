from django.contrib import admin
from .models import Post,Comment




class CommentsInline(admin.TabularInline):
    model = Comment
    extra = 0 #фиксит пустые значения копий книги"""


@admin.register(Post)
class CommentAdminn(admin.ModelAdmin):
    list_display = ('title', 'author')
    inlines = [CommentsInline]







