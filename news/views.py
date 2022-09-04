from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Post, Author, SubscribersCategory, User
from .filters import PostFilter, PostCategoryFilter
from .forms import PostForm, SubscribeForm


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'news/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['is_not_authors'] = not self.request.user.groups.filter(name='authors').exists()
        return context


class PostView(ListView):
    model = Post
    ordering = '-time_create'
    template_name = 'news/postlist.html'
    context_object_name = 'postlist'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostCategoryFilter(self.request.GET, queryset)
        return self.filterset.queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'news/post.html'
    context_object_name = 'post'


class PostSearch(ListView):
    model = Post
    form = PostFilter
    template_name = 'news/search.html'
    context_object_name = 'search'

    def get_queryset(self):
        queryset = super(PostSearch, self).get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.queryset

    def get_context_data(self, **kwargs):
        context = super(PostSearch, self).get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class PostCreate(PermissionRequiredMixin, CreateView):
    form_class = PostForm
    model = Post
    template_name = 'news/create.html'
    permission_required = 'news.add_post'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = Author.objects.get(user_id=self.request.user.id)
        path = self.request.path
        if path == '/news/create/':
            post.type_post = 'NW'
            return super().form_valid(form)
        elif path == '/articles/create/':
            post.type_post ='AR'
            return super().form_valid(form)


class PostUpdate(PermissionRequiredMixin, UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'news/create.html'
    permission_required = 'news.change_post'


class PostDelete(PermissionRequiredMixin, DeleteView):
    model = Post
    template_name = 'news/delete.html'
    success_url = reverse_lazy('postlist')
    permission_required = 'news.delete_post'


class SubscriberView(CreateView):
    model = SubscribersCategory
    form_class = SubscribeForm
    template_name = 'news/subscribe.html'
    success_url = reverse_lazy('postlist')

    def form_valid(self, form):
        subscribe = form.save(commit=False)
        subscribe.subscriber = User.objects.get(pk=self.request.user.id)
        return super(SubscriberView, self).form_valid(form)









