# Generated by Django 3.1 on 2020-08-11 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_knowledge_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='postbase',
            name='display',
            field=models.BooleanField(default=True),
        ),
    ]