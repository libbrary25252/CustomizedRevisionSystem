# Generated by Django 4.1.5 on 2023-03-15 22:03

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('CRS', '0021_alter_question_description_alter_question_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questionquestion',
            old_name='question_id',
            new_name='state_id',
        ),
        migrations.AddField(
            model_name='questionquestion',
            name='qid',
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, to='CRS.question'),
            preserve_default=False,
        ),
    ]
