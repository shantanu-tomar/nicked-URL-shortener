# Generated by Django 3.0.8 on 2020-07-30 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200730_1313'),
    ]

    operations = [
        migrations.RenameField(
            model_name='url',
            old_name='shortened_url',
            new_name='shortened_suffix',
        ),
    ]
