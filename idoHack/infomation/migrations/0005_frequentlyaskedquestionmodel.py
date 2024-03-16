# Generated by Django 5.0.3 on 2024-03-16 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infomation', '0004_alter_infomationmodel_infomation_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='FrequentlyAskedQuestionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(default='', verbose_name='質問')),
                ('answer', models.TextField(default='', verbose_name='回答')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
            ],
            options={
                'verbose_name_plural': 'Frequently Asked Question',
            },
        ),
    ]