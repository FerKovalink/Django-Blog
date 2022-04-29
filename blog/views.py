from .models import Post
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView



def about(request):
    return render(request, 'about.html')


class PostList(ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_at')
    template_name = 'index.html'


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'


class PostDetalle(DetailView):
      model = Post
      template_name = 'post.html'


class PostCreacion(CreateView):
      model = Post
      success_url = 'post_create.html'
      fields = ['title', 'author', 'content', 'published', 'slug', 'status']


class PostUpdate(UpdateView):
      model = Post
      success_url = 'post_edit.html'
      fields = ['title', 'author', 'content', 'published', 'slug', 'status']


class PostDelete(DeleteView):
      model = Post
      success_url = 'post_confirm_delete.html'


def buscar(request):
      if  request.GET['title']:
            title = request.GET['title'] 
            post = Post.objects.filter(title__icontains=title)
            return render(request, 'base.html', {'post':post, 'title':title})

      else: 
            return HttpResponse('No se encuentra {title}')