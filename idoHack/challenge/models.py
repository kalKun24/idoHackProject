from django.db import models
from account.models import CustomUser
from django.db import models
from mdeditor.fields import MDTextField

# カテゴリ
class CategoryModel(models.Model):
    category = models.CharField(max_length=100, default="", verbose_name="カテゴリ名") # カテゴリ名
    category_discription = models.TextField(blank=True, default="", verbose_name="説明") # カテゴリの説明

    def __str__(self):
        return self.category
    
    class Meta:
        verbose_name = 'Category'

# 演習クラス
class ExerciseModel(models.Model):

    category = models.ForeignKey(CategoryModel, on_delete=models.SET_NULL, null=True, verbose_name="カテゴリ") # カテゴリ

    exercise_number = models.IntegerField(default=0, verbose_name="番号") # 演習の番号

    exercise_title = models.CharField(max_length=100, default="", verbose_name="タイトル") # 演習のタイトル
    exercise_discription = models.TextField(default="", verbose_name="説明") # 演習の説明
    visible = models.BooleanField(default=False, verbose_name="一般ユーザへの公開") # 演習が公開されているかどうか

    textbook_url = models.URLField(blank=True, verbose_name="教科書URL") # 教科書のURL
    explanation_url = models.URLField(blank=True, verbose_name="解説URL") # 解説のURL

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成日時") # 課題の作成日時
    updated_at = models.DateTimeField(auto_now=True, verbose_name="作成日時") # 課題の更新日時

    def __str__(self):
        return self.exercise_title

    class Meta:
        verbose_name = 'Exercise'


# 課題クラス
class ChallengeModel(models.Model):

    category = models.ForeignKey(CategoryModel, on_delete=models.SET_NULL, null=True, verbose_name="カテゴリ") # カテゴリ
    exercise_title = models.ForeignKey(ExerciseModel, on_delete=models.SET_NULL, null=True, verbose_name="演習名") # 演習のタイトル

    challenge_number = models.IntegerField(default=0, verbose_name="番号") # 課題の番号

    challenge_title = models.CharField(max_length=100,  default="", verbose_name="タイトル", unique=True) # 課題のタイトル
    score = models.IntegerField(default="", verbose_name="配点") # 課題の配点
    flag = models.CharField(max_length=100,  default="", verbose_name="フラグ") # フラグ
    visible = models.BooleanField(default=False, verbose_name="一般ユーザへの公開") # 課題が公開されているかどうか
    is_practice = models.BooleanField(default=False, verbose_name="実戦問題に表示する。") # 実戦問題かどうか
    problem = models.TextField(default="", verbose_name="問題文") # 課題の問題文

    # ヒント3つ
    hint_one = models.CharField(max_length=200, default="", blank=True, verbose_name="ヒントその１")
    hint_two = models.CharField(max_length=200, default="", blank=True, verbose_name="ヒントその２")
    hint_three = models.CharField(max_length=200, default="", blank=True, verbose_name="ヒントその３")

    cleared_count = models.IntegerField(default=0, verbose_name="クリア者数") # 課題をクリアした人数

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成日時") # 課題の作成日時
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新日時") # 課題の更新日時

    def __str__(self):
        return self.challenge_title

    class Meta:
        verbose_name = 'Challenge'

class TextBookModel(models.Model):
    name = models.CharField(max_length=10)
    Exercise_title = models.ForeignKey(ExerciseModel, on_delete=models.SET_NULL, null=True, verbose_name="演習名") # 演習のタイトル
    text_page = models.IntegerField()
    content = MDTextField()


class SubmitModel(models.Model):
        challenge_title = models.ForeignKey(ChallengeModel, to_field="challenge_title", on_delete=models.SET_NULL, null=True, verbose_name="課題") # 課題
        username = models.ForeignKey(CustomUser, to_field="username", on_delete=models.SET_NULL, null=True, verbose_name="ユーザ") # ユーザ
    
        submit_time = models.DateTimeField(auto_now_add=True, verbose_name="提出日時") # 提出日時
    
        def __str__(self):
            return self.challenge
    
        class Meta:
            verbose_name = 'Submit'