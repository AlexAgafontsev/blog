# Generated by Django 4.0.3 on 2022-03-11 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='description',
            field=models.TextField(default=None, max_length=400),
        ),
    ]