# Generated by Django 4.0.5 on 2022-06-13 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
