# Generated by Django 4.1.5 on 2023-03-15 22:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CRS', '0022_rename_question_id_questionquestion_state_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionquestion',
            name='qid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='CRS.question'),
        ),
    ]
