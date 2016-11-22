from django.contrib import admin
from .models import MyPost

# Register your models here.


class MyPostAdmin(admin.ModelAdmin):
    list_display = ('author', 'date_created', 'date_published', 'title')
    search_fields = ('text', 'title')

admin.site.register(MyPost, MyPostAdmin)
