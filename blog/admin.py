from django.contrib import admin
from blog.models import Category, Author, Post, Comment

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)
