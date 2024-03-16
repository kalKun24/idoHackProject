# Generated by Django 5.0.3 on 2024-03-14 10:31

import mdeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0018_exercisemodel_summary'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercisemodel',
            name='explanation_url',
        ),
        migrations.RemoveField(
            model_name='exercisemodel',
            name='textbook_url',
        ),
        migrations.AddField(
            model_name='exercisemodel',
            name='explanation',
            field=mdeditor.fields.MDTextField(blank=True, verbose_name='解説URL'),
        ),
        migrations.AddField(
            model_name='exercisemodel',
            name='textbook',
            field=mdeditor.fields.MDTextField(blank=True, verbose_name='教科書URL'),
        ),
    ]