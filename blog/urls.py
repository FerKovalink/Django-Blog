from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('about', views.about, name= 'about'),
    path('post/list', views.PostLista.as_view(), name='List'),
    path(r'^(?P<pk>\d+)$', views.PostDetalle.as_view(), name='Detail'),
    path(r'^nuevo$', views.PostCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.PostUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.PostDelete.as_view(), name='Delete'),

]