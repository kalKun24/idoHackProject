# Generated by Django 5.0.3 on 2024-03-12 00:57

import mdeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0016_remove_challengemodel_problem_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercisemodel',
            name='discription',
        ),
        migrations.AddField(
            model_name='exercisemodel',
            name='exercise_discription',
            field=mdeditor.fields.MDTextField(default='', verbose_name='説明'),
        ),
        migrations.DeleteModel(
            name='TextBookModel',
        ),
    ]