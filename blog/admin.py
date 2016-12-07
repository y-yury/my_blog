from django.contrib import admin
from .models import MyPost

# Register your models here.


class MyPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_drafted', 'date_published', 'image',)
    list_display_links = ('title',)
    search_fields = ('text', 'title')

admin.site.register(MyPost, MyPostAdmin)
