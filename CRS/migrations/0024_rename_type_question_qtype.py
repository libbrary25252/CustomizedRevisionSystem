# Generated by Django 4.1.7 on 2023-03-16 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("CRS", "0023_alter_questionquestion_qid"),
    ]

    operations = [
        migrations.RenameField(
            model_name="question", old_name="type", new_name="Qtype",
        ),
    ]
