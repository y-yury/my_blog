from django import forms
from .models import MyPost


class PostForm(forms.ModelForm):

    class Meta:
        model = MyPost
        fields = ('title', 'text', 'image',)
