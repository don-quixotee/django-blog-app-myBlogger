# Generated by Django 3.0.5 on 2020-06-28 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_bookmarks'),
    ]

    operations = [
        migrations.DeleteModel(
            name='bookmarks',
        ),
    ]
