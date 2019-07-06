# Generated by Django 2.2.3 on 2019-07-06 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_post_news_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='genre',
        ),
        migrations.RemoveField(
            model_name='book',
            name='isbn',
        ),
        migrations.RemoveField(
            model_name='book',
            name='summary',
        ),
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, upload_to='catalog/', verbose_name='Изображение'),
        ),
    ]