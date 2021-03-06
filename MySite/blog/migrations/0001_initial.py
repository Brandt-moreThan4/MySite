# Generated by Django 2.2.14 on 2020-07-30 17:58

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='Knowledge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=250, unique_for_date='created')),
                ('author', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('source', models.TextField()),
                ('tags', models.TextField(default='Placeholder')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PostBase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=300)),
                ('slug', models.SlugField(max_length=300, unique_for_date='created')),
                ('post_body', models.TextField()),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateField(auto_now=True)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('postbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blog.PostBase')),
            ],
            bases=('blog.postbase',),
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('postbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blog.PostBase')),
                ('book_title', models.CharField(max_length=300)),
                ('author', models.CharField(max_length=300)),
                ('cover_description', models.TextField()),
                ('body', models.TextField()),
                ('image_name', models.TextField()),
            ],
            bases=('blog.postbase',),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.PostBase')),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
