# Generated by Django 4.1.3 on 2022-12-07 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_user_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='test',
        ),
    ]
