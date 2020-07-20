# Generated by Django 2.2.14 on 2020-07-16 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_title', models.CharField(max_length=300)),
                ('slug', models.SlugField(max_length=250, unique_for_date='created')),
                ('author', models.CharField(max_length=300)),
                ('cover_description', models.TextField()),
                ('body', models.TextField()),
                ('image_name', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
            ],
        ),
    ]
