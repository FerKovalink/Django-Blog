from django.shortcuts import render
from django.views import generic
from .models import Post
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_at')
    template_name = 'index.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post.html'

def about(request):
    return render(request, "about.html")

class CursoList(LoginRequiredMixin, ListView):

      model = Post 
      template_name = "AppCoder/cursos_list.html"



class CursoDetalle(DetailView):

      model = Post
      template_name = "AppCoder/curso_detalle.html"



class CursoCreacion(CreateView):

      model = Post
      success_url = "/AppCoder/curso/list"
      fields = ['nombre', 'camada']


class CursoUpdate(UpdateView):

      model = Post
      success_url = "/AppCoder/curso/list"
      fields  = ['nombre', 'camada']


class CursoDelete(DeleteView):

      model = Post
      success_url = "/AppCoder/curso/list"