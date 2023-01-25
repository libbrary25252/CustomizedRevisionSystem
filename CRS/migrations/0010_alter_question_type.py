# Generated by Django 4.1.5 on 2023-01-25 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRS', '0009_alter_question_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='type',
            field=models.CharField(choices=[('LQ', 'Long Question'), ('SQ', 'Short Question'), ('MC', 'Multiple Choice')], default='MC', max_length=2),
        ),
    ]