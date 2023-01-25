# Generated by Django 4.1.5 on 2023-01-25 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CRS', '0007_remove_question_category_category_c_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='c_name',
            field=models.CharField(default='c001', max_length=30),
        ),
        migrations.AlterField(
            model_name='question',
            name='type',
            field=models.CharField(choices=[('LG', 'Long Question'), ('SH', 'Short'), ('MC', 'Multiple Choice')], default='MC', max_length=2),
        ),
        migrations.CreateModel(
            name='QuestionCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CRS.category')),
                ('Qid', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='CRS.question')),
            ],
        ),
    ]
