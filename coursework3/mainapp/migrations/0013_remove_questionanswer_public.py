# Generated by Django 4.1.3 on 2022-12-15 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0012_rename_message_questionanswer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionanswer',
            name='public',
        ),
    ]