# Generated by Django 2.0.6 on 2018-06-11 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0005_auto_20180611_1759'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='photo_url',
            new_name='photo',
        ),
    ]