from django.contrib import admin
from .models import MyPost, MyComment

# Register your models here.


class MyPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_drafted', 'date_published', 'date_archived', 'image',)
    list_display_links = ('title',)
    search_fields = ('text', 'title')


class MyCommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'date_drafted', 'comment_approved',)
    list_display_links = ('post',)
    search_fields = ('post', 'author')

admin.site.register(MyPost, MyPostAdmin)
admin.site.register(MyComment, MyCommentAdmin)
