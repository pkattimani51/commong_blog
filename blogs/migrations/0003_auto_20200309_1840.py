# Generated by Django 2.2.11 on 2020-03-09 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_auto_20200218_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
