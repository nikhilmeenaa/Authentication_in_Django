# Generated by Django 4.2.1 on 2023-06-28 07:12

import authsystem.manager
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("authsystem", "0003_remove_custommodel_username"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="custommodel",
            managers=[
                ("objects", authsystem.manager.UserManager()),
            ],
        ),
    ]
