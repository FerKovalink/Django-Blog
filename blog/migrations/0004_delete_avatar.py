# Generated by Django 4.0.3 on 2022-04-29 02:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_avatar_imagen'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Avatar',
        ),
    ]
