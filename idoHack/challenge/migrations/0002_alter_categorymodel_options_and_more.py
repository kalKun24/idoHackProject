# Generated by Django 5.0.3 on 2024-03-07 09:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categorymodel',
            options={'verbose_name': 'Category'},
        ),
        migrations.AlterModelOptions(
            name='challengemodel',
            options={'verbose_name': 'Challenge'},
        ),
        migrations.AlterModelOptions(
            name='exercisemodel',
            options={'verbose_name': 'Exercise'},
        ),
        migrations.AlterField(
            model_name='categorymodel',
            name='category',
            field=models.CharField(default='', max_length=100, verbose_name='カテゴリ名'),
        ),
        migrations.AlterField(
            model_name='categorymodel',
            name='category_discription',
            field=models.TextField(default='', verbose_name='説明'),
        ),
        migrations.AlterField(
            model_name='challengemodel',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='challenge.categorymodel', verbose_name='カテゴリ'),
        ),
        migrations.AlterField(
            model_name='challengemodel',
            name='challenge_title',
            field=models.CharField(default='', max_length=100, verbose_name='タイトル'),
        ),
        migrations.AlterField(
            model_name='challengemodel',
            name='cleared_count',
            field=models.IntegerField(default=0, verbose_name='クリア者数'),
        ),
        migrations.AlterField(
            model_name='challengemodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='作成日時'),
        ),
        migrations.AlterField(
            model_name='challengemodel',
            name='exercise_title',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='challenge.exercisemodel', verbose_name='演習名'),
        ),
        migrations.AlterField(
            model_name='challengemodel',
            name='flag',
            field=models.CharField(default='', max_length=100, verbose_name='フラグ'),
        ),
        migrations.AlterField(
            model_name='challengemodel',
            name='hint_one',
            field=models.CharField(default='', max_length=200, verbose_name='ヒントその１'),
        ),
        migrations.AlterField(
            model_name='challengemodel',
            name='hint_three',
            field=models.CharField(default='', max_length=200, verbose_name='ヒントその３'),
        ),
        migrations.AlterField(
            model_name='challengemodel',
            name='hint_two',
            field=models.CharField(default='', max_length=200, verbose_name='ヒントその２'),
        ),
        migrations.AlterField(
            model_name='challengemodel',
            name='problem',
            field=models.TextField(default='', verbose_name='問題文'),
        ),
        migrations.AlterField(
            model_name='challengemodel',
            name='score',
            field=models.IntegerField(default='', verbose_name='配点'),
        ),
        migrations.AlterField(
            model_name='challengemodel',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='更新日時'),
        ),
        migrations.AlterField(
            model_name='challengemodel',
            name='visiable',
            field=models.BooleanField(default=False, verbose_name='一般ユーザへの公開'),
        ),
        migrations.AlterField(
            model_name='exercisemodel',
            name='exercise_discription',
            field=models.TextField(default='', verbose_name='説明'),
        ),
        migrations.AlterField(
            model_name='exercisemodel',
            name='exercise_title',
            field=models.CharField(default='', max_length=100, verbose_name='タイトル'),
        ),
        migrations.AlterField(
            model_name='exercisemodel',
            name='visiable',
            field=models.BooleanField(default=False, verbose_name='一般ユーザへの公開'),
        ),
    ]
