# Generated by Django 4.1.3 on 2022-12-03 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_recipe'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(default=10, upload_to='images'),
            preserve_default=False,
        ),
    ]