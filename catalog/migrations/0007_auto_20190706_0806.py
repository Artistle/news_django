# Generated by Django 2.2.3 on 2019-07-06 05:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_book_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='author',
            new_name='text',
        ),
    ]