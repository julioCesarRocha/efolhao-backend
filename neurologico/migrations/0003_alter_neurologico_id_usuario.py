# Generated by Django 4.0.5 on 2023-06-08 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neurologico', '0002_alter_neurologico_id_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neurologico',
            name='id_usuario',
            field=models.CharField(blank=True, max_length=350, null=True),
        ),
    ]
