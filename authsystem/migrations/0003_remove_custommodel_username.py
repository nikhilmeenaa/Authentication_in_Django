# Generated by Django 4.2.1 on 2023-06-28 07:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("authsystem", "0002_alter_custommodel_username"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="custommodel",
            name="username",
        ),
    ]
