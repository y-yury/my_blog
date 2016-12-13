from django import forms
from .models import MyPost, MyComment


class PostForm(forms.ModelForm):

    class Meta:
        model = MyPost
        fields = ('title', 'text', 'image',)


class CommentForm(forms.ModelForm):

    class Meta:
        model = MyComment
        fields = ('author', 'text',)