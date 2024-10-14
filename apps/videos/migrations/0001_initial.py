# Generated by Django 5.1.2 on 2024-10-11 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TopImageV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Titulo')),
                ('image', models.ImageField(upload_to='images/', verbose_name='Imagem')),
                ('description', models.TextField(verbose_name='Descrição')),
            ],
        ),
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=30, verbose_name='Tipo')),
                ('thumb', models.ImageField(upload_to='images/', verbose_name='Imagem')),
                ('videoUrl', models.URLField(max_length=255, verbose_name='URL do Vídeo')),
                ('title', models.CharField(max_length=50, verbose_name='Titulo')),
            ],
        ),
    ]
