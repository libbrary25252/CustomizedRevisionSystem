# Generated by Django 4.1.5 on 2023-03-20 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRS', '0031_alter_questioninput_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='questioninput',
            name='seq',
            field=models.CharField(
                default='fuckyoula-202303211536', max_length=100),
        ),
    ]
