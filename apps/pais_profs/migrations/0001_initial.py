# Generated by Django 5.1.2 on 2024-10-11 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DrawingAndCardAndKnow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/', verbose_name='Imagem')),
                ('file', models.FileField(blank=True, null=True, upload_to='downloads/', verbose_name='Arquivo para Download')),
                ('type', models.CharField(max_length=30, verbose_name='Tipo')),
                ('description', models.TextField(verbose_name='Descrição')),
            ],
        ),
        migrations.CreateModel(
            name='TopDesc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Titulo')),
                ('description', models.TextField(verbose_name='Descrição')),
            ],
        ),
    ]
