# Generated by Django 3.2 on 2021-04-21 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20210421_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='Iamge',
            field=models.URLField(max_length=500),
        ),
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]