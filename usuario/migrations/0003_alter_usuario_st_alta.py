# Generated by Django 4.0.4 on 2023-05-29 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_usuario_st_alta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='st_alta',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
