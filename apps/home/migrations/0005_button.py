# Generated by Django 5.1.2 on 2024-10-16 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_topdesch'),
    ]

    operations = [
        migrations.CreateModel(
            name='Button',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('urls', models.URLField(verbose_name='Saiba mais urls')),
            ],
        ),
    ]
