# Generated by Django 5.0.3 on 2024-03-07 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infomation', '0003_alter_infomationmodel_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infomationmodel',
            name='infomation_category',
            field=models.CharField(choices=[('infomation', 'お知らせ'), ('update', 'アップデート'), ('event', 'イベント告知'), ('maintenance', 'メンテナンス'), ('other', 'その他')], max_length=50, verbose_name='カテゴリー'),
        ),
    ]