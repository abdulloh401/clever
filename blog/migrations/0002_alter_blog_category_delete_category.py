# Generated by Django 5.1.3 on 2024-11-23 03:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
        ('course', '0003_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.category'),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
