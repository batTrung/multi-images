# Generated by Django 2.1.7 on 2019-04-11 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20190411_1804'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='post',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
