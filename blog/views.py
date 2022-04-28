from django.shortcuts import render
from django.views import generic
from .models import Post
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


def about(request):
    return render(request, "about.html")


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_at')
    template_name = 'index.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post.html'


class PostLista(LoginRequiredMixin, ListView):
      model = Post 
      template_name = "post_list.html"


class PostDetalle(DetailView):
      model = Post
      template_name = "post_detalle.html"


class PostCreacion(CreateView):
      model = Post
      success_url = "post/list"
      fields = ['title', 'authon', 'content', 'published', 'slug', 'status']


class PostUpdate(UpdateView):
      model = Post
      success_url = "post/list"
      fields = ['title', 'authon', 'content', 'published', 'slug', 'status']


class PostDelete(DeleteView):
      model = Post
      success_url = "post/list"