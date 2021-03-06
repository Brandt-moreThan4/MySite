# Generated by Django 3.1 on 2020-08-21 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('slug', models.SlugField(max_length=300, unique_for_date='date')),
                ('body', models.TextField()),
                ('date', models.DateField()),
                ('author', models.CharField(max_length=300)),
                ('url', models.TextField()),
                ('website', models.TextField()),
                ('name', models.CharField(max_length=300)),
            ],
            options={
                'ordering': ('-date',),
            },
        ),
    ]
