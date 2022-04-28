from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User


class Post(models.Model):

    ESTADO = (
    (0,'Borrador'),
    (1,'Publicado'),
    )

    title = models.CharField(verbose_name='Titulo', max_length=300, unique=True)
    #subtitle = models.CharField(verbose_name='Subtitulo', max_length=100, unique=True)
    author = models.ForeignKey(User, verbose_name='Autor', on_delete=models.CASCADE, related_name='blog_posts')
    content = models.TextField(verbose_name='Contenido')
    published = models.DateTimeField(verbose_name="Fecha de publicación", default=now)
    #image = models.ImageField(verbose_name="Imagen", upload_to="blog", null=True, blank=True)
    slug = models.SlugField(verbose_name='Link' ,max_length=300, unique=True)
    status = models.IntegerField(verbose_name='Estado', choices=ESTADO, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title