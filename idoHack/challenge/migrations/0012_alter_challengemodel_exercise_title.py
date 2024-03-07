# Generated by Django 5.0.3 on 2024-03-07 12:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0011_challengemodel_is_practice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challengemodel',
            name='exercise_title',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='challenge.exercisemodel', verbose_name='演習名'),
        ),
    ]