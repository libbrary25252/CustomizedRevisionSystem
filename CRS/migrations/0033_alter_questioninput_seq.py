# Generated by Django 4.1.5 on 2023-03-20 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRS', '0032_questioninput_seq'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questioninput',
            name='seq',
            field=models.CharField(
                default='fuckyoula-2023032115364', max_length=100),
        ),
    ]