import django_filters
from .models import Post, PostCategory


class PostFilter(django_filters.FilterSet):
    class Meta:
        model = Post
        fields = {
            'title_post': ['icontains'],
            'text_post': ['icontains'],
            'time_create': ['gte']
        }


class PostCategoryFilter(django_filters.FilterSet):
    class Meta:
        model = PostCategory
        fields = ['category']