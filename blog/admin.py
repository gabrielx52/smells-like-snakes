from django.contrib import admin
from .models import Post, Category


class PostInline(admin.TabularInline):
    model = Post.category.through
    max_num = 2


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_published')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [PostInline]

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
