# Generated by Django 4.1.7 on 2023-03-16 21:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("CRS", "0028_alter_questioninput_uid"),
    ]

    operations = [
        migrations.DeleteModel(name="QuestionInput",),
    ]
