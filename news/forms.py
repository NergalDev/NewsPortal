from django import forms
from .models import Post, SubscribersCategory


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title_post', 'text_post', 'category']


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = SubscribersCategory
        fields = ['category']