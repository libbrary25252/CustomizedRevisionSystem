# Generated by Django 4.1.5 on 2023-01-20 21:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("CRS", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user", old_name="address", new_name="role_id",
        ),
    ]
