from django.db import models
from django.contrib.auth.models import User


class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.FileField(verbose_name='Imagen', upload_to='media/', null=True)

    def __str__(self):
        return self.user + ": " + str(self.imagen)
