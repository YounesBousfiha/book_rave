# Generated by Django 5.0.2 on 2024-02-18 22:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='description',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='img',
            new_name='media',
        ),
    ]
