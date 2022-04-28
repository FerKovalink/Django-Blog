from . import views
from django.urls import path
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login', views.login_request, name='login'),
    path('register', views.register, name='register'),
    path('logout', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('editarPerfil', views.editarPerfil, name='editarperfil'),
    
]