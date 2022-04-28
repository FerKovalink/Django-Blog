from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('about', views.about, name= 'about'),
    #path(r'^(?P<pk>\d+)$', views.CursoDetalle.as_view(), name='Detail'),
    #path(r'^nuevo$', views.CursoCreacion.as_view(), name='New'),
    #path(r'^editar/(?P<pk>\d+)$', views.CursoUpdate.as_view(), name='Edit'),
    #path(r'^borrar/(?P<pk>\d+)$', views.CursoDelete.as_view(), name='Delete'),

]