# Generated by Django 4.1.5 on 2023-03-26 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRS', '0033_alter_questioninput_seq'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/images/'),
        ),
    ]
