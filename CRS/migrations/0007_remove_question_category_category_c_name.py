# Generated by Django 4.1.5 on 2023-01-25 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRS', '0006_alter_question_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='category',
        ),
        migrations.AddField(
            model_name='category',
            name='c_name',
            field=models.CharField(default='cname', max_length=30),
        ),
    ]