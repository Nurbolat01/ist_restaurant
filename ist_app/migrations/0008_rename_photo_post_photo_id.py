# Generated by Django 3.2.19 on 2023-08-18 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ist_app', '0007_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='photo',
            new_name='photo_id',
        ),
    ]