# Generated by Django 5.1.3 on 2024-11-30 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_comment_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='image',
        ),
    ]
