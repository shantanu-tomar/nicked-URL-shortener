# Generated by Django 3.0.8 on 2020-07-30 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200730_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='shortened_suffix',
            field=models.CharField(max_length=6, unique=True),
        ),
    ]
